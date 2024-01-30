import time

from django.test.selenium import LiveServerTestCase
from pytest import mark
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from statbov.settings import BASE_DIR

CHROMEDRIVER_NAME = 'chromedriver'
CHROMEDRIVER_PATH = BASE_DIR / 'bin' / CHROMEDRIVER_NAME


def make_chrome_browser(*options):
    """
    Function to make a headless Chrome browser.

    Args:
        *options: options to add to the browser

    Returns:
        headless Chrome browser
    """
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')

    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    chrome_service = Service(executable_path=str(CHROMEDRIVER_PATH))
    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
    return browser


@mark.functional_test
class FunctionalTestBase(LiveServerTestCase):
    def setUp(self) -> None:
        self.browser = make_chrome_browser()
        return super().setUp()

    def tearDown(self) -> None:
        self.browser.quit()  # Is necessary to quit the browser to avoid memory leak
        return super().tearDown()

    @staticmethod
    def sleep(seconds: int = 1) -> None:
        time.sleep(seconds)

    def get_content(self, html_tag_name: str, url: str = ''):
        """
        Method to get the content of an HTML tag.
        Args:
            html_tag_name: HTML tag name to get the content
            url: URL to get the content

        Returns:
            content of an HTML tag
        """
        self.browser.get(self.live_server_url + url)
        return self.browser.find_element(By.TAG_NAME, html_tag_name)
