from selenium.webdriver.common.by import By


class Locators():
    # --- Home Page Locators ---
    SEARCH_TOGGLE = (By.CLASS_NAME, 'search-toggle.search-label')
    HOME_CARD = (By.CLASS_NAME, 'card--inner > h3')
    SEARCH_INPUT = (By.ID, 'edit-search-api-fulltext')
    # Search results page locators
    SEARCH_RESULTS_HEADER = (By.CSS_SELECTOR, 'div.search--listing > header')
    SEARCH_RESULTS = (By.CLASS_NAME, 'views-row')
    SEARCH_SUBMIT_BUTTON = (By.ID, 'edit-submit-sitewide-search')
    # Data locators
    DATA_LINK = (By.LINK_TEXT, 'DATA')
    CATALOGUE_LINK = (By.LINK_TEXT, 'Access the catalogue')
    # catalogue page locators
    CATALOGUE_PRODUCTS = (By.CLASS_NAME, 'product-details')
    TOP_PRODUCT = (By.CSS_SELECTOR, 'div.product-details > h3 > a')
    CATALOGUE_IMG = (By.CSS_SELECTOR, 'div.item-box > div.item-image > img')
