from collections import defaultdict
import re


def count_words(words):
    result = defaultdict(int)

    for word in re.findall("[\w']+", words):
        result[word.lower()] += 1

    return result
