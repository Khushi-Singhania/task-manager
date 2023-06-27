# Use a Python base image
FROM python:3.9 as base

# Set the working directory
WORKDIR /app

# Copy the project files to the container
COPY . .

RUN npm install

RUN npm run build

# Install the project dependencies
RUN python -m pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

# Run the unit tests
RUN python -m unittest discover test_agriculture

# Build the final production image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the project files from the previous stage
COPY --from=base /app .

# Expose any necessary ports
EXPOSE 80
# Set the entrypoint command for the application
CMD ["python", "test_agriculture.py"]