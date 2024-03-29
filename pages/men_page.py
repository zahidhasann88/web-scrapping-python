from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MenPage:
    MEN_PAGE_URL: str = "https://shop.adidas.jp/men"
    ALL_MEN_TEXT: tuple[str, str] = (By.XPATH, "//a[@data-ga-event-label='mens-all']")

    def __init__(self, driver):
        self.driver = driver

    def go_to_men_page(self):
        self.driver.get(self.MEN_PAGE_URL)

    def go_to_all_men_page(self):
        try:
            all_men_element = WebDriverWait(self.driver, 60).until(
                EC.element_to_be_clickable(self.ALL_MEN_TEXT)
            )
            all_men_element.click()
        except Exception as e:
            print(f"Error while navigating to all men's page: {e}")
