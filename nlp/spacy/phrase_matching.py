import spacy
from spacy.matcher import PhraseMatcher


nlp = spacy.load('en_core_web_sm')

matcher = PhraseMatcher(nlp.vocab)

with open('reaganomics.txt') as f:
    doc = nlp(f.read())

# for token in doc:
#     print(token.text)

phrase_list = ['supply side economics', 'voodoo economics', 'States economy', 'allocation controls']

phrase_patterns = [nlp(text) for text in phrase_list]

matcher.add("Econ", None, *phrase_patterns)

found_matches = matcher(doc)

for match_id, start, end in found_matches:
    string_id = nlp.vocab.strings[match_id] # Gets string representation
    span = doc[start:end]                   # Gets the matched span or text
    span_context = doc[start-5:end+5]                   # Gets the matched span or text
    print(f"{match_id:{10}} {string_id:{10}} {start:{10}} {end:{10}} {span.text:{40}} {span_context.text:{10}}")
