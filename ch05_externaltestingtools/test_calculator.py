# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 10:27:38 2019

@author: gracy
"""

# writing the test file first

import unittest
from calculator import Calculator

class TddInPythonExample(unittest.TestCase):
      
      def setup(self):
            self.calc=Calculator()
      
      def test_calculator_add_method_correct(self):
            calc=Calculator()
            result = calc.add(2,2)
            self.assertEqual(4, result)
      
      def test_calculator_returns_error_if_both_args_not_numbers(self):
            self.calc=Calculator()
            self.assertRaises(ValueError, self.calc.add, 'two', 'three')
            
      def test_calculator_returns_error_if_x_not_number(self):
            self.assertRaises(ValueError, self.calc.add, 'two', 3)
            
      def test_calculator_returns_error_if_y_not_number(self):
            self.assertRaises(ValueError, self.calc.add, 2, 'three')
            
            