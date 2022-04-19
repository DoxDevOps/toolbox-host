import subprocess
import os
from os.path import exists, isdir, getsize
from flask import json
import glob
import netifaces
import getpass


class emr_systems:
    def __init__(self):
        pass

    # Gets POC information
    command = "whoami"
    user = getpass.getuser()
    backup_dir = "/home/"+user+"/backup"
    emc_dir = "/var/www/emastercard-upgrade-automation"  # EMC installation directory
    emc_dir2 = "/emastercard-upgrade-automation"  # some sites have EMC in the Home directory.
    """TO DO :
    # POC -html: 1. check all possible directory 
    #"""
    poc_api_dir = "/var/www/BHT-EMR-API"  # POC Api Folder
    poc_core_dir = "/var/www/BHT-Core"  # POC Core Folder
    poc_core_art_dir = "/var/www/BHT-Core/apps/ART"  # POC ART Folder'''

    def check_backups(self):
        """Check for Back up"""
        if exists(self.backup_dir) and isdir(self.backup_dir):  # check if the folder exists
            list_of_files = glob.glob("{}/*.gz*".format(self.backup_dir))  # check for only zipped files
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

        return False

    def get_poc_versions(self):
        command = "git describe --tags"
        api_result = subprocess.Popen(command, shell=True, cwd='{}'.format(self.poc_api_dir), stdout=subprocess.PIPE)
        core_result = subprocess.Popen(command, shell=True, cwd='{}'.format(self.poc_core_dir), stdout=subprocess.PIPE)
        art_result = subprocess.Popen(command, shell=True, cwd='{}'.format(self.poc_core_art_dir),
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
        json_object = json.loads(json_object)
        return json_object

    # Get EMC information

    def get_emc_versions(self):
        command = "git describe --tags"
        emc_result = subprocess.Popen(command, shell=True, cwd='{}'.format(self.emc_dir), stdout=subprocess.PIPE)
        emc_result = emc_result.stdout.read().strip()

        emc_version_dict = \
            {
                "emc": emc_result
            }
        json_object = json.dumps(emc_version_dict)
        json_object = json.loads(json_object)
        return json_object

    # Check for Installed Systems

    def check_systems(self):
        """Checks if a site has POC or EMC installed"""
        if exists(self.emc_dir or self.emc_dir2):  # check if emc folder exist
            return self.get_emc_versions()
        elif exists(self.poc_api_dir):  # check if poc api, core, art folder exist
            if exists(self.poc_core_art_dir):
                if exists(self.poc_core_dir):
                    return self.get_poc_versions()
        else:
            return False


    def get_site_ip_address(self):
        iface = netifaces.gateways()['default'][netifaces.AF_INET][1]
        site_ip_address = netifaces.ifaddresses(iface)[netifaces.AF_INET][0]['addr']
        ip_dict = \
            {
                "ip": site_ip_address
            }
        json_object = json.dumps(ip_dict["ip"])
        return json_object
