"""Build an editable Word copy of the interim report from reports/ara_rapor/main.tex.

The PDF stays the document to submit. This copy is for reading and editing: it opens
with Track Changes on, so edits can be carried back to main.tex afterwards. Numbers
and cross-references become plain text and do not follow the code.

Needs Tectonic (TECTONIC env variable or PATH) for the numbering and the bibliography.
"""
from __future__ import annotations

import os
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

import fitz
from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "reports" / "ara_rapor"
FIGURES = ROOT / "results" / "figures"
OUT = REPORT / "ara_rapor_duzenleme.docx"
FONT = "Times New Roman"
MONO = "Consolas"
TEXT_W = 17.0  # cm between the margins

GREEK = {"gg": "≫", "leq": "≤", "geq": "≥", "in": "∈", "to": "→", "Rightarrow": "⇒", "times": "×",
         "rho": "ρ", "eta": "η", "gamma": "γ", "Delta": "Δ", "ell": "ℓ", "dots": "…", "dagger": "†",
         "log": "log", "pm": "±"}
SKIP = {"large", "noindent", "scriptsize", "centering", "small", "normalsize"}
unknown: set[str] = set()


# ---------------------------------------------------------------- LaTeX helpers
def arg(s: str, i: int, op: str = "{", cl: str = "}") -> tuple[str, int]:
    """Balanced group starting at s[i]; returns its content and the index after it."""
    assert s[i] == op, s[i:i + 40]
    depth, j = 0, i
    while True:
        if s[j] == "\\":
            j += 2
            continue
        depth += (s[j] == op) - (s[j] == cl)
        j += 1
        if depth == 0:
            return s[i + 1:j - 1], j


def split_top(s: str, sep: str) -> list[str]:
    """Split on `sep` outside braces, ignoring escaped characters."""
    out, depth, cur, i = [], 0, "", 0
    while i < len(s):
        if s.startswith(sep, i) and depth == 0:
            out.append(cur)
            cur = ""
            i += len(sep)
        elif s[i] == "\\":
            cur += s[i:i + 2]
            i += 2
        else:
            depth += (s[i] == "{") - (s[i] == "}")
            cur += s[i]
            i += 1
    return out + [cur]


def expand_macros(s: str, macros: dict[str, str]) -> str:
    for name in sorted(macros, key=len, reverse=True):
        s = re.sub(r"\\" + name + r"(?![A-Za-z])(\{\})?", lambda m: macros[name], s)
    return s.replace(r"\ensuremath{-}", "−").replace("{,}", ",").replace("{.}", ".")


class Refs:
    def __init__(self, aux: str, bbl: str):
        self.labels = dict(re.findall(r"\\newlabel\{([^}]+)\}\{\{([^}]*)\}", aux))
        body = bbl[bbl.index(r"\bibitem"):bbl.index(r"\end{thebibliography}")]
        items = re.split(r"\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}", body)[1:]
        self.keys = items[0::2]
        self.num = {k: i + 1 for i, k in enumerate(self.keys)}
        self.texts = items[1::2]

    def cite(self, keys: str) -> str:
        ns = sorted(self.num[k.strip()] for k in keys.split(","))
        parts, i = [], 0
        while i < len(ns):
            j = i
            while j + 1 < len(ns) and ns[j + 1] == ns[j] + 1:
                j += 1
            if j - i >= 2:
                parts.append(f"[{ns[i]}]–[{ns[j]}]")
            else:
                parts += [f"[{n}]" for n in ns[i:j + 1]]
            i = j + 1
        return ", ".join(parts)


