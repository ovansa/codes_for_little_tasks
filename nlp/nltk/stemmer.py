import nltk

from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer


p_stemmer = PorterStemmer()
s_stemmer = SnowballStemmer(language='english')

words = ['run', 'runnner', 'ran', 'runs', 'fairly', 'easily']

for word in words:
    print(word + ' ----------> ' + p_stemmer.stem(word))

print('\n')

for word in words:
    print(word + ' ----------> ' + s_stemmer.stem(word))
