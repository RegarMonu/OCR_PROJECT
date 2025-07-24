import spacy

nlp = spacy.load("en_core_web_sm")

def extract_ner_and_pos(text):
    doc = nlp(text)
    ner = [(ent.text, ent.label_) for ent in doc.ents]
    pos_tags = [(token.text, token.pos_) for token in doc]
    return ner, pos_tags
