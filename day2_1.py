# preprocess dataset
# set validity criteria
# check validity of each game
# sum game ids of valid games

import pandas as pd
import re

DRAW_LIST = ['draw1', 'draw2', 'draw3', 'draw4', 'draw5', 'draw6']
VALID_VALUES = {'r': 12, 'g': 13, 'b': 14}

raw = pd.read_csv('./Day2_1.csv', header=None)

raw.columns = ['raw']

split_series = raw['raw'].str.split(pat=':', n=1, expand=True)
id = split_series[0].str.split(pat=' ', n=1, expand=True)
raw['gameID'] = id[1].astype(int)
raw['data'] = split_series[1]

# each game has three draws separated by semi-colons
# need to make a column for each draw

split_draws = raw['data'].str.split(pat=';', expand=True)
raw['draw1'] = split_draws[0]
raw['draw2'] = split_draws[1]
raw['draw3'] = split_draws[2]
raw['draw4'] = split_draws[3]
raw['draw5'] = split_draws[4]
raw['draw6'] = split_draws[5]


# convert each of these draws into lists of strings

for draw in DRAW_LIST:
    color_split = raw[draw].str.split(pat=', ', expand=False)

    raw[draw] = color_split

# convert lists to dicts with color as key and number as value

def convert_to_dict(list):
    dict = {}
    if not list:
        pass
    else:
        for i in list: 
            key = re.findall(r'[^ \d+]', i)
            val = re.findall(r'\d+', i)
            dict[key[0]] = int(val[0])
        return dict

for draw in DRAW_LIST:
    raw[draw] = raw[draw].apply(convert_to_dict)


def check_if_valid(dict): 
    if not dict:
        pass
    else:
        keys = ['r', 'g', 'b']
        results = []
        for key in keys:
            if key not in dict.keys():
                pass
            elif dict[key] > VALID_VALUES[key]:
                results.append(False)
            else: 
                results.append(True)
        if not all(results):
            return False
        else:
            return True
        

if __name__ == "__main__":
    for draw in DRAW_LIST:
        raw[draw] = raw[draw].apply(check_if_valid)

    raw = raw.fillna(True, axis=0)
    raw['result'] = raw.all(axis='columns', bool_only=True)

    filtered = raw[raw.result]

    sum = filtered['gameID'].sum()
    print(sum)

    raw.to_csv('./output.csv', index=False)