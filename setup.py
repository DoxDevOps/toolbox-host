#! /usr/bin/python
import os


def configure_site():
    """COnfigures the site"""
    # install pip
    print(" Step 1 : Update laptop")
    answer = os.system("sudo apt-get update")
    print("Step 2: Install Pip.")
    answer1 = os.system("sudo apt install python-pip")
    print(answer1)
    print("Step3 : install python environment")
    os.system("sudo apt install virtualenv")
    os.system("virtualenv flask")
    os.system(
        ". tool-box/bin/activate && pip install -r requirements.txt && FLASK_APP=app.py FLASK_ENV=development flask run --port 6070")
    print("creating Toolbox Service")
    # here is the code for creating the site.
    os.system("cat > /etc/systemd/system/autotransfer.service <<EOF \
            [Unit]"
              "Description=EGPAF Auto Data Transfer Service"
              "After=network.target"
              "[Service]"
              "WorkingDirectory=$INSTALL_DIR"
              "ExecStart=$VPYTHONB ${INSTALL_DIR}/sms_send.py &> ${INSTALL_DIR}/send_sms.log"
              "ExecStop=/bin/kill -INT \$MAINPID"
              "ExecReload=/bin/kill -TERM \$MAINPID"
              "# In case if it gets stopped, restart it immediately"
              "Restart=always"
              "Type=simple"

              "[Install]"
              "# multi-user.target corresponds to run level 3"
              "# roughtly meaning wanted by system start"
              "WantedBy=multi-user.target"
              "EOF ")
    os.system("sudo systemctl daemon-reload && sudo systemctl start autotransfer && sudo systemctl enable autotransfer")
    return True


def create_service():
    """ Create Service """
    os.system("")
    return True


def main():
    configure_site()
    return True


if __name__ == '__main__':
    main()
