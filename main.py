import __future__
from spacy.tokenizer import Tokenizer
import plac
import spacy

nlp = spacy.load('es_core_news_sm')

test = open("prueba.txt", "r")
contenido = test.read()
doc = nlp(contenido)

for ent in doc.ents:
    if (ent.label_ == 'PER' or ent.label_ == 'LOC'):
        print("{0}\t{1}".format(
            ent,
            ent.label_
        ))
for token in doc:
    if (token.like_num):
        print("{0}".format(
            token
        ))
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
