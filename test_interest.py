import unittest
from interest import loan_calculator

class loan_calculator(unittest.TestCase):
	def testloan_calculator(self):
		self.assertEquals(loan_calculator(100000, 12, 12), 112000)
	def test_more_than_year(self):
		#self.assertEqual(loan_calculator(13),'Return invalid time')


if __name__ == '__main__':
	unittest.main()