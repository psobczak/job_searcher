from job_offer import JobOffer
from pages.page import Page


class NBC(Page):
    """
    Represents https://nbc.com.pl
    """

    def __init__(self, city):
        super().__init__()
        self.city = city
        self.complete_url = f'https://www.nbc.com.pl/?lang=pl&post_type=offer&s={self.city}'

    def create_job_offers(self):
        containers = self._get_elements_containers('div', 'col-sm-8', 'post', 'item', 'job-offer')
        for container in containers:
            job_offer = self._get_job_offer_information(container)
            self._add_job_offer(job_offer)

    def _get_job_offer_information(self, container) -> JobOffer:
        title = container.select_one('article.text-center.animate-this > h2').text
        link = container.select_one('article.text-center.animate-this > a')['href']
        return JobOffer(title, 'NBC', link)
