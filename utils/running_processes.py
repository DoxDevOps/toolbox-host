# check for mysql service
import subprocess

from utils.encrypt import encrypt_data


def check_service():
    services = ["docker", "mysql", "nginx"]
    for service in services:
        p = subprocess.Popen(["systemctl", "is-active", service], stdout=subprocess.PIPE)
        (output, err) = p.communicate()
        output = output.decode('utf-8')
        encrypt_data(service, output)
