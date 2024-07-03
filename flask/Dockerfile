#FROM --platform=linux/amd64 python:3.9.2-alpine
FROM python:3.9-alpine AS base

RUN pip install --upgrade pip
RUN apk add curl

WORKDIR /home/app
COPY . .

ENV VIRTUAL_ENV=/home/app/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN export FLASK_APP=app.py
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
