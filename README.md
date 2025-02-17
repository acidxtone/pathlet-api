# Pathlet API

## Overview
Pathlet is an advanced API generating personalized insights using Astrology, Numerology, and Human Design.

## Deployment Platforms
- **Vercel**: Web API Hosting
- **Hugging Face Spaces**: Alternative Deployment

## Features
- Ascendant Sign Estimation
- Numerology Calculations
- Human Design Type Analysis

## Setup

### Local Development
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up environment variables
4. Run the application: `python backend/app.py`

### Deployment
- **Vercel**: 
  * Automatically deploys from GitHub
  * Configure environment variables in Vercel dashboard
- **Hugging Face Spaces**:
  * Docker-based deployment
  * Requires Hugging Face Spaces configuration

## API Endpoints
- `GET /`: Health check
- `POST /get_ascendants`: Estimate possible ascendant signs
- `POST /calculate_all`: Comprehensive personal insights

## Contributing
Please read `CONTRIBUTING.md` for details on our code of conduct and the process for submitting pull requests.

## License
This project is licensed under the MIT License.
