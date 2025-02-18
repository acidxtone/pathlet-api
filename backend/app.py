import os
from flask import Flask, jsonify
from flask_cors import CORS

# Create Flask application
app = Flask(__name__)
CORS(app)

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
