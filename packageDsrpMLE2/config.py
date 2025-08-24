from pathlib import Path

from loguru import logger

# Paths
PROJ_ROOT = Path(__file__).resolve().parents[1]
logger.info(f"La ruta del proyecto es: {PROJ_ROOT}")

DATA_DIR = PROJ_ROOT / "data"
CSV_FILE = DATA_DIR / "fake_bills.csv"
MODELS_DIR = PROJ_ROOT / "models"
REPORTS_DIR = PROJ_ROOT / "reports"