# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 10:39:34 2019

@author: gracy
"""

class Calculator(object):
      def add (self, x, y):
            number_types=(int,float, complex)
            if isinstance(x, number_types) and (y, number_types):
                  return x+y
            else:
                  raise ValueError
                  