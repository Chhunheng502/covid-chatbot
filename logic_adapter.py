import math
from collections import Counter

def proportional_similarity(list1, list2):
    confidence_level = 0
    for word in list1:
        if word in list2:
            confidence_level += 1

    return float(confidence_level) / float(len(list2))


def cosine_similarity(list1, list2):
    list1, list2 = Counter(list1), Counter(list2)
    terms = set(list1).union(list2)
    dotprod = sum(list1.get(k, 0) * list2.get(k, 0) for k in terms)
    magA = math.sqrt(sum(list1.get(k, 0)**2 for k in terms))
    magB = math.sqrt(sum(list2.get(k, 0)**2 for k in terms))
    
    return dotprod / (magA * magB)

def length_similarity(list1, list2):
    lenlist1 = sum(list1.values())
    lenlist2 = sum(list2.values())

    return min(lenlist1, lenlist2) / float(max(lenlist1, lenlist2))

def similarity_score(list1, list2):
    list1, list2 = Counter(list1), Counter(list2)
    return length_similarity(list1, list2) * cosine_similarity(list1, list2)

# def euclidean_distance(list1, list2):
#     list1, list2 = Counter(list1), Counter(list2)
#     print(list1, list2)
#     squares = [(p-q) ** 2 for p, q in zip(list1.values(), list2.values())]

#     return sum(squares) ** .5

