from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv
from backend.services.hugging_face import get_possible_ascendants
from backend.services.numerology import calculate_numerology
from backend.services.human_design import calculate_human_design
from backend.services.compatibility import calculate_compatibility

load_dotenv()

app = Flask(__name__)

# Hugging Face Configuration
HUGGING_FACE_API_KEY = os.getenv("HUGGING_FACE_API_KEY")
HUGGING_FACE_MODEL = "google/flan-t5-large"

@app.route('/')
def home():
    """
    Home endpoint for Hugging Face Space
    """
    return jsonify({
        "message": "Pathlet API is running!",
        "version": "1.1.0",
        "endpoints": [
            "/get_ascendants", 
            "/calculate_numerology", 
            "/calculate_human_design", 
            "/calculate_compatibility"
        ]
    })

@app.route('/get_ascendants', methods=['POST'])
def get_ascendants():
    """
    Endpoint to get possible ascendant signs
    """
    try:
        data = request.get_json()
        result = get_possible_ascendants(
            data['birth_date'], 
            data['birth_location']
        )
        return jsonify(result), 200
    except Exception as e:
        return jsonify({
            "error": "Ascendant calculation failed",
            "details": str(e)
        }), 500

@app.route('/calculate_numerology', methods=['POST'])
def numerology_endpoint():
    """
    Endpoint to calculate numerology insights
    """
    try:
        data = request.get_json()
        result = calculate_numerology(data['birth_date'])
        return jsonify(result), 200
    except Exception as e:
        return jsonify({
            "error": "Numerology calculation failed",
            "details": str(e)
        }), 500

@app.route('/calculate_human_design', methods=['POST'])
def human_design_endpoint():
    """
    Endpoint to calculate human design insights
    """
    try:
        data = request.get_json()
        result = calculate_human_design(
            data['birth_date'],
            data.get('birth_time'),
            data.get('birth_location')
        )
        return jsonify(result), 200
    except Exception as e:
        return jsonify({
            "error": "Human Design calculation failed",
            "details": str(e)
        }), 500

@app.route('/calculate_compatibility', methods=['POST'])
def compatibility_endpoint():
    """
    Endpoint to calculate comprehensive compatibility
    """
    try:
        data = request.get_json()
        result = calculate_compatibility(
            data['person1'], 
            data['person2']
        )
        return jsonify(result), 200
    except Exception as e:
        return jsonify({
            "error": "Compatibility calculation failed",
            "details": str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True)
