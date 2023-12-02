import unittest

import Day1
import FileHelper


class MyTestCase(unittest.TestCase):
    def test_Solves(self):
        self.assertEqual(Day1.solve_1(['1abc2']), 12)
        self.assertEqual(Day1.solve_1(['pqr3stu8vwx']), 38)

    def test_solves_line_with_more_then2_numbers(self):
        self.assertEqual(Day1.solve_1(['a1b2c3d4e5f']), 15)

    def test_solve_sums_values_of_all_lines(self):
        self.assertEqual(Day1.solve_1(['1abc2',
                                     'pqr3stu8vwx',
                                     'a1b2c3d4e5f',
                                     'treb7uchet']), 142)

    def test_solves_day1(self):
        self.assertEqual(Day1.solve_1(FileHelper.read_file(1)), 53334)

    def test_considers_lettered_numbers_as_numbers(self):
        self.assertEqual(Day1.solve_2(
            ['two1nine',
             'eightwothree',
             'abcone2threexyz',
             'xtwone3four',
             '4nineeightseven2',
             'zoneight234',
             '7pqrstsixteen']), 281)

    def test_solves_complex_line(self):
        self.assertEqual(Day1.solve_2(['sevenine', ]), 79)

    def test_solves_day2(self):
        self.assertEqual(Day1.solve_2(FileHelper.read_file(1)), 52834)


if __name__ == '__main__':
    unittest.main()
