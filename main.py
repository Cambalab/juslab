import __future__
from spacy.tokenizer import Tokenizer
import plac
import spacy
import re

nlp = spacy.load('es_core_news_sm')

test = open("prueba.txt", "r")
contenido = test.read()
doc = nlp(contenido)

res = []

def is_email(string):
    return re.match(r'@', str(string))


for ent in doc.ents:
    if (ent.label_ == 'PER' and not is_email(ent)):
        res.append(('NOMBRE', ent.start, ent))

    if (ent.label_ == 'LOC'):
        res.append(('LUGAR', ent.start, ent))


for token in doc:
    # if (token.like_num):
    #     res.append(('DNI', ent.start, ent))


    if (token.like_email):
        res.append(('EMAIL', token.idx, token.text))

print(res)

    #if (token.like_email):
        # print("{0}\t{1}\t{2}".format(
        # token.text,
        # token.idx,
        # token.prefix
        # ))
    # print("{0}\t{1}\t{2}\t{3}".format(
    #     token.text,
    #     token.idx,
    #     token.like_email,
    #     token.like_num
    # ))
