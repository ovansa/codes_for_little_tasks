import spacy
from spacy import displacy

nlp = spacy.load('en_core_web_sm')

doc = nlp(u"The quick brown fox jumped over the lazy dog.")

options = {'distance':120, 'compact':True, 'color':'yellow', 'bg':'#09a3d5', 'font':'Garamond'} # Creates display options

# displacy.serve(doc, style='dep', options=options) # Displays part of speech tag

doc2 = nlp(u"I am not afraid to take a stand. Everybody, come take my hands. We walk this road together through the storm.")

spans = list(doc2.sents) # Splits a longs doc into sentences

displacy.serve(spans, style='dep', options=options)
