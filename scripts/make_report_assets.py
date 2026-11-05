"""Turn analysis outputs into LaTeX assets for the report.

    results/numbers.tex                    \\newcommand macros for every quoted number
    reports/ara_rapor/generated/*.tex      tables built from CSV outputs

Run after scripts/run_eda.py. Nothing in the report is typed by hand: if a
number changes in the analysis, re-running this script updates the PDF.
"""
from __future__ import annotations

import csv
import json
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TR = os.environ.get("REPORT_LANG", "tr") == "tr"  # same switch as leukemia.config
RES = ROOT / "results"
GEN = ROOT / "reports" / "ara_rapor" / "generated"


def dec(s: str) -> str:
    """Decimal mark of the report language (braces keep math spacing right)."""
    return s.replace(".", "{,}").replace("-", r"\ensuremath{-}") if TR else s


def pct(x, d=1):
    return dec(f"{100 * x:.{d}f}")


def num(x, d=2):
    return dec(f"{x:.{d}f}")


def intc(x):
    s = f"{abs(int(x)):,}".replace(",", "{.}" if TR else "{,}")
    return r"\ensuremath{-}" + s if x < 0 else s


def sci(p):
    """Math-mode body (use inside $...$)."""
    if p == 0:
        return r"<10^{-300}"
    m, e = f"{p:.1e}".split("e")
    return rf"{dec(m)}\times10^{{{int(e)}}}"


def tex_escape(s: str) -> str:
    return (str(s).replace("\\", r"\textbackslash{}").replace("&", r"\&").replace("%", r"\%")
            .replace("_", r"\_").replace("#", r"\#").replace("~", r"\textasciitilde{}")
            .replace("≥", r"$\geq$").replace("×", r"$\times$").replace("–", "--"))


def genes_list(gs, n=10):
    return ", ".join(tex_escape(g.split("///")[0]) for g in gs[:n] if g != "?")


