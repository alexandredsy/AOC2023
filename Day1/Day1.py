import re


def replace_string_to_number(val):
    return (val.replace("one", "1").replace("two", "2").replace("three", "3").replace("four", "4")
            .replace("five", "5").replace("six", "6").replace("seven", "7").replace("eight", "8").replace("nine", "9"))


def get_value_for_line(line, pattern):
    numbers = pattern.findall(line)
    return int(replace_string_to_number(numbers[0]) + replace_string_to_number(numbers[-1]))


def solve_1(values):
    result = 0
    pattern = re.compile('\d')
    for val in values:
        result += get_value_for_line(val, pattern)
    return result


def solve_2(values):
    pattern = re.compile('(?=(\d|one|two|three|four|five|six|seven|eight|nine))')
    result = 0
    for val in values:
        result += get_value_for_line(val, pattern)
    return result
