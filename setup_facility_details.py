#!/bin/bash
import json
import urllib2
import re
import uuid
from utils.check_config import facility_details


def get_facility_name():
    """
    starting point. prompts user to enter a suggested facility name
    :return: Boolean (just a checker )
    """
    facility_name = raw_input("Enter Facility Name Please : ")
    search_facilities(facility_name)
    return True


def search_facilities(facility_name):
    """
    get suggested name and search in a remote server
    :param facility_name: string
    :return: boolean (just a checker)
    """
    settings = load_settings("config/.json")
    url = settings["endpoint"]
    token = settings["token"]
    json_dict = {'site_name': facility_name}

    # convert json_dict to JSON
    json_data = json.dumps(json_dict)

    # Creating a Post request
    req = urllib2.Request(url, json_data)
    req.get_method = lambda: 'GET'
    req.add_header('Content-type', 'application/json')
    req.add_header('Accept', 'text/plain')
    req.add_header('Authorization', token)
    r = urllib2.urlopen(req)
    results = r.read()
    if len(results) != 2:
        display_facilities(results)
    else:
        print("\n No match Found, Please try again :")
        get_facility_name() # start all over
    return True


def display_facilities(facilities):
    """
    displays all possible sites
    :param facilities: json object
    :return:
    """
    facilities = json.loads(facilities)
    counter = 0
    for facility in facilities:
        counter += 1
        print(str(counter) + " " + facility['fields']['name'])
    select_facility(facilities, counter)
    return True


def select_facility(facilities, counter):
    """
    gives a user an option to select sites from a given list
    :type counter: int
    :type facilities: json object
    :param facilities: json object
    :param counter: a counter on the number of sites retrieved
    """
    while True:
        try:
            facility_number = int(raw_input("\nConfirm Facility Name by Entering a Number : ")) - 1

            if facility_number + 1 > counter:
                print("The number selected is not on the list, Please try again.")
                continue
            if facility_number < 0:
                print("Please Select a POSITIVE number")
                continue
            save_facility(facilities, facility_number)
        except ValueError:
            print("\nPlease enter a valid number")
            continue
        else:
            break


def save_facility(facilities, facility_number):
    """
    saves facility details after configuration
    :type facilities: json object
    :type facility_number: int
    :param facilities:
    :param facility_number: number se
    :return: Boolean
    """
    selected_facility = facilities[facility_number]['fields']['name']
    site_data = {"apps": facilities[facility_number]['fields']['apps'], "name": selected_facility,
                 "uuid": facilities[facility_number]['fields']['uuid']}
    print("Selected District : " + selected_facility)
    facility_details().save_facility_details(site_data)  # then save the details in config file
    return True


def mac_address():
    """
    gets machine MAC address
    :return:
        mac_address : mac address of a machine
    """
    # convert to hex and separate two figures with :
    mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
    return mac


def send_mac_address():
    return True


def load_settings(location):
    """
    a function that loads settings (token and endpoint)
    :type location: string
    :return: json object
    """
    with open(location) as f:
        settings = json.load(f)
    return settings