def math_runs(tex: str, fmt: dict) -> list[tuple[str, dict]]:
    s = re.sub(r"\\sqrt\{([^}]*)\}", r"√\1", tex)
    s = s.replace(r"\%", "%").replace(r"\{", "{ ").replace(r"\}", " }").replace(r"\,", " ")
    s = re.sub(r"\\([A-Za-z]+)", lambda m: GREEK.get(m.group(1), m.group(0)), s)
    if "\\" in s:
        unknown.add(s)
    s = s.replace("{ ", "\x01").replace(" }", "\x02").replace("-", "−")
    runs, i, cur = [], 0, ""

    def flush():
        nonlocal cur
        for piece in re.split(r"((?<![A-Za-zçğıöşüÇĞİÖŞÜ])[A-Za-z](?![A-Za-zçğıöşüÇĞİÖŞÜ]))", cur):
            if piece:
                italic = len(piece) == 1 and piece.isascii() and piece.isalpha()
                runs.append((piece.replace("\x01", "{").replace("\x02", "}"),
                             {**fmt, "italic": italic or fmt.get("italic", False)}))
        cur = ""

    while i < len(s):
        if s[i] in "^_":
            flush()
            key = "sup" if s[i] == "^" else "sub"
            if s[i + 1] == "{":
                body, i = arg(s, i + 1)
            else:
                body, i = s[i + 1], i + 2
            runs.append((body, {**fmt, key: True}))
        elif s[i] in "{}":
            i += 1
        else:
            cur += s[i]
            i += 1
    flush()
    return runs


def inline(tex: str, refs: Refs, fmt: dict | None = None) -> list[tuple[str, dict]]:
    fmt = fmt or {}
    runs: list[tuple[str, dict]] = []
    i, buf = 0, ""

    def flush():
        nonlocal buf
        if buf:
            runs.append((buf, fmt))
            buf = ""

    while i < len(tex):
        c = tex[i]
        if c == "\\":
            m = re.match(r"\\([A-Za-z]+)", tex[i:])
            if not m:
                nxt = tex[i + 1]
                buf += {" ": " ", ",": " ", "-": "", "\\": " "}.get(nxt, nxt)
                i += 2
                continue
            name, i = m.group(1), i + len(m.group(0))
            if name in ("textbf", "emph", "textit", "texttt", "AS"):
                body, i = arg(tex, i)
                flush()
                if name == "AS":
                    runs.append((f"AS{body}", {**fmt, "bold": True}))
                else:
                    key = {"textbf": "bold", "emph": "italic", "textit": "italic", "texttt": "mono"}[name]
                    runs.extend(inline(body, refs, {**fmt, key: True}))
            elif name == "cite":
                body, i = arg(tex, i)
                buf += refs.cite(body)
            elif name in ("ref", "figref", "tabref"):
                body, i = arg(tex, i)
                pre = {"ref": "", "figref": "Şekil ", "tabref": "Tablo "}[name]
                buf += pre + refs.labels[body]
            elif name == "url":
                body, i = arg(tex, i)
                buf += body
            elif name == "href":
                _, i = arg(tex, i)
                body, i = arg(tex, i)
                buf += body.replace(r"\_", "_")
            elif name == "LaTeX":
                buf += "LaTeX"
                if tex[i:i + 2] == "{}":
                    i += 2
            elif name in ("label",):
                _, i = arg(tex, i)
            elif name in SKIP:
                pass
            else:
                unknown.add(name)
        elif c == "$":
            j = i + 1
            while tex[j] != "$" or tex[j - 1] == "\\":
                j += 1
            flush()
            runs.extend(math_runs(tex[i + 1:j], fmt))
            i = j + 1
        elif c == "{":
            body, i = arg(tex, i)
            flush()
            runs.extend(inline(body, refs, fmt))
        elif tex.startswith("---", i):
            buf += "—"
            i += 3
        elif tex.startswith("--", i):
            buf += "–"
            i += 2
        elif tex.startswith("``", i):
            buf += "“"
            i += 2
        elif tex.startswith("''", i):
            buf += "”"
            i += 2
        else:
            buf += {"~": "\u00a0", "'": "’", "\n": " "}.get(c, c)
            i += 1
    flush()
    return runs


