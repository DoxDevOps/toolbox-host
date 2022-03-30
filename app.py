from flask import Flask, render_template
from utils.system_check import *
from utils.check_config import *
from utils.encrypt_make_qr_image import *
from utils.emr_systems import *


app = Flask(__name__, static_folder="templates/static")

@app.route('/home')
def test():
    """
    Just Testing if the app is Alright and Reachable
    :return: Json String.
    """
    return json.dumps({"status": "success", "message": "Welcome to Toolbox-host QR Service !!"}), 200


@app.route('/toolbox')
def get_qr_image():
    """This is the entry point."""
    make_qr_image()  # This calls a function that creates a QR image
    return render_template('index.html')


@app.route('/getEmrData')
def get_emr_data():
    """
    This function get all Information required on a sites(emr, memory utilization,
    :return: a json file with all details
    """
    print("called 1")
    # first check if the config file is configured.
    site_result = facility_details().get_facility_details()  # If all Site Information is correct.
    print("SITE DETAILS")
    print(site_result["uuid"])
    if not site_result:  # If the file is  not complete. then the application will exit.
        return render_template('error.html')  # Render the Error page
    else:  # if the config file is set correctly, continue checking the services
        emr_result = emr_systems().check_systems()  # checks if site is running a POC or EMC system
        #ip_result = emr_systems().get_site_ip_address()  # gets site ip WAN address
        #hdd_result = system_check().get_hdd_details()  # gets HDD used percentage
        #ram_result = system_check().get_ram_details()  # gets RAM details
        #services_result = system_check().check_service()  # gets services running e.g mysql, docker, nginx
        # platform().platform_info() #currenlty disabled
        #backup_result = emr_systems().check_backups()  # checks if back up is working (returns true or false)

        # This is a final Dictionary to be sent for encryption
        final_string_to_decrypt = \
            {
                "1": "Toolbox",
                "uuid": site_result["uuid"],
                "app_id":site_result["app_id"],
                "module": emr_result

            }
        ''' TO DO : (TIWONGE LWARA)
        Try to send an ordered dictionary . Still searching on this.
        tt = OrderedDict((word, word1) for word in final_string_to_decrypt)

        print(tt)
        '''
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
    result = encrypt_make_qr_image().add_qr_data(final_string_to_decrypt)  # NOTE : If there is
    # another QR Image, it will be replaced when the code runs
    return str(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
