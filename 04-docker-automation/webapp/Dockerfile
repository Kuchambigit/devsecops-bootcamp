# Use the official NGINX Alpine image as our base
FROM nginx:alpine

# Update Alpine packages to include available security patches
RUN apk upgrade --no-cache

# Copy custom webpage into NGINX's default web directory
COPY index.html /usr/share/nginx/html/index.html

# Document the port used by the web server
EXPOSE 80
