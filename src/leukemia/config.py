"""Project-wide constants: paths, random seeds and preprocessing defaults."""
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA_RAW = ROOT / "data" / "raw"
DATA_PROCESSED = ROOT / "data" / "processed"
RESULTS = ROOT / "results"
FIGURES = RESULTS / "figures"
TABLES = RESULTS / "tables"

# Language of generated figures, tables and number macros: "tr" for the interim
# report and slides, "en" for the final paper.
REPORT_LANG = os.environ.get("REPORT_LANG", "tr")

# One global seed for everything that is stochastic (t-SNE, CV splits, models).
SEED = 42
# Seeds for repeated CV in the final report (guide 6.3: at least 5 seeds).
CV_SEEDS = (42, 7, 123, 2024, 31337)

# Label convention required by the course guide: ALL = 0, AML = 1.
LABELS = {"ALL": 0, "AML": 1}
CLASS_NAMES = ("ALL", "AML")

# Clipping window from the course guide. Dudoit et al. (2002) used the same ceiling
# with a floor of 100 and log10; their filter keeps genes with max/min > 5 and
# max-min > 500, which gives 3,571 genes at floor 100 and 3,859 at floor 20.
CLIP_FLOOR = 20.0
CLIP_CEIL = 16000.0
FOLD_MIN = 5.0
DIFF_MIN = 500.0

# Number of top-ranked genes shown in EDA heatmaps.
TOP_GENES = 30
