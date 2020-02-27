from src.common.Pages import HomePage
from src.common.common import BrowserTestCase
from src.data.Locators import Locators


class ProductsCatalogueTest(BrowserTestCase):
    def test_catalogue_search_links(self):
        """ Clicks on the first product listed in Catalogue page
            Asserts the image alt corresponds to the first product title
            when clicked on
        """
        self.catalogue_page = HomePage(self.driver, self.url)
        first_product_elem = self.catalogue_page.is_visible(
            Locators.TOP_PRODUCT)
        self.catalogue_page.click(Locators.TOP_PRODUCT)
        first_product_title = first_product_elem.text
        self.catalogue_page.switch_to_new_window()
        image_element = self.catalogue_page.is_enabled(Locators.CATALOGUE_IMG)
        image_alt = " ".join(image_element.get_attribute('alt').split())
        self.assertEqual(first_product_title, image_alt)
