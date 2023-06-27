# Stage 1: Build the frontend assets
FROM node:14 AS build-stage
WORKDIR /app
COPY frontend/package*.json ./
RUN npm install
COPY frontend ./
RUN npm run build

# Stage 2: Serve the built assets using Nginx
FROM nginx:1.21
COPY --from=build-stage /app/dist /usr/share/nginx/html
COPY backend /app/backend
COPY nginx/default.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
