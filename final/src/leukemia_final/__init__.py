"""Final-phase code (models, nested CV, bonuses).

It reuses the interim package ``leukemia`` (loaders, preprocessing, seeds)
without changing it; that package is made importable here.
"""
import sys
from pathlib import Path

_REPO_SRC = Path(__file__).resolve().parents[3] / "src"
if str(_REPO_SRC) not in sys.path:
    sys.path.insert(0, str(_REPO_SRC))
