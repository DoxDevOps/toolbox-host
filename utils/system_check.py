import subprocess
import json
import psutil
from psutil._common import bytes2human


class system_check:
    # check for mysql, docker service etc
    def __init__(self):
        pass
        # Gets all information about Random Access Memory (RAM) and Disk Storage

    ram = psutil.virtual_memory()
    disk_space = psutil.disk_usage('/')

    # RAM

    def get_ram_details(self):
        ram_dict = \
            {
                "total": bytes2human(self.ram.total),
                "used": bytes2human(self.ram.used),
                "free": bytes2human(self.ram.free),
                "percentage": int(self.ram.percent)

            }
        json_object = json.dumps(ram_dict)

        return json_object

    # HDD
    @property
    def get_hdd_details(self):
        hdd_dict = \
            {
                "total": self.disk_space.total,
                "used": self.disk_space.used,
                "free": self.disk_space.free,
                "percentage": int(self.disk_space.percent)
            }
        json_object = json.dumps(hdd_dict)

        return json_object

    @property
    def check_service(self):
        services = ["docker", "mysql", "nginx"]  # service to check (Active or Inactive)
        running_services_dict = {}
        for service in services:
            p = subprocess.Popen(["systemctl", "is-active", service], stdout=subprocess.PIPE)
            (output, err) = p.communicate()
            output = output.decode('utf-8')
            running_services_dict[service] = output

            '''running_services_dict = \
                {
                    service: output
                }'''
        json_object = json.dumps(running_services_dict)

        return json_object


# this checks if a facility is running a POC or EMC System
'''This functionality has been disabled for now 
class platform:

    # check for Platform Information
    def platform_info(self):
        osname = platform.system()
        version = platform.release()
        osname = osname.split('\n')
        version = version.split('\n')
        for x in version:
            version_str = x.strip()
        for y in osname:
            osname_str = y.strip()
        encrypt.encrypt_data("OS release", version_str)
        encrypt.encrypt_data("OS", osname_str)'''
