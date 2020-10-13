import requests

def get_fivedots_data():
    r = requests.get('https://fivedots.coe.psu.ac.th')

    if r.status_code == 200:
        return r.text
    return None
