FROM python:3.10.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
EXPOSE 8000

WORKDIR /app

COPY pyproject.toml .

RUN apt-get update \
    && pip install --upgrade pip \
    && pip install poetry \
    && poetry install

COPY . .
