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
    os.system(". flask/bin/activate && pip install -r requirements.txt && python app.py")

    return True


def main():
    configure_site()
    return True


if __name__ == '__main__':
    main()