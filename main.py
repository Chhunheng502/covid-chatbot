import re
import json
import nltk
import preprocessing
import logic_adapter


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    has_required_words = True

    if has_required_words or single_response:
        return logic_adapter.cosine_similarity(user_message, recognised_words)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    dataset = json.loads(open('dataset.json', 'r').read())

    for data in dataset:

        response(data['response'], data['question'], single_response=True)

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    # 0.5 is minimum similarity threshold
    return 'Could you please re-phrase that?' if highest_prob_list[best_match] < 0.5  else best_match


# Used to get the response
def get_response(user_input):
    split_message = preprocessing.run(user_input)
    print(split_message)
    response = check_all_messages(split_message)
    return response


# Testing the response system
while True:
    print('Bot: ' + get_response(input('You: ')))