FROM python:3.12

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

COPY . /app/

WORKDIR /app/