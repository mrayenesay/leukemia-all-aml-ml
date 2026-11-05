# Literature search log

Project: ALL vs. AML classification (Golub et al. 1999; external validation on MILE GSE13159 and Andersson 2007 GSE7186)
Search and verification date: 2026-11-03

## Databases and services used

| Source | Use |
|---|---|
| Crossref REST API (`api.crossref.org/works`) | Finding records by keyword, and checking the metadata for every DOI |
| Europe PMC REST API (`ebi.ac.uk/europepmc`) | Full-text keyword search; abstracts; open-access full text (XML) |
| PubMed / NCBI E-utilities (esearch, efetch) | Abstracts looked up by DOI; PMC full text for older papers |
| NCBI GEO (`acc.cgi`, text view) | Checking which publications are linked to GSE7186 and GSE13159 |
| arXiv abstract pages, NeurIPS proceedings, JMLR | Checking items that have no DOI |

Google Scholar and general web search were **not** used, so no record comes from them. All discovery used the APIs listed above.

## Date range

- Classic and foundational items, 1999–2020: added because the coverage list names them. They were not found by searching. Each one was looked up by its DOI.
- Recent items: searches were filtered to `from-pub-date:2021-01-01` (Crossref) or `PUB_YEAR:[2021 TO 2026]` (Europe PMC).

## Exact queries

Crossref, keyword discovery:

1. `query=golub leukemia gene expression classification` with `filter=from-pub-date:2021-01-01,type:journal-article`, `rows=40`
2. `query=ALL AML leukemia microarray feature selection classification` with `filter=from-pub-date:2021-01-01,type:journal-article`, `rows=40`
3. `query=machine learning cancer classification gene expression data review` with `filter=from-pub-date:2021-01-01,type:journal-article`, `rows=20`
4. `query=leukemia transcriptome machine learning classification acute leukemia subtypes RNA-seq microarray` with `filter=from-pub-date:2021-01-01,type:journal-article`, `rows=25`
5. `query=Andersson microarray-based classification consecutive series 121 childhood acute leukemias` with `filter=from-pub-date:2007-01-01,until-pub-date:2007-12-31`, `rows=5`. This was needed to correct the DOI (see Notes).
6. `query=GenePT simple but effective foundation model genes cells ChatGPT Chen Zou`, `rows=5` (4 records returned before an output error)

Europe PMC, full-text search:

7. `"7129" AND "72 samples" AND (leukemia OR leukaemia) AND (classification) AND PUB_YEAR:[2021 TO 2026] AND SRC:MED` (18 hits)

Lookups by known identifier:

- Crossref `works/<DOI>` for all 27 DOIs in `references.bib`, plus the GenePT bioRxiv DOI 10.1101/2023.10.16.562533.
- JMLR v11 cawley10a, arXiv 2106.11959, arXiv 2207.08815, NeurIPS 2021 and 2022 proceedings pages.
- GEO GSE7186 and GSE13159.

## Inclusion criteria

- Peer-reviewed journal article or peer-reviewed conference paper (NeurIPS, including the Datasets and Benchmarks track). A preprint was accepted only when a peer-reviewed version could be cited instead (GenePT: Nat. Biomed. Eng. 2025).
- Directly relevant to one of the following:
  - (a) the datasets used;
  - (b) classic machine learning or feature selection on microarrays;
  - (c) validation bias or batch effects;
  - (d) recent machine learning or deep learning for leukemia or cancer gene-expression classification, or for small-n tabular data.
- Metadata (title, first author, year, venue, volume, pages) matches the Crossref record or the official proceedings or journal page.
- For "papers that report results on Golub": the full text had to show the Golub data (72 samples, 47 ALL / 25 AML, 7129 genes), and any result recorded had to be visible in that text.

## Exclusion criteria

- Conference abstracts and posters (for example the many *Clin Lymphoma Myeloma Leuk* and *Leuk Res* abstract supplements), and withdrawn papers.
- Imaging-based leukemia work (blood smears) and studies not about gene expression.
- Studies whose leukemia data were not the Golub set:
  - Ilyas 2023 PLOS ONE (CuMiDa GSE9476)
  - Mahmood 2025 Leuk Res (CuMiDa, 281 samples)
  - Park & Miyano 2025 (cell lines)
- Studies where the Golub dataset or a Golub-specific result could not be confirmed from the abstract or full text fetched:
  - Shukla 2025 Sci Rep
  - Rahimi 2023 JCRCO
  - Fourquet 2025 BMC Bioinf
  - Dhamercherla 2025 Front Genet
- Low-visibility or unindexed venues, where a stronger alternative already covered the topic. Examples are IJCA, IJDKP and similar.
- Kept to the 30-reference cap. Some eligible papers were left out for this reason (for example Osama 2023 ESWA and Mazlan 2021 Processes reviews).

## Counts

| Stage | n |
|---|---|
| Records screened from discovery queries 1–7 (titles; duplicates included) | 152 |
| Abstracts screened (Europe PMC / PubMed) | 24 |
| Full texts assessed during the search (PMC XML) | 5 (Selvaraj 2024, Awotunde 2022, Xie 2022, Rezaee 2022, Díaz-Uriarte 2006) |
| Full texts consulted in the later claim audit (2026-11-05, AI-assisted) | 31 of 38; 6 abstract only; 1 citation only (see `reading_notes.md`) |
| Known classic/foundational items added by identifier | 22 |
| Included from discovery searches | 8 (Alhenawi 2022, Alharbi 2023, Selvaraj 2024, Awotunde 2022, Xie 2022, Rezaee 2022; plus the corrected Andersson 2007 DOI and the GenePT journal version) |
| **Final included** | **30** (30 peer-reviewed; 11 published 2021 or later) |
| Dropped as unverifiable | 0 |

## Notes from verification

- **Andersson 2007.** The DOI that first came to mind, 10.1038/sj.leu.2404657, resolves to a different paper (Sengupta et al., CML signalling). The correct DOI is **10.1038/sj.leu.2404688**: Leukemia 21(6):1198–1203. GEO GSE7186 lists PMID 17410184, which is this paper.
- **GSE13159.** GEO links it to both Kohlmann 2008 (PMID 18573112) and Haferlach 2010 (PMID 20406941). It is the MILE **stage 1** data.
- **Grinsztajn 2022.** The proceedings title ends "…on *typical* tabular data?". The arXiv title does not include "typical". The bib uses the proceedings title.
- **GenePT.** Cited as Chen & Zou, Nat. Biomed. Eng. 9(4):483–493 (2025). The journal title differs from the bioRxiv title.
- **Armstrong 2002.** Crossref gives online publication 2001-12-03 and print 2002-01 (vol. 30, no. 1). The bib uses 2002.
- **Values in "best_result".** These were copied from the text that was actually fetched: an abstract or a PMC full-text table. Where the fetched text did not report a Golub-specific number, the cell says "n/r".
