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

## Deployment

### Vercel Deployment

1. **Environment Variables**
   - Set `HUGGING_FACE_API_KEY` in Vercel project settings
   - Ensure the key is kept secret and not exposed in the codebase

2. **Deployment Steps**
   ```bash
   # Install Vercel CLI
   npm install -g vercel

   # Link project
   vercel link

   # Set environment variables
   vercel env add HUGGING_FACE_API_KEY
   ```

### Local Development

1. **Clone Repository**
   ```bash
   git clone https://github.com/acidxtone/pathlet-api.git
   cd pathlet-api
   ```

2. **Setup Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Environment Variables**
   - Create a `.env` file
   - Add `HUGGING_FACE_API_KEY=your_api_key_here`

5. **Run Application**
   ```bash
   python api/index.py
   ```

## Running the API

### Local Development
```bash
flask run
```

### Deployment
Supports deployment on:
- Vercel
- Hugging Face Spaces

## Security Notes
- Never commit sensitive API keys to the repository
- Use environment variables for configuration
- Rotate API keys periodically

## Troubleshooting
- Verify all environment variables are correctly set
- Check Vercel logs for deployment issues
- Ensure all dependencies are installed

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
