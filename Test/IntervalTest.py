import unittest
from DocumentObject import Interval

class IntervalTest(unittest.TestCase):

    def test_sample(self):
        self.assertTrue(Interval(0,100))
        self.assertRaises(ValueError,Interval(10,0))
        # self.assertRaises(ValueError,Interval(-10,100))

if __name__ == "__main__":
    unittest.main()