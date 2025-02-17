# Pathlet API: Personalized Astrological & Numerological Insights

## Overview
Pathlet is an advanced API that provides personalized insights based on astronomical calculations, including Ascendant Signs, Numerology, and Human Design.

## Features
- 🌟 Precise Ascendant Sign Calculation
- 🔢 Advanced Numerology Analysis
- 🧬 Comprehensive Human Design Typing

## Services

### 1. Ascendant Sign Calculator
Calculates possible ascendant signs using precise astronomical methods.

**Endpoint**: `/get_ascendants`
**Method**: POST
**Payload**:
```json
{
    "birth_date": "YYYY-MM-DD",
    "birth_location": "City, Country"
}
```

### 2. Numerology Calculator
Provides comprehensive life path analysis with detailed insights.

**Endpoint**: `/calculate_numerology`
**Method**: POST
**Payload**:
```json
{
    "birth_date": "YYYY-MM-DD"
}
```

### 3. Human Design Calculator
Determines Human Design type with strategic and personal insights.

**Endpoint**: `/calculate_human_design`
**Method**: POST
**Payload**:
```json
{
    "birth_date": "YYYY-MM-DD",
    "birth_time": "HH:MM AM/PM",  // Optional
    "birth_location": "City, Country"  // Optional
}
```

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
- Create a `.env` file
- Add necessary API keys and configurations

## Running the API

### Local Development
```bash
flask run
```

### Deployment
Supports deployment on:
- Vercel
- Hugging Face Spaces

## Libraries Used
- Flask
- Ephem (Astronomical Calculations)
- Skyfield
- NumPy
- SciPy

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License
MIT License

## Contact
Developed by the Pathlet Team
support@pathlet.com
