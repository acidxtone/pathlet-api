<<<<<<< HEAD
from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

HUGGING_FACE_API_KEY = os.getenv("HUGGING_FACE_API_KEY")
HUGGING_FACE_MODEL = "google/flan-t5-large"

def query_hugging_face(prompt):
    url = f"https://api-inference.huggingface.co/models/{HUGGING_FACE_MODEL}"
    headers = {"Authorization": f"Bearer {HUGGING_FACE_API_KEY}"}
    data = {"inputs": prompt}
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        try:
            result = response.json()
            if isinstance(result, list) and "generated_text" in result[0]:
                return result[0]["generated_text"]
            return "Purpose could not be determined."
        except Exception as e:
            return f"Error parsing response: {str(e)}"
    else:
        return f"Error: {response.status_code} - {response.text}"

def get_possible_ascendants(birth_date, birth_location):
    prompt = f"List possible Ascendant signs with time ranges for {birth_date} in {birth_location}. Provide a brief description of each."
    return query_hugging_face(prompt)

def assign_birth_time(selected_ascendant):
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

def calculate_human_design(birth_date, birth_time, birth_location):
    return {
        "type": "Projector",
        "strategy": "Wait for the Invitation",
        "authority": "Splenic",
        "not_self_theme": "Bitterness",
        "signature": "Success"
    }

def calculate_numerology(birth_date):
    digits = list(map(int, birth_date.replace('-', '')))
    life_path = sum(digits)
    while life_path > 9:
        life_path = sum(map(int, str(life_path)))
    
    personal_year = (sum(map(int, birth_date.split('-'))) % 9) or 9
    expression_number = (sum(digits) % 9) or 9
    soul_urge_number = (sum(digits[:2]) % 9) or 9
    karmic_debt_number = (sum(digits[-2:]) % 9) or 9
    
    return {
        "life_path": life_path,
        "personal_year": personal_year,
        "expression_number": expression_number,
        "soul_urge_number": soul_urge_number,
        "karmic_debt_number": karmic_debt_number
    }

def calculate_astrology_career(birth_date, birth_time, birth_location):
    prompt = f"Provide career guidance based on astrology for someone born on {birth_date} at {birth_time} in {birth_location}."
    return {"career_guidance": query_hugging_face(prompt)}

def calculate_astrology_growth(birth_date, birth_time, birth_location):
    prompt = f"Provide personal growth insights based on astrology for someone born on {birth_date} at {birth_time} in {birth_location}."
    return {"growth_insights": query_hugging_face(prompt)}

def estimate_birth_time(data):
    birth_date = data.get("birth_date")
    location = data.get("birth_location")
    if not birth_date or not location:
        return {"error": "Birth date and location are required."}
    possible_ascendants = get_possible_ascendants(birth_date, location)
    return {
        "possible_ascendants": possible_ascendants,
        "instructions": "Review the listed Ascendants and choose the one that resonates most with you. Once selected, this will determine your estimated birth time."
    }

@app.route('/')
def home():
    return jsonify({"message": "Pathlet API is running! Use the available endpoints."})

@app.route('/get_ascendants', methods=['POST'])
def get_ascendants():
    data = request.json
    if not data.get("birth_date") or not data.get("birth_location"):
        return jsonify({"error": "Birth date and location are required."}), 400
    ascendants = estimate_birth_time(data)
    if "error" in ascendants:
        return jsonify(ascendants), 400
    return jsonify(ascendants)

@app.route('/calculate_all', methods=['POST'])
def calculate_all():
    data = request.json
    birth_date = data.get("birth_date")
    birth_time = data.get("birth_time")
    birth_location = data.get("birth_location")
    
    if not birth_date or not birth_location:
        return jsonify({"error": "Birth date and location are required."}), 400
    
    if not birth_time and "selected_ascendant" in data:
        ascendant_selection = data["selected_ascendant"]
        birth_time = assign_birth_time(ascendant_selection)
    
    human_design = calculate_human_design(birth_date, birth_time, birth_location)
    numerology = calculate_numerology(birth_date)
    astrology = calculate_astrology_career(birth_date, birth_time, birth_location)
    growth = calculate_astrology_growth(birth_date, birth_time, birth_location)
    
    return jsonify({
        "human_design": human_design,
        "numerology": numerology,
        "career": astrology,
        "growth": growth,
        "birth_time": birth_time
    })

if __name__ == '__main__':
    app.run(debug=True)
=======
from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

