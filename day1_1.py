# Aims: extract the first and last number from each string
# Sum the formed double-digit numbers

import pandas as pd
import re


data = pd.read_csv('./day1_1.csv', header=None)
data.columns = ['input']
test_string = '852bfkjmccknlqreight1'

def find_numbers(string):
    nums = re.findall(r'\d+', string)
    if len(nums) < 2:
        if int(nums[0]) <= 9:
            return (nums[0], nums[0])
        else:
            return (nums[0][:1], nums[0][-1])
    else:
        return (nums[0], nums[-1])


def make_double_digit(nums_tuple):
    new_num = nums_tuple[0][:1] + nums_tuple[1][-1]
    return new_num


def check_all_doubles(value_list):
    for i in value_list:
        assert len(i) == 2


def collect_doubledigits(df):
    values = []
    for i in df:    
        extracted_num = find_numbers(i)
        new_num = make_double_digit(extracted_num)
        values.append(new_num)
    check_all_doubles(values)
    return values


def convert_to_int(value_list):
    return list(map(int, value_list))


def sum_list(int_list):
    return sum(int_list)


def get_calibration_values(dataframe):
    str_list = collect_doubledigits(dataframe)
    int_list = convert_to_int(str_list)
    sum = sum_list(int_list)
    return sum


if __name__ == "__main__":
    sum = get_calibration_values(data['input'])
    print(f"The sum of the calibration values is {sum}")
