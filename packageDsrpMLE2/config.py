from pathlib import Path

from loguru import logger

# Paths
PROJ_ROOT = Path(__file__).resolve().parents[1]
logger.info(f"La ruta del proyecto es: {PROJ_ROOT}")

DATA_DIR = PROJ_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
CSV_FILE = RAW_DIR / "PJME_hourly.csv"
MODELS_DIR = PROJ_ROOT / "models"
REPORTS_DIR = PROJ_ROOT / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"
FEAST_PROJ_DIR = PROJ_ROOT / "FR_MLE2" / "feature_repo"
PARQUET_PATH = PROCESSED_DIR / "ec_ft.parquet"

rutas = {
"DATA_DIR":DATA_DIR,
"RAW_DIR":RAW_DIR,
"PROCESSED_DIR":PROCESSED_DIR,
"CSV_FILE":CSV_FILE,
"MODELS_DIR":MODELS_DIR,
"REPORTS_DIR":REPORTS_DIR,
"FIGURES_DIR":FIGURES_DIR,
"FEAST_PROJ_DIR":FEAST_PROJ_DIR,
"PARQUET_PATH":PARQUET_PATH
}

for i in rutas:
    logger.info(f"Variable {i} = {rutas[i]}")