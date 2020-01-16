from bs4 import BeautifulSoup as soup
import requests

from job_offer import JobOffer


class Page:
    """
    Parent class for all job offer pages
    """

    def __init__(self):
        self.complete_url = None
        self.job_offers = []

    @staticmethod
    def get_page(url):
        r = requests.get(url).text
        return soup(r, 'html.parser')

    def add_job_offer(self, job_offer):
        if isinstance(job_offer, JobOffer):
            self.job_offers.append(job_offer)
        else:
            raise TypeError(f'Can not add {type(job_offer)} to page\'s job offers')

    def get_job_offers_containers(self, tag, *args):
        page = self.get_page(self.complete_url)
        return page.find_all(tag, [*args])

    def __len__(self):
        return len(self.job_offers)

    def __getitem__(self, item):
        return self.job_offers[item]

    def __repr__(self):
        return f'{self.__class__.__name__}, job offers - {self.__len__()}'

    def get_job_offers(self):
        ...

    def print_offers(self):
        source = len(self.__class__.__name__)
        padding = int((120 - source - 2) / 2)

        print('-' * padding, self.__class__.__name__, '-' * padding)
        for i, job_offer in enumerate(self.job_offers):
            print(f'{i + 1}. {job_offer}')
