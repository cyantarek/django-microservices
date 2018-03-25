FROM python:3.6.4-slim

ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code

COPY . .

RUN pip install -r requirements.txt

RUN python manage.py runserver 0.0.0.0:8001