import nltk
import sanitizer

def run(words):
    words = nltk.word_tokenize(words)
    words = sanitizer.lower_case(words)
    words = sanitizer.remove_punctuations(words)
    words = sanitizer.to_root(words)

    return words