def build_macros(d: dict) -> dict:
    M = {}
    g = d.get("golub", {})
    if g:
        q, e, de, b, ld = g["quality"], g["embedding"], g["de"], g["batch"], g["logdist"]
        c = g["label_check"]["counts"]
        M.update({
            "GolubN": g["n_samples"], "GolubP": intc(g["n_probes"]), "GolubMapped": intc(g["n_symbol_mapped"]),
            "GolubTrainALL": c["train_ALL"], "GolubTrainAML": c["train_AML"],
            "GolubTestALL": c["test_ALL"], "GolubTestAML": c["test_AML"],
            "GolubValues": intc(q["n_values"]), "GolubNonFinite": q["n_nonfinite"],
            "GolubNegPct": pct(q["frac_negative"]), "GolubBelowPct": pct(q["frac_below_20"]),
            "GolubAbovePct": pct(q["frac_above_16000"], 2),
            "GolubMin": intc(q["min_value"]), "GolubMax": intc(q["max_value"]),
            "GolubAffx": q["n_affx"], "GolubAllNeg": q["genes_all_negative"],
            "GolubCallP": pct(q["frac_call_P"]), "GolubCallA": pct(q["frac_call_A"]),
            "GolubCallM": pct(q["frac_call_M"]),
            "GolubMedP": intc(q["median_value_P"]), "GolubMedA": intc(q["median_value_A"]),
            "GolubNeverPresent": intc(q["genes_never_present"]),
            "GolubPresMin": pct(q["pct_present_min"]), "GolubPresMax": pct(q["pct_present_max"]),
            "GolubFilt": intc(g["n_after_fold_filter"]),
            "GolubFiltDudoit": intc(g["n_after_fold_filter_floor100"]),
            "GolubSkewRaw": num(ld["skew_raw"]), "GolubSkewLog": num(ld["skew_log"]),
            "GolubRhoLin": num(ld["rho_meansd_linear"]), "GolubRhoLog": num(ld["rho_meansd_log"]),
            "GolubPCOne": pct(e["evr_pc1"]), "GolubPCTwo": pct(e["evr_pc2"]),
            "GolubCumTen": pct(e["evr_cum10"]), "GolubNEighty": e["n_pc_80"],
            "GolubPCOneAUC": num(e["auc_pc"][0], 3), "GolubSilPCA": num(e["silhouette_pca10"]),
            "GolubSilTSNE": num(e["silhouette_tsne"]),
            "GolubSig": intc(de["n_sig_q05"]), "GolubSigOne": intc(de["n_sig_q01"]),
            "GolubSigMWU": intc(de["n_sig_mwu_q05"]), "GolubUpAML": de["n_up_aml"], "GolubUpALL": de["n_up_all"],
            "GolubRhoSNR": num(de["rho_snr_t"], 3), "GolubARI": num(de["ari_top_clusters"]),
            "GolubTop": genes_list(g["top_genes"]),
            "GolubPresTrain": pct(b["present_train_mean"]), "GolubPresTest": pct(b["present_test_mean"]),
            "GolubPresP": num(b["present_mwu_p"], 3), "GolubQP": num(b["q75_mwu_p"], 3),
            "GolubQTrain": intc(b["q75_train_median"]), "GolubQTest": intc(b["q75_test_median"]),
            "GolubKSAll": pct(b["ks_frac_p05_all"]), "GolubKSAml": pct(b["ks_frac_p05_aml"]),
            "GolubKSqAll": b["ks_n_q05_all"], "GolubKSqAml": b["ks_n_q05_aml"],
        })
    for key, pre in (("mile", "Mile"), ("andersson", "And")):
        m = d.get(key, {})
        if not m:
            continue
        q, e, de = m["quality"], m["embedding"], m["de"]
        M.update({
            f"{pre}N": intc(m["n_samples"]), f"{pre}P": intc(m["n_probes"]),
            f"{pre}Mapped": intc(m["n_symbol_mapped"]),
            f"{pre}MissingPct": pct(q["frac_missing"], 2), f"{pre}Inf": q["n_inf"],
            f"{pre}GenesMissing": intc(q["genes_with_missing"]),
            f"{pre}GenesMissingTwenty": intc(q["genes_missing_gt20"]),
            f"{pre}MaxSampleMissing": pct(q["max_sample_missing"]),
            f"{pre}Min": num(q["min_value"]), f"{pre}Max": num(q["max_value"]),
            f"{pre}Median": num(q["median_value"]), f"{pre}NegPct": pct(q["frac_negative"]),
            f"{pre}OutlierPct": pct(q["frac_outlier_3iqr"], 2),
            f"{pre}PCOne": pct(e["evr_pc1"]), f"{pre}PCTwo": pct(e["evr_pc2"]),
            f"{pre}CumTen": pct(e["evr_cum10"]), f"{pre}PCOneAUC": num(e["auc_pc"][0], 3),
            f"{pre}BestPC": e["best_pc"], f"{pre}BestPCAUC": num(e["best_pc_auc"], 3),
            f"{pre}SilPCA": num(e["silhouette_pca10"]), f"{pre}SilTSNE": num(e["silhouette_tsne"]),
            f"{pre}Sig": intc(de["n_sig_q05"]), f"{pre}SigPct": pct(de["n_sig_q05"] / de["n_tested"]),
            f"{pre}UpAML": intc(de["n_up_aml"]), f"{pre}UpALL": intc(de["n_up_all"]),
            f"{pre}ARI": num(de["ari_top_clusters"]), f"{pre}Top": genes_list(m["top_genes"]),
        })
    mi = d.get("mile", {})
    if mi:
        st = mi["subtypes"]
        M["MileALL"] = intc(sum(v for k, v in st.items() if "AML" not in k))
        M["MileAML"] = intc(sum(v for k, v in st.items() if "AML" in k))
        M["MileNSubtypes"] = len(st)
        ser = mi.get("series", {})
        if ser:
            M["MileTotal"] = intc(ser["n_total"])
            M["MileClassesTotal"] = len(ser["classes"])
        sc = mi.get("scale_check", {})
        if sc:
            M["MileScaleSpearman"] = num(sc["spearman_signal"], 3)
            M["MileScalePearsonLog"] = num(sc["pearson_log2_signal"], 3)
            M["MileScalePearsonLin"] = num(sc["pearson_linear_signal"], 2)
        M["MileAllMissing"] = mi.get("n_probes_all_missing", 0)
        tis = mi.get("tissue", {})
        M["MileBM"] = intc(sum(v for k, v in tis.items() if "marrow" in k.lower()))
        M["MilePB"] = intc(sum(v for k, v in tis.items() if "blood" in k.lower()))
    an = d.get("andersson", {})
    if an:
        M["AndBALL"] = an["lineage"].get("B-lineage ALL", 0)
        M["AndTALL"] = an["lineage"].get("T-cell ALL", 0)
        M["AndALL"] = M["AndBALL"] + M["AndTALL"]
        M["AndAML"] = an["lineage"].get("AML", 0)
        M["AndExcluded"] = an["n_excluded"]
    x = d.get("cross", {})
    if x:
        M.update({
            "CommonAll": intc(x["n_common_all"]),
            "CommonGM": intc(x["n_common_golub_mile"]), "CommonGA": intc(x["n_common_golub_andersson"]),
            "CommonMA": intc(x["n_common_mile_andersson"]),
            "GenesGolub": intc(x["n_genes"]["Golub"]), "GenesMile": intc(x["n_genes"]["MILE"]),
            "GenesAnd": intc(x["n_genes"]["Andersson"]),
            "RhoGM": num(x["spearman_t"]["golub_mile"]), "RhoGA": num(x["spearman_t"]["golub_andersson"]),
            "RhoMA": num(x["spearman_t"]["mile_andersson"]),
            "OvGM": x["top_overlap"]["golub_mile"]["k"], "OvGA": x["top_overlap"]["golub_andersson"]["k"],
            "OvMA": x["top_overlap"]["mile_andersson"]["k"], "OvN": x["top_overlap"]["golub_mile"]["n"],
            "OvGMp": sci(x["top_overlap"]["golub_mile"]["p"]), "OvGAp": sci(x["top_overlap"]["golub_andersson"]["p"]),
            "OvMAp": sci(x["top_overlap"]["mile_andersson"]["p"]),
            "OvGMdir": pct(x["top_overlap"]["golub_mile"]["same_direction"], 0),
            "OvGAdir": pct(x["top_overlap"]["golub_andersson"]["same_direction"], 0),
            "SharedTopN": len(x["shared_top_genes"]), "SharedTop": genes_list(x["shared_top_genes"], 12),
            "EtaRawDataset": pct(x["pc1_eta2"]["raw_dataset"]), "EtaRawClass": pct(x["pc1_eta2"]["raw_class"]),
            "EtaStdDataset": pct(x["pc1_eta2"]["std_dataset"]), "EtaStdClass": pct(x["pc1_eta2"]["std_class"]),
            "MedGolub": num(x["median_expr"]["Golub"]), "MedMile": num(x["median_expr"]["MILE"]),
            "MedAnd": num(x["median_expr"]["Andersson"]),
            "RhoMeansGM": num(x["spearman_gene_means"]["golub_mile"]),
        })
    return M


