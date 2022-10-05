import requests
import sys

def get_user_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]


def get_location():
    if len(sys.argv) == 1:
        ip_address = get_user_ip()
    elif len(sys.argv) == 2:
        ip_address = sys.argv[1];
    else:
        return "Usage: ./ip-location.py IP";
    
    response = requests.get(f'http://ipwho.is/{ip_address}').json()
    location_data = {
    "ip": ip_address,
    "city": response.get("city"),
    "region": response.get("region"),
    "country": response.get("country"),
    "country capital": response.get("capital"),
    "IP Type": response.get("type")
    }
    return location_data


print(get_location())
