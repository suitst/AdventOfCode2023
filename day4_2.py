# need to track how many times each card is unlocked

CARD_TOTALS = {}
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


def init_cards(list):
    for i in list:
        CARD_TOTALS[f'card {list.index(i)+1}'] = 1


def generate_copies(index, wins):
    if wins != 0:
        for i in range((index+2), (index+wins+2)):
                CARD_TOTALS[f'card {i}'] += CARD_TOTALS[f'card {index+1}']
    else:
        pass


def count_cards(list):
    for line in list:
        wins, tests = get_wins_and_tests(line)
        num_wins = check_for_wins(wins, tests)
        generate_copies(list.index(line), num_wins)


init_cards(raw_input)
count_cards(raw_input)

sum = sum(CARD_TOTALS.values())
print(sum)
