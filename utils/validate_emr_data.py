# coding=utf-8
import json

from utils.utilities import write_file


def validate_config_file(location):
    """
    validates if data is in the correct format
    :return: Return False when the file is not correct
    """
    try:
        with open(location) as f:
            return json.load(f)
    except ValueError as e:
        return False


def save_facility_details(site_data):  # this function will be called whe we implement a POP UP MENU for Site
    """
    gets facility details as dictionary and saves the file as a json file
    :param site_data:
    :return:
    """
    # details to be entered on the web browser
    if site_data["apps"][0] == "Point of Care":
        app_id = 1
        information = {"core": "/var/www/BHT-Core", "art": "/var/www/BHT-Core/apps/ART", "api": "/var/www/BHT-EMR-API"}
        write_file("config/apps.json", information)
    else:
        app_id = 2
        information_emc = {"emc": "/var/www/emastercard-upgrade-automation"}
        write_file("config/apps.json", information_emc)

    site_name = site_data["name"]
    uuid = site_data["uuid"]
    information = {"uuid": uuid, "app_id": app_id, "site_name": site_name}
    write_file("config/config.json", information)
    return True
