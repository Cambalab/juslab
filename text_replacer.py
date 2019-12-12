from re import sub
from spacy import load

def replace(text, classifications, label = "XX"):
  names = classifications['names']
  name_regex = '|'.join(names)

  new_text = sub(name_regex, label, text)

  return new_text

def tokenized(text, classifications, label = "XX"):
  nlp = load('es_core_news_sm')
  doc = nlp(text)
  names = classifications['names']
  transformed = []
  for token in doc:
    if token.text in names:
      transformed.append(label)
    else:
      transformed.append(token.text)
  return ' '.join(transformed)

# file = open("prueba.txt", "r")
# text = file.read()
# classifications = {'names': ['Ayelén', 'Lopez', 'Carlos', 'González', 'Espinoza']}
# new_text = replace(text, classifications)
# new_text = tokenized(text, classifications)
# print("BEFORE")
# print(text)
# print("AFTER")
# print(new_text)