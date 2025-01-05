import pytesseract
from PIL import Image

def extract_text_from_image(image_path):
    """
    Extract text from an image using Tesseract OCR.
    """
    try:
        return pytesseract.image_to_string(Image.open(image_path))
    except Exception as e:
        print(f"Error extracting text from image: {e}")
        return None
