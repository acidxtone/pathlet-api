#!/bin/bash

# Vercel Deployment Script for Pathlet API

# Install dependencies
pip install -r requirements.txt

# Set environment variables
export HUGGING_FACE_API_KEY=$HUGGING_FACE_API_KEY

# Run any necessary migrations or setup
# python manage.py migrate  # Uncomment if using Django/Flask migrations

# Start the application
gunicorn api.index:app
