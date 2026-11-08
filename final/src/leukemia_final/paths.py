"""Output locations of the final phase (kept apart from the interim results/)."""
from pathlib import Path

FINAL = Path(__file__).resolve().parents[2]
RESULTS = FINAL / "results"
FIGURES = RESULTS / "figures"
TABLES = RESULTS / "tables"
LOCK_LOG = RESULTS / "locked_test_log.json"
