import unittest
from get_primes.py import is_prime

class generateprimeTestcase(unittest.Testcase)
	def test_isprime(self):
		self.assertEqual(generate_primes(5),(3,5))
	def test_negative(self):
		self.assertEqual(generate_primes(-1),'Return negative numbers')
	def test_lessthantwo(self):
		self.assertEqual(generate_primes(1),'Not a prime number')
	def test_string(self):
		self.assertEqual(generate_primes('hhhdh'),'Not a prime number')
if __name__ == '__main__':
	unittest.main()