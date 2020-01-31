from job_offer import JobOffer
from pages.page import Page


class NoFluffJobs(Page):
    def __init__(self, city, category, driver):
        super().__init__(driver=driver)
        self.city = city
        self.category = category
        self.base_url = 'https://nofluffjobs.com/'
        self.complete_url = f'{self.base_url}/jobs/{self.city}/{self.category}?criteria=city%3D{self.city}%20category%3D{self.category}'

    def create_job_offers(self):
        containers = self._get_elements_containers('div', 'list-item')
        for container in containers:
            job_offer = self._get_job_offer_information(container)
            self._add_job_offer(job_offer)

    def _get_job_offer_information(self, container) -> JobOffer:
        title = container.select_one('h4.posting-title__position').text
        link = self.base_url + container.select_one('a.posting-list-item.posting-list-item--testing')['href']
        return JobOffer(title, 'NoFluffJobs', link, city=self.city, category=self.category)
