from os.path import exists, isdir, getsize
import glob
import os

from utils.generate_qr_image import add_qr_data

_backup_directory = "/home/adm1n/backup"


def check_backups():
    if exists(_backup_directory):  # check if the folder exists
        print("the folder exists !!")
        if isdir(_backup_directory):  # check if there is any content in the folder
            print("the Folder is not empty")
            list_of_files = glob.glob("{}/*.gz*".format(_backup_directory))  # check for only zipped files
            latest_file = max(list_of_files, key=os.path.getctime)
            size = getsize(latest_file) >> 20
            add_qr_data('%-10s : %7s' % ("filename", latest_file) + ';')
            add_qr_data('%-10s : %7s' % ("fileSize", size >> 30) + 'GB;')
        else:
            print("Backup not installed")
    else:
        print("no backup script installed")
