import unittest


def fibonacci(n):
    if type(n) != int or n < 0:
        print("Incorrect the enter the value of n")
        return - 1
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


class TestFibonacci(unittest.TestCase):

    def setUp(self):
        self.n = 6
        self.n1 = -6
        self.n2 = ""
        self.n3 = 2

    def testNValueNotNumber(self):
        print("Result of testNValueNotNumber: ", fibonacci(self.n2))
        self.assertEqual(-1, fibonacci(self.n2))

    def testNValuelessThanXero(self):
        print("Result of testNValuelessThanXero: ", fibonacci(self.n1))
        self.assertEqual(-1, fibonacci(self.n1))

    def testNValuelessThan3(self):
        print("Result of testNValuelessThan3: ", fibonacci(self.n3))
        self.assertEqual(1, fibonacci(self.n3))

    def testNormalData(self):
        print("Result of testNormalData: ", fibonacci(self.n))
        self.assertEqual(8, fibonacci(self.n))


if __name__ =="__main__":
    unittest.main()