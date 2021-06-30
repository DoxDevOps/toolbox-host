from os.path import exists, isdir, getsize
import glob
import os
import subprocess
import json
import platform
import netifaces
import psutil
import psutil._common



class auto_backup:
    _backup_directory = "/home/adm1n/backup"

    def __init__(self):
        pass

    def check_backups(self):
        if exists(self._backup_directory) and isdir(self._backup_directory):  # check if the folder exists
            list_of_files = glob.glob("{}/*.gz*".format(self._backup_directory))  # check for only zipped files
            latest_file = max(list_of_files, key=os.path.getctime)
            size = getsize(latest_file) >> 20  # convert the zipped backup file to MB.
            if size < 1:
                return False

            backup_dict = \
                {
                    "backup": True
                }
            json_object = json.dumps(backup_dict["backup"])

            return json_object
        else:
            return False


# this checks if a facility is running a POC or EMC System
class emr_systems:
    # Gets POC information

    _backup_dir = "/home/adm1n/backup"
    _emc_dir = "/var/www/emastercard-upgrade-automation"  # EMC installation directory
    _poc_api_dir = "/var/www/BHT-EMR-API"  # POC Api Folder
    _poc_core_dir = "/var/www/BHT-Core"  # POC Core Folder
    _poc_core_art_dir = "/var/www/BHT-Core/apps/ART"  # POC ART Folder'''

    def __init__(self):
        pass

    #
    def get_poc_versions(self):
        command = "git describe --tags"
        api_result = subprocess.Popen(command, shell=True, cwd='{}'.format(self._poc_api_dir), stdout=subprocess.PIPE)
        core_result = subprocess.Popen(command, shell=True, cwd='{}'.format(self._poc_core_dir), stdout=subprocess.PIPE)
        art_result = subprocess.Popen(command, shell=True, cwd='{}'.format(self._poc_core_art_dir),
                                      stdout=subprocess.PIPE)
        api_result = api_result.stdout.read().strip()
        core_result = core_result.stdout.read().strip()
        art_result = art_result.stdout.read().strip()

        poc_version_dict = \
            {
                "api": api_result,
                "core": core_result,
                "art": art_result
            }
        json_object = json.dumps(poc_version_dict)
        return json_object

    # Get EMC information
    def get_emc_versions(self):
        command = "git describe --tags"
        emc_result = subprocess.Popen(command, shell=True, cwd='{}'.format(self._emc_dir), stdout=subprocess.PIPE)
        emc_result = emc_result.stdout.read().strip()

        emc_version_dict = \
            {
                "emc": emc_result
            }
        json_object = json.dumps(emc_version_dict)
        return json_object

    # Check for Installed Systems
    def check_systems(self):
        print("the method has been called")

        if exists(self._emc_dir):  # check if emc folder exist
            return self.get_emc_versions()
        elif exists(self._poc_api_dir):  # check if poc api, core, art folder exist
            if exists(self._poc_core_art_dir):
                if exists(self._poc_core_dir):
                    return self.get_poc_versions()

        else:
            return False


'''
This Function gets facility code / site code from a json installed in /config folder
'''


class facility_details:

    def __init__(self):
        pass

    def get_facility_details(self):
        site_info = open('config/config.json', )  # Read the Json File
        site_data = json.load(site_info)  # return JSON object as a dictionary

        site_name = site_data["name"].lstrip()
        site_code = site_data["code"].lstrip()
        site_zone = site_data["zone"].lstrip()
        site_district = site_data["district"].lstrip()

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


'''This functionality has been disabled for now 
class platform:

    # check for Platform Information
    def platform_info(self):
        osname = platform.system()
        version = platform.release()
        osname = osname.split('\n')
        version = version.split('\n')
        for x in version:
            version_str = x.strip()
        for y in osname:
            osname_str = y.strip()
        encrypt.encrypt_data("OS release", version_str)
        encrypt.encrypt_data("OS", osname_str)'''


class running_processes:
    # check for mysql, docker service etc
    def check_service(self):
        services = ["docker", "mysql", "nginx"]
        for service in services:
            p = subprocess.Popen(["systemctl", "is-active", service], stdout=subprocess.PIPE)
            (output, err) = p.communicate()
            output = output.decode('utf-8')

            running_services_dict = \
                {
                    "running_services": output
                }
            json_object = json.dumps(running_services_dict["running_services"])

            return json_object



class site_ip_address:

    def get_site_ip_address(self):
        iface = netifaces.gateways()['default'][netifaces.AF_INET][1]
        site_ip_address = netifaces.ifaddresses(iface)[netifaces.AF_INET][0]['addr']

        ip_dict = \
            {
                "ip": site_ip_address
            }
        json_object = json.dumps(ip_dict["ip"])
        return json_object


# get RAM and DISK SPACE.
class system_utilization:
    # Gets all information about Random Access Memory (RAM) and Disk Storage
    ram = psutil.virtual_memory().available
    disk_space = psutil.disk_usage('/').percent

    def __init__(self):
        pass

    # RAM
    def get_ram_details(self):
        ram_dict = \
            {
                "ram": self.ram >> 30
            }
        json_object = json.dumps(ram_dict["ram"])

        return json_object

    # HDD
    def get_hdd_details(self):
        hdd_dict = \
            {
                "hdd": self.disk_space
            }
        json_object = json.dumps(hdd_dict["hdd"])

        return json_object
