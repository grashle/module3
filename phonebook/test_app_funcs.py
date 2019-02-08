# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 09:22:06 2019

@author: amand
"""

import sqlite3
import os


def check_db(db_path):
    if os.path.exists(db_path):
        return True
    else:
        return False
    
    
def get_db():
    conn = sqlite3.connect("phonebook.db")
    c = conn.cursor()
    return c

def person_search(name, postcode):
    persons = get_person_data(name)
    if len(persons) == 0:
        return "Sorry, your search produced no results."
    else:
        if postcode != '':
            persons = narrow_by_location(persons, postcode)
            if len(persons) == 0:
                return "Sorry, your search produced no results."
            else:
                return persons
        else:
            return persons

def person_search_results(name, postcode):
      person_result=person_search(name, postcode)
      person_results_list=[]
      for each_person in person_result:
            person_dictionary={}
            person_dictionary["surname"]=each_person[0]
            person_dictionary["first_name"]=each_person[1]
            person_dictionary["street"]=each_person[2]
            person_dictionary["town"]=each_person[3]
            person_dictionary["postcode"]=each_person[5]
            person_dictionary["tel_number"]=each_person[6]
        
            person_results_list.append(person_dictionary)
      results=sorted(person_results_list, key=lambda s:s["first_name"])
      return(results)

def business_name_search(business_name, postcode):
    businesses = get_businessName_data(business_name)
    if len(businesses) == 0:
        return "Sorry, your search produced no results."
    else:
        if postcode != '':
            businesses = narrow_by_location(businesses, postcode)
            if len(businesses) == 0:
                return "Sorry, your search produced no results."
            else:
                return businesses
        else:
            return businesses

def business_type_search(business_type, postcode):
    businesses = get_businessType_data(business_type)
    if len(businesses) == 0:
        return "Sorry, your search produced no results."
    else:
        if postcode != '':
            businesses = narrow_by_location(businesses, postcode)
            if len(businesses) == 0:
                return "Sorry, your search produced no results."
            else:
                return businesses
        else:
            return businesses

def get_person_data(person):
    c = get_db()
    c.execute("SELECT * FROM person WHERE surname = ?", (person,))
    return c.fetchall()

def get_businessName_data(businessName):
    c = get_db()
    c.execute("SELECT * FROM business WHERE business_name = ?", (businessName,))
    return c.fetchall()

def get_businessType_data(businessType):
    c = get_db()
    c.execute("SELECT * FROM business WHERE business_category = ?", (businessType,))
    return c.fetchall()

def narrow_by_location(results_list, postcode):
        results = []
        for deets in results_list:
            if postcode in deets:
                results.append(deets)
            else:
                results = results
        return results

def location_of_postcode_entered(postcode):
      c = get_db()
      c.execute("SELECT * FROM coordinate_mapping WHERE postcode = ?", (postcode,))
      return c.fetchall()

def location_of_businesses(business_name_or_type, business_search_type):
      if business_search_type == "type":
            business_list = get_businessType_data(business_name_or_type)
      elif business_search_type == "name":
            business_list = get_businessName_data(business_name_or_type)
      else: 
            return 'error'
      location_list = []
      
      for business in business_list:
            individual_business=[]
            for feature in business:
                  individual_business.append(feature)
            co_ords=location_of_postcode_entered(business[5])
            individual_business.append(co_ords[0][2])
            individual_business.append(co_ords[0][3])
            individual_business.remove(None)
            location_list.append(individual_business)
            
      return location_list
      
def compare_distance(postcode, business_name_or_type, business_search_type):
      user_postcode = location_of_postcode_entered(postcode)
      business_list = location_of_businesses(business_name_or_type, business_search_type)
      results_list=[] 

      for business in business_list:
            
            dlon=business[6]-user_postcode[0][2]
            dlat=business[7]-user_postcode[0][3]
            dist=((dlon**2 + dlat**2) **0.5)
            business_dict={}
            business_dict["name"]=business[0]
            business_dict["type"]=business[1]
            business_dict["street"]=business[2]
            business_dict["town"]=business[3]
            business_dict["postcode"]=business[4]
            business_dict["phone"]=business[5]
            business_dict["distance"]=dist
            results_list.append(business_dict)
      results=sorted(results_list, key=lambda s:s["distance"])
      for dictionary in results:
            dictionary["distance"]=round(dictionary["distance"], 3)
      return (results)


                        
      

      