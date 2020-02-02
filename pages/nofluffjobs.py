from job_offer import JobOffer
from pages.page import Page

FLUFF_CITIES = ['remote', 'warszawa', 'wroclaw', 'gdansk', 'poznan', 'trojmiasto', 'slask', 'lodz', 'katowice',
                'lublin', 'szczecin', 'bydgoszcz', 'bialystok', 'gdynia', 'gliwice', 'sopot']

FLUFF_CATEGORIES = ['backend', 'frontend', 'fullstack', 'mobile', 'testing', 'devops']


class NoFluffJobs(Page):

    def __init__(self, city, category, driver):
        super().__init__(driver=driver)
        if city.lower() in FLUFF_CITIES:
            self.city = city
        else:
            raise AttributeError(f'Attribute CITY must be one of the following: {FLUFF_CITIES}')
        if category.lower() in FLUFF_CATEGORIES:
            self.category = category
        else:
            AttributeError(f'Attribute CATEGORY must be one of the following: {FLUFF_CATEGORIES}')
        self.base_url = 'https://nofluffjobs.com/'
        self.complete_url = f'{self.base_url}/jobs/{self.city}/{self.category}?criteria=city%3D{self.city}%20category%3D{self.category}'

    def create_job_offers(self):
        containers = self._get_elements_containers('div', 'list-item')
        for container in containers:
            job_offer = self._get_job_offer_information(container)
            self._add_job_offer(job_offer)

    def _get_job_offer_information(self, container) -> JobOffer:
        title = container.select_one('h4.posting-title__position').text
        link = self.base_url + container.select_one('a.posting-list-item')['href']
        employer = container.select_one('span.posting-title__company').text.strip()[3:]
        return JobOffer(title, 'NoFluffJobs', link, city=self.city, category=self.category, employer=employer)