# ---------------------------------------------------------------- Word helpers
def set_font(style, size=None, bold=None, italic=None, name=FONT):
    style.font.name = name
    rpr = style.element.get_or_add_rPr()
    fonts = rpr.find(qn("w:rFonts"))
    for attr in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        fonts.set(qn(attr), name)
    for attr in ("w:asciiTheme", "w:hAnsiTheme", "w:cstheme", "w:eastAsiaTheme"):
        fonts.attrib.pop(qn(attr), None)
    style.font.color.rgb = None
    if size:
        style.font.size = Pt(size)
    if bold is not None:
        style.font.bold = bold
    if italic is not None:
        style.font.italic = italic


def write_runs(par, runs, size=None):
    for text, f in runs:
        r = par.add_run(text)
        r.bold = f.get("bold") or None
        r.italic = f.get("italic") or None
        if f.get("sup"):
            r.font.superscript = True
        if f.get("sub"):
            r.font.subscript = True
        if f.get("mono"):
            r.font.name = MONO
            r._element.get_or_add_rPr().get_or_add_rFonts().set(qn("w:cs"), MONO)
        if size:
            r.font.size = Pt(size)


def field(par, code: str):
    for kind, text in (("begin", None), (None, code), ("end", None)):
        r = par.add_run()
        if kind:
            el = OxmlElement("w:fldChar")
            el.set(qn("w:fldCharType"), kind)
        else:
            el = OxmlElement("w:instrText")
            el.text = text
        r._element.append(el)


def setup(doc: Document) -> None:
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Cm(21), Cm(29.7)
    sec.left_margin = sec.right_margin = Cm(2)
    sec.top_margin, sec.bottom_margin = Cm(2.2), Cm(2)
    st = doc.styles
    set_font(st["Normal"], 11)
    st["Normal"].paragraph_format.space_after = Pt(6)
    st["Normal"].paragraph_format.line_spacing = 1.08
    set_font(st["Title"], 20, bold=True)
    st["Title"].paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    st["Title"].paragraph_format.space_after = Pt(4)
    ppr = st["Title"].element.get_or_add_pPr()
    for el in ppr.findall(qn("w:pBdr")):
        ppr.remove(el)
    set_font(st["Subtitle"], 13, italic=False)
    rpr = st["Subtitle"].element.get_or_add_rPr()
    for el in rpr.findall(qn("w:spacing")):
        rpr.remove(el)
    st["Subtitle"].paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    set_font(st["Heading 1"], 13, bold=True)
    st["Heading 1"].paragraph_format.space_before = Pt(14)
    st["Heading 1"].paragraph_format.space_after = Pt(6)
    set_font(st["Heading 2"], 11.5, bold=True, italic=True)
    st["Heading 2"].paragraph_format.space_before = Pt(10)
    st["Heading 2"].paragraph_format.space_after = Pt(4)
    set_font(st["Caption"], 9.5, bold=False)
    st["Caption"].paragraph_format.space_after = Pt(8)
    for name in ("List Bullet", "List Number"):
        set_font(st[name], 11)
    set_font(st["Header"], 9)
    set_font(st["Footer"], 9)

    # Turkish proofing language
    defaults = st.element.find(qn("w:docDefaults"))
    lang = defaults.find(f"{qn('w:rPrDefault')}/{qn('w:rPr')}/{qn('w:lang')}")
    if lang is not None:
        lang.set(qn("w:val"), "tr-TR")

    head = sec.header.paragraphs[0]
    head.alignment = WD_ALIGN_PARAGRAPH.CENTER
    head.add_run("Düzenleme kopyası: teslim edilecek belge reports/ara_rapor/main.pdf dosyasıdır.")
    foot = sec.footer.paragraphs[0]
    foot.alignment = WD_ALIGN_PARAGRAPH.CENTER
    field(foot, "PAGE")

    # open with Track Changes on (element order is fixed by the schema)
    settings = doc.settings.element
    track = OxmlElement("w:trackRevisions")
    later = ("doNotTrackMoves", "doNotTrackFormatting", "documentProtection", "autoFormatOverride",
             "styleLockTheme", "styleLockQFSet", "defaultTabStop")
    for child in settings:
        if child.tag.split("}")[1] in later:
            child.addprevious(track)
            break
    else:
        settings.append(track)


