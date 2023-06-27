# Use a Python base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy the backend files to the container
COPY . .

# Install Python dependencies
RUN python -m pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

# Run the unit tests
RUN python -m unittest discover test_agriculture

# Expose the backend port
EXPOSE 8000

# Start the backend server
CMD ["python", "app.py"]