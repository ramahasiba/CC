FROM mysql:5.7

ENV MYSQL_ROOT_PASSWORD=root
ENV MYSQL_DATABASE=newsdb
ENV MYSQL_USER=user
ENV MYSQL_PASSWORD=password

COPY news.sql /docker-entrypoint-initdb.d/

EXPOSE 3307
