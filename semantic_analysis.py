import nltk
from nltk.corpus import stopwords


#   Tokenize our data into words
tokenizedWords = nltk.tokenize.word_tokenize('Hey, im walking here!')
fdist = nltk.FreqDist(tokenizedWords)
print(fdist.most_common(5))

#   words to be filtered out from our data
stopwords = set(stopwords.words('english'))
print(stopwords)
