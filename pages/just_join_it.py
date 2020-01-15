from job_offer import JobOffer
from pages.page import Page
import re


class JustJoinIT(Page):
    """
    Represents https://justjoinit.pl
    """

    def __init__(self, url):
        super().__init__(url)
        self.page = self.get_page()
        self.base_url = 'https://justjoinit.pl'

    def get_job_offers(self):
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


j = JustJoinIT('https://justjoin.it/wroclaw/testing')
# print(len(j.get_job_offers_containers()))

j.get_job_offers()

j.print_offers()
