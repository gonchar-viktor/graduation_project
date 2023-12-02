FROM python:3.11

WORKDIR /app

COPY requirements.txt .

COPY . /app

RUN apt-get update && apt-get install -y \
    microsoft-edge-dev\
    google-chrome-stable\
    && pip install -r requirements.txt

CMD ["pytest"]
