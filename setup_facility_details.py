#! /usr/bin/python
# import os
from distutils.log import error
import json
import urllib2
import netifaces as nif
from utils.check_config import facility_details

def get_facility_name():
    facility_name =raw_input("\n\n Enter Facility Name = ")
    search_facilities(facility_name)

def search_facilities(facility_name):
    url = 'https://toolbox.hismalawi.org/ext-api/site/get/details'

    token = 'yyJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE2MzY0MjQ0NjR9.iRlIMoZgYUQxZMq-CZiLusUfPyofkLCA8djNbOaJYT0'
    json_dict = {'site_name' : facility_name}

    # convert json_dict to JSON
    json_data = json.dumps(json_dict)

    req = urllib2.Request(url,json_data)
    req.get_method = lambda: 'GET'
    req.add_header('Content-type', 'application/json')
    req.add_header('Accept', 'text/plain')
    req.add_header('Authorization', token)
    r = urllib2.urlopen(req)
    results = r.read()
    if len(results) != 2:
        display_facilities(results)
    else:
        print("\n No match Found")
        get_facility_name()
    

def display_facilities(facilities):
    facilities = json.loads(facilities)
    counter = 0
    for facilitie in facilities:
        counter +=1
        print(str(counter) +" "+ facilitie['fields']['name'])
    select_facility(facilities,counter)

def select_facility(facilities,counter):
    while True:
        try:
            facility_number =int(raw_input("\n\nConfirm Facility Name by Entering a number = ")) - 1
            if facility_number+1 > counter:
                print("\n No district found with that number")
                select_facility(facilities,counter)
            save_facility(facilities,facility_number)
        except ValueError: 
            print("\nPlease enter a valid number") 
            continue
        else:
            break
   
def save_facility(facilities,facility_number):
    selected_facility =facilities[facility_number]['fields']['name']
    site_data = {}
    site_data["apps"] = facilities[facility_number]['fields']['apps']
    site_data["name"] = selected_facility
    site_data["uuid"] = facilities[facility_number]['fields']['uuid']
    print("\nSelected District : "+ selected_facility)
    
    print("Mac address : "+mac_for_ip())
    facility_details().save_facility_details(site_data)

def mac_for_ip():
    'Returns a list of MACs for interfaces that have given IP, returns None if not found'
    iface = nif.gateways()['default'][nif.AF_INET][1]
    ip = nif.ifaddresses(iface)[nif.AF_INET][0]['addr']
    for i in nif.interfaces():
        addrs = nif.ifaddresses(i)
        try:
            if_mac = addrs[nif.AF_LINK][0]['addr']
            if_ip = addrs[nif.AF_INET][0]['addr']
        except IndexError: #ignore ifaces that dont have MAC or IP
            if_mac = if_ip = None
        if if_ip == ip:
            return if_mac
    return None

get_facility_name()