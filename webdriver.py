from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class WebDriver:
    """
    This class is responsible for creating and managing webdriver instances
    """

    def __init__(self):
        self.driver = self._prepare_webdriver()

    @staticmethod
    def _prepare_webdriver():
        chrome_options = Options()
        chrome_options.headless = True
        return webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)

    def get_driver(self):
        return self.driver

    def close_driver(self):
        self.driver.close()
        return None

    def quit_driver(self):
        self.driver.quit()
        return None

    def get_page_source(self, url: str) -> str:
        try:
            self.driver.get(url)
            return self.driver.page_source
        except:
            ...
