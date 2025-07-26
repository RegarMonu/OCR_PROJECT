FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libgl1-mesa-glx \
 && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["chainlit", "run", "chatbot/chainlit_app.py", "--host", "0.0.0.0", "--port", "8000"]
