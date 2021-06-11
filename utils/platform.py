import platform
from utils.generate_qr_image import add_qr_data


# check for Platform Information
def platform_info():
    osname = platform.system()
    version = platform.release()
    osname = osname.split('\n')
    version = version.split('\n')
    for x in version:
        version_str = x.strip()
    for y in osname:
        osname_str = y.strip()
    add_qr_data('%-10s : %7s' % ("OS release", version_str) + ';')
    add_qr_data('%-10s : %7s' % ("OS", osname_str) + ';')
