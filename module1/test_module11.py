import unittest
import inspect


class Module11TestCase(unittest.TestCase):

    def test_method11_1(self):
        print("Test", self.__class__, inspect.stack()[0][3])
        self.assertTrue(True)

    def test_method11_2(self):
        print("Test", self.__class__, inspect.stack()[0][3])
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()

