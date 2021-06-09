# check for mysql service
import subprocess


def check_service():
    service = ["docker", "mysql", "nginx"]
    for x in service:
        p = subprocess.Popen(["systemctl", "is-active", x], stdout=subprocess.PIPE)
        (output, err) = p.communicate()
        output = output.decode('utf-8')
        print(x + " :{}".format(output))
