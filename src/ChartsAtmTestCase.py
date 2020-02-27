from src.common.Pages import HomePage
from src.common.common import BrowserTestCase
from src.data.Locators import Locators


class ChartsTest(BrowserTestCase):
    def test_charts_image(self):
        """ Checks for the Forecast charts link and image 
        """
        self.home_page = HomePage(self.driver, self.url)
        link_to_charts_element = self.home_page.click(Locators.CHARTS_LINK)
        self.assertTrue(
            link_to_charts_element,
            'Link to forecast charts not found'
            )
        # self.home_page.switch_to_new_window()
        image_element = self.home_page.is_visible(Locators.CHART_IMAGE)
        self.assertTrue(
            image_element,
            'Image on the forecast chart detail page not found'
            )
