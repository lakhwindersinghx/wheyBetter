from flask import Flask
from controllers.ingredient_controller import ingredient_bp

app = Flask(__name__)

# Register the blueprint for ingredients
app.register_blueprint(ingredient_bp, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)
