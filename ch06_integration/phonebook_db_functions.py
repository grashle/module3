# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 10:11:31 2019

@author: amand
"""

import sqlite3
import json
import requests

conn = sqlite3.connect("phonebook.db")
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS business(business_name TEXT, business_category TEXT, address1 TEXT, town_city TEXT, county TEXT, postcode TEXT, telephone_number TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS person(surname TEXT, firstname TEXT, address1 TEXT, town_city TEXT, county TEXT, postcode TEXT, telephone_number TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS coordinate_mapping(town_city TEXT, postcode TEXT, x_coordinate REAL, y_coordinate REAL)")

#create_table()

person_file = open("json/mock_data_people_json.json")
person_data = json.load(person_file)

def dynamic_data_entry_person():
    for i in range(len(person_data)):
        surname = person_data[i]["last_name"]
        firstname = person_data[i]["first_name"]
        address1 = person_data[i]["address_line_1"]
        town_city = person_data[i]["address_line_2"]
        postcode = person_data[i]["postcode"]
        telephone_number = person_data[i]["telephone_number"]
        c.execute("INSERT INTO person(surname, firstname, address1, town_city, postcode, telephone_number) VALUES (?, ?, ?, ?, ?, ?)", (surname, firstname, address1, town_city, postcode, telephone_number))
        conn.commit()

business_file = open("json/mock_data_business_json.json")
business_data = json.load(business_file)

def dynamic_data_entry_business():
    for i in range(len(business_data)):
        business_name = business_data[i]["business name"]
        business_category = business_data[i]["business_category"]
        address1 = business_data[i]["address_line_1"]
        town_city = business_data[i]["address_line_2"]
        postcode = business_data[i]["postcode"]
        telephone_number = business_data[i]["telephone_number"]
        c.execute("INSERT INTO business(business_name, business_category, address1, town_city, postcode, telephone_number) VALUES (?, ?, ?, ?, ?, ?)", (business_name, business_category, address1, town_city, postcode, telephone_number))
        conn.commit()

def get_postcodes():
    c.execute("SELECT postcode FROM business")
    business_postcodes = c.fetchall()
    postcode_list = []
    for postcode in business_postcodes:
        postcode_list.append(postcode[0])
    c.execute("SELECT postcode FROM person")
    person_postcodes = c.fetchall()
    for postcode in person_postcodes:
        if postcode[0] not in postcode_list:
            postcode_list.append(postcode[0])
        else:
            pass
    return postcode_list
            
def remove_spaces():
    postcode_list = get_postcodes()
    spaceless_postcode_list = []
    for postcode in postcode_list:
        separated_postcode = postcode.split()
        spaceless_postcode_list.append(separated_postcode[0] + separated_postcode[1])
    return spaceless_postcode_list
        
def populate_location_table():
    postcode_list = remove_spaces()
    endpoint = "https://api.postcodes.io/postcodes/"
    for postcode in postcode_list:
        postcode_response = requests.get(endpoint + postcode)
        print
        data_postcode = postcode_response.json()
        print(data_postcode)
        if data_postcode["status"] == 200:
            x_coordinate = data_postcode["result"]["latitude"]
            y_coordinate = data_postcode["result"]["longitude"]
            postcodefromapi = data_postcode["result"]["postcode"]
            c.execute("INSERT INTO coordinate_mapping(postcode, x_coordinate, y_coordinate) VALUES (?, ?, ?)", (postcodefromapi, x_coordinate, y_coordinate))
            conn.commit()

def identifying_missing_postcodes():
    postcode_list = get_postcodes()
    c.execute("SELECT postcode FROM coordinate_mapping")
    location_pc_list = c.fetchall()
    new_list = []
    for postcode in location_pc_list:
        new_list.append(postcode[0])
    missing_pc_list = []
    for postcode in postcode_list:
        if postcode not in new_list:
            missing_pc_list.append(postcode)
        else:
            pass
    print(missing_pc_list)
            

        
