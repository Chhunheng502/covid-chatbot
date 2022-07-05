from logic_adapter import cosine_similarity
from logic_adapter import length_similarity
from logic_adapter import jaccard_similarity
from logic_adapter import euclidean_distance
from logic_adapter import levenshtein_distance

recognized_words = ['what', 'be', 'the', 'symptom', 'of', 'covid-19']

print('Cosine similarity:')
print(cosine_similarity(['what', 'be', 'covid-19', 'disease'], recognized_words))
print(cosine_similarity(['what', 'be', 'covid-19', 'symptom'], recognized_words))
print('\n')

print('Length similarity:')
print(length_similarity(['what', 'be', 'covid-19', 'disease'], recognized_words))
print(length_similarity(['what', 'be', 'covid-19', 'symptom'], recognized_words))
print('\n')

print('Jaccard similarity:')
print(jaccard_similarity(['what', 'be', 'covid-19', 'disease'], recognized_words))
print(jaccard_similarity(['what', 'be', 'covid-19', 'symptom'], recognized_words))
print('\n')

print('Euclidean distance:')
print(euclidean_distance(['what', 'be', 'covid-19', 'disease'], recognized_words))
print(euclidean_distance(['what', 'be', 'covid-19', 'symptom'], recognized_words))
print('\n')

print('Levenshtein distance:')
print(levenshtein_distance(['what', 'be', 'covid-19', 'disease'], recognized_words))
print(levenshtein_distance(['what', 'be', 'covid-19', 'symptom'], recognized_words))