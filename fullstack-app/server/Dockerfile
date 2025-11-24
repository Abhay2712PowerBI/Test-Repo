# Server Dockerfile
FROM node:18-alpine

WORKDIR /usr/src/app

# Install dependencies
COPY package*.json ./
RUN npm ci --production=false

# Copy source
COPY . .

EXPOSE 4000
CMD ["node", "src/index.js"]
