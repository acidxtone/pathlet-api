import os
import requests
from dotenv import load_dotenv

load_dotenv()

HUGGING_FACE_API_KEY = os.getenv("HUGGING_FACE_API_KEY")
HUGGING_FACE_MODEL = "google/flan-t5-large"

def query_hugging_face(prompt):
    """
    Query Hugging Face API with a given prompt.
    
    Args:
        prompt (str): The input prompt for the AI model.
    
    Returns:
        str: Generated text or error message.
    """
    url = f"https://api-inference.huggingface.co/models/{HUGGING_FACE_MODEL}"
    headers = {"Authorization": f"Bearer {HUGGING_FACE_API_KEY}"}
    data = {"inputs": prompt}
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        
        result = response.json()
        if isinstance(result, list) and "generated_text" in result[0]:
            return result[0]["generated_text"]
        return "Purpose could not be determined."
    
    except requests.exceptions.RequestException as e:
        return f"API Request Error: {str(e)}"
    except Exception as e:
        return f"Error parsing response: {str(e)}"

def get_possible_ascendants(birth_date, birth_location):
    """
    Generate possible ascendant signs for given birth details.
    
    Args:
        birth_date (str): Date of birth
        birth_location (str): Location of birth
    
    Returns:
        str: Possible ascendant signs with descriptions
    """
    prompt = f"List possible Ascendant signs with time ranges for {birth_date} in {birth_location}. Provide a brief description of each."
    return query_hugging_face(prompt)