PREFIXES = ("Golub", "Mile", "And", "Common", "Genes", "Rho", "Ov", "Shared", "Eta", "Med", "Pilot")


def pilot_macros(f: dict) -> dict:
    """Numbers of the feasibility pilot (scripts/run_feasibility.py)."""
    leak, rows = f["leakage"], f["transfer_rows"]
    z = [r for r in rows if r["mode"] == "zscore"]
    raw = [r for r in rows if r["mode"] == "raw"]
    m_a = next(r for r in z if (r["train"], r["test"]) == ("MILE", "Andersson"))
    g_m = next(r for r in z if (r["train"], r["test"]) == ("Golub", "MILE"))
    return {
        "PilotK": leak["k"], "PilotNPerm": leak["n_perm"], "PilotKT": f["transfer"]["k"],
        "PilotInReal": num(leak["inside"]["real_mean"]), "PilotOutReal": num(leak["outside"]["real_mean"]),
        "PilotInPerm": num(leak["inside"]["perm_mean"]), "PilotOutPerm": num(leak["outside"]["perm_mean"]),
        "PilotAucMin": num(min(r["auc"] for r in z)), "PilotAucMax": num(max(r["auc"] for r in z)),
        "PilotBaMin": num(min(r["bacc"] for r in z)), "PilotBaMax": num(max(r["bacc"] for r in z)),
        "PilotRawSingle": sum(r["bacc"] == 0.5 for r in raw),
        "PilotTallMA": pct(m_a["tall_error"]), "PilotBallMA": pct(m_a["ball_error"]),
        "PilotTallGM": pct(g_m["tall_error"]), "PilotBallGM": pct(g_m["ball_error"]),
        "PilotNTallM": int(g_m["n_tall"]),
    }


