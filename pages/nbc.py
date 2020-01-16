from job_offer import JobOffer
from pages.page import Page


class NBC(Page):
    """
    Represents https://nbc.com.pl
    """

    def __init__(self, keyword):
        super().__init__()
        self.city = keyword
        self.complete_url = f'https://www.nbc.com.pl/?lang=pl&post_type=offer&s={self.city}'

    def get_job_offers(self):
        containers = self.get_job_offers_containers('div', 'col-sm-8', 'post', 'item', 'job-offer')
        for container in containers:
            title = container.select_one('h2').text

            link = container.select_one('a.link-absolute')['href']

            job_offer = JobOffer(title, 0, 0, link)

            self.job_offers.append(job_offer)


