from flask import json


class facility_details:

    def __init__(self):
        pass

    def get_facility_details(self):
        site_info = open('config/config.json', )  # Read the Json File
        site_data = json.load(site_info)  # return JSON object as a dictionary

        site_uuid = site_data["uuid"]
        app_id = site_data["app_id"]

        if site_uuid and app_id:
            # Save the site code in a dictionary and convert it to json format
            site_code_dict = {"uuid": site_uuid}
            json_object = json.dumps(site_code_dict)
            json_object = json.loads(json_object)
            site_info.close()
            return {"uuid":site_uuid,"app_id": app_id}

        else:
            return False

    def save_facility_details(
            self):  # this function will be called whe we implement a POP UP MENU for Site details to be entered on the web browser
        print("save the details")
