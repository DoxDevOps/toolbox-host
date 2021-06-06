import socket
from sys import stdout

import flask
import os
import psutil
import qrcode
import subprocess
from psutil._common import bytes2human
import psutil._common
from flask import Flask, render_template

#from fabric import *
from os.path import exists
from invoke import run

app = Flask(__name__, static_folder="templates/static")

#app = Flask(__name__)

_emc_dir = "/var/www/emastercard-upgrade-automation"
_poc_api_dir = "/var/www/BHT-EMR-API"
_poc_core_dir = "/var/www/BHT-Core"
_poc_core_art_dir = "/var/www/BHT-Core/apps/ART"
_con = socket.gethostbyname(socket.gethostname())
#_con = flask.request.remote_addr
# **************sample data will be taken from the following functions*********************


# Create QR Code Instance. It determines the size of the QR code
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)


# Gets all information about Random Access Memory (RAM)

def get_ram_details(ram):
    qr.add_data("MEMORY\n")
    for name in ram._fields:
        value = getattr(ram, name)
        if name != 'percent':
            value = bytes2human(value)
        add_qr_data('%-10s : %7s' % (name.capitalize(), value) + '\n')  # add to QR image


# Gets all information about Hard Disk Drive storage
def get_disk_usage(disk_space):
    qr.add_data("DISK SPACE\n")
    for name in disk_space._fields:
        value = getattr(disk_space, name)
        if name != 'percent':
            value = bytes2human(value)
        add_qr_data('%-10s : %7s' % (name.capitalize(), value) + '\n')  # add to QR image


# Gets POC information
def get_poc_versions():
    qr.add_data("\n POC VERSION \n")
    api_result = subprocess.run('cd ', _poc_api_dir | 'git describe --tags')
    core_result = subprocess.run('cd ', _poc_core_dir | 'git describe --taps')
    art_result = run('cd', _poc_core_art_dir | 'git describe --tags')

    add_qr_data('%-10s : %7s' % ("API ", api_result) + '\n')
    add_qr_data('%-10s : %7s' % ("CORE ", core_result) + '\n')
    add_qr_data('%-10s : %7s' % ("ART", art_result) + '\n')

# Get EMC information
def get_emc_versions():
    qr.add_data("\n EMC CURRENT VERSION \n")
    command = "git describe --tags"
    emc_result = subprocess.Popen(command, shell=True, cwd='{}'.format(_emc_dir))
    #print (emc_result)
    add_qr_data('%-10s : %7s' % ("EMC ", emc_result) + '\n')


# Check for Installed Systems
def check_systems():
    if exists(_emc_dir):
        get_emc_versions()
    elif exists(_poc_api_dir, _poc_core_art_dir, _poc_core_dir):
        get_poc_versions()


def add_qr_data(input_data):
    qr.add_data(input_data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save('templates/static/images/toolbox.png')


#@app.route('/')
def index():
    # qr.add_data("Hello, world!")
    # qr.make(fit=True)
    # img = qr.make_image(fill='black', back_color='red')
    return render_template('index.html')


#def get_image():
    #image_name = 'templates/static/images/toolbox.png'
    #Simage_name.Seek(0)


@app.route('/')
def main():
    get_ram_details(psutil.virtual_memory())
    get_disk_usage(psutil.disk_usage('/'))
    check_systems()

    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    # main()
