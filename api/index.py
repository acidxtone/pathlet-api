import sys
import os
import traceback
import logging
import json

# Enhanced logging configuration
logging.basicConfig(
    level=logging.DEBUG, 
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

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

from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

# Wrap import in try-except for detailed error tracking
try:
    from backend.services.hugging_face import get_possible_ascendants
    from backend.services.numerology import calculate_numerology
    from backend.services.human_design import calculate_human_design
    from backend.utils.validators import validate_request_data, ValidationError
    logger.info("Successfully imported backend modules")
except ImportError as import_error:
    logger.error(f"Import Error: {import_error}")
    logger.error(f"Sys Path: {sys.path}")
    logger.error(traceback.format_exc())
    raise

app = Flask(__name__)

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
    if isinstance(e, ValidationError):
        return jsonify(error=str(e)), 400
    
    # Generic server error for unexpected exceptions
    return jsonify(error='Internal Server Error'), 500

def assign_birth_time(selected_ascendant):
    """
    Assign estimated birth time based on selected ascendant.
    
    Args:
        selected_ascendant (str): Selected ascendant sign
    
    Returns:
        str: Estimated birth time range
    """
    ascendant_time_ranges = {
        "Aries": "04:00 AM - 06:00 AM",
        "Taurus": "06:00 AM - 08:00 AM",
        "Gemini": "08:00 AM - 10:00 AM",
        "Cancer": "10:00 AM - 12:00 PM",
        "Leo": "12:00 PM - 02:00 PM",
        "Virgo": "02:00 PM - 04:00 PM",
        "Libra": "04:00 PM - 06:00 PM",
        "Scorpio": "06:00 PM - 08:00 PM",
        "Sagittarius": "08:00 PM - 10:00 PM",
        "Capricorn": "10:00 PM - 12:00 AM",
        "Aquarius": "12:00 AM - 02:00 AM",
        "Pisces": "02:00 AM - 04:00 AM"
    }
    return ascendant_time_ranges.get(selected_ascendant, "Unknown Time Range")

@app.route('/')
def home():
    """
    Home route to confirm API is running.
    
    Returns:
        JSON response with welcome message
    """
    logger.info("Home route accessed")
    return jsonify({
        "message": "Pathlet API is running! Use the available endpoints.",
        "version": "1.0.0",
        "endpoints": ["/get_ascendants", "/calculate_all"]
    })

@app.route('/get_ascendants', methods=['POST'])
def get_ascendants():
    """
    Endpoint to estimate possible ascendant signs.
    
    Returns:
        JSON response with possible ascendants or error
    """
    try:
        # Validate request data
        data = request.get_json()
        validated_data = validate_request_data(data)
        
        # Get possible ascendants
        ascendants = get_possible_ascendants(
            validated_data['birth_date'], 
            validated_data['birth_location']
        )
        
        logger.info(f"Ascendants calculated: {ascendants}")
        return jsonify({
            "possible_ascendants": ascendants,
            "instructions": "Review the listed Ascendants and choose the one that resonates most with you."
        })
    
    except ValidationError as ve:
        logger.error(f"Validation Error in get_ascendants: {ve}")
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        logger.error(f"Error in get_ascendants: {e}")
        logger.error(traceback.format_exc())
        return jsonify({"error": "Failed to calculate ascendants"}), 500

@app.route('/calculate_all', methods=['POST'])
def calculate_all():
    """
    Comprehensive endpoint to calculate all insights.
    
    Returns:
        JSON response with various insights or error
    """
    try:
        # Validate request data
        data = request.get_json()
        validated_data = validate_request_data(data)
        
        # If no birth time and an ascendant is selected, estimate time
        if not validated_data.get("birth_time") and "selected_ascendant" in validated_data:
            validated_data["birth_time"] = assign_birth_time(validated_data["selected_ascendant"])
        
        human_design = calculate_human_design(
            validated_data['birth_date'], 
            validated_data['birth_time'],
            validated_data['birth_location']
        )
        
        numerology = calculate_numerology(
            validated_data['birth_date']
        )
        
        logger.info("All calculations completed successfully")
        return jsonify({
            "human_design": human_design,
            "numerology": numerology,
            "birth_time": validated_data['birth_time']
        })
    
    except ValidationError as ve:
        logger.error(f"Validation Error in calculate_all: {ve}")
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        logger.error(f"Error in calculate_all: {e}")
        logger.error(traceback.format_exc())
        return jsonify({"error": "Failed to calculate insights"}), 500

def handler(event, context):
    """
    Comprehensive Vercel serverless function handler with robust error management
    
    Args:
        event (dict): Serverless event data
        context (dict): Serverless context
    
    Returns:
        dict: Standardized response with error handling
    """
    try:
        logger.info(f"Received serverless event: {event}")
        
        # Extract request details
        method = event.get('httpMethod', 'GET')
        path = event.get('path', '/')
        body = event.get('body', '{}')
        
        # Simulate Flask request context
        with app.request_context(environ={
            'REQUEST_METHOD': method,
            'PATH_INFO': path,
            'wsgi.input': body
        }):
            # Dispatch request through Flask
            response = app.full_dispatch_request()
        
        # Convert Flask response to Vercel response format
        return {
            'statusCode': response.status_code,
            'body': response.get_data(as_text=True),
            'headers': dict(response.headers)
        }
    
    except Exception as e:
        # Log full traceback for debugging
        logger.error(f"Serverless Handler Error: {str(e)}")
        logger.error(traceback.format_exc())
        
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': 'Internal Server Error',
                'details': str(e),
                'traceback': traceback.format_exc()
            }),
            'headers': {'Content-Type': 'application/json'}
        }

if __name__ == '__main__':
    app.run(debug=True)
