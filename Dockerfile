FROM python:3.8

WORKDIR /workspace

COPY requirements.txt /workspace

RUN python3 -m pip install -r requirements.txt