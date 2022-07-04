from logic_adapter import proportional_similarity
from logic_adapter import cosine_similarity
from logic_adapter import similarity_score
# from logic_adapter import euclidean_distance

recognized_words = ['what', 'be', 'the', 'symptom', 'of', 'covid-19']

print(proportional_similarity(['what', 'be', 'covid-19'], recognized_words))
print(proportional_similarity(['what', 'be', 'covid-19', 'symptom'], recognized_words))

print(cosine_similarity(['what', 'be', 'covid-19'], recognized_words))
print(cosine_similarity(['what', 'be', 'covid-19', 'symptom'], recognized_words))

print(similarity_score(['what', 'be', 'covid-19'], recognized_words))
print(similarity_score(['what', 'be', 'covid-19', 'symptom'], recognized_words))

# print(euclidean_distance(['what', 'be', 'covid-19'], recognized_words))
# print(euclidean_distance(['what', 'be', 'covid-19', 'symptom'], recognized_words))