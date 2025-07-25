import base64
import requests
import os

def check_ollama_working():
    try:
        res = requests.get("http://localhost:11434")
        return res.status_code == 200
    except Exception:
        return False

def encode_image_to_base64(image_path):
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

def generate_summary(image_path, ocr_text, ner, pos):
    if not check_ollama_working():
        raise RuntimeError("Ollama server is not running at http://localhost:11434")

    image_b64 = encode_image_to_base64(image_path)

    prompt = f"""
You are a vision-language model. Here is some context extracted from the image:

OCR Text:
{ocr_text}

Named Entities:
{ner}

Part-of-Speech Tags:
{pos}

Based on this information and the image itself, write a brief and concise summary of the image.
"""

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llava:7b",
                "prompt": prompt.strip(),
                "images": [image_b64],
                "stream": False
            },
            timeout=180
        )
        response.raise_for_status()
        data = response.json()
        # print("Ollama response:", data)
        return data.get("response", "No response from model").strip()
    except requests.RequestException as e:
        print(f"Error during Ollama API call: {e}")
        return "Error generating summary"
