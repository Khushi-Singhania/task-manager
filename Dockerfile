# Use an official Node.js runtime as the base image
FROM node:14

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install the application dependencies
RUN npm install

# Copy the entire application code to the working directory
COPY . .

# Expose the desired port (replace 3000 with your application's port if needed)
EXPOSE 3000

# Define the command to start the application
CMD [ "node", "index.html" ]