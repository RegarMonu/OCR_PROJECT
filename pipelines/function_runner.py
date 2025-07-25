import os
from functions.ocr_runner import extract_text
from functions.text_cleaner import clean_text, correct_spelling
from functions.nlp_extractor import extract_ner_and_pos
from utils.llm_json_updater import save_to_json
from llm.llava_summary import generate_summary  # <-- Import this properly

def process_image(image_path, output_dir):
    output_path = os.path.join(output_dir, os.path.basename(image_path).replace(".jpg", ".json"))

    raw_text = extract_text(image_path, "tesseract")
    cleaned_text = clean_text(raw_text)
    corrected_text = correct_spelling(cleaned_text)

    ner, pos = extract_ner_and_pos(corrected_text)
    summary = generate_summary(image_path, corrected_text, ner, pos)

    result = {
        "image_id": os.path.basename(image_path),
        "file_path": image_path,
        "summary": summary,
        "corrected_text": corrected_text,
        "ner": ner,
        "pos_tags": pos
    }

    save_to_json(output_path, result)
    print(f"Processed and saved: {output_path}")
