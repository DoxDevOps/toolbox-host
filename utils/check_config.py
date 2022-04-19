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

    def get_facility_details(self):
        site_data = self.validate_config_file()  # return JSON object as a dictionary

        if site_data:
            site_uuid = site_data["uuid"]
            app_id = site_data["app_id"]
            return {"uuid": site_uuid, "app_id": app_id}

        else:
            return False

    def save_facility_details(self, uuid):  # this function will be called whe we implement a POP UP MENU for Site
        # details to be entered on the web browser
        with open('config/.sites.json') as f:
            all_sites = json.load(f)
            for x in all_sites:
                getit = json.dumps(x["uuid"])
                if getit == uuid:
                    app_id = x["apps"]
                    site_name = x["name"]

                    with open("config/config.json", "w") as data:
                        information = {"uuid": json.loads(uuid), "app_id": int(app_id), "site_name": site_name}
                        data.write(json.dumps(information))
                        data.close()
            f.close()
            return True
