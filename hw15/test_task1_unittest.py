import unittest
import logging
from task1 import Matrix


class TestMatrix(unittest.TestCase):
    def setUp(self) -> None:
        self.m1 = Matrix(3, 2)
        self.m1.data = [[1, 2], [3, 4], [5, 6]]
        self.m2 = Matrix(2, 3)
        self.m2.data = [[7, 8, 4], [9, 10, 5]]
        self.m3 = Matrix(2, 3)
        self.m3.data = [[7, 8, 4], [9, 10, 5]]
        self.m4 = Matrix(3, 3)
        self.m5 = Matrix(2, 2)
        self.m5.data = [[7, 8], [9, 10]]

    def test_matrix_eq(self):
        self.assertEqual(self.m2, self.m3, 'Матрицы не равны')

    def test_matrix_add(self):
        self.assertIsInstance(self.m2+self.m3, Matrix, 'Проверьте, что результат сложения - Matrix')

    def test_matrix_add_invalid(self):
        with self.assertRaises(ValueError):
            result = self.m1 + self.m2

    def test_matrix_add_valid(self):
        result = Matrix(2, 3)
        result.data = [[14, 16, 8], [18, 20, 10]]
        self.assertEqual(self.m2 + self.m3, result)

    def test_matrix_mul_invalid_data(self):
        with self.assertRaises(IndexError):
            result = self.m1 * self.m2

    def test_matrix_mul_invalid(self):
        with self.assertRaises(ValueError):
            result = self.m1 * self.m4

    def test_matrix_mul_valid(self):
        result = self.m1 *  self.m5
        self.assertIsInstance(result, Matrix, 'При умножении двух матриц возникла ошибка. Проверьте правильность введенных данных.')
    
if __name__ == '__main__':
    unittest.main(verbosity=4)
    
    