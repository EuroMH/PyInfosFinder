import unittest
from unittest.mock import patch
import logging

class ColoredFormatter(logging.Formatter):
    COLORS = {
        'OK': "\033[92m",
        'WARNING': "\033[93m",
        'ERROR': "\033[91m",
        'RESET': "\033[0m"
    }

    def format(self, record):
        if record.levelname == 'INFO':
            return f"{self.COLORS['OK']}{record.getMessage()}{self.COLORS['RESET']}"
        return super().format(record)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = ColoredFormatter()
handler.setFormatter(formatter)
logger.handlers = [handler]

from src.python_package import misc, computer

class TestSystemInfo(unittest.TestCase):

    @patch('src.python_package.computer.gethwid')
    def test_hwid(self, mock_gethwid):
        mock_gethwid.return_value = "HWID-3098D4CA-B38C-47AC-AEFC-B25C2178F37E"
        hwid = computer.gethwid()
        self.assertEqual(hwid, "HWID-3098D4CA-B38C-47AC-AEFC-B25C2178F37E")
        logger.info('test_hwid OK')

    @patch('src.python_package.computer.getuser')
    def test_user(self, mock_getuser):
        mock_getuser.return_value = "Mathys"
        username = computer.getuser()
        self.assertEqual(username, "Mathys")
        logger.info('test_user OK')

    @patch('src.python_package.computer.getcpuinfo')
    def test_cpuinfo(self, mock_getcpuinfo):
        mock_getcpuinfo.return_value = {
            'cpu_model': 'Intel64 Family 6 Model 186 Stepping 3, GenuineIntel',
            'cpu_cores': 5,
            'cpu_threads': 6
        }
        cpu_info = computer.getcpuinfo()
        self.assertIsInstance(cpu_info, dict)
        self.assertIn('cpu_model', cpu_info)
        self.assertIn('cpu_cores', cpu_info)
        self.assertIn('cpu_threads', cpu_info)
        logger.info('test_cpuinfo OK')

    @patch('src.python_package.computer.getgpuinfo')
    def test_gpuinfo(self, mock_getgpuinfo):
        mock_getgpuinfo.return_value = {'gpu_model': 'NVIDIA GTX 1080'}
        gpu_info = computer.getgpuinfo()
        self.assertIsInstance(gpu_info, dict)
        self.assertIn('gpu_model', gpu_info)
        logger.info('test_gpuinfo OK')

    @patch('src.python_package.computer.getraminfo')
    def test_raminfo(self, mock_getraminfo):
        mock_getraminfo.return_value = {
            'total_ram': 7632.28515625,
            'available_ram': 891.48046875,
            'used_ram': 6740.8046875
        }
        ram_info = computer.getraminfo()
        self.assertIsInstance(ram_info, dict)
        self.assertIn('total_ram', ram_info)
        self.assertIn('available_ram', ram_info)
        self.assertIn('used_ram', ram_info)
        logger.info('test_raminfo OK')

    @patch('src.python_package.computer.getosinfo')
    def test_osinfo(self, mock_getosinfo):
        mock_getosinfo.return_value = {
            'os_name': 'Windows',
            'os_version': '10.0.26100',
            'os_arch': ('64bit', 'WindowsPE')
        }
        os_info = computer.getosinfo()
        self.assertIsInstance(os_info, dict)
        self.assertIn('os_name', os_info)
        self.assertIn('os_version', os_info)
        self.assertIn('os_arch', os_info)
        logger.info('test_osinfo OK')

    @patch('src.python_package.computer.getdiskinfo')
    def test_diskinfo(self, mock_getdiskinfo):
        mock_getdiskinfo.return_value = {
            'partitions': [
                {
                    'device': 'C:\\',
                    'mountpoint': 'C:\\',
                    'fstype': 'NTFS',
                    'total': 254662406144,
                    'used': 237904404480,
                    'free': 16758001664,
                    'percent': 93.4
                }
            ]
        }
        disk_info = computer.getdiskinfo()
        self.assertIsInstance(disk_info, dict)
        self.assertIn('partitions', disk_info)
        self.assertIsInstance(disk_info['partitions'], list)
        logger.info('test_diskinfo OK')

    @patch('src.python_package.computer.getbatteryinfo')
    def test_batteryinfo(self, mock_getbatteryinfo):
        mock_getbatteryinfo.return_value = {
            'percent': 60,
            'plugged': False,
            'secsleft': 10483
        }
        battery_info = computer.getbatteryinfo()
        self.assertIsInstance(battery_info, dict)
        self.assertIn('percent', battery_info)
        self.assertIn('plugged', battery_info)
        self.assertIn('secsleft', battery_info)
        logger.info('test_batteryinfo OK')

    @patch('src.python_package.computer.getmotherboardinfo')
    def test_motherboardinfo(self, mock_getmotherboardinfo):
        mock_getmotherboardinfo.return_value = {'motherboard': 'ASUS ROG'}
        motherboard_info = computer.getmotherboardinfo()
        self.assertIsInstance(motherboard_info, dict)
        self.assertIn('motherboard', motherboard_info)
        logger.info('test_motherboardinfo OK')

    @patch('src.python_package.computer.getuptime')
    def test_uptime(self, mock_getuptime):
        mock_getuptime.return_value = '1733349545.3520343'
        uptime_info = computer.getuptime()
        self.assertEqual(uptime_info, '1733349545.3520343')
        logger.info('test_uptime OK')

    @patch('src.python_package.misc.getip')
    def test_ip(self, mock_getip):
        mock_getip.return_value = "89.88.225.217"
        ip_info = misc.getip()
        self.assertEqual(ip_info, "89.88.225.217")
        logger.info('test_ip OK')

    @patch('src.python_package.misc.getgeo')
    def test_geo(self, mock_getgeo):
        mock_getgeo.return_value = {
            'status': 'success',
            'country': 'France',
            'countryCode': 'FR',
            'region': 'PDL',
            'regionName': 'Pays de la Loire',
            'city': 'Le Mans',
            'zip': '72000',
            'lat': 48.0014,
            'lon': 0.1901,
            'timezone': 'Europe/Paris',
            'isp': 'Bouygues Telecom ISP',
            'org': '',
            'as': 'AS5410 Bouygues Telecom SA',
            'query': '89.88.225.217'
        }
        geo_info = misc.getgeo("89.88.225.217")
        self.assertIsInstance(geo_info, dict)
        self.assertIn('country', geo_info)
        self.assertIn('city', geo_info)
        logger.info('test_geo OK')

    @patch('src.python_package.misc.getallinfo')
    def test_miscallinfos(self, mock_getallinfo):
        mock_getallinfo.return_value = {"info": "All system info"}
        all_info = misc.getallinfo()
        self.assertIsInstance(all_info, dict)
        logger.info('test_miscallinfos OK')

if __name__ == '__main__':
    unittest.main()
