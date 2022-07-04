import math
from collections import Counter
import numpy as np
import Levenshtein as lev

def cosine_similarity(list1, list2):
    list1, list2 = Counter(list1), Counter(list2)
    terms = set(list1).union(list2)
    dotprod = sum(list1.get(k, 0) * list2.get(k, 0) for k in terms)
    magA = math.sqrt(sum(list1.get(k, 0)**2 for k in terms))
    magB = math.sqrt(sum(list2.get(k, 0)**2 for k in terms))
    
    return dotprod / (magA * magB)

def length_similarity(list1, list2):
    list1, list2 = Counter(list1), Counter(list2)
    lenlist1, lenlist2 = sum(list1.values()), sum(list2.values())

    return (min(lenlist1, lenlist2) / float(max(lenlist1, lenlist2))) * cosine_similarity(list1, list2)

def jaccard_similarity(list1, list2):
    intersection = len(list(set(list1).intersection(list2)))
    union = (len(list1) + len(list2)) - intersection

    return float(intersection) / union

def euclidean_distance(list1, list2):
    list1, list2 = Counter(list1), Counter(list2)
    terms = set(list1).union(list2)
    list1 = [list1.get(k, 0) for k in terms]
    list2 = [list2.get(k, 0) for k in terms]

    return np.linalg.norm(np.array(list1) - np.array(list2))

def levenshtein_distance(list1, list2):
    return lev.seqratio(list1, list2)

