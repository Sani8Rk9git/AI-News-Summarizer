import spacy

nlp = spacy.load("en_core_web_sm") #loading the english language model

def clean_text(text):
    return text.strip() #remove spaces from beginning and end

def extract_keywords(text):
    doc = nlp(text) # break into token
    keywords = []

    for token in doc:
        if token.is_stop == False and token.is_punct == False and token.is_alpha == True :
            keywords.append(token.lemma_)

    keywords = list(set(keywords))
    return keywords[:10]

def extract_entities(text):
    doc = nlp(text)

    entities = []

    for ent in doc.ents:
        entities.append({
            "text": ent.text,
            "label": ent.label_
        })

    return entities

        