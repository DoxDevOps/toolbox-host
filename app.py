import json
from flask import Flask, render_template, request

from utils.check_config import facility_details
from utils.encrypt_make_qr_image import encrypt_make_qr_image
from utils.emr_systems import emr_systems
from utils.utils import load_sites

app = Flask(__name__, static_folder="templates/static")


@app.route('/home')
def test():
    """
    Just Testing if the app is Alright and Reachable
    :return: Json String.
    """
    return json.dumps({"status": "success", "message": "Welcome to Toolbox-host QR Service !!"}), 200


@app.route('/')
def get_qr_image():
    """This is the entry point."""
    result = make_qr_image()  # This calls a function that creates a QR image
    if not result:
        all_sites = load_sites("config/.sites.json")
        return render_template('configure.html', sites=all_sites)

    # get site name. So that it is displayed on the home page as well.
    with open('config/config.json') as f:
        site_name = json.load(f)
        print(site_name["site_name"])
    return render_template('index.html', site_name=site_name["site_name"])


@app.route('/config', methods=['GET', 'POST'])
def configure():
    if "POST" == request.method:
        select = request.form.get('site')
        select = json.dumps(select)
        facility_details().save_facility_details(select)
        return get_qr_image()

    if "GET" == request.method:
        all_sites = load_sites("config/.sites.json")
        return render_template('configure.html', sites=all_sites)

    # return render_template('index.html')





@app.route('/getEmrData')
def get_emr_data():
    """
    This function get all Information required on a sites(emr, memory utilization,
    :return: a json file with all details
    """
    # first check if the config file is configured.
    site_result = facility_details().get_facility_details()  # If all Site Information is correct.
    if not site_result:  # If the file is  not complete. then the application will exit.

        return False  # Render the Error page
    else:  # if the config file is set correctly, continue checking the services
        emr_result = emr_systems().check_systems()  # checks if site is running a POC or EMC system
        # This is a final Dictionary to be sent for encryption
        final_string_to_decrypt = \
            {
                "1": "Toolbox",
                "uuid": site_result["uuid"],
                "app_id": site_result["app_id"],
                "module": emr_result

            }

        final_string_to_decrypt = json.dumps(final_string_to_decrypt)
        return final_string_to_decrypt


@app.route('/encrypt')
def encrypt():
    """
    This method is encrypting the data and then forming a QR image
    :return:
    """
    final_string_to_decrypt = get_emr_data()
    # now send to QR IMAGE after Encrypting the final string
    encrypted_data = encrypt_make_qr_image().encrypt_data("data", final_string_to_decrypt)

    return str(encrypted_data)


@app.route('/createImage')
def make_qr_image():
    final_string_to_decrypt = get_emr_data()
    if final_string_to_decrypt:
        result = encrypt_make_qr_image().add_qr_data(final_string_to_decrypt)  # NOTE : If there is
        # another QR Image, it will be replaced when the code runs
        return str(result)
    return False


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=6070)
