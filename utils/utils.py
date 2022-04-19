import json


def load_sites(directory):
    with open(directory) as f:
        all_data = json.load(f)
    return all_data