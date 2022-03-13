import unittest
from find_square_roots import find_square_roots
"""
Тестируем нашу функцию
"""


class SquareRootsTest(unittest.TestCase):

    def test_1(self):
        """ Проверяем работу с двумя параметрами """
        self.assertEqual(find_square_roots(1.0, 0.0, -4.0), (-2, 2))

    def test_no_roots(self):
        """ Проверяем работу функции при D < 0 """
        self.assertEqual(find_square_roots(1.0, 1.0, 1.0), (None, None))

    def test_two_roots(self):
        """ Проверяем работу функции с двумя корнями """
        self.assertEqual(find_square_roots(2.0, -4.0, -10.0), (-1.4494897427831779, 3.449489742783178))

    def test_one_root(self):
        """ Проверяем работу функции с одним корнем """
        self.assertEqual(find_square_roots(1.0, -6.0, 9.0), (3, None))

    def test_string(self):
        """ Проверяем, было ли поднято исключение при вводе строки """
        with self.assertRaises(TypeError):
            find_square_roots('c', 'b', 'a')