import unittest
import sys
from src.common import common
from src.SearchCliTestCase import SearchTest
from src.HomePageCliTestCase import HomePageTest
# from src.DataStoreTestCase import DataStoreTest


BASE_URL = 'https://climate.copernicus.eu'
TESTS = [
    HomePageTest,
    SearchTest,
    # DataStoreTest,
]

URL_EXT = {
    HomePageTest: '',
    SearchTest: '',
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
        test_case = test(name, driver, home_url + URL_EXT[test])
        test_suite.addTest(test_case)

runner = unittest.TextTestRunner(verbosity=args.verbose)
code = not runner.run(test_suite).wasSuccessful()
driver.quit()
sys.exit(code)
