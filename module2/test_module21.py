import unittest
import inspect


class Module21TestCase(unittest.TestCase):

    def test_method21_1(self):
        print("Test", self.__class__, inspect.stack()[0][3])
        self.assertTrue(True)

    def test_method21_2(self):
        print("Test", self.__class__, inspect.stack()[0][3])
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()

