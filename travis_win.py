import os

DOWNLOAD_DIR = os.environ['DOWNLOAD_DIR']
TBB_DIST_URL = os.environ['TBB_DIST_URL']
VERSION_ARCH = os.environ['VERSION_ARCH']
MAR = os.environ['MAR']

geckodriver_url = "https://github.com/mozilla/geckodriver/releases/download/v0.27.0/geckodriver-v0.27.0-win64.zip"
gecko_filename = "geckodriver-v0.27.0-win64.zip"

print(__name__, ': About to start')
os.makedirs(DOWNLOAD_DIR)
cmd = f"curl {TBB_DIST_URL}/{VERSION_ARCH} -o {DOWNLOAD_DIR}/{MAR}"
os.system(cmd)
cmd = f"unzip -o {DOWNLOAD_DIR}/{MAR} -d {DOWNLOAD_DIR}"
os.system(cmd)
cmd = f"curl {geckodriver_url} -o {DOWNLOAD_DIR}/{gecko_filename}"
os.system(cmd)
cmd = f"unzip -o {geckodriver_url} -d {DOWNLOAD_DIR}"
os.system(cmd)

print(os.listdir(DOWNLOAD_DIR))