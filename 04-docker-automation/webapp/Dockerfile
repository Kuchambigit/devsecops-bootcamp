# Use the official NGINX Alpine image as our base
FROM nginxinc/nginx-unprivileged:stable-alpine

# Copy custom webpage into NGINX's default web directory
COPY index.html /usr/share/nginx/html/index.html

# Document the port used by the web server
EXPOSE 8080
