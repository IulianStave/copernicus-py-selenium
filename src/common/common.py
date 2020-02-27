import os
import unittest
import argparse
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

DRIVERS = {
    'chrome': webdriver.Chrome,
    'firefox': webdriver.Firefox,
    'phantomjs': webdriver.PhantomJS,
    'edge': webdriver.Edge,
    'ie': webdriver.Ie,
    'safari': webdriver.Safari,
}


HEADLESS_OPTIONS = {
    'chrome': ChromeOptions,
    'firefox': FirefoxOptions
}


def get_browser(name, RunHeadless=False, path=None):
    browser = DRIVERS[name]
    if RunHeadless:
        options = HEADLESS_OPTIONS[name]()
        options.add_argument("--headless")
        if path:
            return browser(options=options, executable_path=path)
        return browser(options=options)
    return browser(executable_path=path) if path else browser()


def build_cmd_arguments() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            'Run tests on website with some tweaking .\n'
            'The given browser webdriver must be in your $PATH\n'
            'or given via the --browserpath option.\n\n'
            'E.g.: chrome: chromedriver, firefox: geckodriver, '
            'edge: MicrosoftWebDriver.exe.'
        )
    )
    parser.add_argument(
        '-U', '--url', type=str,
        help='Site url, eg: https://atmoshpere.copernicus.eu'
    )
    parser.add_argument(
        '-V', '--verbose', action='count', default=1,
        help='Verbosity. Default: 1'
    )
    parser.add_argument(
        '-B', '--browser', default='chrome',
        help='Browser to use, known: "{}". Default: chrome'.format(
            ', '.join(DRIVERS.keys())
        )
    )
    parser.add_argument(
        '-P', '--browserpath', default=None,
        help='Custom path to browser executable.'
    )

    parser.add_argument(
        '-sw', '--screenwidth', default=1024,
        help='Screen width. Default: 1024.'
    )

    parser.add_argument(
        '-sh', '--screenheight', default=768,
        help='Screen height. Default: 768.'
    )

    parser.add_argument(
        '-H', '--headless', action='store_true',
        help='Run headless mode'
    )
    return parser


class BrowserTestCase(unittest.TestCase):
    """ Custom TestCase wrapper.
        Needed to support the browser
    """
    driver = None
    url = None

    def __init__(self, methodName, driver: WebDriver, url: str):
        super().__init__(methodName)
        self.driver = driver
        self.url = url

    @classmethod
    def my_tests(cls):
        """ Helper method used to fetch the available tests for a TestSuite
        """
        return unittest.defaultTestLoader.getTestCaseNames(cls)

    def screenshot(self, suffix: str = ''):
        """ Capture a screeenshot.
            Uses `suffix` if given or the current browser url.
        """
        suffix = suffix or self._get_screenshot_suffix()
        name = '{}/screenshot_{}.png'.format(os.getcwd(), suffix)
        self.driver.save_screenshot(name)

    def _get_screenshot_suffix(self) -> str:
        return '_'.join(self.driver.current_url.split('#')[0].split('/')[2:])
