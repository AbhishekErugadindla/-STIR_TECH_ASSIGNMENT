# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# import os

# def setup_driver():
#     """Setup Chrome WebDriver for both local and production environments"""
#     chrome_options = Options()
#     chrome_options.add_argument('--headless')
#     chrome_options.add_argument('--disable-dev-shm-usage')
#     chrome_options.add_argument('--no-sandbox')
#     chrome_options.add_argument('--disable-gpu')
#     chrome_options.add_argument('--disable-notifications')
#     chrome_options.add_argument('--window-size=1920,1080')

#     if os.environ.get('RENDER'):
#         CHROME_PATH = "/opt/render/project/.render/chrome/opt/google/chrome/chrome"
#         chrome_options.binary_location = CHROME_PATH
#         service = Service("/opt/render/project/.render/chromedriver/chromedriver")
#     else:
#         service = Service(ChromeDriverManager().install())

#     return webdriver.Chrome(service=service, options=chrome_options)
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def setup_driver():
    chrome_options = Options()
    
    # Production settings for Chrome
    chrome_options.binary_location = "/usr/bin/google-chrome"
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-notifications')
    chrome_options.add_argument('--window-size=1920,1080')

    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        return driver
    except Exception as e:
        print(f"Error creating WebDriver: {str(e)}")
        raise
