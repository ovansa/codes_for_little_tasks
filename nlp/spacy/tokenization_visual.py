import spacy
from spacy import displacy


nlp = spacy.load('en_core_web_sm')

doc = nlp(u"Apple is going to build a factory for $7 million")

displacy.serve(doc, style='ent', options={'distance':110})

doc1 = nlp(u"Over the last two weeks, Apple sold 20 thousand iPods for a profit of 7 million.")

for et in doc1.ents:
    print(et, end=" | ")
    print(et.label_)
