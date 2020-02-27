from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from src.data.TestData import TestData
from src.data.Locators import Locators


TIMEOUT = 20


class BasePage():
    """ Contains all common elements and functionalities
        available to all pages.
    """

    def __init__(self, driver):
        self.driver = driver

    def click(self, by_locator):
        """ Clicks on the web element identified by locator passed to it"""
        element = WebDriverWait(self.driver, TIMEOUT).until(
            EC.visibility_of_element_located(by_locator))
        element.click()
        return element

    def assert_element_text(self, by_locator, expected_element_text):
        """ Asserts comparison of a web element's text with passed in text
        """
        web_element = WebDriverWait(self.driver, TIMEOUT).until(
            EC.visibility_of_element_located(by_locator))
        assert web_element.text == expected_element_text

    def enter_text(self, by_locator, text):
        """ Performs text entry of the passed in text,
            in a web element whose locator is passed to it.
        """
        return WebDriverWait(self.driver, TIMEOUT).until(
            EC.visibility_of_element_located(by_locator)).send_keys(text)

    def is_enabled(self, by_locator):
        """ Checks if the web element whose locator
            has been passed to it, is enabled or not
            and returns the web element if it is enabled
        """
        return WebDriverWait(self.driver, TIMEOUT).until(
            EC.visibility_of_element_located(by_locator))

    def get_elements(self, by_locator):
        """ Checks if the web elements whose locator
            has been passed to it, is present or not
            and returns the web elements list if they are
        """
        return WebDriverWait(self.driver, timeout=TIMEOUT).until(
                EC.presence_of_all_elements_located(locator=by_locator)
                )

    def is_visible(self, by_locator):
        """ Checks if the web element whose locator has been passed to it,
            is visible or not and returns true or false
            depending upon its visibility
        """
        element = WebDriverWait(self.driver, TIMEOUT).until(
            EC.visibility_of_element_located(by_locator))
        return element

    def hover_to(self, by_locator):
        """ Moves the mouse pointer over a web element
            whose locator has been passed to it.
        """
        element = WebDriverWait(self.driver, TIMEOUT).until(
            EC.visibility_of_element_located(by_locator))
        ActionChains(self.driver).move_to_element(element).perform()

    def switch_to_new_window(self):
        # WebDriverWait(self.driver, TIMEOUT).until(
        #     EC.number_of_windows_to_be(2))
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)


class HomePage(BasePage):
    """Home Page"""

    def __init__(self, driver, url):
        super().__init__(driver)
        self.driver.get(url)

    def search(self):
        self.driver.find_element(*Locators.SEARCH_TOGGLE).click()
        self.driver.find_element(*Locators.SEARCH_INPUT).clear()
        self.enter_text(Locators.SEARCH_INPUT, TestData.SEARCH_TEXT_ATM)
        self.click(Locators.SEARCH_SUBMIT_BUTTON)


class CataloguePage(BasePage):
    """Catalogue Page"""

    def __init__(self, driver, url):
        super().__init__(driver)
        self.driver.get(url)
        # TestData.CATALOGUE_URL


class DataPage(BasePage):
    """Data Page"""

    def __init__(self, driver, url):
        super().__init__(driver)
        self.driver.get(url)
        # TestData.DATA_URL
