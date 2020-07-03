# Unittest
# Author: vonewman

import unittest
from fibonacci import fib
from fibonacci_dp import fibonacciVal
from fibonacci_rec import F

class TestFibonacci(unittest.TestCase):
    """Doing Unittest on fibonacci algorithms"""

    def test_fib1(self):
        "testing the method from fibonacci"
        actual = fib(10)
        expected = 55
        self.assertEqual(expected, actual)

    def test_fib2(self):
        "testing the method from fibonacci_dp"
        actual = fibonacciVal(10)
        expected = 55
        self.assertEqual(expected, actual)

    def test_fib3(self):
        "testing the method from fibonacci_rec"
        actual = F(10)
        expected = 55
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main(exit=True)
