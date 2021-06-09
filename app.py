import psutil
import psutil._common
from flask import Flask, render_template

from utils.emr_systems import check_systems
from utils.platform import platform_info
from utils.system_utilization import get_ram_details, get_disk_usage


app = Flask(__name__, static_folder="templates/static")


# @app.route('/')
def index():
    return render_template('index.html')


@app.route('/')
def main():
    get_ram_details(psutil.virtual_memory().available)
    get_disk_usage(psutil.disk_usage('/').free)
    platform_info()
    check_systems()
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    # main()
