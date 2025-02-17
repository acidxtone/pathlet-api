# Stage 1: Backend Build
FROM python:3.9-slim-buster AS backend-build

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt setup.py ./
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir .

# Copy backend code
COPY backend/ ./backend/

# Stage 2: Frontend Build
FROM node:18-alpine AS frontend-build

# Set working directory
WORKDIR /app

# Copy frontend files
COPY frontend/package*.json ./
RUN npm install

# Copy frontend source
COPY frontend/ ./
RUN npm run build

# Stage 3: Production Image
FROM python:3.9-slim-buster

# Set working directory
WORKDIR /app

# Install production dependencies
RUN apt-get update && apt-get install -y \
    nginx \
    && rm -rf /var/lib/apt/lists/*

# Copy backend from build stage
COPY --from=backend-build /app /app
COPY --from=backend-build /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages

# Copy frontend build
COPY --from=frontend-build /app/build ./frontend/build

# Copy Nginx configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Set environment variables
ENV FLASK_ENV=production
ENV PYTHONPATH=/app

# Expose port
EXPOSE 80 443

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
  CMD curl -f http://localhost/healthz || exit 1

# Run application
CMD ["gunicorn", "-b", "0.0.0.0:8000", "backend.app:app"]
