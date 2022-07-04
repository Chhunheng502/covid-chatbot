import nltk
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
import numpy as np

def lower_case(words):
    return [word.lower() for word in words]

def remove_stopwords(words):
    return [word for word in words if word not in set(stopwords.words('english'))]
    

def remove_punctuations(words):
    symbols = "!\"#$%&()*+./:;<=>?@[\]^_`{|}~\n"
    for i in symbols:
        words = np.char.replace(words, i, '')

    return [word for word in words if word]

def to_root(words):
    lemmatized_words = []
    lemmatizer = WordNetLemmatizer()
    tagged = nltk.pos_tag(words)
    for (word, tag) in tagged:
        if tag.startswith('J'):
            pos = wordnet.ADJ
        elif tag.startswith('V'):
            pos = wordnet.VERB
        elif tag.startswith('N'):
            pos = wordnet.NOUN
        elif tag.startswith('R'):
            pos = wordnet.ADV
        else:
            pos = 'n'

        lemmatized_words.append(lemmatizer.lemmatize(word, pos))
    
    return lemmatized_words

def find_keys(words):
    keys = []
    tagged = nltk.pos_tag(words)
    for (word, tag) in tagged:
        if tag == 'VB' or tag == 'NN' or tag == 'NNP':
            keys.append(word)

    return keys
