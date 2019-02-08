# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 14:49:03 2019

@author: gracy
"""

from flask import Flask, render_template, request
from test_app_funcs import *
app=Flask("MyApp")

@app.route("/")
def homepage():
      return render_template("index.html")

###PERSON###
@app.route("/person")
def person():      
      return render_template("person.html")

@app.route("/person_results", methods=["POST"])
def person_results():
      form_data=request.form
      name=form_data["name"]
      postcode=form_data["postcode"]
      
      result= person_search_results(name,postcode) 
     
      return render_template ("person_results.html", title="results_page", **locals())


###BUSINESS###
      
@app.route("/business")
def business():      
      return render_template("business.html")

@app.route("/business_results", methods=["POST"])
def business_results():
      form_data=request.form
      postcode=form_data["postcode"]
      if postcode == '':
            result = 'please enter a postcode'
      else: 
            if "name" in form_data:
                  if form_data["name"]=='':
                        result = 'please enter a search term'
                  else: 
                        name=form_data["name"]
                        result = compare_distance(postcode, name, "name")
                     
            else:
                  if form_data["type"]=='':
                        result = 'please enter a search term'
                  else: 
                        business_type=form_data["type"]
                        result = compare_distance(postcode, business_type, "type")
                  
      return render_template ("business_results.html", title="results_page", **locals())

app.run(debug=True)