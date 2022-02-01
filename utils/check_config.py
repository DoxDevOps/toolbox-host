from flask import json


class facility_details:

    def __init__(self):
        pass

    def get_facility_details(self):
        site_info = open('config/config.json', )  # Read the Json File
        site_data = json.load(site_info)  # return JSON object as a dictionary

        site_name = site_data["name"].strip()
        site_code = site_data["code"].strip()
        site_zone = site_data["zone"].strip()
        site_district = site_data["district"].strip()
        site_ip_address = site_data["site_ip_address"].strip()

        if len(site_name) < 1 and len(site_code) < 1 and len(site_zone) < 1 and len(site_district) < 1:

            return False

        else:

            # Save the site code in a dictionary and convert it to json format

            site_code_dict = \
                {
                    "site_code": site_code
                }
            json_object = json.dumps(site_code_dict["site_code"])

            return json_object

        site_info.close()

    def save_facility_details(
            self):  # this function will be called whe we implement a POP UP MENU for Site details to be entered on the web browser
        print("save the details")
