import unittest
from logic import get_number_index, get_empty_list, get_index_from_number, \
    is_zero_in_mas, move_left, move_up, move_down

class Test_2048(unittest.TestCase):

    def test_get_number_1(self):
        self.assertEqual(get_number_index(1, 2), 7)

    def test_get_number_2(self):
        self.assertEqual(get_number_index(3, 3), 16)

    def test_get_empty_1(self):
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        mas = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        self.assertEqual(get_empty_list(mas), a)

    def test_get_empty_2(self):
        a = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        mas = [
            [1, 1, 1, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]

    def test_get_empty_3(self):
        a = []
        mas = [
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
        ]
        self.assertEqual(get_empty_list(mas), a)

    def test_get_index_1(self):
        self.assertEqual(get_index_from_number(1), (0, 0))

    def test_get_index_2(self):
        self.assertEqual(get_index_from_number(16), (3, 3))

    def test_is_zero1(self):
        mas = [
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
        ]
        self.assertEqual(is_zero_in_mas(mas), False)

    def test_is_zero2(self):
        mas = [
            [1, 1, 1, 1],
            [1, 1, 0, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
        ]
        self.assertEqual(is_zero_in_mas(mas), True)

    def test_move_left(self):
        mas = [
            [2, 0, 0, 2],
            [2, 4, 0, 0],
            [0, 0, 2, 2],
            [4, 0, 4, 0],
        ]
        rez = [
            [4, 0, 0, 0],
            [2, 4, 0, 0],
            [4, 0, 0, 0],
            [8, 0, 0, 0],
        ]
        self.assertEqual(move_left(mas), (rez, 16))

    def test_move_up(self):
        mas = [
            [2, 0, 0, 2],
            [2, 4, 0, 0],
            [0, 0, 2, 2],
            [4, 0, 4, 0],
        ]
        rez = [
            [4, 4, 2, 4],
            [4, 0, 4, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        self.assertEqual(move_up(mas), (rez, 8))

    def test_move_down(self):
        mas = [
            [2, 0, 0, 2],
            [2, 4, 0, 0],
            [0, 0, 2, 2],
            [4, 0, 4, 0],
        ]
        rez = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [4, 0, 2, 0],
            [4, 4, 4, 4],
        ]
        self.assertEqual(move_down(mas), (rez, 8))
