import netifaces

from utils.encrypt import encrypt_data


def get_site_ip_address():
    iface = netifaces.gateways()['default'][netifaces.AF_INET][1]
    site_ip_address = netifaces.ifaddresses(iface)[netifaces.AF_INET][0]['addr']
    encrypt_data("EMC ", site_ip_address)
