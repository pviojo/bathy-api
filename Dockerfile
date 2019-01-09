FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
MAINTAINER Pablo Viojo <pviojo@gmail.com>

RUN echo "http://mirror.leaseweb.com/alpine/edge/testing" >> /etc/apk/repositories

RUN apk update && apk add mysql-client python-dev && apk add --virtual build-deps gcc python-dev musl-dev && apk add mysql-dev

WORKDIR /app
ADD src/requirements.txt /app/

RUN pip install -r requirements.txt
ADD ./src /app/

EXPOSE 5000
EXPOSE 80

