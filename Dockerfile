FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PORT=8080 \
    GOOGLE_CLOUD_PROJECT=dm-data-aiml

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080
CMD ["chainlit", "run", "main.py", "--host", "0.0.0.0", "--port", "8080"]
