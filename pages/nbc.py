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
        self.job_offer_links = self._find_job_offer_links()

    def create_job_offers(self):
        for link in self.job_offer_links:
            page = self._get_page(link)

            title = page.select_one('h1.banner-title').text
            min_salary = 0
            max_salary = 0

            job_offer = JobOffer(title, min_salary, max_salary, link)
            self.job_offers.append(job_offer)

    def _find_job_offer_links(self):
        """Extracts job offer links from containers. Returns a list of links"""
        links = []
        job_offer_containers = self._get_elements_containers('div', 'col-sm-8', 'post', 'item', 'job-offer')
        for container in job_offer_containers:
            link = container.select_one('a.link-absolute')['href']
            links.append(link)
        return links
