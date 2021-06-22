from os.path import exists, isdir, getsize
import glob
import os

from utils.encrypt import encrypt_data

_backup_directory = "/home/adm1n/backup"


def check_backups():
    if exists(_backup_directory):  # check if the folder exists
        print("the folder exists !!")
        if isdir(_backup_directory):  # check if there is any content in the folder
            print("the Folder is not empty")
            list_of_files = glob.glob("{}/*.gz*".format(_backup_directory))  # check for only zipped files
            latest_file = max(list_of_files, key=os.path.getctime)
            size = getsize(latest_file) >> 20
            encrypt_data("filename", latest_file)
            encrypt_data("fileSize", size >> 30)
        else:
            print("Backup not installed")
    else:
        print("no backup script installed")
