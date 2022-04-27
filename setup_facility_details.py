#! /usr/bin/python
import json
import os
import urllib2


from utils.check_config import facility_details
import re
import uuid


def get_facility_name():
    facility_name = raw_input("Enter Facility Name Please : ")
    search_facilities(facility_name)


def search_facilities(facility_name):
    settings = load_settings("config/.json")
    url = settings["endpoint"]
    token = settings["token"]
    json_dict = {'site_name': facility_name}

    # convert json_dict to JSON
    json_data = json.dumps(json_dict)

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
        get_facility_name()


def display_facilities(facilities):
    facilities = json.loads(facilities)
    counter = 0
    for facility in facilities:
        counter += 1
        print(str(counter) + " " + facility['fields']['name'])
    select_facility(facilities, counter)


def select_facility(facilities, counter):
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
    :param facilities:
    :param facility_number: number se
    :return:
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
    mac_address = ':'.join(re.findall('..', '%012x' % uuid.getnode()))  # type: Union[Union[str, unicode], Any]
    return mac_address


def send_mac_address():
    return True


def load_settings(location):
    # type: () -> object
    """
    a function that loads settings (token and endpoint)
    :type location: string
    :return: json object
    """
    with open(location) as f:
        settings = json.load(f)  # type: object
    return settings
