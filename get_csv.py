import requests
from config import config


def get_pickup(sites, month):
    date = "Current+Month" if month == "current" else "Previous+Month"
    site = "site%5B%5D=4" if sites == 1 else "site%5B%5D=3&site%5B%5D=6"
    csv = requests.get(
        f"https://krameramerica.locateinv.com/report/114/run?{site}&removelineswithnovalues=AND&orderby=1&includedeletedsites=AND&formatassinglepage=1&daterange={date}&daterange2={date}&format=csv",
        auth=(config["key"]),
    ).content

    return csv