def pilot_table(f: dict) -> None:
    """Transfer pilot, one row per train -> test direction."""
    rows = f["transfer_rows"]
    get = {(r["train"], r["test"], r["mode"]): r for r in rows}
    out = [r"\begin{tabular}{@{}lcccc@{}}", r"\toprule",
           r"Eğitim $\to$ test & AUC ($z$) & DD ham & DD $z$ & DD sıra\\ \midrule"
           if TR else r"Train $\to$ test & AUC ($z$) & BA raw & BA $z$ & BA rank\\ \midrule"]
    pairs = [(a, b) for a in ("Golub", "MILE", "Andersson") for b in ("Golub", "MILE", "Andersson") if a != b]
    for a, b in pairs:
        z = get[(a, b, "zscore")]
        out.append(rf"{a} $\to$ {b} & {num(z['auc'])} & {num(get[(a, b, 'raw')]['bacc'])} & "
                   rf"{num(z['bacc'])} & {num(get[(a, b, 'rank')]['bacc'])}\\")
    out += [r"\bottomrule", r"\end{tabular}"]
    (GEN / "pilot_transfer.tex").write_text("\n".join(out) + "\n", encoding="utf-8")


def write_macros(M: dict) -> None:
    # any data macro used by the report but not (yet) computed is shown as ??
    used = set()
    for tex in (ROOT / "reports").rglob("*.tex"):
        used |= set(re.findall(r"\\([A-Z][A-Za-z]+)", tex.read_text(encoding="utf-8")))
    missing = sorted(u for u in used if u.startswith(PREFIXES) and u not in M)
    if missing:
        print("WARNING: no value yet for", ", ".join(missing))
        M = {**M, **{m: r"\textbf{??}" for m in missing}}
    lines = ["% AUTO-GENERATED by scripts/make_report_assets.py -- do not edit"]
    for k, v in M.items():
        assert re.fullmatch(r"[A-Za-z]+", k), k
        lines.append(rf"\newcommand{{\{k}}}{{{v}}}")
    (RES / "numbers.tex").write_text("\n".join(lines) + "\n", encoding="utf-8")


