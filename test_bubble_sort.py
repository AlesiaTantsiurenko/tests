import unittest
from bubble_sort import bubble_sort
"""
Тестируем нашу функцию
"""


class BubbleSortTest(unittest.TestCase):

    def test_integer(self):
        """ Проверяем работу функции с целыми числами """
        self.assertEqual(bubble_sort([4, 8, 3, 5]), [3, 4, 5, 8])

    def test_float(self):
        """ Проверяем работу функции с вещественными числами """
        self.assertEqual(bubble_sort([6.7, 8.7, -3.4, -2.7]), [-3.4, -2.7, 6.7, 8.7])

    def test_str(self):
        """ Проверяем работу со строками """
        self.assertEqual(bubble_sort([
            "orange",
            "prawns",
            "222",
            "картошечка",
            "111"
        ]),  [
                "111",
                "222",
                "orange",
                "prawns",
                "картошечка"
            ])

    def test_mix(self):
        """ Проверяем, было ли поднято исключение при комбинированом использовании типов """
        with self.assertRaises(TypeError):
            bubble_sort([1, 'a', None])