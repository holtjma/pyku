'''
Unit tests matter
For those who care about it
Auth.: holtjma
'''

import unittest

class UnitTests(unittest.TestCase):
    def test_Factorial(self):
        from Factorial import fac
        import math
        for x in xrange(0, 10):
            self.assertEqual(math.factorial(x), fac(x))
    
    def test_FibonacciLinear(self):
        from FibonacciLinear import fib
        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(2), 1)
        self.assertEqual(fib(5), 5)
        self.assertEqual(fib(10), 55)
        self.assertEqual(fib(20), 6765)
        self.assertEqual(fib(100), 354224848179261915075)
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
    unittest.TextTestRunner(verbosity=2).run(suite)