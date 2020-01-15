from job_offer import JobOffer
from pages.page import Page


class NBC(Page):
    """
    Represents https://nbc.com.pl
    """

    def __init__(self, url):
        super().__init__(url)
        self.page = self.get_page()

    def get_job_offers(self):
        containers = self.get_job_offers_containers('div', 'col-sm-8', 'post', 'item', 'job-offer')
        for container in containers:
            title = container.select_one('h2').text

            link = container.select_one('a.link-absolute')['href']

            job_offer = JobOffer(title, 0, 0, link)

            self.job_offers.append(job_offer)


n = NBC('https://www.nbc.com.pl/?lang=pl&post_type=offer&s=Wroc%C5%82aw')
n.get_job_offers()
n.print_offers()