def literature_table() -> None:
    """Full literature table (appendix) from reports/literature/literature_table.csv."""
    lit = ROOT / "reports" / "literature"
    rows = list(csv.DictReader(open(lit / "literature_table.csv", encoding="utf-8")))
    if TR:  # Turkish cells live in their own file; the English table serves the final paper
        tr = {r["key"]: r for r in csv.DictReader(open(lit / "literature_table_tr.csv", encoding="utf-8"))}
        assert set(tr) == {r["key"] for r in rows}
        assert all(None not in r for r in tr.values()), "unquoted comma in literature_table_tr.csv"
        rows = [{**r, **tr[r["key"]]} for r in rows]
    rows.sort(key=lambda r: int(r["year"]))
    head = (r"\toprule Kaynak & Yıl & Veri seti & Ön işleme/öznitelik seçimi & Yöntem & Doğrulama & En iyi sonuç & Not\\ \midrule"
            if TR else
            r"\toprule Ref. & Year & Data set & Pre-proc./feature sel. & Method & Validation & Best result & Note\\ \midrule")
    caption = ("Tam literatür özet tablosu (dahil edilen 30 çalışmanın tamamı, kronolojik)." if TR else
               "Full literature summary table (all 30 included studies, chronological).")
    out = [r"\begin{longtable}{@{}p{0.9cm}p{0.5cm}p{2.3cm}p{2.6cm}p{2.6cm}p{2.3cm}p{2.6cm}p{2.4cm}@{}}",
           rf"\caption{{{caption}}}\label{{tab:litfull}}\\",
           head + r"\endfirsthead",
           head + r"\endhead"]
    for r in rows:
        cells = [rf"\cite{{{r['key']}}}", r["year"]] + [tex_escape(r[k]) for k in
                 ("dataset", "preprocessing_feature_selection", "method", "validation", "best_result", "note")]
        out.append(" & ".join(cells) + r"\\")
    out += [r"\bottomrule", r"\end{longtable}"]
    (GEN / "lit_table_full.tex").write_text("\n".join(out) + "\n", encoding="utf-8")


def top_gene_table(n: int = 12) -> None:
    """Side-by-side top genes (by Welch p) for the three datasets."""
    cols = []
    for key in ("golub", "mile", "andersson"):
        f = RES / "tables" / f"de_{key}_top20.csv"
        if not f.exists():  # data set not analysed yet
            cols.append([("--", float("nan"), float("nan"))] * n)
            continue
        rows = list(csv.DictReader(open(f, encoding="utf-8")))[:n]
        cols.append([(tex_escape((r["symbol"] or "--").split("///")[0]), float(r["log2FC"]), float(r["t"]))
                     for r in rows])
    gene = "gen" if TR else "gene"
    out = [r"\begin{tabular}{@{}r lrr lrr lrr@{}}", r"\toprule",
           r" & \multicolumn{3}{c}{Golub} & \multicolumn{3}{c}{MILE} & \multicolumn{3}{c}{Andersson}\\",
           r"\cmidrule(lr){2-4}\cmidrule(lr){5-7}\cmidrule(l){8-10}",
           rf"\# & {gene} & $\Delta$ & $t$ & {gene} & $\Delta$ & $t$ & {gene} & $\Delta$ & $t$\\ \midrule"]
    for i in range(n):
        cells = [str(i + 1)]
        for c in cols:
            s, fc, t = c[i]
            cells += [s, "--", "--"] if s == "--" else [s, dec(f"{fc:+.2f}"), dec(f"{t:+.1f}")]
        out.append(" & ".join(cells) + r"\\")
    out += [r"\bottomrule", r"\end{tabular}"]
    (GEN / "top_genes.tex").write_text("\n".join(out) + "\n", encoding="utf-8")


def bib_with_doi() -> None:
    """IEEEtran.bst ignores the doi field; copy it into a printed note."""
    src = (ROOT / "reports" / "literature" / "references.bib").read_text(encoding="utf-8")

    def add_note(m):
        doi = m.group(2)
        return m.group(0) + ",\n  note    = {doi: \\href{https://doi.org/" + doi + "}{" + doi + "}}"
    out = re.sub(r"(doi\s*=\s*\{([^}]+)\})", add_note, src)
    (GEN / "references.bib").write_text(out, encoding="utf-8")


def main() -> None:
    GEN.mkdir(parents=True, exist_ok=True)
    bib_with_doi()
    d = json.loads((RES / "eda_numbers.json").read_text())
    M = build_macros(d)
    pilot = RES / "feasibility.json"
    if pilot.exists():
        f = json.loads(pilot.read_text())
        M.update(pilot_macros(f))
        pilot_table(f)
    write_macros(M)
    literature_table()
    top_gene_table()
    print(f"wrote {len(M)} macros, literature and gene tables")


if __name__ == "__main__":
    main()
