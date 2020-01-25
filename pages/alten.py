from job_offer import JobOffer
from pages.page import Page

ALLOWED_CITIES = ['warszawa', 'krakow', 'wroclaw', 'trojmiasto', 'slaks', 'poznan', 'remote', 'inne']


class Alten(Page):
    """Represents https://altenpolska.pl"""

    def __init__(self, city):
        super().__init__()
        if city in ALLOWED_CITIES:
            self.city = city
            self.complete_url = f'https://www.altenpolska.pl/kariera/oferty-pracy-{city}/'
        else:
            raise AttributeError(f'Attribute CITY must be one of the following: {ALLOWED_CITIES}')
        self.job_offer_links = self._find_job_offer_links()

    def _find_job_offer_links(self):
        links = []
        for container in self._get_elements_containers('div', 'elementor-post__card'):
            link = container.select_one('h3.elementor-post__title > a')['href']
            links.append(link)
        return links

    def create_job_offers(self):
        for link in self.job_offer_links:
            page = self._get_page(link)

            try:
                title = page.select_one('h3.elementor-icon-box-title > span').text
                min_salary = 0
                max_salary = 0
                job_offer = JobOffer(title, 'alten', min_salary, max_salary, link)
                self._add_job_offer(job_offer)
            except AttributeError:
                pass
        return self
