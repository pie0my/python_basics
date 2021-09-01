# teste de game
from typing import Type
import unittest
import gametest


class TestGametest(unittest.TestCase):
    def test_input(self):
        resultado = gametest.guess_gaming(5, 5)
        self.assertTrue(resultado)

    def test_input_chute_errado(self):
        resultado = gametest.guess_gaming(5, 0)
        self.assertFalse(resultado)

    def test_input_numero_errado(self):
        resultado = gametest.guess_gaming(5, 16)
        self.assertFalse(resultado)

    def test_input_tipo_errado(self):
        resultado = gametest.guess_gaming(5, '16')
        self.assertFalse(resultado)


if __name__ == '__main__':
    unittest.main()
