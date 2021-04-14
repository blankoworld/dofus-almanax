FROM nginx:1.19-alpine

RUN curl -sSL "https://github.com/h5bp/server-configs-nginx/archive/3.3.0.tar.gz" | tar -xzf - --strip-components=1 -C /etc/nginx && \
    sed -i -r 's/user www-data/user nginx/' /etc/nginx/nginx.conf && \
    rm -rf /etc/nginx/conf.d/*

COPY /container_root /
COPY /src /var/www/html

EXPOSE 5000
