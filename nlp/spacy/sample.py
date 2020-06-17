import spacy


nlp = spacy.load('en_core_web_sm')
doc = nlp(u'Tesla is looking at buying U.S. startup for $6 million')

for token in doc:
    print(f'{token.text:{10}} {token.pos_:{10}} {token.dep_:{10}}')
#
# nlp.pipeline
#
# # print(nlp.pipe_names)
# print('\n\n')
#
# doc2 = nlp(u"Tesla is not that they wouldn't demdn't looking into starups anymore")
#
# for token in doc2:
#     print(f'{token.text:{10}} {token.pos_:{10}} {token.dep_:{10}} {token.shape_:{10}}')

doc3 = nlp(u'Although commmonly attributed to John Lennon from his song "Beautiful Boy", \
the phrase "Life is what happens to us while we are making other plans" was written by \
cartoonist Allen Saunders and published in Reader\'s Digest in 1957, when Lennon was 17.')

print('\n\n')
life_quote = doc3[16:30]

print(life_quote)
print('\n\n')

doc4 = nlp(u'You sent the Prophet to show us the way. You made the religion perfect that day. Peace be upon him, upon him we pray. Sallatullah, wasallam alaik')

for sentence in doc4.sents:
    print(sentence)

print('\n\n')
print(doc4[11].is_sent_start)
