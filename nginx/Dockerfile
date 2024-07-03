FROM nginx:1.19.7-alpine

RUN apk add bash

COPY nginx.conf /etc/nginx/nginx.conf
COPY start.sh /app/start.sh

WORKDIR /app

CMD ["nginx", "-g", "'daemon off;'"]
