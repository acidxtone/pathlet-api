from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from services.hugging_face import get_possible_ascendants
from services.numerology import calculate_numerology
from services.human_design import calculate_human_design
from utils.validators import validate_request_data
from config.settings import Config

app = Flask(__name__)
app.config.from_object(Config)

# Rate Limiting
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=[f"{Config.REQUEST_LIMIT_PER_MINUTE} per minute"]
)

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
@limiter.limit("10 per minute")
def get_ascendants():
    """
    Endpoint to estimate possible ascendant signs.
    
    Returns:
        JSON response with possible ascendants or error
    """
    data = request.json
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

@app.route('/calculate_all', methods=['POST'])
@limiter.limit("10 per minute")
def calculate_all():
    """
    Comprehensive endpoint to calculate all insights.
    
    Returns:
        JSON response with various insights or error
    """
    data = request.json
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

if __name__ == '__main__':
    app.run(debug=Config.DEBUG)
