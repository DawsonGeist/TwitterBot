import requests
import pprint


def formatPhrase(phrase):
    sentence = str(phrase)
    wordArray = sentence.split(' ')
    blanks = []
    # Find the repeated spaces
    for i in range(len(wordArray)):
        if wordArray[i] == '':
            blanks.append(i)
    # Remove repeated spaces
    for x in range(len(blanks)):
        index = blanks.pop(-1)
        wordArray.pop(index)

    # generate api call
    formatedPhrase = ''
    for z in range(len(wordArray)):
        if z == len(wordArray) - 1:
            formatedPhrase += str(wordArray[z])
        else:
            formatedPhrase += str(wordArray[z]) + '+'
    return formatedPhrase


def getWordsWithSimilarMeaning(phrase, topics):
    formatedPhrase = formatPhrase(phrase)
    formatedTopics = formatPhrase(topics)
    r = requests.get('https://api.datamuse.com/words?ml=' + str(formatedPhrase) + '&v=enwiki' + '&topics=' + formatedTopics)

    if r.status_code != 200:
        print('Bad API Call')
        return []
    else:
        pprint.pprint(r.json())
        return r.json()


def getAdjThatDescribeAWord(word, topics):
    w = formatPhrase(word)
    formatedTopics = formatPhrase(topics)
    r = requests.get('https://api.datamuse.com/words?rel_jjb=' + w + '&v=enwiki' + '&topics=' + formatedTopics)
    if r.status_code != 200:
        print('Bad API Call')
        return []
    else:
        pprint.pprint(r.json())
        return r.json()


def getAssosciatedWords(word, topics):
    w = formatPhrase(word)
    formatedTopics = formatPhrase(topics)
    r = requests.get('https://api.datamuse.com/words?rel_trg=' + w + '&v=enwiki' + '&topics=' + formatedTopics)
    if r.status_code != 200:
        print('Bad API Call')
        return []
    else:
        pprint.pprint(r.json())
        return r.json()

# Gets words that are a more General to the scope provided by the argument word
# "word is a kind of returned value"
def getHypernym(word, topics):
    w = formatPhrase(word)
    formatedTopics = formatPhrase(topics)
    r = requests.get('https://api.datamuse.com/words?rel_spc=' + w + '&v=enwiki' + '&topics=' + formatedTopics)
    if r.status_code != 200:
        print('Bad API Call')
        return []
    else:
        pprint.pprint(r.json())
        return r.json()

# Gets words that are a more specific to the scope provided by the argument word
# "word is more general than returned value"
def getHyponym(word, topics):
    w = formatPhrase(word)
    formatedTopics = formatPhrase(topics)
    r = requests.get('https://api.datamuse.com/words?rel_gen=' + w + '&v=enwiki' + '&topics=' + formatedTopics)
    if r.status_code != 200:
        print('Bad API Call')
        return []
    else:
        pprint.pprint(r.json())
        return r.json()


def getWordsComprisedOf(word, topics):
    w = formatPhrase(word)
    formatedTopics = formatPhrase(topics)
    r = requests.get('https://api.datamuse.com/words?rel_com=' + w + '&v=enwiki' + '&topics=' + formatedTopics)
    if r.status_code != 200:
        print('Bad API Call')
        return []
    else:
        pprint.pprint(r.json())
        return r.json()


def getPopularAdj(word, topics):
    w = formatPhrase(word)
    formatedTopics = formatPhrase(topics)
    r = requests.get('https://api.datamuse.com/words?rel_jjb=' + w + '&v=enwiki' + '&topics=' + formatedTopics)
    if r.status_code != 200:
        print('Bad API Call')
        return []
    else:
        pprint.pprint(r.json())
        return r.json()


def getSynonyms(word, topics):
    w = formatPhrase(word)
    formatedTopics = formatPhrase(topics)
    r = requests.get('https://api.datamuse.com/words?rel_syn=' + w + '&v=enwiki' + '&topics=' + formatedTopics)
    if r.status_code != 200:
        print('Bad API Call')
        return []
    else:
        pprint.pprint(r.json())
        return r.json()

