import spacy
from spacy import displacy
nlp = spacy.load('en_core_web_sm')


# 1. Create a Doc object from the file peterrabbit.txt
with open('peterrabbit.txt') as f:
    doc = nlp(f.read())

# for sent in doc.sents:
#     print(sent)

# 2. For every token in the third sentence, print the token text, the POS tag, the fine-grained TAG tag, and the description of the fine-grained tag.
doc_list = [dom for dom in doc.sents]

print(doc_list[2])

for token in doc_list[2]:
    print(f"{token.text:{15}} {token.pos_:{15}} {token.tag_:{15}} {spacy.explain(token.tag_)}")
print('\n')

# 3. Provide a frequency list of POS tags from the entire document
pos = [token.pos_ for token in doc]

pos_freq = [pos.count(token) for token in pos]


def postListtoFreq(pos_list):
    word_freq = [pos_list.count(token) for token in pos_list]
    return dict(list(zip(pos_list, word_freq)))

freq = postListtoFreq(pos)

for key, value in sorted(freq.items()):
    print(f"{key} : {value}")

print('\n')

# 4. CHALLENGE: What percentage of tokens are nouns?

noun_percentage = freq['NOUN'] / len(pos) * 100
print(noun_percentage)

# 5. Display the Dependency Parse for the third sentence
# displacy.serve(doc_list[2], style='dep', options={'distance':110})

# *6. Show the first two named entities from Beatrix Potter's *The Tale of Peter Rabbit **

for ent in doc.ents[:2]:
    print(ent.text)
# pos_count = doc.count_by(spacy.attrs.POS)
#
# print(pos_count)
