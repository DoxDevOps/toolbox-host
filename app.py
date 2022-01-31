from flask import Flask, render_template
from utils.system_check import *
from utils.encrypt_make_qr_image import *
from collections import OrderedDict

app = Flask(__name__)


@app.route('/home')
def test():
    """
    Just Testing if the app is Alright and Reachable
    :return: Json String
    """
    return json.dumps({"status": "success", "message": "Welcome to Toolbox-host QR Service !!"}), 200


@app.route('/check-site')
def main():
    # first check if the config file is configured.
    site_result = facility_details().get_facility_details()  # If all Site Information is correct.
    if not site_result:  # If the file is  not complete. then the application will exit.
        return render_template('error.html')  # Render the Error page
        exit()

    # if the config file is set correctly, continue checking the services
    emr_result = emr_systems().check_systems()  # checks if site is running a POC or EMC system
    ip_result = site_ip_address().get_site_ip_address()  # gets site ip WAN address
    hdd_result = system_utilization().get_hdd_details()  # gets HDD used percentage
    ram_result = system_utilization().get_ram_details()  # gets RAM details
    services_result = running_processes().check_service()  # gets services running e.g mysql, docker, nginx
    # platform().platform_info() #currenlty disabled
    backup_result = auto_backup().check_backups()  # checks if back up is working (returns true or false)


    #This is a final Dictionaly to be sent for encryption
    final_string_to_decrypt =\
        {
            "site_code": site_result,
            "emr": emr_result,
            "services": services_result,
            "ip_address": ip_result,
            "hdd_used": hdd_result,
            "ram_available": ram_result,
            "backup": backup_result
        }
    ''' TO DO : (TIWONGE LWARA)
    Try to send an ordered dictionary . Still searching on this.
    tt = OrderedDict((word, word1) for word in final_string_to_decrypt)

    print(tt)
    '''

    # now send to QR IMAGE after Encrypting the final string
    generate_qr_image().add_qr_data(encrypt().encrypt_data("data", final_string_to_decrypt))  # NOTE : If there is
    # another QR Image, it will be replaced when the code runs

    #****** TESTING TESTING ********** will be removed for later**********
    # just checking if the encrypted data can be decrypted
    testing = encrypt().encrypt_data("data", final_string_to_decrypt)

    decoded_jwt = jwt.decode(testing, "secret", algorithms="HS256")
    print(decoded_jwt)
    #*********END OF TESTING ******************


if __name__ == '__main__':
    main()
    app.run(host='0.0.0.0', debug=True)
