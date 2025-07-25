import re
from spellchecker import SpellChecker

spell = SpellChecker()

def clean_text(text):
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)     # Remove non-ASCII
    text = re.sub(r'[\r\n]+', ' ', text)           # Newlines
    text = re.sub(r'\s+', ' ', text).strip()       # Extra spaces
    return text

def correct_spelling(text):
    words = text.split()
    corrected_words = [
        spell.correction(w) if w.isalpha() else w for w in words
    ]
    # Replace None with original word
    corrected_words = [w if w is not None else original for w, original in zip(corrected_words, words)]
    return ' '.join(corrected_words)
