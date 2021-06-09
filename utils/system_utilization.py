# Gets all information about Random Access Memory (RAM) and Disk Storage
from generate_qr_image import qr, add_qr_data


# RAM
def get_ram_details(ram):
    qr.add_data("MEMORY\n")
    add_qr_data('%-10s : %7s' % ("API ", ram >> 30) + 'GB\n')


# Gets all information about Hard Disk Drive storage
def get_disk_usage(disk_space):
    qr.add_data("DISK SPACE\n")
    add_qr_data('%-10s : %7s' % ("HDD space Available ", disk_space >> 30) + 'GB\n')  # sends data to QR image