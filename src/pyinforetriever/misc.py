import requests

def getip() -> str:
    ip = 'None'
    try:
        ip = requests.get('https://api.ipify.org').text.strip()
    except:
        pass
    return ip

def getgeo(ip) -> dict:
    geo = {}
    try:
        geo = requests.get(f'http://ip-api.com/json/{ip}').json()
    except:
        pass
    return geo

def getallinfo() -> str:
    system_info = ""

    system_info += f"IP: {getip()}\n"
    system_info += f"GeoLocation: {getgeo(getip())}\n"

    return system_info

