import string
import re
from spacy import load
from spacy.lang.es.stop_words import STOP_WORDS

def is_email(string):
    return re.match(r'@', str(string))

def classify(text):
  classifications = {}
  nlp = load('es_core_news_sm')
  tokenized = nlp(text)
  names = set()
  locations = set()
  emails = set()
  for ent in tokenized.ents:
    if (ent.label_ == 'PER' and not is_email(ent)):
      names.add((ent, ent.start))
    if (ent.label_ == 'LOC'):
      locations.add((ent, ent.start))
    for token in tokenized:
      if (token.like_email):
        emails.add((token.text, token.idx))
  classifications['NAMES'] = names
  classifications['LOCATIONS'] = locations
  classifications['EMAILS'] = emails
  return classifications

# nlp = load('es_core_news_sm')
# f = open("prueba.txt", "r")
# text = f.read()

# classifications = classify(text)

# print("classifications")
# print(classifications)
