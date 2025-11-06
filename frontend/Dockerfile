FROM node:20-alpine AS build
WORKDIR /app
# Copy package files
COPY package*.json ./
# Install dependencies with clean slate
RUN npm ci
# Copy source code
COPY . .
# Set NODE_ENV to production for optimized build
ENV NODE_ENV=production
# Run build with CI=true to avoid interactive prompts
RUN CI=true npm run build

FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
