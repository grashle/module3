# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 11:12:28 2019

@author: 612383423
"""

import unittest

from ch4_gracy import is_prime

class PrimesTestCase(unittest.TestCase):
    """tests for ch4_gracy.py """
    def test_is_five_prime(self):
        """is five successfully determined to be prime?"""
        self.assertTrue(is_prime(5))
    
    def test_is_four_non_prime(self):
        """is four correctly determined not to be prime?"""
        self.assertTrue(is_prime(4), msg="four is not prime!")
        
    def test_is_zero_not_prime(self):
        """is zero correctly determined to be not prime?"""
        self.assertFalse(is_prime(0))

if __name__=='__main__':
    unittest.main()