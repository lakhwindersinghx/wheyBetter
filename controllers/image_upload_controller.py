import os
import pymysql
from flask import Blueprint, request, jsonify, make_response
from werkzeug.utils import secure_filename
from utils.ocr_util import extract_text_from_image
from services.nutrition_service import analyze_nutritional_info
from services.ingredient_service import analyze_ingredients
from flask_cors import CORS
from database import connect_to_mysql

# Flask Blueprint
image_upload_bp = Blueprint("image_upload", __name__)
UPLOAD_FOLDER = "./uploads"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}
CORS(image_upload_bp)

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

def split_label_sections(extracted_text):
    """
    Splits extracted text into nutrition facts and ingredient list.
    """
    lines = extracted_text.split("\n")
    nutrition_section = []
    ingredient_section = []
    current_section = None

    for line in lines:
        line = line.strip()

        if "Amount Per Serving" in line or "Calories" in line:
            current_section = "nutrition"
        elif "Other Ingredients" in line or "Ingredients" in line:
            current_section = "ingredients"

        if current_section == "nutrition":
            nutrition_section.append(line)
        elif current_section == "ingredients":
            ingredient_section.append(line)

    return " ".join(nutrition_section).strip(), " ".join(ingredient_section).strip()

@image_upload_bp.route("/upload-label", methods=["POST"])
def upload_label():
    try:
        file_key = list(request.files.keys())[0]
        file = request.files[file_key]

        # Save uploaded file
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)

        # Perform OCR
        extracted_text = extract_text_from_image(file_path)
        if not extracted_text:
            return make_response(jsonify({"error": "Failed to extract text from the image"}), 500)

        # Split the label into sections
        nutrition_text, ingredient_text = split_label_sections(extracted_text)

        # Analyze extracted nutrition information
        nutrition_info = analyze_nutritional_info(nutrition_text)

        # Analyze extracted ingredients
        final_ingredients, ingredient_analysis = analyze_ingredients(ingredient_text)

        # Create response
        response = make_response(
            jsonify({
                "message": "File uploaded successfully",
                "nutrition_info": nutrition_info,
                "final_ingredients": final_ingredients,
                "analysis": ingredient_analysis,
            }), 200
        )

        response.headers["Access-Control-Allow-Origin"] = "*"
        return response

    except Exception as e:
        print(f"Error: {e}")
        return make_response(jsonify({"error": f"Internal server error: {str(e)}"}), 500)
