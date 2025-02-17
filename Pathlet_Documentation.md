# Pathlet API Documentation

## Overview
Pathlet is an API that generates personalized esoteric insights based on Astrology, Numerology, and Human Design. Users input their birth date, time, and location to receive a full spiritual analysis. If the birth time is unknown, the API provides possible Ascendants to help estimate it.

## Features & Step-by-Step Breakdown

### **1. User Inputs Birth Details**
- Users submit their **birth date, time, and location**.
- If the birth time is unknown, users can request potential Ascendants.

### **2. Optional Birth Time Estimation**
- If no birth time is provided, the API returns **possible Ascendants** with time ranges and descriptions.
- Users select the Ascendant that resonates most with them.
- The estimated birth time is assigned accordingly.

### **3. Esoteric Readings Are Generated**
The API provides detailed insights, including:

#### **Astrology Readings**
- **Life Purpose Statement** (Generated using AI)
- **Sun, Moon, and Rising Signs**
- **Midheaven & Career Guidance**
- **North & South Node Interpretations**
- **Saturn & Personal Growth Challenges**

#### **Numerology Readings**
- **Life Path Number** (Core life theme)
- **Personal Year Number** (Yearly cycle influences)
- **Expression Number** (Communication style & strengths)
- **Soul Urge Number** (Inner desires and motivations)
- **Karmic Debt Number** (Past-life influences & lessons)

#### **Human Design Readings**
- **Type** (Manifestor, Generator, Projector, Reflector)
- **Strategy** (How to best navigate the world)
- **Authority** (Decision-making process)
- **Not-Self Theme** (Indicates misalignment)
- **Signature** (Indicates alignment and success)

### **Examples of types of readings:**
- # **Who Am I? A Personalized Astrology, Human Design, and Numerology Reading**

## **1. Who am I?**
- **Sun in Aries** → Independent, bold, thrives on challenges.  
- **Moon in Scorpio** → Deep emotions, strong intuition, private.  
- **Rising in Gemini** → Seen as witty, adaptable, loves communication.  
- **Life Path 1** → Natural leader, must carve their own path.  
- **Human Design Type: Manifesting Generator** → Multitasker, high-energy, needs variety.  

---

## **2. How do I function best?**
- **Mercury in Pisces** → Intuitive thinking, creative mind.  
- **Mars in Cancer** → Motivated by emotional security, not aggression.  
- **Authority: Sacral** → Should listen to gut reactions for decisions.  
- **Expression Number 3** → Best when expressing creativity (art, speaking, writing).  

---

## **3. How should I interact with the world?**
- **Jupiter in Leo** → Expansion comes through self-expression, leadership, visibility.  
- **Profile 2/4** → Natural networker, needs close-knit relationships for opportunities.  
- **Personality Number 5** → People see you as adventurous, free-spirited.  

---

## **4. What hinders me?**
- **Saturn in Capricorn** → Fear of failure, needs discipline to succeed.  
- **South Node in Libra** → Overly focused on pleasing others, must embrace independence.  
- **Not-Self Theme: Frustration** → If frustrated, not following correct energy flow.  
- **Karmic Debt Number 14** → Past-life patterns of instability, must master focus.  

---

## **5. What can I improve upon?**
- **North Node in Aries** → Embrace bold self-leadership, stop seeking approval.  
- **Shadow of Type: Rushing Decisions** → Needs to slow down, trust gut (Sacral).  
- **Growth Number 6** → Learn responsibility, avoid escapism.  

---

## **6. What career paths fit me?**
- **Midheaven in Aquarius** → Unconventional careers, technology, humanitarian work.  
- **10th House Uranus** → Best in innovative, self-directed work, not corporate.  
- **Expression 3 + Life Path 1** → Creativity + leadership = Writer, Public Speaker, Entrepreneur.  
- **Human Design Channels:**  
  - **34-20 (Power Channel):** Strong energy for action, working independently, excelling under self-direction. These people work best when fully engaged in activities that excite them.  
  - **2-14 (Keeper of the Keys):** This channel provides a strong sense of direction and purpose, guiding them toward a path that is uniquely theirs, often leading in unconventional ways.  
  - **43-23 (Genius to Freak):** A highly creative and innovative mind that may struggle to communicate its ideas clearly to others but thrives when given space to express itself.  

