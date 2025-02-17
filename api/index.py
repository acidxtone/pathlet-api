import sys
import os
import traceback
import logging
import json

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Add the backend directory to the Python path
backend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend'))
sys.path.insert(0, backend_path)

from flask import Flask, request, jsonify
from backend.services.hugging_face import get_possible_ascendants
from backend.services.numerology import calculate_numerology
from backend.services.human_design import calculate_human_design
from backend.utils.validators import validate_request_data

app = Flask(__name__)

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
    return jsonify({"message": "Pathlet API is running! Use the available endpoints."})

@app.route('/get_ascendants', methods=['POST'])
def get_ascendants():
    """
    Endpoint to estimate possible ascendant signs.
    
    Returns:
        JSON response with possible ascendants or error
    """
    try:
        data = request.get_json()
        is_valid, error_message = validate_request_data(data)
        
        if not is_valid:
            return jsonify({"error": error_message}), 400
        
        birth_date = data.get("birth_date")
        birth_location = data.get("birth_location")
        
        ascendants = get_possible_ascendants(birth_date, birth_location)
        return jsonify({
            "possible_ascendants": ascendants,
            "instructions": "Review the listed Ascendants and choose the one that resonates most with you."
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/calculate_all', methods=['POST'])
def calculate_all():
    """
    Comprehensive endpoint to calculate all insights.
    
    Returns:
        JSON response with various insights or error
    """
    try:
        data = request.get_json()
        is_valid, error_message = validate_request_data(data)
        
        if not is_valid:
            return jsonify({"error": error_message}), 400
        
        birth_date = data.get("birth_date")
        birth_time = data.get("birth_time", "")
        birth_location = data.get("birth_location")
        
        # If no birth time and an ascendant is selected, estimate time
        if not birth_time and "selected_ascendant" in data:
            birth_time = assign_birth_time(data["selected_ascendant"])
        
        human_design = calculate_human_design(birth_date, birth_time, birth_location)
        numerology = calculate_numerology(birth_date)
        
        return jsonify({
            "human_design": human_design,
            "numerology": numerology,
            "birth_time": birth_time
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

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
        logger.info(f"Received event: {event}")
        
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
