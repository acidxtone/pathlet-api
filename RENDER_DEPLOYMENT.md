# Pathlet Deployment on Render

## Prerequisites
- GitHub account
- Render account
- Project repository on GitHub

## Deployment Steps

### Backend Deployment
1. Go to Render Dashboard
2. Create a new Web Service
3. Connect to your GitHub repository
4. Select the main branch
5. Configure the following settings:
   - Environment: Python 3.9
   - Build Command: 
     ```
     python -m pip install --upgrade pip
     pip install -r requirements.txt
     pip install .
     ```
   - Start Command: `gunicorn backend.app:app`
   - Environment Variables:
     - FLASK_ENV: production
     - HUGGING_FACE_API_KEY: [Your API Key]

### Frontend Deployment
1. Create a new Static Site on Render
2. Connect to your GitHub repository
3. Configure:
   - Build Command: `npm run build`
   - Publish Directory: `frontend/build`

### Environment Variables
- Set all sensitive variables in Render's dashboard
- Do NOT commit `.env` files to the repository

## Troubleshooting
- Ensure all dependencies are in `requirements.txt`
- Check Python and Node.js versions
- Verify environment variable configurations

## Post-Deployment
- Test all API endpoints
- Verify frontend functionality
- Monitor application logs
