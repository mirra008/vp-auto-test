import unittest
import inspect


class Submodule1TestCase(unittest.TestCase):

    def test_method_sub1_1(self):
        print("Test", self.__class__, inspect.stack()[0][3])
        self.assertTrue(True)

    def test_method_sub1_2(self):
        print("Test", self.__class__, inspect.stack()[0][3])
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()

