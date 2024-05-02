FROM python:3.11-slim

ENV PYTHONUNBUFFERED 1

COPY . /src

WORKDIR /src

RUN pip3 install -r requirements.txt

WORKDIR /src/cpu_load


