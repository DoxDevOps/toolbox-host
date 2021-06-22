import psutil
import psutil._common
from flask import Flask, render_template

from utils.auto_backup import check_backups
from utils.emr_systems import check_systems
from utils.facility_details import get_facility_details
from utils.platform import platform_info
from utils.running_processes import check_service
from utils.site_ip_address import get_site_ip_address
from utils.system_utilization import get_ram_details, get_disk_usage

app = Flask(__name__, static_folder="templates/static")


# @app.route('/')
def index():
    return render_template('index.html')


@app.route('/')
def main():
    #first check if the config file is configured
    result = get_facility_details()  # If all Site Information is correct.
    if result == 0:  # If the file is  not complete. then the application will exit.
        return render_template('error.html')  # Render the Error page
        exit()
    #if the config file is set corretly, continue checking the services 
    else:
        check_systems()
        get_site_ip_address()
        get_ram_details(psutil.virtual_memory().available)
        get_disk_usage(psutil.disk_usage('/').free)
        # platform_info()
        check_backups()
        check_service()

        #import platform
        #print(platform.system())

    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    # main()
