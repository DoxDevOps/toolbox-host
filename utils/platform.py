import platform
from utils.encrypt import encrypt_data


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
    encrypt_data("OS release", version_str)
    encrypt_data("OS", osname_str)
