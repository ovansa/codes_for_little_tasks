import spacy
from spacy.pipeline import SentenceSegmenter

nlp = spacy.load('en_core_web_sm')

doc = nlp(u"This is the first sentence. This is the first sentence. This is the first sentence.")

# for sent in doc.sents:
#     print(sent)

# print('\n')
# # Notes!!! You can grab token via doc index but you can't grab sentence via sents index
# print(list(doc.sents))
# print('\n')

doc1 = nlp(u'"Management is doing the right things; leadership is doing the right things." - Peter Drucker')

# Add a segmentation rule
def set_custom_boundaries(doc):
    for token in doc[:-1]:
        if token.text == ";":
            doc[token.i+1].is_sent_start = True
    return doc

nlp.add_pipe(set_custom_boundaries, before='parser')
print(nlp.pipe_names)
print('\n')

for sent in doc1.sents:
    print(sent)
print('\n')


# Change the segmentation rule completely

nlp = spacy.load('en_core_web_sm')

mystring = u"This is a sentence. This is another.\n\nThis is a \nthird sentence."

doc = nlp(mystring)

for sent in doc.sents:
    print(sent)
print('\n')

def split_on_newlines(doc):
    start = 0
    seen_newline = False

    for word in doc:
        if seen_newline:
            yield doc[start:word.i]
            start = word.i
            seen_newline = False
        elif word.text.startswith('\n'):
            seen_newline = True
    yield doc[start:]

sbd = SentenceSegmenter(nlp.vocab, strategy=split_on_newlines)
nlp.add_pipe(sbd)
doc2 = nlp(mystring)

for sent in doc2.sents:
    print(sent)
