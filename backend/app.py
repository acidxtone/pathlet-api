import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

# Create Flask application
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Minimal configuration
app.config['DEBUG'] = False
app.config['ENV'] = 'production'

@app.route('/')
def home():
    """
    Minimal root endpoint
    """
    return jsonify({
        'status': 'ok',
        'message': 'Pathlet API is running'
    }), 200

@app.route('/healthz')
def health_check():
    """
    Health check endpoint
    """
    return jsonify({
        'status': 'healthy',
        'environment': os.getenv('FLASK_ENV', 'unknown')
    }), 200

@app.route('/get_ascendants', methods=['POST'])
def get_ascendants():
    """
    Mock endpoint for ascendant retrieval
    """
    data = request.json
    birth_date = data.get('birth_date')
    birth_location = data.get('birth_location', '')

    # Mock data for demonstration
    possible_ascendants = [
        'Aries', 'Taurus', 'Gemini', 'Cancer', 
        'Leo', 'Virgo', 'Libra', 'Scorpio', 
        'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces'
    ]

    return jsonify({
        "possible_ascendants": possible_ascendants,
        "instructions": "Review the listed Ascendants and choose the one that resonates most with you."
    }), 200

@app.route('/calculate_all', methods=['POST'])
def calculate_all():
    """
    Mock endpoint for comprehensive calculations
    """
    data = request.json
    birth_date = data.get('birth_date')
    birth_time = data.get('birth_time', '')
    birth_location = data.get('birth_location', '')

    # Mock data for demonstration
    return jsonify({
        "numerology": {
            "life_path_number": 7,
            "destiny_number": 5,
            "soul_urge_number": 3
        },
        "human_design": {
            "type": "Generator",
            "strategy": "Wait to Respond",
            "authority": "Sacral"
        },
        "birth_time": birth_time
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
