FROM python:3.11

WORKDIR /usr/src/catsFandom
COPY requirements.txt .

RUN pip install -r requirements.txt