import os
from pathlib import Path

# настройки веб сервиса
# scheme = 'https://'
# host = 'demo.opencrx.org'
# port = 443
# url = f'{scheme}{host}:{port}'
url = os.getenv('base_url', 'https://demo.opencrx.org')
username = 'guest'
password = 'guest'

# настройки браузера
implicit_wait = float(os.getenv('implicit_wait', 10))
browser_name = os.getenv('browser_name', 'chrome')
browser_version = None
local_driver_cache_valid_range = 7  # время жизни кэша локального драйвера (в днях)
grid_url = 'http://192.168.4.79:4444/wd/hub'
local_run = os.getenv('local_run', 'True').lower() in ('true', '1')
headless = os.getenv('headless', 'False').lower() in ('true', '1')