def borders(table) -> None:
    pr = table._tbl.tblPr
    b = OxmlElement("w:tblBorders")
    for edge, size in (("top", 8), ("bottom", 8), ("insideH", 2)):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:val"), "single")
        el.set(qn("w:sz"), str(size))
        el.set(qn("w:color"), "808080" if edge == "insideH" else "000000")
        b.append(el)
    pr.append(b)
    mar = OxmlElement("w:tblCellMar")
    for edge in ("left", "right"):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:w"), "45")
        el.set(qn("w:type"), "dxa")
        mar.append(el)
    pr.append(mar)


def add_table(doc, rows, n_head, refs, size=8.5):
    """rows: list of [(span, tex), ...]."""
    ncol = sum(s for s, _ in rows[-1])
    weights = [6.0] * ncol
    for r in rows[n_head - 1:]:  # a column must fit its longest short word
        c = 0
        for span, t in r:
            if span == 1:
                words = "".join(x for x, _ in inline(t, refs)).split() or [""]
                weights[c] = max(weights[c], 1.6 * min(max(map(len, words)), 10) + 2)
            c += span
    for r in rows[n_head:]:
        c = 0
        for span, t in r:
            if span == 1:
                plain = "".join(x for x, _ in inline(t, refs))
                weights[c] = max(weights[c], min(len(plain), 26))
            c += span
    total = sum(weights)
    widths = [TEXT_W * w / total for w in weights]
    table = doc.add_table(rows=len(rows), cols=ncol)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    borders(table)
    for ri, r in enumerate(rows):
        c = 0
        row = table.rows[ri]
        trpr = row._tr.get_or_add_trPr()
        trpr.append(OxmlElement("w:cantSplit"))
        if ri < n_head:
            trpr.append(OxmlElement("w:tblHeader"))
        for span, t in r:
            cell = row.cells[c]
            if span > 1:
                cell = cell.merge(row.cells[c + span - 1])
            cell.width = Cm(sum(widths[c:c + span]))
            par = cell.paragraphs[0]
            par.paragraph_format.space_after = Pt(1)
            par.paragraph_format.line_spacing = 1.0
            par.paragraph_format.keep_with_next = len(rows) <= 16 and ri < len(rows) - 1
            if span > 1:
                par.alignment = WD_ALIGN_PARAGRAPH.CENTER
            f = {"bold": True} if ri < n_head else {}
            write_runs(par, inline(t, refs, f), size)
            c += span
    return table


def parse_rows(tabular: str) -> tuple[list, int, str]:
    """Rows, number of header rows and an optional note row after \\bottomrule."""
    rows, n_head, note = [], 0, ""
    for seg in split_top(tabular, r"\\"):
        ended = r"\bottomrule" in seg
        had_mid = r"\midrule" in seg
        if had_mid and not n_head:
            n_head = len(rows)
        seg = re.sub(r"\\cmidrule(\([a-z]*\))?\{[^}]*\}", "", seg)
        if r"\endfirsthead" in seg:  # what follows is the repeated longtable header
            continue
        seg = seg.split(r"\endhead")[-1]
        seg = re.sub(r"\\(toprule|midrule|bottomrule)", "", seg).strip()
        if not seg:
            continue
        cells = []
        for cell in split_top(seg, "&"):
            cell = cell.strip()
            m = re.match(r"\\multicolumn\{(\d+)\}", cell)
            if m:
                i = m.end()
                _, i = arg(cell, i)
                body, _ = arg(cell, i)
                cells.append((int(m.group(1)), body))
            else:
                cells.append((1, cell))
        if ended:
            note = cells[0][1]
        else:
            rows.append(cells)
    return rows, n_head, note


