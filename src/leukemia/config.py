"""Project-wide constants: paths, random seeds and preprocessing defaults."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA_RAW = ROOT / "data" / "raw"
DATA_PROCESSED = ROOT / "data" / "processed"
RESULTS = ROOT / "results"
FIGURES = RESULTS / "figures"
TABLES = RESULTS / "tables"

# One global seed for everything that is stochastic (t-SNE, CV splits, models).
SEED = 42
# Seeds for repeated CV in the final report (guide 6.3: at least 5 seeds).
CV_SEEDS = (42, 7, 123, 2024, 31337)

# Label convention required by the course guide: ALL = 0, AML = 1.
LABELS = {"ALL": 0, "AML": 1}
CLASS_NAMES = ("ALL", "AML")

# Hu6800 (MAS4/GeneChip average-difference) preprocessing used by Dudoit et al.
# (2002): clip to [20, 16000] and keep genes with max/min > 5 and max-min > 500.
CLIP_FLOOR = 20.0
CLIP_CEIL = 16000.0
FOLD_MIN = 5.0
DIFF_MIN = 500.0

# Number of top-ranked genes shown in EDA heatmaps.
TOP_GENES = 50
