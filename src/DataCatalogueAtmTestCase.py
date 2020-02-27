from src.common.Pages import HomePage
from src.common.common import BrowserTestCase
from src.data.TestData import TestData
from src.data.Locators import Locators


class DataCatalogueTest(BrowserTestCase):
    def test_access_the_catalogue(self):
        """ Clicks on the Data Catalogue page link
        """
        self.data_page = HomePage(self.driver, self.url)
        catalogue_link = self.data_page.is_enabled(
            Locators.CATALOGUE_LINK)
        catalogue_link.click()
        self.assertTrue(
            self.driver.current_url.endswith(TestData.CATALOGUE_URL_EXT)
        )