def tabular_body(env: str) -> str:
    m = re.search(r"\\begin\{(tabularx|tabular|longtable)\}", env)
    i = m.end()
    if m.group(1) == "tabularx":
        _, i = arg(env, i)
    _, i = arg(env, i)
    return env[i:env.index(r"\end{" + m.group(1) + "}")]


ACCENTS = {r"{\'\i}": "í", r"{\'e}": "é", r"{\'a}": "á", r"{\'o}": "ó", r"{\v{s}}": "š", r"{\"u}": "ü",
           r"{\"o}": "ö", r"{\"O}": "Ö", r"{\"a}": "ä", r"{\c{c}}": "ç", r"{\c{s}}": "ş", r"{\u{g}}": "ğ",
           r"{\i}": "ı", r"{\~a}": "ã", r"{\'c}": "ć", r"{\v{Z}}": "Ž"}


def clean_bib(text: str) -> str:
    for tex, char in ACCENTS.items():
        text = text.replace(tex, char)
    text = re.sub(r"\\BIBentry[A-Za-z]+(\[[^\]]*\])?", "", text)
    text = text.replace(r"\newblock", " ")
    text = re.sub(r"\\url\{([^}]*)\}", r"\1", text)
    return re.sub(r"\s+", " ", text).strip()


# ---------------------------------------------------------------- report
class Builder:
    def __init__(self, doc, refs, pipeline_png):
        self.doc, self.refs, self.pipeline = doc, refs, pipeline_png
        self.sec = self.sub = self.fig = self.tab = 0
        self.appendix = False

    def para(self, tex):
        tex = tex.strip()
        if not tex:
            return
        p = self.doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        write_runs(p, inline(tex, self.refs))

    def text(self, chunk):
        for block in re.split(r"\n\s*\n", chunk):
            self.para(block)

    def heading(self, tex, level, numbered=True):
        tex = re.sub(r"\\label\{[^}]*\}", "", tex)
        if level == 1 and numbered:
            self.sec += 1
            self.sub = 0
            pre = (f"Ek {chr(64 + self.sec)}: " if self.appendix else f"{roman(self.sec)}. ")
        elif level == 2:
            self.sub += 1
            pre = f"{chr(64 + self.sub)}. "
        else:
            pre = ""
        p = self.doc.add_heading(level=level)
        write_runs(p, [(pre, {})] + inline(tex, self.refs))

    def caption(self, kind, n, tex, keep_next=False):
        p = self.doc.add_paragraph(style="Caption")
        write_runs(p, [(f"{kind} {n}. ", {"bold": True})] + inline(tex, self.refs))
        p.paragraph_format.keep_with_next = keep_next
        return "".join(t for t, _ in inline(tex, self.refs))

    def figure(self, env):
        self.fig += 1
        m = re.search(r"\\fig(?:\[[^\]]*\])?\{([^}]+)\}", env)
        path = FIGURES / m.group(1).replace(".pdf", ".png") if m else self.pipeline
        i = env.index(r"\caption") + len(r"\caption")
        cap, _ = arg(env, i)
        lab = re.search(r"\\label\{([^}]+)\}", env)
        if lab:
            assert self.refs.labels[lab.group(1)] == str(self.fig), lab.group(1)
        p = self.doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.keep_with_next = True
        pic = p.add_run().add_picture(str(path), width=Cm(TEXT_W if m else 15))
        plain = self.caption("Şekil", self.fig, cap)
        pic._inline.docPr.set("descr", plain[:250])

    def table(self, env, source=None):
        self.tab += 1
        i = env.index(r"\caption") + len(r"\caption")
        cap, _ = arg(env, i)
        lab = re.search(r"\\label\{([^}]+)\}", env)
        if lab:
            assert self.refs.labels[lab.group(1)] == roman(self.tab), lab.group(1)
        self.caption("Tablo", roman(self.tab), cap, keep_next=True)
        body = source if source is not None else env
        if r"\input{generated/" in body and source is None:
            name = re.search(r"\\input\{(generated/[^}]+)\}", body).group(1)
            body = expand_gen(name, self.macros)
        tb = tabular_body(body)
        if "longtable" in body:
            tb = tb[tb.index(r"\toprule"):]
        rows, n_head, note = parse_rows(tb)
        add_table(self.doc, rows, n_head, self.refs)
        p = self.doc.add_paragraph()
        p.paragraph_format.space_after = Pt(8)
        if note:
            write_runs(p, inline(note, self.refs), 8.5)

    def bibliography(self):
        p = self.doc.add_heading(level=1)
        p.add_run("Kaynaklar")
        for n, raw in enumerate(self.refs.texts, 1):
            q = self.doc.add_paragraph()
            q.paragraph_format.left_indent = Cm(0.8)
            q.paragraph_format.first_line_indent = Cm(-0.8)
            q.paragraph_format.space_after = Pt(3)
            write_runs(q, [(f"[{n}] ", {})] + inline(clean_bib(raw), self.refs), 10)


