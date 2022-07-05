import json
import logic_adapter
import preprocessing

minimum_similarity_threshold = 0.1

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    has_required_words = True

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return logic_adapter.cosine_similarity(user_message, recognised_words)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = [{
        'response': '',
        'probability': 0
    }]
    
    dataset = json.loads(open('dataset.json', 'r').read())

    for data in dataset:
        probability = message_probability(message, data['question'], single_response=True)
        if (probability > minimum_similarity_threshold):
            highest_prob_list.append({
                'response': data['response'],
                'probability': probability
            })

    best_match = max(highest_prob_list, key=lambda ev: ev['probability'])
    print(*highest_prob_list, sep='\n\n')
    # print(best_match)

    return 'Could you please re-phrase that?' if best_match['probability'] < minimum_similarity_threshold  else best_match['response']


def get_response(user_input):
    split_message = preprocessing.run(user_input)
    response = check_all_messages(split_message)
    return response


# Testing the response system
while True:
    print('\nBot: ' + get_response(input('You: ')))