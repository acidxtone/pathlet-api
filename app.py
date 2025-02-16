from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

HUGGING_FACE_API_KEY = os.getenv("HUGGING_FACE_API_KEY")
HUGGING_FACE_MODEL = "mistral-7b"

def query_hugging_face(prompt):
    url = f"https://api-inference.huggingface.co/models/{HUGGING_FACE_MODEL}"
    headers = {"Authorization": f"Bearer {HUGGING_FACE_API_KEY}"}
    data = {"inputs": prompt}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

def calculate_human_design(birth_date, birth_time, birth_location):
    return {
        "type": "Projector",
        "strategy": "Wait for the Invitation",
        "authority": "Splenic",
        "not_self_theme": "Bitterness",
        "signature": "Success"
    }

def calculate_numerology(birth_date):
    personal_year = (sum(map(int, birth_date.split('-'))) % 9) or 9
    return {"personal_year": personal_year}

def calculate_astrology_purpose(birth_date, birth_time, birth_location):
    prompt = f"Generate a concise life purpose statement based on astrology for someone born on {birth_date} at {birth_time} in {birth_location}."
    result = query_hugging_face(prompt)
    return {"life_purpose_snippet": result.get("generated_text", "Purpose could not be determined.")}

def estimate_birth_time(data):
    return {
        "final_estimated_birth_time": "10:15 AM",
        "selected_ascendant": "Sagittarius",
        "confidence_score": 85.5,
        "adjustment_notes": "Time adjusted based on selected Ascendant and evening birth timeframe."
    }

@app.route('/calculate_all', methods=['POST'])
def calculate_all():
    data = request.json
    birth_date = data.get("birth_date")
    birth_time = data.get("birth_time")
    birth_location = data.get("birth_location")
    
    if not birth_date or not birth_location:
        return jsonify({"error": "Birth date and location are required."}), 400
    
    human_design = calculate_human_design(birth_date, birth_time, birth_location)
    numerology = calculate_numerology(birth_date)
    astrology = calculate_astrology_purpose(birth_date, birth_time, birth_location)
    
    return jsonify({
        "human_design": human_design,
        "numerology": numerology,
        "astrology": astrology
    })

@app.route('/estimate_birth_time', methods=['POST'])
def estimate_time():
    data = request.json
    estimated_time = estimate_birth_time(data)
    return jsonify(estimated_time)

if __name__ == '__main__':
    app.run(debug=True)
