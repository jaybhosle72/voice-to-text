FROM python:3.11-slim

RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir flask gunicorn werkzeug

RUN pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu \
    --no-deps

RUN pip install --no-cache-dir tqdm more-itertools regex numpy \
    tiktoken numba

RUN pip install --no-cache-dir openai-whisper --no-deps

COPY . .

RUN mkdir -p uploads

EXPOSE 8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--timeout", "120", "--workers", "1", "app:app"]
