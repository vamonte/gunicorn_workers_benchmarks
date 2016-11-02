FROM python:3.5-alpine
RUN apk add --update --no-cache \
    git \
    build-base \
    postgresql-dev

WORKDIR /app
RUN mkdir ./static
COPY ./workers_benchmarks /app/src
WORKDIR /app/src

RUN pip3 install -r requirements.txt
EXPOSE 8000

