from src.common.Pages import HomePage
from src.common.common import BrowserTestCase
from src.data.TestData import TestData
from src.data.Locators import Locators


class HomePageTest(BrowserTestCase):
    def test_homepage_loaded(self):
        """ Asserts the home page title is correct
        """
        self.home_page = HomePage(self.driver, self.url)
        self.assertIn(TestData.HOME_PAGE_TITLE, self.home_page.driver.title)

    def test_homepage_search_toggle(self):
        """Asserts the search toggle is present on homepage
        """
        self.home_page = HomePage(self.driver, self.url)
        self.assertTrue(self.home_page.is_enabled(
            Locators.SEARCH_TOGGLE))

    def test_homepage_top_cards(self):
        """ Asserts first two cards are loaded
        """
        self.home_page = HomePage(self.driver, self.url)
        cards_list = self.home_page.get_elements(Locators.HOME_CARD)
        first_two_cards = [card.text for card in cards_list[:2]]
        self.assertEqual(first_two_cards, TestData.TOP_CARDS_CLIMATE)

    def test_homepage_top_menu_data_link(self):
        """ Checks for the Data link in the header
        """
        self.home_page = HomePage(self.driver, self.url)
        self.home_page.is_enabled(Locators.DATA_LINK)
