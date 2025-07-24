Project Structure till now 

OCR_PROJECT/
├── config/
│   └── find_config.py                # Loads .env & returns paths
├── utils/
│   └── input_directory_processing.py # Walks dirs, calls OCR, NLP
├── ocr_engines/
│   ├── tesseract_ocr.py
│   ├── easyocr_ocr.py
│   └── paddleocr_ocr.py
├── text_cleaning/
│   └── cleaner.py                    # clean_text, correct_spelling
├── nlp/
│   └── extractor.py                  # extract_ner_and_pos
├── vectorizer/
│   └── embedder.py                  # (Future) for embeddings
├── main.py                          # Your main script
├── requirements.txt
└── .env
