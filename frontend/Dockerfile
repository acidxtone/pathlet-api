# Use an official Nginx runtime as a base image
FROM nginx:alpine

# Copy the static HTML file to the Nginx html directory
COPY index.html /usr/share/nginx/html/index.html

# Optional: Copy a custom Nginx configuration if needed
# COPY nginx.conf /etc/nginx/nginx.conf

# Expose port 80
EXPOSE 80

# Start Nginx when the container launches
CMD ["nginx", "-g", "daemon off;"]
