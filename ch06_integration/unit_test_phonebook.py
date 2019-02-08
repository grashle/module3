# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 10:43:11 2019

@author: amand
"""

import os
from sqlite3 import OperationalError
import unittest
from funcs import *
from unittest.mock import patch 


class search_engine_test(unittest.TestCase): #Testcase is a function in unittest.
    def test_check_db(self):
       self.assertTrue(check_db("phonebook.db"))
    
    def test_get_db(self):
        self.assertIsNotNone(get_db())
        
    def test_name_input(self):
        with patch('builtins.input', return_value = "Gracy"):
            self.assertEqual(name_input(), "Gracy")
            
    def test_search_type_input(self):
        with patch('builtins.input', return_value = "Person"):
            self.assertEqual(search_type_input(), "person")     
        with patch('builtins.input', return_value = "peop"):
            self.assertEqual(search_type_input(), "peop") 
        with patch('builtins.input', return_value = "1"):
            self.assertEqual(search_type_input(), "1") 
            
    def test_business_search_type_input(self):
        with patch('builtins.input', return_value = "Name"):
            self.assertEqual(business_search_type_input(), "name")            
        with patch('builtins.input', return_value = "type"):
            self.assertEqual(business_search_type_input(), "type")            
                
    def test_business_type_input(self):
        with patch('builtins.input', return_value = "Name"):
            self.assertEqual(business_type_input(), "Name")            
        with patch('builtins.input', return_value = "toys"):
            self.assertEqual(business_type_input(), "Toys")   
            
    def test_postcode_input(self):
        with patch('builtins.input', return_value = "LE14 2WB"):
            self.assertEqual(postcode_input(), "LE14 2WB")
        with patch('builtins.input', return_value = "LE142WB"):
            self.assertEqual(postcode_input(), "LE142WB")
        with patch('builtins.input', return_value = "le14 2wb"):
            self.assertEqual(postcode_input(), "LE14 2WB")
            
    def test_get_data_from_db(self):
        self.assertEqual(get_data_from_db("SELECT * FROM person WHERE surname = ?", "Jolly"),[('Jolly', 'Wright','726 Arrowood Junction','Liverpool', None,
  'L33 0XB','0913 285 5440')])
        self.assertEqual(get_data_from_db("SELECT * FROM person WHERE surname = ?", "Gracy"),[])
        self.assertEqual(get_data_from_db("SELECT * FROM business WHERE business_name = ?", "Oodoo"),[('Oodoo',  'Toys',  '9110 Havey Circle',  'Halton',  None,  'LS9 0AE', '0513 213 6316')])
        self.assertEqual(get_data_from_db("SELECT * FROM business WHERE business_name = ?", "Ood"),[])
        self.assertEqual(get_data_from_db("SELECT * FROM coordinate_mapping WHERE postcode = ?", "LS9 0AE"),[('LS9 0AE', 53.791042, -1.51594)])
        self.assertEqual(get_data_from_db("SELECT * FROM coordinate_mapping WHERE postcode = ?", "LF9 0AE"),[])
        
    def test_postcode_validation(self):
        self.assertTrue(postcode_validation("LS9 0AE"))
        self.assertFalse(postcode_validation("LS90AE"))
    
    def test_calculate_distance(self):
        self.assertEqual(calculate_distance("SL8 0AE", "LS9 0AE"), "no result")
        self.assertEqual(calculate_distance("LS9 0AE", "LS9 0AE"), 0.0)
    
#    
    def test_sort_by_distance(self):
        self.assertEqual(sort_by_distance([{'name': 'DabZ', 'category': 'Toys', 'street': '271 Sage Place', 'town': 'Church End', 'postcode': 'N3 1AA', 'tel_number': '0204 686 0032', 'distance': 2.554142318489907}, {'name': 'Oodoo', 'category': 'Toys', 'street': '9110 Havey Circle', 'town': 'Halton', 'postcode': 'LS9 0AE', 'tel_number': '0513 213 6316', 'distance': 0.0}, {'name': 'Plajo', 'category': 'Toys', 'street': '7962 Walton Park', 'town': 'Newtown', 'postcode': 'RG20 0AD', 'tel_number': '0146 210 8394', 'distance': 2.4482446449546234}, {'name': 'Vipe', 'category': 'Toys', 'street': '18 Garrison Center', 'town': 'London', 'postcode': 'EC1V 0AG', 'tel_number': '0795 178 2746', 'distance': 2.6714401798522465}, {'name': 'Eimbee', 'category': 'Toys', 'street': '03 Old Shore Trail', 'town': 'Norton', 'postcode': 'NN11 0GB', 'tel_number': '0361 836 3475', 'distance': 1.5554165868399963}]),[{'name': 'Oodoo',
  'category': 'Toys',
  'street': '9110 Havey Circle',
  'town': 'Halton',
  'postcode': 'LS9 0AE',
  'tel_number': '0513 213 6316',
  'distance': 0.0},
 {'name': 'Eimbee',
  'category': 'Toys',
  'street': '03 Old Shore Trail',
  'town': 'Norton',
  'postcode': 'NN11 0GB',
  'tel_number': '0361 836 3475',
  'distance': 1.56},
 {'name': 'Plajo',
  'category': 'Toys',
  'street': '7962 Walton Park',
  'town': 'Newtown',
  'postcode': 'RG20 0AD',
  'tel_number': '0146 210 8394',
  'distance': 2.45},
 {'name': 'DabZ',
  'category': 'Toys',
  'street': '271 Sage Place',
  'town': 'Church End',
  'postcode': 'N3 1AA',
  'tel_number': '0204 686 0032',
  'distance': 2.55},
 {'name': 'Vipe',
  'category': 'Toys',
  'street': '18 Garrison Center',
  'town': 'London',
  'postcode': 'EC1V 0AG',
  'tel_number': '0795 178 2746',
  'distance': 2.67}] )
            
if __name__ == '__main__':
    unittest.main()   
            
   