from job_offer import JobOffer
from pages.page import Page
import re


class JustJoinIT(Page):
    """
    Represents https://justjoin.it
    """

    def __init__(self, city, category):
        super().__init__()
        self.base_url = 'https://justjoin.it'
        self.city = city
        self.category = category
        self.complete_url = f'{self.base_url}/{city}/{category}'

    def get_job_offers(self):
        """ Finds job offers containers, create JobOffer objects and adds them to the page object"""
        for container in self.get_job_offers_containers('li', 'offer-item', 'testing'):
            title = container.select_one('span.title').text

            # Use re to match max and min salary
            salary = container.select_one('span.salary').text
            salary_raw = re.match('(\d*\s\d*)\s+-\s+(\d*\s\d*)', salary)
            if salary_raw is not None:
                max_salary = salary_raw.group(2)
                min_salary = salary_raw.group(1)
            else:
                max_salary, min_salary = 0, 0

            # Add base_url and link to form complete link
            link = container.select_one('a.item')['href']
            link = self.base_url + link

            job_offer = JobOffer(title, min_salary, max_salary, link)
            self.job_offers.append(job_offer)



