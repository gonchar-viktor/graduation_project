FROM python:3.11

WORKDIR /app

COPY requirements.txt .

COPY . /app

RUN apt-get update \
    && apt-get install -y curl \
    && apt-get install -y gnupg \
    && curl -sSL https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && echo "deb [arch=amd64] https://packages.microsoft.com/repos/edge stable main" > /etc/apt/sources.list.d/microsoft-edge-dev.list \
    && apt-get update && apt-get install -y microsoft-edge-dev \
    && curl -sSL https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update && apt-get install -y google-chrome-stable \
    && pip install -r requirements.txt

CMD ["pytest"]
