# Use the official Node.js image
FROM node:18

# Set working directory
WORKDIR /rag-frontend

# Copy package.json and install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy the entire project
COPY . .

# Expose Vue development server port
EXPOSE 8080

# Start the Vue app
CMD ["npm", "run", "serve"]
