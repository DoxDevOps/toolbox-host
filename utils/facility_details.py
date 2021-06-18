import json
from utils.generate_qr_image import add_qr_data


def get_facility_details():
    site_info = open('config/config.json', )  # Read the Json File
    site_data = json.load(site_info)  # return JSON object as a dictionary

    site_name = site_data["facility_name"]
    site_code = site_data["facility_code"]
    site_zone = site_data["facility_zone"]
    site_district = site_data["facility_district"]

    if len(site_name) > 0 and len(site_code) > 0 and len(site_zone) > 0 and len(site_district) > 0:
        print ("Need More Details")
        add_qr_data('%-10s : %7s' % ("facility_name ", site_name) + ';')
        add_qr_data('%-10s : %7s' % ("facility_code ", site_code) + ';')
        add_qr_data('%-10s : %7s' % ("facility_zone", site_zone) + ';')
        add_qr_data('%-10s : %7s' % ("facility_district", site_district) + ';')

        return 1

    else:
        return 0

    site_info.close()


def save_facility_details():
    print("save the details")
