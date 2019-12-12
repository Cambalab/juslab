import __future__
from spacy.matcher import Matcher, PhraseMatcher
from spacy.tokenizer import Tokenizer
from spacy.tokens import Token
import plac
import spacy
import re
from dateparser import parse


# Auxiliary functions
def is_date(string):
    try:
        parse(str(string))
        return True

    except ValueError:
        return False

def is_email(string):
    return re.match(r'\S+@\S+', str(string))

def is_phone(string):
    return re.match(r'\d{8,10}', str(string))



# Setup
nlp = spacy.load('es_core_news_sm')
matcher = Matcher(nlp.vocab)

# Dni number Pattern
pattern = [{"TEXT": u'DNI'},{"SHAPE": "dd.ddd.ddd"}]
matcher.add("DNI", None, pattern)

# Phone Number Pattern
pattern = [{"TEXT": u'Tel'},{"SHAPE": "dddd"}]
matcher.add("TELEFONO", None, pattern)

test = open("prueba.txt", "r")
contenido = test.read()
doc = nlp(contenido)
res = []
matches = matcher(doc)

for match_id, start, end in matches:
    span = doc[start:end]
    res.append((nlp.vocab.strings[match_id], start, span.text))

for ent in doc.ents:
    if (ent.label_ == 'PER' and not is_email(ent.text)):
        res.append(('NOMBRE', ent.start, ent.text))

    if (ent.label_ == 'LOC' and not is_email(ent) and not is_phone(ent)):
        res.append(('LUGAR', ent.start, ent))


for token in doc:

    if (token.like_email):
        res.append(('EMAIL', token.idx, token.text))

    if (token.like_num and is_phone(token.text)):
        res.append(('TELEFONO', token.idx, token.text))

print(res)