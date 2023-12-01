# convert written numbers to roman number
# perform same treatment as 1-1

import pandas as pd
import re

from day1_1 import get_calibration_values

NUMBERS_DICT = {'eighthree': 83,
            'eightwo': 82,
            'fiveight': 58,
            'nineight': 98,
            'oneight': 18,
            'sevenine': 79,
            'threeight': 38,
            'twone': 21,
            'one': 1,
            'two': 2,
            'three': 3, 
            'four': 4,
            'five': 5,
            'six': 6,
            'seven': 7,
            'eight': 8,
            'nine': 9}

KEYS = NUMBERS_DICT.keys()

data = pd.read_csv('./day1_1.csv', header=None)
data.columns = ['input']

test_string = 'jneightwofivetwo9eightgjtnrneight'


def find_indexes(word, string):
    indexes = [x.start() for x in re.finditer(word, string)]
    return indexes


def find_words_in_string(string):
    words = []
    for i in KEYS:
        indexes = find_indexes(i, string)
        for x in indexes:
            words.append((i, x))
    words.sort(key=lambda tup: tup[1])
    return words


def replace_words_with_digits(string):
    for i in KEYS:
        if i in string:
            string = string.replace(i, str(NUMBERS_DICT[i]))
    return string


if __name__ == "__main__":
    data['output'] = data['input'].apply(replace_words_with_digits)
    sum = get_calibration_values(data['output'])
    data.to_csv('./day1_2_output.csv', index=False)
    print(f"The sum of the calibration values is {sum}")