# Gets POC information
from utils.generate_qr_image import add_qr_data
import subprocess
from os.path import exists

from utils.running_processes import check_service

_emc_dir = "/var/www/emastercard-upgrade-automation"  # EMC installation directory
_poc_api_dir = "/var/www/BHT-EMR-API"  # POC Api Folder
_poc_core_dir = "/var/www/BHT-Core"  # POC Core Folder
_poc_core_art_dir = "/var/www/BHT-Core/apps/ART"  # POC ART Folder


def get_poc_versions():
    command = "git describe --tags"
    api_result = subprocess.Popen(command, shell=True, cwd='{}'.format(_poc_api_dir), stdout=subprocess.PIPE)
    core_result = subprocess.Popen(command, shell=True, cwd='{}'.format(_poc_core_dir), stdout=subprocess.PIPE)
    art_result = subprocess.Popen(command, shell=True, cwd='{}'.format(_poc_core_art_dir), stdout=subprocess.PIPE)
    api_result = api_result.stdout.read()
    core_result = core_result.stdout.read()
    art_result = art_result.stdout.read()
    add_qr_data('%-10s : %7s' % ("API ", api_result) + ';')
    add_qr_data('%-10s : %7s' % ("CORE ", core_result) + ';')
    add_qr_data('%-10s : %7s' % ("ART", art_result) + ';')


# Get EMC information
def get_emc_versions():
    command = "git describe --tags"
    emc_result = subprocess.Popen(command, shell=True, cwd='{}'.format(_emc_dir), stdout=subprocess.PIPE)
    emc_result = emc_result.stdout.read()
    add_qr_data('%-10s : %7s' % ("EMC ", emc_result) + ';')
    # Then check if the required services are running : nginx, docker, msql
    check_service()  # checks if services are active


# Check for Installed Systems
def check_systems():
    if exists(_emc_dir):
        get_emc_versions()
    if exists(_poc_api_dir):
        if exists(_poc_core_art_dir):
            if exists(_poc_core_dir):
                get_poc_versions()
            else:
                print("NOT POC SITE")
    else:
        print("EBRS, ETC SITES")
