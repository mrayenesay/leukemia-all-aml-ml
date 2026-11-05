"""One command to reproduce the interim report from scratch.

    python run_all.py              # download -> EDA -> LaTeX assets -> PDF
    python run_all.py --skip-download

The PDF step needs a LaTeX engine: `tectonic` (preferred, set TECTONIC=<path>
if it is not on PATH) or `latexmk`. Without one, upload reports/ara_rapor
together with results/ to Overleaf.
"""
from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PY = sys.executable


def run(cmd, cwd=ROOT):
    print("\n$", " ".join(map(str, cmd)), flush=True)
    subprocess.run(cmd, cwd=cwd, check=True)


def build_pdf(tex_dir: Path, tex: str = "main.tex") -> None:
    tectonic = os.environ.get("TECTONIC") or shutil.which("tectonic")
    if tectonic:
        run([tectonic, "-X", "compile", tex], cwd=tex_dir)
    elif shutil.which("latexmk"):
        run(["latexmk", "-pdf", tex], cwd=tex_dir)
    else:
        print(f"[skip] no LaTeX engine found; compile {tex_dir / tex} manually")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--skip-download", action="store_true")
    args = ap.parse_args()
    if not args.skip_download:
        run([PY, "scripts/download_data.py"])
    run([PY, "scripts/run_eda.py"])
    run([PY, "scripts/run_feasibility.py"])
    run([PY, "scripts/make_report_assets.py"])
    build_pdf(ROOT / "reports" / "ara_rapor")
    build_pdf(ROOT / "reports" / "genai")
    build_pdf(ROOT / "reports" / "sunum", "slides.tex")


if __name__ == "__main__":
    main()
