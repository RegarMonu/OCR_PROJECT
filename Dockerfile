FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libgl1-mesa-glx \
 && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

# Set PYTHONPATH so Python can resolve local packages like `chatbot/`
ENV PYTHONPATH=/app

EXPOSE 8000
EXPOSE 8001

CMD ["python", "start.py"]
