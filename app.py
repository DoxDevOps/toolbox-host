import json
from flask import Flask, render_template
from config.config import data
from utils.export_emr_data import check_installation_folders
from utils.generate_qr_image import add_qr_data
from utils.setup_toolbox import mac_address
from utils.utilities import load_file
from utils.validate_emr_data import validate_config_file


app = Flask(__name__, static_folder="templates/static")


@app.route('/')
def extract_data():
    """gets EMR data and creates a QR Image
    Args: None
    Returns:
        dict: hosts from api
    """
    # first verify if the data is correct in the config file

    config_file_data = validate_config_file(data["config"])
    if not config_file_data:
        return render_template('error.html')  # this will load a page that informs the user to reconfigure toolbox
    # if all is alright, then do the following
    # 1. get EMR version and mac address
    emr_data = check_installation_folders(data["apps_loc"])
    mac = mac_address()
    if not emr_data:
        return render_template('error.html')
    # 2. This is a final Dictionary to be sent for QR Image generation
    final_emr_data = \
        {
            "1": "Toolbox",
            "uuid": config_file_data["uuid"],
            "app_id": config_file_data["app_id"],
            "module": emr_data,
            "mac": mac

        }

    final_string_to_decrypt = json.dumps(final_emr_data)
    # 3. Add the data to QR Image
    add_qr_data(final_string_to_decrypt, data["toolbox_image"])

    # 4 Get facility name . This name will be displayed on UI
    site_name = load_file(data["config"])
    return render_template('index.html', site_name=site_name["site_name"])

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, port=6070)
