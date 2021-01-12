FROM python:3.7-alpine
ENV PYTHONUNBUFFERED 1

COPY ./requirenments.txt /requirenments.txt

RUN apk update
RUN apk add --update --no-cache postgresql-client

RUN apk add --update --no-cache --virtual .tmp-build-deps gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirenments.txt
RUN apk del .tmp-build-deps
RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user

