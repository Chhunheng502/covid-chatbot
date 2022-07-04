import nltk
import json
import sanitizer

convo = open('dataset.txt','r',encoding='utf-8').readlines()

dataset = []

for i, item in enumerate(convo):

    keys = []
    words = nltk.word_tokenize(convo[i])

    if (i % 2 == 0):
        keys = sanitizer.find_keys(sanitizer.remove_stopwords(words))

        # Data to be written
        data = {
            "question" : sanitizer.to_root(sanitizer.lower_case(sanitizer.remove_punctuations(words))),
            'keys': sanitizer.lower_case(keys),
            "response": convo[i + 1]
        }

        dataset.append(data)

        json_array = json.dumps(dataset, indent=2)

        with open("dataset.json", "w") as outfile:
            outfile.write(json_array)