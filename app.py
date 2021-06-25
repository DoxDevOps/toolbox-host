import psutil
import psutil._common
from flask import Flask, render_template
from utils.system_check import *

app = Flask(__name__, static_folder="templates/static")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/')
def main():
    # first check if the config file is configured
    get_facility = facility_details.get_facility_details()
    result = get_facility()  # If all Site Information is correct.
    if result == 0:  # If the file is  not complete. then the application will exit.
        return render_template('error.html')  # Render the Error page
        exit()
    # if the config file is set corretly, continue checking the services
    else:
        emr_systems.check_systems()
        site_ip_address.get_site_ip_address()
        system_utilization.get_ram_hdd_details(psutil.virtual_memory().available, psutil.disk_usage('/').free)
        # platform_info()
        auto_backup.check_backups()
        emr_systems.check_service()

        # import platform
        # print(platform.system())

    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    # main()
