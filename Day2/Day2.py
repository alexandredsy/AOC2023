import re


def get_game_number(input):
    pattern = re.compile('Game (\d*)')
    return int(pattern.findall(input)[0])


def get_count(input, color):
    pattern = re.compile(f'(\d*) {color}')
    return max(map(int, pattern.findall(input)), default=0)


def game_is_valid(result, blue, green, red):
    return ((get_count(result, 'blue') <= blue) &
            (get_count(result, 'green') <= green) &
            (get_count(result, 'red') <= red))


def solve_1(results, blue, green, red):
    solution = 0
    for result in results:
        if game_is_valid(result, blue, green, red):
            solution += get_game_number(result)
    return solution


def solve_2(results, blue, green, red):
    solution = 0
    for result in results:
        solution += get_count(result, 'blue') * get_count(result, 'green') * get_count(result, 'red')
    return solution
