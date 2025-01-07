from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os

def setup_driver():
    """Setup Chrome WebDriver for both local and production environments"""
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-notifications')
    chrome_options.add_argument('--window-size=1920,1080')

    if os.environ.get('RENDER'):
        # Production settings for Render
        CHROME_PATH = "/opt/render/project/.render/chrome/opt/google/chrome/chrome"
        CHROMEDRIVER_PATH = "/opt/render/project/.render/chromedriver/chromedriver"

        chrome_options.binary_location = CHROME_PATH
        service = Service(executable_path=CHROMEDRIVER_PATH)
    else:
        # Local development settings
        service = Service('chromedriver/chromedriver-win64/chromedriver.exe')

    return webdriver.Chrome(service=service, options=chrome_options)
