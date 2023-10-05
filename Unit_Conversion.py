#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def miles_to_km(miles):
    kilometers = miles * 1.60934
    return(kilometers)

def km_to_miles(kilometer):
    miles = kilometer * 0.621371
    return(miles)

def kilo_to_pound(kilograms):
    pound = kilograms * 2.20462262185
    return(pound)

def pound_to_kilo(pound):
    kilogram = pound * 2.20462262185
    return(kilogram)

def fahren_to_cel(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return(celsius)

def cel_to_fahren(celsius):
    fahrenheit =(celsius * 9/5) + 32
    return(fahrenheit)

