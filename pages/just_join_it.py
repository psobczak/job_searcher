import re

from job_offer import JobOffer
from pages.page import Page

JUST_CITIES = [
    'waraszawa', 'krakow', 'wroclaw', 'poznan', 'trojmiasto', 'remote', 'world',
    'bialystok', 'bielsko-biala', 'bydgoszcz', 'czestochowa', 'gliwice', 'katowice',
    'kielce', 'lublin', 'lodz', 'olsztyn', 'opole', 'torun', 'rzeszow', 'szczecin', 'zielona_gora'
]

JUST_CATEGORIES = [
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
        if city.lower() in JUST_CITIES:
            self.city = city
        else:
            raise AttributeError(f'Attribute CITY must be one of the following: {JUST_CITIES}')
        if category.lower() in JUST_CATEGORIES:
            self.category = category
        else:
            raise AttributeError(f'Attribute CATEGORY must be one of the following: {JUST_CATEGORIES}')
        self.complete_url = f'{self.base_url}/{city}/{category}'

    def create_job_offers(self):
        """Loads pages from links, extracts data and creates JobOffer objects"""
        for container in self._get_elements_containers('li', 'offer-item', 'testing'):
            job_offer = self._get_job_offer_information(container)
            self._add_job_offer(job_offer)

    def _get_job_offer_information(self, container) -> JobOffer:
        title = container.select_one('span.title').text

        salary = container.select_one('span.salary').text
        salary_raw = re.match(r'(\d*\s\d*)\s+-\s+(\d*\s\d*)', salary)
        if salary_raw is not None:
            max_salary = int(salary_raw.group(2).replace(' ', ''))
            min_salary = int(salary_raw.group(1).replace(' ', ''))
        else:
            max_salary, min_salary = 0, 0

        employer = container.select_one('span.company-name').text.strip('\ue0af\n\n')
        address = container.select_one('span.company-address').text.strip('\ue0c8\n\n')
        link = self.base_url + container.select_one('a.item')['href']

        job_offer = JobOffer(title, 'Just join IT', link, min_salary=min_salary, max_salary=max_salary, address=address,
                             employer=employer, city=self.city, category=self.category)
        return job_offer
