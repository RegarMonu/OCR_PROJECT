import requests

# Replace with your actual keys
AZURE_ENDPOINT = "https://<your-endpoint>.cognitiveservices.azure.com/"
AZURE_KEY = "<your-key>"

def ocr_azure(image_path):
    ocr_url = AZURE_ENDPOINT + "vision/v3.2/ocr"
    headers = {
        'Ocp-Apim-Subscription-Key': AZURE_KEY,
        'Content-Type': 'application/octet-stream'
    }
    with open(image_path, 'rb') as f:
        data = f.read()
    response = requests.post(ocr_url, headers=headers, data=data)
    result = response.json()

    lines = []
    for region in result.get("regions", []):
        for line in region["lines"]:
            line_text = ' '.join([word["text"] for word in line["words"]])
            lines.append(line_text)
    return ' '.join(lines).strip()
