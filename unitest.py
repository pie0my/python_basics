from typing import Type
import unittest
import arquivo


class TestArquivo(unittest.TestCase):
    def test_algo(self):
        test_param = 10
        result = arquivo.algo(test_param)
        self.assertEqual(result, 15)

    def test_algo2(self):
        test_param = 'asdasd'
        result = arquivo.algo(test_param)
        self.assertIsInstance(result, ValueError)

    def test_algo3(self):
        test_param = None
        result = arquivo.algo(test_param)
        self.assertEqual(result, 'utilize um numero')

    def test_algo4(self):
        test_param = ''
        result = arquivo.algo(test_param)
        self.assertEqual(result, 'utilize um numero')


if __name__ == '__main__':
    unittest.main()
