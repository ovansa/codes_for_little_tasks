import spacy
nlp = spacy.load('en_core_web_sm')
from spacy.matcher import Matcher

matcher = Matcher(nlp.vocab)

# 1. Create a Doc object from the file owlcreek.txt
with open('owlcreek.txt') as owl:
    doc = nlp(owl.read())

# Verify the copied file works
# print(doc[:36])
# print('\n')

# 2. How many tokens are contained in the file?
print(len(doc))
print('\n')

# 3. How many sentences are contained in the file?
sentences = []

for text in doc.sents:
    sentences.append(text)

print(len(sentences))
print('\n')

# 4. Print the second sentence in the document
print(sentences[2])
print('\n')

# 5. For each token in the sentence above, print its text, POS tag, dep tag and lemma
# CHALLENGE: Have values line up in columns in the print output.
for token in sentences[2]:
    print(f'{token.text:{10}} {token.pos_:{15}} {token.dep_:{10}} {token.lemma:{10}}')

print('\n')

# 6. Write a matcher called 'Swimming' that finds both occurrences of the phrase "swimming vigorously" in the text
pattern = [{'LOWER':'swimming'}, {'IS_SPACE':True}, {'LOWER':'vigorously'}]

matcher.add('Swimming', None, pattern)

found_matches = matcher(doc)

#7. Print the text surrounding each found matchk
for match_id, start, end in found_matches:
    span = doc[start-10:end+10]
    print(span.text)

print('\n')

# 8. Print the *sentence* that contains each found match**
matched_sentences = []

for text in doc.sents:
    # print(type(text.text))
    found_matches = matcher(nlp(text.text))
    if len(found_matches) > 0:
        matched_sentences.append(text.text)

for text in matched_sentences:
    print(text)
