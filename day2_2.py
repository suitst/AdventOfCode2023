# find the power of the minimum set of cubes to make each game possible
# for each game, find the highest number of each color
# multiply these numbers together
# sum these multiples

import pandas as pd
import re
import numpy as np

DRAW_LIST = ['draw1', 'draw2', 'draw3', 'draw4', 'draw5', 'draw6']
COLOR_LIST = ['red', 'green', 'blue']

raw = pd.read_csv('./Day2_1.csv', header=None)

raw.columns = ['raw']

split_series = raw['raw'].str.split(pat=':', n=1, expand=True)
raw['data'] = split_series[1]
raw.drop(['raw'], axis=1, inplace=True)

draws = raw['data'].str.split('; ', expand=False)

print(draws.head())

test_list = ' 4 red, 5 blue, 4 green, 7 red, 8 blue,'

def get_color_values(draw_list):
    values = {'red': [], 'green': [], 'blue': []}
    for color in COLOR_LIST:
        for a in draw_list:
            color_vals = re.findall(rf"(\d+ {color})", a)
            for i in color_vals:
                split_string = i.split(' ')
                values[color].append(int(split_string[0]))

    return values

draws['values'] = draws.apply(get_color_values)


def get_max_value(values):
    for key in values.keys():
        highest = max(values[key])
        values[key] = highest
    return values

draws['values'] = draws['values'].apply(get_max_value)


def get_product(values):
    return np.prod(list(values.values()))

draws['product'] = draws['values'].apply(get_product)


sum = draws['product'].sum()

print(sum)