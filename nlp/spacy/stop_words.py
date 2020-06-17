# Stops words occur frequently and do not requuire tagging as thoroughly as nouns
# This code removes stop words e.g. "a", "the"

import spacy

nlp = spacy.load('en_core_web_sm')

# Prints out all stop words
print(nlp.Defaults.stop_words)

# Prints the counts of stop words
print(len(nlp.Defaults.stop_words))

print('\n')

# Checks if provided word is a stop word
print(nlp.vocab['Elementary'].is_stop)
print(nlp.vocab['Am'].is_stop)

# Adds a word to list of existing default stop words
nlp.Defaults.stop_words.add('btw')
nlp.vocab['btw'].is_stop = True

# Removes a word from list of default stop words
nlp.Defaults.stop_words.remove('word')
nlp.vocab['word'].is_stop = False

print(nlp.vocab['btw'].is_stop)

print('\n')

print(len(nlp.Defaults.stop_words))
