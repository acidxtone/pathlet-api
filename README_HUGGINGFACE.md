# Pathlet API on Hugging Face Spaces

## Overview
Pathlet is an AI-powered API that generates personalized insights based on Astrology, Numerology, and Human Design.

## Endpoints
- `/get_ascendants`: Estimate possible ascendant signs
- `/calculate_all`: Comprehensive personal insights

## Usage
Send a POST request with JSON payload containing:
- `birth_date`: YYYY-MM-DD
- `birth_location`: City, Country
- Optional: `birth_time`, `selected_ascendant`

## Example Request
```python
import requests

url = "https://your-hugging-face-space-url.app/calculate_all"
payload = {
    "birth_date": "1990-05-15",
    "birth_location": "New York, USA"
}
response = requests.post(url, json=payload)
print(response.json())
```

## Powered by
- Hugging Face Spaces
- Flask
- AI-driven insights
