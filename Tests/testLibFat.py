import unittest
import libfat

class testLibFat(unittest.TestCase):
    # testar fatorial de 0 e 1
    def test_fatorial_0(self):
        self.assertEqual(1, libfat.fatorial(0))
        
    def test_fatorial_1(self):
        self.assertEqual(1, libfat.fatorial(1))
        
    def test_fatorial_maior_que_1(self):
        self.assertEqual(2, libfat.fatorial(2))
        self.assertEqual(6, libfat.fatorial(3))
        self.assertEqual(24, libfat.fatorial(4))
        self.assertEqual(120, libfat.fatorial(5))
        self.assertEqual(720, libfat.fatorial(6))
        
    def test_fatorial_negativos(self):
        with self.assertRaises(ValueError):
            libfat.fatorial(-1)

    def test_fatorial_decimal(self):
        with self.assertRaises(ValueError):
            libfat.fatorial(1.5)
        """
        Other way 👇

        try:
            self.assertRaises(ValueError)
        except:
            libfat.fatorial(1.5)
        """
            
if __name__ == "__main__":
    unittest.main()