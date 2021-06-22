import json

from utils.encrypt import encrypt_data


def get_facility_details():
    site_info = open('config/config.json', )  # Read the Json File
    site_data = json.load(site_info)  # return JSON object as a dictionary

    site_name = site_data["name"].lstrip()
    site_code = site_data["code"].lstrip()
    site_zone = site_data["zone"].lstrip()
    site_district = site_data["district"].lstrip()



    if len(site_name) > 0 and len(site_code) > 0 and len(site_zone) > 0 and len(site_district) > 0:
        print ("Need More Details")
        encrypt_data("name ", site_name)
        encrypt_data("code ", site_code)
        encrypt_data("zone", site_zone)
        encrypt_data("district", site_district)

        return 1

    else:
        return 0

    site_info.close()


def save_facility_details():
    print("save the details")
