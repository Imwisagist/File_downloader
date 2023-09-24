FROM python:3.10.11-slim

WORKDIR /app

COPY pyproject.toml .

RUN apt-get update \
    && pip install --upgrade pip \
    && pip install poetry \
    && poetry install

COPY . .
