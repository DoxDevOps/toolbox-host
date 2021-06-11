# check for mysql service
import subprocess

from utils.generate_qr_image import add_qr_data


def check_service():
    services = ["docker", "mysql", "nginx"]
    for service in services:
        p = subprocess.Popen(["systemctl", "is-active", service], stdout=subprocess.PIPE)
        (output, err) = p.communicate()
        output = output.decode('utf-8')
        print(service + " :{}".format(output))
        add_qr_data('%-10s : %7s' % (service, output) + ';')
