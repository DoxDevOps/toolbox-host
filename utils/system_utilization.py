# Gets all information about Random Access Memory (RAM) and Disk Storage
from generate_qr_image import add_qr_data

# RAM
from utils.encrypt import encrypt_data


def get_ram_details(ram):
    add_qr_data('%-10s : %7s' % ("API ", ram >> 30) + 'GB\n')


# Gets all information about Hard Disk Drive storage
def get_disk_usage(disk_space):
    encrypt_data("HDD space Available ", disk_space >> 30)  # sends data to QR image
