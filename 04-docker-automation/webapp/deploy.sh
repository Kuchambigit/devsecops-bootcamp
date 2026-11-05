#!/bin/bash

# Stop the script if a command fails
set -e

# Define the Docker image and container names
IMAGE_NAME="devsecops-webapp"
IMAGE_TAG="v1"
CONTAINER_NAME="devsecops-webapp"

# Step 1: Build the Docker image
echo "Building Docker image..."
docker build -t "$IMAGE_NAME:$IMAGE_TAG" .

# Step 2: Remove the previous container if it exists
echo "Removing previous container..."
docker rm -f "$CONTAINER_NAME" 2>/dev/null || true

# Step 3: Start the new application container
echo "Starting application container..."
docker run -d \
  --name "$CONTAINER_NAME" \
  -p 8080:80 \
  "$IMAGE_NAME:$IMAGE_TAG"

# Step 4: Verify the container is running
echo "Checking container status..."
docker ps --filter "name=^/${CONTAINER_NAME}$"

# Step 5: Test the application endpoint
echo "Testing application..."
curl --fail --retry 5 --retry-delay 1 --retry-connrefused \
  http://localhost:8080

echo "Deployment completed successfully!"
