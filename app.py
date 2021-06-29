from flask import Flask, render_template
from utils.system_check import *
from utils.encrypt_make_qr_image import *

app = Flask(__name__, static_folder="templates/static")


@app.route('/')
def index():
    return render_template('index.html')


def main():
    # first check if the config file is configured

    site_result = facility_details().get_facility_details()  # If all Site Information is correct.
    if not site_result:  # If the file is  not complete. then the application will exit.
        return render_template('error.html')  # Render the Error page
        exit()

    # if the config file is set correctly, continue checking the services
    emr_result = emr_systems().check_systems()
    ip_result = site_ip_address().get_site_ip_address()
    hdd_result = system_utilization().get_hdd_details()
    ram_result = system_utilization().get_ram_details()
    # platform().platform_info()
    backup_result = auto_backup().check_backups()


    #This is a final Dictionaly to be sent for encryption
    final_string_to_decrypt =\
        {
            "site_code": site_result,
            "emr": emr_result,
            "ip_address": ip_result,
            "hdd_used": hdd_result,
            "ram_available": ram_result,
            "backup": backup_result
        }


    # now send to QR IMAGE after Encrypting the final string
    generate_qr_image().add_qr_data(encrypt().encrypt_data("data", final_string_to_decrypt))

    #**************************
    # just checking if the encrpted data can be decrypted
    testing = encrypt().encrypt_data("data", final_string_to_decrypt)

    decoded_jwt = jwt.decode(testing, "secret", algorithms="HS256")
    print(decoded_jwt)
    #***************************


if __name__ == '__main__':
    main()
    app.run(host='0.0.0.0', debug=True)
