from bs4 import BeautifulSoup as soup
import requests

from job_offer import JobOffer


class Page:
    """
    Parent class for all job offer pages
    """

    def __init__(self, url):
        self.url = url
        self.job_offers = []

    def get_page(self):
        r = requests.get(self.url).text
        return soup(r, 'html.parser')

    def add_job_offer(self, job_offer):
        if isinstance(job_offer, JobOffer):
            self.job_offers.append(job_offer)
        else:
            raise TypeError(f'Can not add {type(job_offer)} to page\'s job offers')

    def __len__(self):
        return len(self.job_offers)

    def __getitem__(self, item):
        return self.job_offers[item]

    def __repr__(self):
        return f'{self.__class__.__name__}, job offers - {self.__len__()}'

    def get_job_offers_containers(self, tag, *args):
        page = self.get_page()
        return page.find_all(tag, [*args])

    def get_job_offers(self):
        ...

    def print_offers(self):
        for i, job_offer in enumerate(self.job_offers):
            print(f'{i+1}. {job_offer}')
