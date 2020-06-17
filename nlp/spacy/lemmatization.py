# Using spacy's lemmatization to categorise words

import spacy


def show_lemmas(text):
    for token in text:
        print(token.text, '\t', token.lemma_)

nlp = spacy.load('en_core_web_sm')

doc1 = nlp(u"I am a runner in a race because i love to run since i ran today.")

show_lemmas(doc1)
