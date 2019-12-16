from re import sub
from spacy import load
import itertools

def replace(text, classifications, label = "XX"):
  new_text = text
  values = map(lambda x: x[2], classifications)
  # for typ, idx, val in classifications:
  name_regex = '|'.join(values)
  new_text = sub(name_regex, label, new_text)
  return new_text

def tokenize(text, classifications, label = "XX"):
  nlp = load('es_core_news_sm')
  doc = nlp(text)
  names = classifications['NAMES']

  anonimyze = list(itertools.chain.from_iterable(classifications.values()))
  anonimyze = list(map(lambda x: x[0], anonimyze))

  # transformed = []
  # for idx in range(len(doc)):
  #   if idx = 
    
  transformed = []
  for token in doc:
    if token.text in anonimyze:
      transformed.append(label)
    else:
      transformed.append(token.text)
  return ' '.join(transformed)