def roman(n: int) -> str:
    out = ""
    for v, r in ((10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")):
        while n >= v:
            out += r
            n -= v
    return out


def expand_gen(name: str, macros: dict) -> str:
    return expand_macros((REPORT / name).read_text(encoding="utf-8"), macros)


def compile_report(tmp: Path) -> None:
    exe = os.environ.get("TECTONIC") or shutil.which("tectonic")
    if not exe:
        raise SystemExit("Tectonic not found: set TECTONIC to the executable")
    subprocess.run([exe, "-X", "compile", "main.tex", "--keep-intermediates", "--outdir", str(tmp)],
                   cwd=REPORT, check=True, capture_output=True)


def pipeline_png(pdf: Path, tmp: Path) -> Path:
    doc = fitz.open(pdf)
    for page in doc:
        cap = page.search_for("Planlanan sızıntısız işlem")
        box = page.search_for("ham matris")
        if cap and box:
            clip = fitz.Rect(40, box[0].y0 - 8, page.rect.width - 40, cap[0].y0 - 2)
            out = tmp / "pipeline.png"
            page.get_pixmap(dpi=260, clip=clip).save(out)
            return out
    raise SystemExit("pipeline figure not found")


def main() -> None:
    src = (REPORT / "main.tex").read_text(encoding="utf-8")
    macros = {}
    for line in (ROOT / "results" / "numbers.tex").read_text(encoding="utf-8").splitlines():
        m = re.match(r"\\newcommand\{\\(\w+)\}\{(.*)\}$", line)
        if m:
            macros[m.group(1)] = m.group(2)
    video = re.search(r"\\newcommand\{\\VideoURL\}\{(.*)\}$", src, re.M).group(1)
    repo = re.search(r"\\newcommand\{\\RepoURL\}\{(.*)\}$", src, re.M).group(1)
    affil = arg(src, src.index(r"\newcommand{\Affil}") + len(r"\newcommand{\Affil}"))[0]
    body = src[src.index(r"\begin{document}") + len(r"\begin{document}"):src.index(r"\end{document}")]
    body = "\n".join(l for l in body.splitlines() if not l.lstrip().startswith("%"))
    body = body.replace(r"\VideoURL", video).replace(r"\RepoURL", repo).replace(r"\Affil", affil)
    body = expand_macros(body, macros)
    body = body.replace("{\\scriptsize\\setlength{\\tabcolsep}{3pt}\n\\input{generated/lit_table_full.tex}}",
                        r"\LITTABLE ")

    with tempfile.TemporaryDirectory() as t:
        tmp = Path(t)
        compile_report(tmp)
        refs = Refs((tmp / "main.aux").read_text(encoding="utf-8"), (tmp / "main.bbl").read_text(encoding="utf-8"))
        pipe = pipeline_png(tmp / "main.pdf", tmp)
        doc = Document()
        setup(doc)
        doc.core_properties.title = "ALL ve AML Lösemi Alt Tip Sınıflandırması: Ara Rapor (düzenleme kopyası)"
        doc.core_properties.author = "Enes AY"
        doc.core_properties.language = "tr-TR"
        b = Builder(doc, refs, pipe)
        b.macros = macros

        start = re.compile(r"\\(section\*?|subsection|title|author|maketitle|appendices|clearpage|onecolumn"
                           r"|bibliographystyle|bibliography|LITTABLE"
                           r"|begin\{(?:abstract|IEEEkeywords|itemize|enumerate|figure\*?|table\*?)\})")
        pos = 0
        while True:
            m = start.search(body, pos)
            b.text(body[pos:m.start()] if m else body[pos:])
            if not m:
                break
            cmd, i = m.group(1), m.end()
            if cmd in ("section", "section*", "subsection"):
                title, i = arg(body, i)
                b.heading(title, 2 if cmd == "subsection" else 1, numbered=cmd != "section*")
                lab = re.match(r"\\label\{[^}]*\}", body[i:])
                i += lab.end() if lab else 0
            elif cmd == "title":
                title, i = arg(body, i)
                main_t, sub_t = split_top(title, r"\\")
                write_runs(doc.add_paragraph(style="Title"), inline(main_t, refs))
                write_runs(doc.add_paragraph(style="Subtitle"), inline(sub_t, refs))
            elif cmd == "author":
                author, i = arg(body, i)
                name = arg(author, author.index(r"\IEEEauthorblockN") + len(r"\IEEEauthorblockN"))[0]
                block = arg(author, author.index(r"\IEEEauthorblockA") + len(r"\IEEEauthorblockA"))[0]
                thanks = arg(author, author.index(r"\thanks") + len(r"\thanks"))[0]
                for k, line in enumerate([name] + split_top(block, r"\\")):
                    p = doc.add_paragraph()
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    p.paragraph_format.space_after = Pt(0)
                    write_runs(p, inline(line.strip(), refs, {"bold": k == 0}))
                p = doc.add_paragraph()
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p.paragraph_format.space_before = Pt(8)
                write_runs(p, inline(thanks, refs), 9.5)
            elif cmd.startswith("begin"):
                env = re.match(r"begin\{([^}]+)\}", cmd).group(1)
                end = body.index(r"\end{" + env + "}", i)
                inner = body[i:end]
                i = end + len(r"\end{" + env + "}")
                if env == "abstract":
                    p = doc.add_paragraph()
                    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
                    write_runs(p, [("Özet—", {"bold": True, "italic": True})] + inline(inner.strip(), refs))
                elif env == "IEEEkeywords":
                    p = doc.add_paragraph()
                    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
                    write_runs(p, [("Anahtar Kelimeler—", {"bold": True, "italic": True})] + inline(inner.strip(), refs))
                elif env in ("itemize", "enumerate"):
                    style = "List Bullet" if env == "itemize" else "List Number"
                    for item in inner.split(r"\item")[1:]:
                        p = doc.add_paragraph(style=style)
                        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
                        write_runs(p, inline(item.strip(), refs))
                elif env.startswith("figure"):
                    b.figure(inner)
                else:
                    b.table(inner)
            elif cmd == "bibliographystyle":
                _, i = arg(body, i)
            elif cmd == "bibliography":
                _, i = arg(body, i)
                b.bibliography()
            elif cmd == "appendices":
                b.appendix, b.sec = True, 0
            elif cmd == "LITTABLE":
                full = expand_gen("generated/lit_table_full.tex", macros)
                b.table(full, source=full)
            pos = i
        doc.save(OUT)
    if unknown:
        print("unhandled:", sorted(unknown))
    print(f"wrote {OUT.relative_to(ROOT)}; figures {b.fig}, tables {b.tab}, references {len(refs.texts)}")


if __name__ == "__main__":
    main()
