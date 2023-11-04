FROM nginx:1.22.1

COPY nginx_docker.conf /etc/nginx/nginx.conf
RUN ln -sf /dev/stdout /var/log/nginx/access.log && ln -sf /dev/stderr /var/log/nginx/error.log
COPY dattebayo.jpg /
EXPOSE 8011