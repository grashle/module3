# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 12:17:35 2019

@author: gracy
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
    search_type = input("Search for person or business?\n")
    if search_type == "person":
        search_for_person()
    elif search_type == "business":
        search_for_business()
    else:
        print("Error.")
        return "Exit due to invalid response."
    
def search_for_person():
    location_choice = include_location()
    inputPersonName = input("Please enter a name: ")
    c = get_db()
    c.execute("SELECT * FROM person WHERE surname = ?", (inputPersonName,))
    psn_results = c.fetchall()
    if len(psn_results) == 0:
        print("Sorry, nobody by that name exists in the database.")
    else:
        if location_choice:
            narrow_by_location(psn_results, "person")
        else:
            for person_deets in psn_results:
                    print(person_deets)


def narrow_by_location(results_list, searchType):
        location = input("Please enter a postcode: ")
        results = []
        for deets in results_list:
            if location in deets:
                results.append(deets)
            else:
                results = results
        if len(results) == 0:
            print("Sorry, no such {} in specified postcode in database.".format(searchType))
        else:
            print(results)


def search_for_business():
    searchChoice = input("Would you like to search by business name or business type?\n")
    if searchChoice == "name":
        include_location()
        print(business_by_name())
    elif searchChoice == "type":
        include_location()
        print(business_by_type())
    else:
        print("Error.")
        return "Exit due to invalid response."

def business_by_name():
    inputBusinessName = "Flashspan"
    location = "AB39 2ZH"
#    inputBusinessName = input("Please enter the name of the business you are looking for: ")
#    location = input("Please enter the location: ")
    c.execute("SELECT * FROM business WHERE business_name = ? AND postcode = ?", (inputBusinessName, location))
    results = c.fetchall()
    if len(results) == 0:
        return("Sorry, no business by that name exists in the database.")
    else:
        for i in range(len(results)):
            businesspostcode = results[i][5]
            c.execute("SELECT x_coordinate , y_coordinate FROM coordinate_mapping WHERE postcode = ?", (businesspostcode,))
            for row in c.fetchall():
                print(row)

def business_by_type():
    inputBusinessType = input("Please enter the type of business you are looking for: ")
    if include_location():
        location = input("Please enter the location: ")
        c.execute("SELECT * FROM business WHERE business_category = ? AND town_city = ? ORDER BY business_name", (inputBusinessType, location))
    else:
        c.execute("SELECT * FROM business WHERE business_category = ? ORDER BY business_name", (inputBusinessType,))
    if len(c.fetchall()) == 0:
        return("Sorry, no business of that type exists in the database.")
    else:
        for row in c.fetchall():
            return(row)

def include_location():
    locationChoice = input("Would you like to narrow your search by postcode?\n")
    if locationChoice == "yes":
        return True
    elif locationChoice == "no":
        return False
    else:
        print("Error.")
        return False