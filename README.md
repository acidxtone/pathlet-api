# Pathlet API  

## Description  
This API integrates **Human Design, Astrology, and Numerology** to help users understand their life purpose.  

## Features  
- **Human Design:** Type, Strategy, Authority, Not-Self Theme, Signature  
- **Numerology:** Personal Year Calculation  
- **Astrology:** Condensed Life Purpose Snippet  

## Endpoints  
- `POST /calculate_all` → Returns Human Design, Numerology, and Astrology insights.  
- `POST /estimate_birth_time` → Helps estimate birth time for users who don't know it.  

## Setup  
1. Clone this repo:  
   ```sh
   git clone https://github.com/acidxtone/pathlet-api.git

✅ 3️⃣ Install Required Python Packages
Run this command in the terminal inside VS Code:

sh
Copy
pip install flask python-dotenv requests
✅ 4️⃣ Run the API Locally
In the terminal, navigate to your project folder and run:

sh
Copy
python app.py
This will start the Flask server on http://127.0.0.1:5000.


