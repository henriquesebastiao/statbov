import time
from pathlib import Path
from typing import Type

from django.db.models import Model
from django.test import TestCase
from django.test.selenium import LiveServerTestCase
from pytest import mark
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from statbov.app.models import CustomUser
from statbov.settings import BASE_DIR


class ModelAttrsTest:
    """Class to set attributes in a model instance.

    Methods:
        __init__: Initialize the class with the attributes to be set
        add: Add attributes to the class
        clean: Return the attributes without the None values

    Example:
        attrs = ModelAttrsTest(
            id='1',
            farm_id='1',
            diet_id='1',
            obs='Test',
            other=None
        )
        attrs.add(id='2', farm_id='2', diet_id='2')
        print(attrs.clean)
        # {'id': '2', 'farm_id': '2', 'diet_id': '2', 'obs': 'Test'}
    """

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __bool__(self):
        """Return True if the class has attributes, otherwise False."""
        if len(self.__dict__) > 0:
            return True
        return False

    def __eq__(self, other):
        if isinstance(other, bool):
            return bool(self) == other
        elif isinstance(other, ModelAttrsTest):
            return self.__dict__ == other.__dict__
        return False

    def __repr__(self):
        return f'{self.__class__.__name__}({self.__dict__})'

    def add(self, **kwargs):
        """Add attributes to the class.

        Args:
            **kwargs: Attributes to be added
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    @property
    def clean(self):
        """Return the attributes without the None values.

        Returns:
            dict: Attributes without the None values
        """
        attrs = self.__dict__.copy()
        for key, value in self.__dict__.items():
            if value is None:
                del attrs[key]
        return attrs


class ModelTest(TestCase):
    """Base class for model tests.

    Attributes:
        MODEL (Type[Model]): Model to be tested
        ATTRS (ModelAttrsTest): Attributes to be set in the instance

    Methods:
        create_instance: Create an instance of a model and return it
    """

    MODEL: Type[Model]
    ATTRS: ModelAttrsTest

    @classmethod
    def create_instance(cls, **kwargs) -> Model:
        """Create an instance of a model and return it.

        Args:
            **kwargs: Additional attributes to be set in the instance

        Returns:
            Model: Instance of the model
        """
        cls.ATTRS.add(**kwargs)

        if cls.MODEL == CustomUser:
            instance = cls.MODEL.objects.create_user(**cls.ATTRS.clean)
        else:
            instance = cls.MODEL.objects.create(**cls.ATTRS.clean)
        instance.full_clean()

        return instance


@mark.functional_test
class FunctionalTestBase(LiveServerTestCase):
    """Base class for functional tests.

    Attributes:
        CHROMEDRIVER_PATH: Path to the chromedriver executable
        CHROME_OPTIONS: Options to be set in the headless Chrome browser

    Methods:
        _make_browser: Make a headless Chrome browser
        setUp: Create a headless Chrome browser before the test
        tearDown: Quit the browser after the test
        sleep: Sleep the test for a given amount of seconds
        get_content: Get the content of an HTML tag
    """

    CHROMEDRIVER_PATH: Path = BASE_DIR / 'bin' / 'chromedriver'
    CHROME_OPTIONS: str = '--headless'

    @classmethod
    def _make_browser(cls):
        """Function to make a headless Chrome browser.

        Returns:
            headless Chrome browser
        """
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument(cls.CHROME_OPTIONS)

        chrome_service = Service(executable_path=str(cls.CHROMEDRIVER_PATH))
        browser = webdriver.Chrome(
            service=chrome_service, options=chrome_options
        )
        return browser

    def setUp(self) -> None:
        """Create a headless Chrome browser before the test."""
        self.browser = self._make_browser()
        return super().setUp()

    def tearDown(self) -> None:
        """Quit the browser after the test."""
        self.browser.quit()
        return super().tearDown()

    @staticmethod
    def sleep(seconds: int = 1) -> None:
        """Method to sleep the test for a given amount of seconds.

        Args:
            seconds: amount of seconds to sleep
        """
        time.sleep(seconds)

    def get_content(self, html_tag_name: str, url: str = ''):
        """Method to get the content of an HTML tag.

        Args:
            html_tag_name: HTML tag name to get the content
            url: URL to get the content

        Returns:
            content of an HTML tag
        """
        self.browser.get(self.live_server_url + url)
        return self.browser.find_element(By.TAG_NAME, html_tag_name)
