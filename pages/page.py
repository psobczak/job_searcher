import logging

from bs4 import BeautifulSoup as soup

from job_offer import JobOffer
from webdriver import WebDriver


class Page:
    """
    Parent class for all job offer pages
    """

    def __init__(self):
        self.complete_url = None
        self.job_offers = []
        self.driver = WebDriver()
        logging.info(f'Creating {str(self)}')

    def _get_page(self, url):
        r = self.driver.get_page_source(url)
        logging.info(f'Parsing and returning HTML content of {url}')
        return soup(r, 'html.parser')

    def add_job_offer(self, job_offer):
        if isinstance(job_offer, JobOffer):
            self.job_offers.append(job_offer)
            logging.info(f'Added {str(job_offer)} to list of job offers')
        else:
            raise TypeError(f'Can not add {type(job_offer)} to page\'s job offers')

    def get_job_offers_containers(self, tag, *args):
        # TODO Figure how to get only exact matches with container classes
        page = self._get_page(self.complete_url)
        return page.find_all(tag, *args)

    def _find_job_offer_links(self):
        ...

    def get_job_offers(self):
        ...

    def print_offers(self):
        """Prints job offers. Includes a nicely formatted header for every page"""
        source = len(self.__class__.__name__)
        padding = int((120 - source - 2) / 2)
        header = '-' * padding, self.__class__.__name__, '-' * padding

        print('-' * padding, self.__class__.__name__, '-' * padding)
        if len(self.job_offers) != 0:
            for i, job_offer in enumerate(self.job_offers):
                print(f'{i + 1}. {job_offer}')
        else:
            print('*' * padding, 'no offers found', '*' * padding)

    def __len__(self):
        return len(self.job_offers)

    def __getitem__(self, item):
        return self.job_offers[item]

    def __repr__(self):
        return f'{self.__class__.__name__}, job offers - {self.__len__()}'
