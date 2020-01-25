from job_offer import JobOffer
from pages.page import Page

ALTEN_CITIES = ['warszawa', 'krakow', 'wroclaw', 'trojmiasto', 'slaks', 'poznan', 'remote', 'inne']


class Alten(Page):
    """Represents https://altenpolska.pl"""

    def __init__(self, city):
        super().__init__()
        if city.lower() in ALTEN_CITIES:
            self.city = city
            self.complete_url = f'https://www.altenpolska.pl/kariera/oferty-pracy-{city}/'
        else:
            raise AttributeError(f'Attribute CITY must be one of the following: {ALTEN_CITIES}')

    def create_job_offers(self):
        containers = self._get_elements_containers('div', 'elementor-post__card')
        for container in containers:
            try:
                job_offer = self._get_job_offer_information(container)
                self._add_job_offer(job_offer)
            except AttributeError:
                print('Unsupported container type')
                pass

    def _get_job_offer_information(self, container):
        title = container.select_one('h3.elementor-post__title > a').text.strip()
        link = container.select_one('h3.elementor-post__title > a')['href']
        address = container.select_one('div.elementor-post__excerpt > p').text.split('\n')[1].split(' ')[0]

        return JobOffer(title, 'Alten', link, address=address)
