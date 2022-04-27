import json


class facility_details:

    def __init__(self):
        pass

    def validate_config_file(self):
        try:
            with open('config/config.json') as f:
                return json.load(f)
        except ValueError as e:
            return False

    def get_facility_details(self):
        site_data = self.validate_config_file()  # return JSON object as a dictionary

        if site_data:
            site_uuid = site_data["uuid"]
            app_id = site_data["app_id"]
            return {"uuid": site_uuid, "app_id": app_id}

        else:
            return False

    def save_facility_details(self,site_data):  # this function will be called whe we implement a POP UP MENU for Site
        # details to be entered on the web browser
        if site_data["apps"][0] == "Point of Care":
            app_id =1
        else: 
            app_id =2

        site_name = site_data["name"]
        uuid = site_data["uuid"]
        with open("config/config.json", "w") as data:
            information = {"uuid": uuid, "app_id": app_id, "site_name": site_name}
            data.write(json.dumps(information))
            data.close()

        return True
