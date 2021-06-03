import flask
import psutil as psutil
import qrcode
import psutil
from psutil._common import bytes2human
import psutil._common
from flask import Flask, render_template

#from fabric import *
from os.path import exists

from invoke import run

app = Flask(__name__, static_folder="templates/static")

_emc_dir = "/var/www/emastercard-upgrade-automation"
_poc_api_dir = "/var/www/BHT-EMR-API"
_poc_core_dir = "/var/www/BHT-Core"
_poc_core_art_dir = "/var/www/BHT-Core/apps/ART"


#**************sample data will be taken from the following functions*********************


#Create QR Code Instance. It determines the size of the QR code
qr = qrcode.QRCode(version=1, box_size=10, border=5)


#Gets all information about Random Access Memory (RAM)
def get_ram_details(ram):
    qr.add_data("MEMORY\n")
    for name in ram._fields:
        value = getattr(ram, name)
        if name != 'percent':
            value = bytes2human(value)
        add_qr_data('%-10s : %7s' % (name.capitalize(), value)+'\n') #add to QR image

#Gets all information about Hard Disk Drive storage
def get_disk_usage(disk_space):
    qr.add_data("DISK SPACE\n")
    for name in disk_space._fields:
        value = getattr(disk_space, name)
        if name != 'percent':
            value = bytes2human(value)
        add_qr_data('%-10s : %7s' % (name.capitalize(), value)+'\n') #add to QR image

#Gets POC information
def get_poc_versions(core, art, api):
    qr.add_data("\n POC VERSION \n")
    api_result = run('cd ', _poc_api_dir | 'git describe --tags')
    core_result = run('cd ', _poc_core_dir | 'git describe --taps')
    art_result = run('cd', _poc_core_art_dir | 'git describe --tags')

    add_qr_data('%-10s : %7s' % ("API ", api_result)+'\n')
    add_qr_data('%-10s : %7s' % ("CORE ", core_result)+'\n')
    add_qr_data('%-10s : %7s' % ("ART", art_result)+'\n')

#Get EMC information
def get_emc_versions(emc):
    qr.add_data("\n EMC CURRENT VERSION \n")
    emc_result = run('cd ',_emc_dir | 'git describe --tags')
    add_qr_data('%-10s : %7s' % ("EMC ", emc_result) + '\n')


#Check for Installed Systems
def check_systems ():
    if exists(_emc_dir):
        #got to EMC unction
    elif exists(_poc_api_dir, _poc_core_art_dir, _poc_core_dir):
        get_poc_versions(_poc_core_dir, _poc_core_art_dir, _poc_api_dir)







def add_qr_data(input_data):
    qr.add_data(input_data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save('qrcode001.png')



@app.route('/')
def index():
    qr.add_data("Hello, world!")
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    return render_template('index.html')

@app.route('/get-qr-Image')
def get_image():
    image_name = 'qrcode001.png'
    #Simage_name.Seek(0)
    return flask.send_file(image_name, mimetype='png')


def main():
    get_ram_details(psutil.virtual_memory().available)
    get_disk_usage(psutil.disk_usage('/'))
    check_systems()
    get_image()



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    #main()

