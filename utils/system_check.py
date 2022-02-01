import subprocess
import json
import psutil


class system_check:
    # check for mysql, docker service etc
    def __init__(self):
        pass
        # Gets all information about Random Access Memory (RAM) and Disk Storage

    ram = psutil.virtual_memory().available
    disk_space = psutil.disk_usage('/').percent

    def __init__(self):
        pass

    # RAM
    def get_ram_details(self):
        ram_dict = \
            {
                "ram": self.ram >> 30
            }
        json_object = json.dumps(ram_dict["ram"])

        return json_object

    # HDD
    def get_hdd_details(self):
        hdd_dict = \
            {
                "hdd": self.disk_space
            }
        json_object = json.dumps(hdd_dict["hdd"])

        return json_object

    def check_service(self):
        services = ["docker", "mysql", "nginx"]
        for service in services:
            p = subprocess.Popen(["systemctl", "is-active", service], stdout=subprocess.PIPE)
            (output, err) = p.communicate()
            output = output.decode('utf-8')

            running_services_dict = \
                {
                    "running_services": output
                }
            json_object = json.dumps(running_services_dict["running_services"])

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
