# coding=utf-8

import os
import subprocess
from os.path import exists
from flask import json

from utils.utilities import load_file


def check_installation_folders(path):
    """
    checks if EMR installation folders are available
    :return:
    """

    version_dict = {}
    apps_dir = load_file(path)
    apps_dir = json.dumps(apps_dir)
    apps_dir = json.loads(apps_dir)
    print(apps_dir)
    for key in apps_dir:
        if exists(apps_dir[key]):
            tag = get_emr_versions(apps_dir[key])
            version_dict[key] = tag
    print(version_dict)
    json_object = json.dumps(version_dict)
    json_object = json.loads(json_object)
    return json_object


def get_emr_versions(directory):
    """
    get emr version from the installation folder
    :return:
        string: emr tags
    """
    emc_result = subprocess.Popen(["/usr/bin/git  --git-dir={}/.git describe --tags `git rev-list --tags --max-count=1`".format(directory)], shell=True, stdout=subprocess.PIPE)
    emc_result = emc_result.stdout.read().strip()
    return emc_result
