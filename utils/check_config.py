from flask import json


class facility_details:

    def __init__(self):
        pass

    def validate_config_file(self):
        try:
            with open('config/config.json') as f:
                return json.load(f)
        except ValueError as e:
            return False
        return False

    def get_facility_details(self):
        site_data = self.validate_config_file()  # return JSON object as a dictionary
        if site_data:
            site_uuid = site_data["uuid"]
            app_id = site_data["app_id"]

            return {"uuid": site_uuid, "app_id": app_id}

        else:
            return False

    def save_facility_details(
            self):  # this function will be called whe we implement a POP UP MENU for Site details to be entered on the web browser
        print("save the details")
