import re

from job_offer import JobOffer
from pages.page import Page
from webdriver import WebDriver

ALLOWED_CITIES = [
    'waraszawa', 'krakow', 'wroclaw', 'poznan', 'trojmiasto', 'remote', 'world',
    'bialystok', 'bielsko-biala', 'bydgoszcz', 'czestochowa', 'gliwice', 'katowice',
    'kielce', 'lublin', 'lodz', 'olsztyn', 'opole', 'torun', 'rzeszow', 'szczecin', 'zielona_gora'
]

ALLOWED_CATEGORIES = [
    'javascript', 'hmtl', 'php', 'ruby', 'python', 'java', 'net', 'scala', 'c', 'mobile', 'testing', 'devops', 'ux',
    'pm', 'game', 'blockchain', 'security', 'data', 'golang', 'sap', 'other'
]


class JustJoinIT(Page):
    """
    Represents https://justjoin.it
    """

    def __init__(self, city, category):
        super().__init__()
        self.base_url = 'https://justjoin.it'
        if city.lower() in ALLOWED_CITIES:
            self.city = city
        else:
            raise AttributeError(f'Attribute CITY must be one of the following: {ALLOWED_CITIES}')
        if category.lower() in ALLOWED_CATEGORIES:
            self.category = category
        else:
            raise AttributeError(f'Attribute CATEGORY must be one of the following: {ALLOWED_CATEGORIES}')
        self.complete_url = f'{self.base_url}/{city}/{category}'
        self.job_offer_links = self._find_job_offer_links()
        self.driver = WebDriver()

    def _find_job_offer_links(self):
        """Extracts job offer links from containers. Returns a list of links"""
        links = []
        job_offer_containers = self._get_elements_containers('li', 'offer-item', 'testing')
        for container in job_offer_containers:
            link = container.select_one('a.item')['href']
            link = self.base_url + link
            links.append(link)
        return links

    def create_job_offers(self):
        """Loads pages from links, extracts data and creates JobOffer objects"""
        for link in self.job_offer_links:
            page = self._get_page(link, self.driver)

            title = page.select_one('span.title').text

            # Use re to match max and min salary - eg. 7 000 - 14 000
            salary = page.select_one('span.salary').text
            salary_raw = re.match('(\d*\s\d*)\s+-\s+(\d*\s\d*)', salary)
            if salary_raw is not None:
                max_salary = salary_raw.group(2)
                min_salary = salary_raw.group(1)
            else:
                max_salary, min_salary = 0, 0

            job_offer = JobOffer(title, min_salary, max_salary, link)
            self.job_offers.append(job_offer)
        self.driver.quit_driver()
        return None
