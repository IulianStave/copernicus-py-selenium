import unittest
import sys
from src.common import common
from src.SearchAtmTestCase import SearchTest
from src.HomePageAtmTestCase import HomePageTest
from src.DataCatalogueAtmTestCase import DataCatalogueTest
from src.ProductsCatalogueAtmTestCase import ProductsCatalogueTest
from src.data.TestData import TestData

BASE_URL = 'https://atmosphere.copernicus.eu'
TESTS = [
    HomePageTest,
    SearchTest,
    DataCatalogueTest,
    ProductsCatalogueTest
]

URL_EXT = {
    HomePageTest: '',
    SearchTest: '',
    DataCatalogueTest: TestData.DATA_URL_EXT,
    ProductsCatalogueTest: TestData.CATALOGUE_URL_EXT
}

parser = common.build_cmd_arguments()
args = parser.parse_args()
driver = common.get_browser(args.browser, args.headless, args.browserpath)
resolution = (args.screenwidth, args.screenheight)
driver.set_window_size(*resolution)
home_url = args.url if args.url else BASE_URL

test_suite = unittest.TestSuite()
for test in TESTS:
    # get the available tests
    for name in test.my_tests():
        test_case = test(
            name,
            driver,
            home_url + URL_EXT[test]
            )
        test_suite.addTest(test_case)

runner = unittest.TextTestRunner(verbosity=args.verbose)
code = not runner.run(test_suite).wasSuccessful()
driver.quit()
sys.exit(code)
