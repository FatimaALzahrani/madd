"""
إعدادات ومسارات مشروع الباك-اند.
كل المسارات مطلقة (absolute) عشان تشتغل من أي مكان تشغّل منه الأمر.
"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

MODELS_DIR = BASE_DIR / "models"


CLASSIFICATION_MODEL_PATH = Path(
    os.getenv("CLASSIFICATION_MODEL_PATH", MODELS_DIR / "arabert_offensive_model")
)

TESSERACT_CMD_WINDOWS = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

HOST = "0.0.0.0"
PORT = 8000
