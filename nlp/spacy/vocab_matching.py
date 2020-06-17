import spacy
from spacy.matcher import Matcher


nlp = spacy.load('en_core_web_sm')

matcher = Matcher(nlp.vocab)

# Set Pattern matches to match the word types below
# SolarPower
# Solar-Power
# Solar Power
pattern1 = [{'LOWER':'solarpower'}]
pattern2 = [{'LOWER':'solar'}, {'IS_PUNCT':True}, {'LOWER':'power'}]
pattern3 = [{'LOWER':'solar'},{'LOWER':'power'}]

matcher.add('SolarPower', None, pattern1, pattern2, pattern3)

doc = nlp(u'The Solar Power industry continues to grow as demand for solarpower increases. Solar-power cars are gaining popularity.')

found_matches = matcher(doc)

# print(found_matches)

for match_id, start, end in found_matches:
    string_id = nlp.vocab.strings[match_id] # Gets string representation
    span = doc[start:end]                   # Gets the matched span or text
    print(match_id, string_id, start, end, span.text)

print('\n')

matcher.remove('SolarPower')

pattern1 = [{'LOWER':'solarpower'}]
pattern2 = [{'LOWER':'solar'}, {'IS_PUNCT':True, 'OP':'*'}, {'LOWER':'power'}]

matcher.add('SolarPower', None, pattern1, pattern2)

doc = nlp(u'The Solar Power industry continues to grow as demand for solar---power increases. Solar-power and Sollar Powers cars are gaining popularity.')

found_matches = matcher(doc)

for match_id, start, end in found_matches:
    string_id = nlp.vocab.strings[match_id] # Gets string representation
    span = doc[start:end]                   # Gets the matched span or text
    print(match_id, string_id, start, end, span.text)
