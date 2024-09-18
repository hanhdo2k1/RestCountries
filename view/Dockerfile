FROM node:16-alpine
WORKDIR /app
ENV API_URL=http://mysql-api-container:8000
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3000
CMD ["npm", "start"]
