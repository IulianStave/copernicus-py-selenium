from src.common.Pages import HomePage
from src.common.common import BrowserTestCase
from src.data.TestData import TestData
from src.data.Locators import Locators


class SearchTest(BrowserTestCase):
    def test_search_by_text(self):
        """ Clicks the search toggle, perform search, asserts counter works
        """
        self.home_page = HomePage(self.driver, self.url)
        self.search_toggle = self.home_page.is_enabled(
            Locators.SEARCH_TOGGLE)
        self.search_toggle.click()
        self.search_input = self.home_page.is_enabled(
            Locators.SEARCH_INPUT)
        self.search_input.clear()
        # enter search keyword and submit
        self.search_input.send_keys(TestData.SEARCH_TEXT_ATM)
        self.search_input.submit()
        # get the list of elements displayed after the search
        results = self.home_page.get_elements(Locators.SEARCH_RESULTS)
        self.header = self.home_page.is_enabled(Locators.SEARCH_RESULTS_HEADER)
        first_page_results_count = int(self.header.text.split()[3])
        self.assertEqual(len(results), first_page_results_count)
