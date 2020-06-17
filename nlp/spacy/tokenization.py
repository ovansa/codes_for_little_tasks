import spacy

nlp = spacy.load('en_core_web_sm')

mystring = '"We\'re moving to L.A."';

doc = nlp(mystring)

print(doc)

print("\n")

# for token in doc:
#     print(f'{token.text:{10}} {token.pos_:{10}}')

doc2 = nlp(u"We're here to help! Send e-mail, email support@email.com or visit us at https://email.com!")

# for t in doc2:
#     print(t)

# print('\n')

print(len(doc2))

doc3 = nlp(u"It is better to give than to recieve.")

print(doc3[0:5])

doc4 = nlp(u"Google to build a hong kong factory for $10 billion.")

for t in doc4:
    print(t.text, end=' | ')

print('\n')

# Splits sentence into entities
for entity in doc4.ents:
    print(entity, end=' | ')
    print(entity.label_)
    print(str(spacy.explain(entity.label_))) # Returns more explanation about labels
    print('\n')


doc5 = nlp(u"Autonomous cars shifts insurance liability towards manufacturers.")

for chunk in doc5.noun_chunks:
    print(chunk)
