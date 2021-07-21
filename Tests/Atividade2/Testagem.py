import unittest
import Q1, Q2, Q3, Q4

class Testagem(unittest.TestCase):

    def test_Q1(self):
        self.assertEqual("Sao multiplos", Q1.multiplos(6, 3))

    def test_Q2(self):
        self.assertEqual("Categoria: juvenil A", Q2.categoria(13))

    def test_Q3(self):
        self.assertEqual(None, Q3.peso("M", 1.8))

    def test_Q4(self):
        self.assertEqual("A ordem eh = [6, 5, 4]", Q4.conj(2, [4, 5, 6]))

if __name__ == "__main__":
    unittest.main()