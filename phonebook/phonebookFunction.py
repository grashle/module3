# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 12:17:35 2019

@author: amanda
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


def phonebook():
    search_type = search_type_input()
    if search_type == "person":
        persons = get_person_data(name_input())
        if len(persons) == 0:
            return "Sorry, your search produced no results."
        else:
            if include_location():
                persons = narrow_by_location(persons)
                if len(persons) == 0:
                    return "Sorry, your search produced no results."
                else:
                    return persons
            else:
                return persons
    elif search_type == "business":
        business_search_type = business_search_type_input()
        if business_search_type == "name":
            businesses = get_businessName_data(name_input())
            if len(businesses) == 0:
                return "Sorry, your search produced no results."
            else:
                if include_location():
                    businesses = narrow_by_location(businesses)
                    if len(businesses) == 0:
                        return "Sorry, your search produced no results."
                    else:
                        return businesses
                else:
                    return businesses
        elif business_search_type == "type":
            businesses = get_businessType_data(business_type_input())
            if len(businesses) == 0:
                return "Sorry, your search produced no results."
            else:
                if include_location():
                    businesses = narrow_by_location(businesses)
                    if len(businesses) == 0:
                        return "Sorry, your search produced no results."
                    else:
                        return businesses
                else:
                    return businesses
    else:
        print("Error.")
        return "Exit due to invalid response."

def search_type_input():
    search_type = input("Search for person or business?\n")
    return search_type

def business_search_type_input():
    business_search_type = input("Search by business name or business type?\n")
    return business_search_type
    
def name_input():
    inputName = input("Please enter a name: ")
    return inputName.title()

def business_type_input():
    inputBusinessType = input("Please enter the type of business you are looking for: ")
    return inputBusinessType

def postcode_input():
    postcode = input("Please enter a postcode: ")
    return postcode

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

def include_location():
    include_location = input("Would you like to narrow your search by postcode?\n")
    if include_location == "yes":
        return True
    elif include_location == "no":
        return False
    else:
        return "Error."

def narrow_by_location(results_list):
        postcode = postcode_input()
        results = []
        for deets in results_list:
            if postcode in deets:
                results.append(deets)
            else:
                results = results
        return results
