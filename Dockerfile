FROM python:3.9.1-slim-buster

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git && \
    pip install pip --upgrade

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt
CMD python main.py