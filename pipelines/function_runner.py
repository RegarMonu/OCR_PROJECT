# scripts/run_pipeline.py
import os
from datetime import datetime
from functions.ocr_runner import extract_text
from functions.text_cleaner import clean_text, correct_spelling
from functions.nlp_extractor import extract_ner_and_pos
from functions.converter import save_to_json

def process_image(image_path, output_dir):
    raw_text = extract_text(image_path)
    cleaned_text = clean_text(raw_text)
    corrected_text = correct_spelling(cleaned_text)
    ner, pos = extract_ner_and_pos(corrected_text)

    result = {
        "image_id": os.path.basename(image_path),
        "file_path": image_path,
        "raw_text": raw_text,
        "cleaned_text": cleaned_text,
        "corrected_text": corrected_text,
        "ner": ner,
        "pos_tags": pos
    }

    output_path = os.path.join(output_dir, os.path.basename(image_path).replace(".jpg", ".json"))
    save_to_json(result, output_path)
    print(f"Processed and saved: {output_path}")

