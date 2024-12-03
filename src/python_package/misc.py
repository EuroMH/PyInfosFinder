import requests
from subprocess import Popen, PIPE

def getip() -> str:
    ip = 'None'
    try:
        ip = requests.get('https://api.ipify.org').text.strip()
    except:
        pass
    return ip


def gethwid() -> str:
    p = Popen('wmic csproduct get uuid', shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    return (p.stdout.read() + p.stderr.read()).decode().split('\n')[1].strip()


def get_geo(ip) -> dict:
    geo = {}
    try:
        geo = requests.get(f'http://ip-api.com/json/{ip}').json()
    except:
        pass
    return geo
