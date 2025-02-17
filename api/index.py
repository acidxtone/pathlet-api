import os
import sys
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
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('vercel_deployment.log')
    ]
)
logger = logging.getLogger(__name__)

# Comprehensive path resolution
def setup_python_path():
    try:
        # Determine absolute paths
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.abspath(os.path.join(current_dir, '..'))
        backend_path = os.path.join(project_root, 'backend')
        
        # Log path information
        logger.info(f"Current Directory: {current_dir}")
        logger.info(f"Project Root: {project_root}")
        logger.info(f"Backend Path: {backend_path}")
        
        # Verify paths exist
        if not os.path.exists(project_root):
            logger.error(f"Project root does not exist: {project_root}")
        if not os.path.exists(backend_path):
            logger.error(f"Backend path does not exist: {backend_path}")
        
        # Add paths to Python path
        sys.path.insert(0, project_root)
        sys.path.insert(0, backend_path)
        
        logger.info(f"Updated Python Path: {sys.path}")
    except Exception as path_error:
        logger.critical(f"Path resolution error: {path_error}")
        logger.error(traceback.format_exc())

# Setup paths before any imports
setup_python_path()

# Import Flask application with error handling
try:
    from backend.app import app as application
except ImportError as import_error:
    logger.critical(f"Failed to import Flask application: {import_error}")
    logger.error(traceback.format_exc())
    application = None
except Exception as e:
    logger.critical(f"Unexpected error importing application: {e}")
    logger.error(traceback.format_exc())
    application = None

# Verify critical environment variables
HUGGING_FACE_API_KEY = os.getenv('HUGGING_FACE_API_KEY')
if not HUGGING_FACE_API_KEY:
    logger.critical("HUGGING_FACE_API_KEY is not set. API functionality may be limited.")

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
    # Log incoming event details
    logger.info(f"Received event: {json.dumps(event, indent=2)}")
    
    # Check application initialization
    if not application:
        error_response = {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                'error': 'Internal Server Error',
                'message': 'Flask application failed to initialize',
                'details': 'Check server logs for more information'
            })
        }
        logger.critical("Flask application not initialized")
        return error_response
    
    try:
        # Optional: Add request preprocessing or validation
        logger.info("Processing request")
        
        # For Vercel serverless, we might need to adapt the request
        if isinstance(event, dict):
            # Convert Vercel event to a format Flask can understand
            # This is a placeholder and might need adjustment
            from flask import Request
            flask_request = Request(event)
            
            # Process the request
            with application.request_context(flask_request):
                response = application.full_dispatch_request()
                
            return {
                'statusCode': response.status_code,
                'headers': dict(response.headers),
                'body': response.get_data(as_text=True)
            }
        
        # Fallback to default application handling
        return application
    
    except Exception as e:
        logger.error(f"Serverless handler error: {e}")
        logger.error(traceback.format_exc())
        
        error_response = {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                'error': 'Internal Server Error',
                'message': str(e),
                'traceback': traceback.format_exc()
            })
        }
        return error_response

# For local development and testing
if __name__ == '__main__':
    if application:
        application.run(debug=True)
    else:
        logger.critical("Cannot start application: Initialization failed")
