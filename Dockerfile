FROM python:3.13-slim
WORKDIR /app

# Add this section right after the FROM line, before any pip installs.
RUN apt-get update && apt-get install -y curl git --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN adduser --disabled-password --gecos "" aiagent && \
    chown -R aiagent:aiagent /app

COPY . .

USER aiagent

ENV PATH="/home/aiagent/.local/bin:$PATH"

CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port $PORT"]