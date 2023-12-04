# split strings into winning nums, test nums
# get number of matches for each card
# return 2^num matches for each
# sum the scores

raw_input = []

with open('./day4_1_input.txt', 'r') as input_file:
    for line in input_file:
        raw_input.append(line.strip('\n'))




example_list = []
with open('./day4_1_example.txt', 'r') as example:
    for line in example:
        example_list.append(line.strip('\n'))


def get_wins_and_tests(string):
    nums = string.split('|')
    wins = nums[0].split(':')[1]
    wins_list = wins.split(' ')
    tests = nums[1].split(' ')
    return wins_list, tests


def check_for_wins(wins, tests):
    num_wins = 0
    for i in tests:
        if i != '':
            if i in wins:
                num_wins += 1
    return num_wins


def get_score(num_wins):
    if num_wins != 0:
        return pow(2, (num_wins-1))
    else:
        return 0


def get_total_score(list):
    total_score = 0
    for line in list:
        wins, tests = get_wins_and_tests(line)
        num_wins = check_for_wins(wins, tests)
        score = get_score(num_wins)
        total_score += score
    return total_score


total_score = get_total_score(raw_input)
print(f'total score: {total_score}')