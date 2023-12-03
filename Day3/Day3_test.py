import re
import unittest

import FileHelper


def find_all(inputs, filter):
    row_count = 0
    symbols = []
    for input in inputs:
        for match in re.finditer(filter, input):
            symbols.append((row_count, match.start(), match.end() - 1, match.group()))
        row_count += 1
    return symbols


def are_adjacent(number, symbol):
    return ((number[0] - symbol[0] < 2) &
            (number[0] - symbol[0] > -2) &
            (symbol[1] >= number[1] - 1) &
            (symbol[1] <= number[2] + 1))


def solve_1(inputs):
    result = 0
    symbols = find_all(inputs, '[^a-zA-Z0-9.\n]')
    numbers = find_all(inputs, '\d+')
    for number in numbers:
        for symbol in symbols:
            if are_adjacent(number, symbol):
                result += int(number[3])
                break
    return result


def solve_2(inputs):
    result = 0
    cogs = find_all(inputs, '\*')
    numbers = find_all(inputs, '\d+')
    for cog in cogs:
        adjacent_numbers = []
        for number in numbers:
            if are_adjacent(number, cog):
                adjacent_numbers.append(number)
        if len(adjacent_numbers) == 2:
            result += int(adjacent_numbers[0][3]) * int(adjacent_numbers[1][3])
    return result


class MyTestCase(unittest.TestCase):

    def test_matches_adjacent_lines(self):
        self.assertEqual(solve_1([
            "1..",
            ".*.",
        ]),
            1)
        self.assertEqual(solve_1([
            ".1.",
            ".*.",
        ]),
            1)
        self.assertEqual(solve_1([
            "..1",
            ".*.",
        ]), 1)
        self.assertEqual(solve_1([
            ".*.",
            "1..",
        ]),
            1)
        self.assertEqual(solve_1([
            ".*.",
            ".1.",
        ]),
            1)
        self.assertEqual(solve_1([
            ".*.",
            "..1",
        ]), 1)

    def test_basic_matching(self):
        self.assertEqual(solve_1(["*467..3$."]), 470)

    def test_ignores_non_parts(self):
        self.assertEqual(solve_1(["%.31.$"]), 0)

    def test_validates_p1(self):
        self.assertEqual(solve_1(["467..114..",
                                  "...*......",
                                  "..35..633.",
                                  "......#...",
                                  "617*......",
                                  ".....+.58.",
                                  "..592.....",
                                  "......755.",
                                  "...$.*....",
                                  "664.598.."]),
                         4361)

    def test_validates_p2(self):
        self.assertEqual(solve_2(["467..114..",
                                  "...*......",
                                  "..35..633.",
                                  "......#...",
                                  "617*......",
                                  ".....+.58.",
                                  "..592.....",
                                  "......755.",
                                  "...$.*....",
                                  "664.598.."]),
                         467835)

    def test_mutiplies_values_of_cogs(self):
        self.assertEqual(solve_2(["2*3.."]), 6)

    def test_solves_1(self):
        self.assertEqual(solve_1(FileHelper.read_file(3)), 544664)

    def test_solves_2(self):
        self.assertEqual(solve_2(FileHelper.read_file(3)), 84495585)


if __name__ == '__main__':
    unittest.main()
