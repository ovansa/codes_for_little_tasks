# Named-entity recognition (NER) seeks to locate and clasify named entity mentions in
# unstructured texts into pre-defined categories such as person names, organizations,
# locations, medical codes, time expressions, quantities, monetary values, percentages,
# etc...

# Goal is to read from raw texts such as "Jim bought 300 hectares of Acme Corp. in 2006."
# And add addition NER information

import spacy
from spacy.tokens import Span # To work on single entity
from spacy.matcher import PhraseMatcher # To match multiple phrase entities
from spacy import displacy


nlp = spacy.load('en_core_web_sm')

matcher = PhraseMatcher(nlp.vocab)

def show_ents(doc):
    if doc.ents:
        for ent in doc.ents:
            print(ent.text + ' - ' + ent.label_ + ' - ' + str(spacy.explain(ent.label_)))
    else:
        print('No entity found')

doc = nlp(u"Where are you going to?")
doc1 = nlp(u"May I go to England next week to see the Governor?")
doc2 = nlp(u"Can I have 500 naira of Apple's stock?")
doc3 = nlp(u"Amin is building a new factory for $6 million")

show_ents(doc)
print('\n')
show_ents(doc1)
print('\n')
show_ents(doc2)
print('\n')
show_ents(doc3)
print('\n')

# To add a named entity to a span
PERSON = doc.vocab.strings[u"PERSON"]
new_ent = Span(doc3,0,1,label=PERSON)
doc3.ents = list(doc3.ents) + [new_ent]
show_ents(doc3)
print('\n')

# Adding multiple phrases as named entities
doc4 = nlp(u"Our company created a brand new vacuum cleaner."
           u"This new vacuum-cleaner is the best in show.")
# show_ents(doc4)

phrase_list = ['vacuum cleaner', 'vacuum-cleaner']
phrase_patterns = [nlp(text) for text in phrase_list]
matcher.add('product', None, *phrase_patterns)
found_matches = matcher(doc4)

PRODUCT = doc.vocab.strings[u"PRODUCT"]
new_ents = [Span(doc4, match[1], match[2], label=PRODUCT) for match in found_matches]

doc4.ents = list(doc4.ents) + new_ents

show_ents(doc4)
print('\n')

doc5 = nlp(u"Originally i paid $28 million for this car, but now it is marked down by $10")

entities = [ent for ent in doc5.ents if ent.label_ == "MONEY"]
print(len(entities))
print('\n')

doc6 = nlp(u"Over the last quarter, Apple sold nearly 20 thousand iPods for a profit of $45 million."
           u"By contrast, Sony only sold 8 thousand Walkman music players.")

options = {'ents':['PRODUCT', 'ORG']}

for sent in doc6.sents[:2]:
    displacy.serve(nlp(sent.text), style='ent', options=options)
