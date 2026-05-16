"""
يُحمَّل تلقائياً عند build على Render.
يجلب major_model.pkl من Google Drive لو غير موجود.
"""
import os
from pathlib import Path

MODELS_DIR = Path(__file__).parent / "models"
MODEL_PATH = MODELS_DIR / "major_model.pkl"

# ← ضعي هنا رابط Google Drive بعد رفع الملف
GDRIVE_FILE_ID = os.getenv("MAJOR_MODEL_GDRIVE_ID", "")


def download():
    if MODEL_PATH.exists():
        print("✅ major_model.pkl موجود — لا حاجة للتحميل")
        return
    if not GDRIVE_FILE_ID:
        print("⚠️  MAJOR_MODEL_GDRIVE_ID غير محدد — ميزة التنبؤ بالتخصص غير متاحة")
        return
    try:
        import urllib.request
        url = f"https://drive.google.com/uc?export=download&id={GDRIVE_FILE_ID}&confirm=t"
        print(f"⏳ جاري تحميل major_model.pkl من Google Drive...")
        MODELS_DIR.mkdir(exist_ok=True)
        urllib.request.urlretrieve(url, MODEL_PATH)
        print(f"✅ تم تحميل major_model.pkl ({MODEL_PATH.stat().st_size//1024//1024}MB)")
    except Exception as e:
        print(f"❌ فشل تحميل النموذج: {e}")


if __name__ == "__main__":
    download()
