import netifaces

from utils.generate_qr_image import add_qr_data


def get_site_ip_address():
    iface = netifaces.gateways()['default'][netifaces.AF_INET][1]
    site_ip_address = netifaces.ifaddresses(iface)[netifaces.AF_INET][0]['addr']
    add_qr_data('%-10s : %7s' % ("EMC ", site_ip_address) + ';')
