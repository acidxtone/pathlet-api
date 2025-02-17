import sys
import os
import traceback
import logging
import json
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from werkzeug.exceptions import HTTPException
from backend.services.hugging_face import get_possible_ascendants
from backend.services.numerology import calculate_numerology
from backend.services.human_design import calculate_human_design
from backend.services.compatibility import calculate_compatibility
from backend.utils.validators import (
    validate_birth_date, 
    validate_birth_time, 
    validate_birth_location
)
import dotenv

# Load environment variables
dotenv.load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Verify critical environment variables
HUGGING_FACE_API_KEY = os.getenv('HUGGING_FACE_API_KEY')
if not HUGGING_FACE_API_KEY:
    logger.critical("HUGGING_FACE_API_KEY is not set. API functionality may be limited.")

# Comprehensive path debugging
logger.info(f"Current Working Directory: {os.getcwd()}")
logger.info(f"Python Path: {sys.path}")

# Add the backend directory to the Python path with comprehensive logging
try:
    backend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend'))
    logger.info(f"Attempting to add backend path: {backend_path}")
    
    if not os.path.exists(backend_path):
        logger.error(f"Backend path does not exist: {backend_path}")
    
    sys.path.insert(0, backend_path)
    logger.info(f"Updated Python Path: {sys.path}")
except Exception as path_error:
    logger.error(f"Path resolution error: {path_error}")
    logger.error(traceback.format_exc())

app = Flask(__name__, static_folder='../frontend')
CORS(app)  # Enable CORS for all routes

# Global error handler
@app.errorhandler(Exception)
def handle_error(e):
    """
    Global error handler for all exceptions.
    
    Args:
        e (Exception): Caught exception
    
    Returns:
        tuple: JSON error response and HTTP status code
    """
    logger.error(f"Unhandled Exception: {e}")
    logger.error(traceback.format_exc())
    
    # Handle known HTTP exceptions
    if isinstance(e, HTTPException):
        return jsonify(error=str(e)), e.code
    
    # Handle validation errors
    if isinstance(e, ValueError):
        return jsonify(error=str(e)), 400
    
    # Generic server error for unexpected exceptions
    return jsonify(error='Internal Server Error'), 500

@app.route('/')
def serve_frontend():
    """
    Serve the main frontend application.
    """
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/get_ascendants', methods=['POST'])
def ascendant_endpoint():
    """
    Endpoint to retrieve possible ascendant signs.
    
    Expected JSON payload:
    {
        "birth_date": "YYYY-MM-DD",
        "birth_location": "City, Country"
    }
    """
    try:
        data = request.get_json()
        
        # Validate input
        validate_birth_date(data.get('birth_date'))
        validate_birth_location(data.get('birth_location'))
        
        # Calculate ascendants
        result = get_possible_ascendants(
            data['birth_date'], 
            data['birth_location']
        )
        
        logger.info(f"Ascendant calculation for {data['birth_date']} successful")
        return jsonify(result), 200
    
    except ValueError as ve:
        logger.error(f"Validation Error: {str(ve)}")
        return jsonify({
            "error": "Invalid input",
            "details": str(ve)
        }), 400
    
    except Exception as e:
        logger.error(f"Unexpected error in ascendant calculation: {str(e)}")
        return jsonify({
            "error": "Calculation failed",
            "details": "Unable to determine ascendant signs"
        }), 500

@app.route('/calculate_numerology', methods=['POST'])
def numerology_endpoint():
    """
    Endpoint to calculate numerological insights.
    
    Expected JSON payload:
    {
        "birth_date": "YYYY-MM-DD"
    }
    """
    try:
        data = request.get_json()
        
        # Validate input
        validate_birth_date(data.get('birth_date'))
        
        # Calculate numerology
        result = calculate_numerology(data['birth_date'])
        
        logger.info(f"Numerology calculation for {data['birth_date']} successful")
        return jsonify(result), 200
    
    except ValueError as ve:
        logger.error(f"Validation Error: {str(ve)}")
        return jsonify({
            "error": "Invalid input",
            "details": str(ve)
        }), 400
    
    except Exception as e:
        logger.error(f"Unexpected error in numerology calculation: {str(e)}")
        return jsonify({
            "error": "Calculation failed",
            "details": "Unable to determine numerological insights"
        }), 500

