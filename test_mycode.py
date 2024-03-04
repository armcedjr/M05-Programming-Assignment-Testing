"""
Armando Cedano
M05 Testing
This is the file containing the unit tests for mycode.py.
"""

# test_mycode.py

import unittest
from mycode import add

class TestMyCode(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
