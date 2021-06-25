from os.path import exists, isdir, getsize
import glob
import os
import subprocess
import json
import platform
import netifaces
from utils.encrypt_make_qr_image import encrypt


class auto_backup:

    def _init_(self, _backup_directory):
        self._backup_directory = "/home/adm1n/backup"

    def check_backups(self):
        if exists(self._backup_directory):  # check if the folder exists
            print("the folder exists !!")
            if isdir(self._backup_directory):  # check if there is any content in the folder
                print("the Folder is not empty")
                list_of_files = glob.glob("{}/*.gz*".format(self._backup_directory))  # check for only zipped files
                latest_file = max(list_of_files, key=os.path.getctime)
                size = getsize(latest_file) >> 20
                encrypt.encrypt_data("filename", latest_file)
                encrypt.encrypt_data("fileSize", size >> 30)

            else:
                print("Backup not installed")
        else:
            print("no backup script installed")


class emr_systems:
    # Gets POC information
    def _init_(self):
        self._emc_dir = "/home/adm1n/backup"
        self._emc_dir = "/var/www/emastercard-upgrade-automation"  # EMC installation directory
        self._poc_api_dir = "/var/www/BHT-EMR-API"  # POC Api Folder
        self._poc_core_dir = "/var/www/BHT-Core"  # POC Core Folder
        self._poc_core_art_dir = "/var/www/BHT-Core/apps/ART"  # POC ART Folder

    #
    def get_poc_versions(self):
        command = "git describe --tags"
        api_result = subprocess.Popen(command, shell=True, cwd='{}'.format(self._poc_api_dir), stdout=subprocess.PIPE)
        core_result = subprocess.Popen(command, shell=True, cwd='{}'.format(self._poc_core_dir), stdout=subprocess.PIPE)
        art_result = subprocess.Popen(command, shell=True, cwd='{}'.format(self._poc_core_art_dir),
                                      stdout=subprocess.PIPE)
        api_result = api_result.stdout.read()
        core_result = core_result.stdout.read()
        art_result = art_result.stdout.read()
        encrypt.encrypt_data("api", api_result)
        encrypt.encrypt_data("core", core_result)
        encrypt.encrypt_data("art", art_result)

    # Get EMC information
    def get_emc_versions(self):
        command = "git describe --tags"
        emc_result = subprocess.Popen(command, shell=True, cwd='{}'.format(self._emc_dir), stdout=subprocess.PIPE)
        emc_result = emc_result.stdout.read()
        encrypt.encrypt_data("emc", emc_result)
        # Then check if the required services are running : nginx, docker, msql
        running_processes.check_service()  # checks if services are active

    # Check for Installed Systems
    def check_systems(self):
        if exists(self._emc_dir):
            self.get_emc_versions()
        if exists(self._poc_api_dir):
            if exists(self._poc_core_art_dir):
                if exists(self._poc_core_dir):
                    self.get_poc_versions()
                else:
                    print("NOT POC SITE")
        else:
            print("EBRS, ETC SITES")


class facility_details:

    def get_facility_details(self):
        site_info = open('config/config.json', )  # Read the Json File
        site_data = json.load(site_info)  # return JSON object as a dictionary

        site_name = site_data["name"].lstrip()
        site_code = site_data["code"].lstrip()
        site_zone = site_data["zone"].lstrip()
        site_district = site_data["district"].lstrip()

        if len(site_name) > 0 and len(site_code) > 0 and len(site_zone) > 0 and len(site_district) > 0:
            print ("Need More Details")
            encrypt.encrypt_data("name ", site_name)
            encrypt.encrypt_data("code ", site_code)
            encrypt.encrypt_data("zone", site_zone)
            encrypt.encrypt_data("district", site_district)

            return 1

        else:
            return 0

        site_info.close()

    def save_facility_details(self):
        print("save the details")


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
        encrypt.encrypt_data("OS", osname_str)


class running_processes:
    # check for mysql, docker service etc
    def check_service(self):
        services = ["docker", "mysql", "nginx"]
        for service in services:
            p = subprocess.Popen(["systemctl", "is-active", service], stdout=subprocess.PIPE)
            (output, err) = p.communicate()
            output = output.decode('utf-8')
            encrypt.encrypt_data(service, output)


class site_ip_address:

    def get_site_ip_address(self):
        iface = netifaces.gateways()['default'][netifaces.AF_INET][1]
        site_ip_address = netifaces.ifaddresses(iface)[netifaces.AF_INET][0]['addr']
        encrypt.encrypt_data("EMC ", site_ip_address)

#get RAM and DISK SPACE.
class system_utilization:
    # Gets all information about Random Access Memory (RAM) and Disk Storage
    def _init_(self, ram, disk_space):
        self.ram = ram
        self.disk_space = disk_space

    # RAM
    def get_ram_hdd_details(self):
        encrypt.encrypt_data('%-10s : %7s' % ("API ", self.ram >> 30) + 'GB\n')
        encrypt.encrypt_data("HDD space Available ", self.disk_space >> 30)  #  Gets all information about Hard Disk Drive storage