@app.route('/calculate_human_design', methods=['POST'])
def human_design_endpoint():
    """
    Endpoint to calculate Human Design type.
    
    Expected JSON payload:
    {
        "birth_date": "YYYY-MM-DD",
        "birth_time": "HH:MM AM/PM",
        "birth_location": "City, Country"
    }
    """
    try:
        data = request.get_json()
        
        # Validate input
        validate_birth_date(data.get('birth_date'))
        
        # Optional parameters
        birth_time = data.get('birth_time')
        birth_location = data.get('birth_location')
        
        # Validate optional parameters if provided
        if birth_time:
            validate_birth_time(birth_time)
        
        # Calculate Human Design
        result = calculate_human_design(
            data['birth_date'], 
            birth_time, 
            birth_location
        )
        
        logger.info(f"Human Design calculation for {data['birth_date']} successful")
        return jsonify(result), 200
    
    except ValueError as ve:
        logger.error(f"Validation Error: {str(ve)}")
        return jsonify({
            "error": "Invalid input",
            "details": str(ve)
        }), 400
    
    except Exception as e:
        logger.error(f"Unexpected error in Human Design calculation: {str(e)}")
        return jsonify({
            "error": "Calculation failed",
            "details": "Unable to determine Human Design type"
        }), 500

@app.route('/calculate_compatibility', methods=['POST'])
def compatibility_endpoint():
    """
    Endpoint to calculate comprehensive compatibility.
    
    Expected JSON payload:
    {
        "person1": {
            "birth_date": "YYYY-MM-DD",
            "birth_time": "HH:MM AM/PM",
            "birth_location": "City, Country"
        },
        "person2": {
            "birth_date": "YYYY-MM-DD",
            "birth_time": "HH:MM AM/PM",
            "birth_location": "City, Country"
        }
    }
    """
    try:
        data = request.get_json()
        
        # Validate inputs
        validate_birth_date(data['person1']['birth_date'])
        validate_birth_date(data['person2']['birth_date'])
        
        # Optional parameter validations
        if data['person1'].get('birth_time'):
            validate_birth_time(data['person1']['birth_time'])
        if data['person2'].get('birth_time'):
            validate_birth_time(data['person2']['birth_time'])
        
        # Calculate compatibility
        result = calculate_compatibility(
            data['person1'], 
            data['person2']
        )
        
        logger.info(f"Compatibility calculation successful")
        return jsonify(result), 200
    
    except ValueError as ve:
        logger.error(f"Validation Error: {str(ve)}")
        return jsonify({
            "error": "Invalid input",
            "details": str(ve)
        }), 400
    
    except Exception as e:
        logger.error(f"Unexpected error in compatibility calculation: {str(e)}")
        return jsonify({
            "error": "Calculation failed",
            "details": "Unable to determine compatibility"
        }), 500

@app.route('/<path:path>')
def serve_static(path):
    """
    Serve static files from the frontend directory.
    """
    return send_from_directory(app.static_folder, path)

@app.route('/home')
def home():
    """
    Home endpoint with system health check
    """
    return jsonify({
        "message": "Pathlet API is running!",
        "version": "1.1.0",
        "environment_check": {
            "hugging_face_api_key": "Configured" if HUGGING_FACE_API_KEY else "Not Set"
        },
        "endpoints": [
            "/get_ascendants", 
            "/calculate_numerology", 
            "/calculate_human_design", 
            "/calculate_compatibility"
        ]
    })

def handler(event, context):
    """
    Comprehensive Vercel serverless function handler
    """
    return app(event, context)

if __name__ == '__main__':
    app.run(debug=True)
