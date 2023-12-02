import unittest

import Day2
import FileHelper


class MyTestCase(unittest.TestCase):
    def test_validates_p1(self):
        self.assertEqual(Day2.solve_1(["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
                                       "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
                                       "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
                                       "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
                                       "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green", ],
                                      14, 13, 12), 8)

    def test_solves_day2_1(self):
        self.assertEqual(Day2.solve_1(FileHelper.read_file(2), 14, 13, 12), 2505)

    def test_validates_p2(self):
        self.assertEqual(Day2.solve_2(["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
                                       "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
                                       "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
                                       "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
                                       "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green", ],
                                      14, 13, 12), 2286)
    def test_solves_day2_2(self):
        self.assertEqual(Day2.solve_2(FileHelper.read_file(2),14, 13, 12), 1)


if __name__ == '__main__':
    unittest.main()