---

## **7. What fulfills me?**
- **Venus in Taurus** → Stability, beauty, sensual pleasures, nature.  
- **Signature: Satisfaction & Success** → Feels aligned when work is meaningful and fun.  
- **Soul Urge Number 5** → Needs freedom, travel, excitement to thrive.  

---

## **8. What personal cycle am I in?**
- **Current Transits: Saturn Return (Age 29-30)** → Big life shifts, redefining purpose.  
- **Personal Year (Birthday to Birthday):** Based on your **Life Path + Current Year**, this cycle is **not tied to January 1st** but instead shifts on your birthday.  
  - Example: If born on **April 15, 1990**, and current year is **2025**, then from **April 15, 2025 – April 15, 2026, you are in a Personal Year 7** → A year of introspection, learning, and spiritual growth.  

---

## **9. How do I know when to respond to the world?**
- **Strategy: Respond, then Act** → Should wait for opportunities before taking action.  
- **Authority: Sacral (Gut Feelings)** → If it’s a strong yes, go for it. If unsure, wait.  
- **Personal Year Influence:** Your **Personal Year Number** shifts on your **birthday** and gives insight into whether it’s a time for action, reflection, expansion, or endings.  

---

## **10. What to avoid?**
- **South Node in Libra** → Stop overcompromising.  
- **Not-Self Theme: Frustration** → Don’t force things; wait for opportunities.  
- **Challenge Number 4** → Avoid scattered energy; build a strong foundation.  

---

## **11. What to move towards?**
- **North Node in Aries** → Lead boldly, take risks, trust instincts.  
- **Signature: Success & Satisfaction** → Align with passion, not just obligations.  
- **Life Path 1** → Be a pioneer, not a follower.  

---

## **Final Thoughts**
This reading integrates **Astrology (your cosmic blueprint), Human Design (how you interact with energy), and Numerology (life path cycles & themes)** to create a **personalized roadmap** for purpose, decision-making, career fulfillment, and alignment with life’s flow.

### **4. API Returns a Full Report**
- The system compiles and returns all insights in a structured JSON response.
- If the user previously selected an Ascendant, the estimated birth time is included.

## Dependencies
Ensure the following dependencies are installed:
```bash
pip install flask requests python-dotenv
```

## Running the API Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/pathlet-api.git
   cd pathlet-api
   ```
2. Set up a `.env` file with your Hugging Face API key:
   ```plaintext
   HUGGING_FACE_API_KEY=your_huggingface_api_key
   ```
3. Start the API:
   ```bash
   python app.py
   ```

## Available Endpoints
### **Check API Status**
```bash
curl -X GET http://127.0.0.1:5000/
```
Response:
```json
{"message": "Pathlet API is running! Use the available endpoints."}
```

### **Get Possible Ascendants (If Birth Time Is Unknown)**
```bash
curl -X POST http://127.0.0.1:5000/get_ascendants -H "Content-Type: application/json" -d '{"birth_date": "1990-05-15", "birth_location": "New York"}'
```

### **Get Full Esoteric Report (If Birth Time Is Known)**
```bash
curl -X POST http://127.0.0.1:5000/calculate_all -H "Content-Type: application/json" -d '{"birth_date": "1990-05-15", "birth_time": "10:30 AM", "birth_location": "New York"}'
```

## Making the API Public on GitHub
1. **Initialize Git**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit - Pathlet API"
   ```
2. **Push to GitHub**:
   ```bash
   git branch -M main
   git remote add origin https://github.com/your-username/pathlet-api.git
   git push -u origin main
   ```

## Future Enhancements
- Add a **frontend UI** using Streamlit or Gradio.
- Expand **AI-generated insights** for deeper analysis.
- Integrate with **database storage** for user history tracking.

## Contact
For questions or contributions, please open an issue on GitHub.

---

This documentation provides a structured breakdown of Pathlet, making it easy to deploy, use, and extend. 🚀
