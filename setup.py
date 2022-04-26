#! /usr/bin/python
import os
import re
import uuid




def configure_site():
    """#Configures the site
    # install pip
    print(" Step 1 : Update laptop")
    answer = os.system("sudo apt-get update")
    print("Step 2: Install Pip.")
    answer1 = os.system("sudo apt install python-pip")
    print(answer1)
    print("Step3 : install python environment")
    os.system("sudo apt install virtualenv")
    os.system("virtualenv flask")      
    print("creating Toolbox Service")
    # here is the code for creating the site.

    os.system("sudo cp toolbox.service /etc/systemd/system/")
    os.system("sudo systemctl daemon-reload && sudo systemctl start toolbox && sudo systemctl enable toolbox")"""

    print (':'.join(re.findall('..', '%012x' % uuid.getnode()))) # convert to hex and seperate two figures with :

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
