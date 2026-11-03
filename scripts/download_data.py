"""Download all raw datasets used in the project into data/raw/.

Raw data is NOT committed to the repository (see .gitignore); this script
recreates it. Downloads are resumable because the NCBI GEO FTP mirror often
drops long connections.

Usage:
    python scripts/download_data.py            # all datasets
    python scripts/download_data.py golub      # only one dataset
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import sys
import time
import urllib.request
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"

GEO = "https://ftp.ncbi.nlm.nih.gov/geo"

SOURCES = {
    # Golub et al. (1999) -- Kaggle mirror of the original Broad Institute files
    "golub": [
        ("https://www.kaggle.com/api/v1/datasets/download/crawford/gene-expression",
         RAW / "golub" / "golub_kaggle.zip"),
    ],
    # MILE study stage 1 (Haferlach et al., 2010), Affymetrix HG-U133 Plus 2.0
    "mile": [
        (f"{GEO}/series/GSE13nnn/GSE13159/matrix/GSE13159_series_matrix.txt.gz",
         RAW / "GSE13159" / "GSE13159_series_matrix.txt.gz"),
        # one ArrayExpress sample table (signal + detection p) used to identify
        # the scale of the series-matrix values
        ("https://ftp.ebi.ac.uk/biostudies/fire/E-GEOD-/159/E-GEOD-13159/Files/GSM329426_sample_table.txt",
         RAW / "GSE13159" / "GSM329426_sample_table.txt"),
    ],
    # Andersson et al. (2007), 121 childhood acute leukemias, Swegene 27K cDNA (GPL4861)
    "andersson": [
        (f"{GEO}/series/GSE7nnn/GSE7186/matrix/GSE7186_series_matrix.txt.gz",
         RAW / "GSE7186" / "GSE7186_series_matrix.txt.gz"),
    ],
    # Platform annotation tables (probe -> gene symbol)
    "platforms": [
        (f"{GEO}/platforms/GPLnnn/GPL80/annot/GPL80.annot.gz",
         RAW / "platforms" / "GPL80.annot.gz"),
        (f"{GEO}/platforms/GPLnnn/GPL570/annot/GPL570.annot.gz",
         RAW / "platforms" / "GPL570.annot.gz"),
        (f"{GEO}/platforms/GPL4nnn/GPL4861/annot/GPL4861.annot.gz",
         RAW / "platforms" / "GPL4861.annot.gz"),
    ],
}


def _remote_size(url: str) -> int | None:
    req = urllib.request.Request(url, method="HEAD")
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                n = r.headers.get("Content-Length")
                return int(n) if n else None
        except Exception:
            time.sleep(3 * (attempt + 1))
    return None


def download(url: str, dest: Path, retries: int = 50, chunk: int = 1 << 20) -> None:
    """Resumable HTTP download (Range requests) with stall retries."""
    dest.parent.mkdir(parents=True, exist_ok=True)
    total = _remote_size(url)
    if dest.exists() and total is not None and dest.stat().st_size == total:
        print(f"[skip] {dest.relative_to(ROOT)} already complete")
        return
    for attempt in range(1, retries + 1):
        have = dest.stat().st_size if dest.exists() else 0
        if total is not None and have >= total:
            break
        req = urllib.request.Request(url, headers={"Range": f"bytes={have}-"} if have else {})
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                # server ignored the Range header -> restart from scratch
                mode = "ab" if (have and r.status == 206) else "wb"
                with open(dest, mode) as f:
                    while True:
                        buf = r.read(chunk)
                        if not buf:
                            break
                        f.write(buf)
                        done = dest.stat().st_size
                        if total:
                            sys.stdout.write(f"\r  {dest.name}: {done/1e6:7.1f}/{total/1e6:.1f} MB")
                            sys.stdout.flush()
            if total is None or dest.stat().st_size >= total:
                break
        except urllib.error.HTTPError as e:
            if e.code == 416:  # requested range not satisfiable -> file complete
                break
            if 400 <= e.code < 500:
                raise
            print(f"\n  retry {attempt}/{retries} after error: {e}")
            time.sleep(min(30, 2 * attempt))
        except Exception as e:  # network hiccup: resume
            print(f"\n  retry {attempt}/{retries} after error: {e}")
            time.sleep(min(30, 2 * attempt))
    print(f"\n[ok]   {dest.relative_to(ROOT)} ({dest.stat().st_size/1e6:.1f} MB)")


def download_parallel(url: str, dest: Path, parts: int = 6, part_size: int = 2 << 20,
                      min_speed: float = 0.0) -> None:
    """Split a large file into byte ranges and fetch them concurrently.

    The GEO mirror throttles single connections, so a ~850 MB series matrix
    downloads an order of magnitude faster this way. Each range is itself
    resumable, so the function can be re-run after an interruption.
    """
    from concurrent.futures import ThreadPoolExecutor

    total = _remote_size(url)
    if total is None:
        return download(url, dest)
    if dest.exists() and dest.stat().st_size == total:
        print(f"[skip] {dest.relative_to(ROOT)} already complete")
        return
    tmp = dest.parent / (dest.name + ".parts")
    tmp.mkdir(parents=True, exist_ok=True)
    ranges = [(i, s, min(s + part_size, total) - 1)
              for i, s in enumerate(range(0, total, part_size))]

    def fetch(rng):
        i, start, end = rng
        p = tmp / f"{i:05d}"
        for attempt in range(100):
            have = p.stat().st_size if p.exists() else 0
            if have >= end - start + 1:
                return
            req = urllib.request.Request(url, headers={"Range": f"bytes={start + have}-{end}"})
            try:
                with urllib.request.urlopen(req, timeout=30) as r, open(p, "ab") as f:
                    t0, got = time.time(), 0
                    while buf := r.read(1 << 16):
                        f.write(buf)
                        got += len(buf)
                        el = time.time() - t0
                        # throttled connection: drop it and reconnect (resumes)
                        if el > 8 and got / el < min_speed:
                            break
            except Exception:
                time.sleep(min(20, 1 + attempt))
        raise RuntimeError(f"range {i} failed")

    done = 0
    with ThreadPoolExecutor(parts) as ex:
        for _ in ex.map(fetch, ranges):
            done += 1
            sys.stdout.write(f"\r  {dest.name}: {done}/{len(ranges)} parts")
            sys.stdout.flush()
    with open(dest, "wb") as out:
        for i, _, _ in ranges:
            out.write((tmp / f"{i:05d}").read_bytes())
    for p in tmp.iterdir():
        p.unlink()
    tmp.rmdir()
    print(f"\n[ok]   {dest.relative_to(ROOT)} ({dest.stat().st_size/1e6:.1f} MB)")


def verify_gzip(path: Path) -> None:
    with gzip.open(path, "rb") as f:
        while f.read(1 << 24):
            pass


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("which", nargs="*", default=list(SOURCES), choices=list(SOURCES))
    args = ap.parse_args()
    for name in args.which:
        print(f"== {name}")
        for url, dest in SOURCES[name]:
            download_parallel(url, dest)
            if dest.suffix == ".gz":
                verify_gzip(dest)
            if dest.suffix == ".zip":
                with zipfile.ZipFile(dest) as z:
                    z.extractall(dest.parent)
                    print("  extracted:", ", ".join(z.namelist()))
            print(f"  sha256 {sha256(dest)[:16]}...")


if __name__ == "__main__":
    main()