HUGGING_FACE_API_KEY = os.getenv("HUGGING_FACE_API_KEY")
HUGGING_FACE_MODEL = "google/flan-t5-large"

def query_hugging_face(prompt):
    url = f"https://api-inference.huggingface.co/models/{HUGGING_FACE_MODEL}"
    headers = {"Authorization": f"Bearer {HUGGING_FACE_API_KEY}"}
    data = {"inputs": prompt}
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        try:
            result = response.json()
            if isinstance(result, list) and "generated_text" in result[0]:
                return result[0]["generated_text"]
            return "Purpose could not be determined."
        except Exception as e:
            return f"Error parsing response: {str(e)}"
    else:
        return f"Error: {response.status_code} - {response.text}"

def get_possible_ascendants(birth_date, birth_location):
    prompt = f"List possible Ascendant signs with time ranges for {birth_date} in {birth_location}. Provide a brief description of each."
    return query_hugging_face(prompt)

def assign_birth_time(selected_ascendant):
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

def calculate_human_design(birth_date, birth_time, birth_location):
    return {
        "type": "Projector",
        "strategy": "Wait for the Invitation",
        "authority": "Splenic",
        "not_self_theme": "Bitterness",
        "signature": "Success"
    }

def calculate_numerology(birth_date):
    digits = list(map(int, birth_date.replace('-', '')))
    life_path = sum(digits)
    while life_path > 9:
        life_path = sum(map(int, str(life_path)))
    
    personal_year = (sum(map(int, birth_date.split('-'))) % 9) or 9
    expression_number = (sum(digits) % 9) or 9
    soul_urge_number = (sum(digits[:2]) % 9) or 9
    karmic_debt_number = (sum(digits[-2:]) % 9) or 9
    
    return {
        "life_path": life_path,
        "personal_year": personal_year,
        "expression_number": expression_number,
        "soul_urge_number": soul_urge_number,
        "karmic_debt_number": karmic_debt_number
    }

def calculate_astrology_career(birth_date, birth_time, birth_location):
    prompt = f"Provide career guidance based on astrology for someone born on {birth_date} at {birth_time} in {birth_location}."
    return {"career_guidance": query_hugging_face(prompt)}

def calculate_astrology_growth(birth_date, birth_time, birth_location):
    prompt = f"Provide personal growth insights based on astrology for someone born on {birth_date} at {birth_time} in {birth_location}."
    return {"growth_insights": query_hugging_face(prompt)}

def estimate_birth_time(data):
    birth_date = data.get("birth_date")
    location = data.get("birth_location")
    if not birth_date or not location:
        return {"error": "Birth date and location are required."}
    possible_ascendants = get_possible_ascendants(birth_date, location)
    return {
        "possible_ascendants": possible_ascendants,
        "instructions": "Review the listed Ascendants and choose the one that resonates most with you. Once selected, this will determine your estimated birth time."
    }

@app.route('/')
def home():
    return jsonify({"message": "Pathlet API is running! Use the available endpoints."})

@app.route('/get_ascendants', methods=['POST'])
def get_ascendants():
    data = request.json
    if not data.get("birth_date") or not data.get("birth_location"):
        return jsonify({"error": "Birth date and location are required."}), 400
    ascendants = estimate_birth_time(data)
    if "error" in ascendants:
        return jsonify(ascendants), 400
    return jsonify(ascendants)

@app.route('/calculate_all', methods=['POST'])
def calculate_all():
    data = request.json
    birth_date = data.get("birth_date")
    birth_time = data.get("birth_time")
    birth_location = data.get("birth_location")
    
    if not birth_date or not birth_location:
        return jsonify({"error": "Birth date and location are required."}), 400
    
    if not birth_time and "selected_ascendant" in data:
        ascendant_selection = data["selected_ascendant"]
        birth_time = assign_birth_time(ascendant_selection)
    
    human_design = calculate_human_design(birth_date, birth_time, birth_location)
    numerology = calculate_numerology(birth_date)
    astrology = calculate_astrology_career(birth_date, birth_time, birth_location)
    growth = calculate_astrology_growth(birth_date, birth_time, birth_location)
    
    return jsonify({
        "human_design": human_design,
        "numerology": numerology,
        "career": astrology,
        "growth": growth,
        "birth_time": birth_time
    })

if __name__ == '__main__':
    app.run(debug=True)
>>>>>>> 4de1b8df8333fdcf73616eefc38de624ab39ada8
