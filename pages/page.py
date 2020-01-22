import logging

import requests
from bs4 import BeautifulSoup as soup

from job_offer import JobOffer


class Page:
    """
    Parent class for all job offer pages
    """

    def __init__(self):
        self.complete_url = None
        self.job_offers = []
        self.city = ""
        self.category = ""
        logging.info(f'Creating {str(self)}')

    @staticmethod
    def _get_page(url, driver=None):
        """
        Reads website url and returns parsed HTML code
        :param url: str
        :param driver: WebDriver
        :return: bs4 parsed HTML code
        """
        if driver is not None:
            r = driver.get_page_source(url)
        else:
            r = requests.get(url).text
            logging.info(f'Parsing and returning HTML content of {url}')
        return soup(r, 'html.parser')

    def _add_job_offer(self, job_offer):
        """
        Adds job offer to list of job offers
        :param job_offer: JobOffer
        :return: JobOffer[]
        """
        if isinstance(job_offer, JobOffer):
            self.job_offers.append(job_offer)
            logging.info(f'Added {str(job_offer)} to list of job offers')
        else:
            raise TypeError(f'Can not add {type(job_offer)} to page\'s job offers')

    def _get_elements_containers(self, tag, *args):
        """
        Returns list of HTML nodes
        :param tag: HTML tag
        :param args: CSS classes
        :return: List of HTML nodes
        """
        page = self._get_page(self.complete_url)
        return page.find_all(tag, class_=[*args])

    def _find_job_offer_links(self):
        """
        Extracts job offer links from containers. Returns a list of links
        :return: List of https links
        """
        ...

    def create_job_offers(self):
        ...

    def print_offers(self):
        """Prints job offers. Includes a nicely formatted header for every page"""
        source = len(f'{self.__class__.__name__} - {self.city} {self.category}')
        padding = int((120 - source - 2) / 2)
        header = '-' * padding, self.__class__.__name__, '-' * padding

        print('-' * padding, f' {self.__class__.__name__} - {self.city} {self.category}', '-' * padding)
        if len(self.job_offers) != 0:
            for i, job_offer in enumerate(self.job_offers):
                print(f'{i + 1}. {job_offer}')
        else:
            print('-' * padding, 'no offers found', '-' * padding)

    def __len__(self):
        return len(self.job_offers)

    def __getitem__(self, item):
        return self.job_offers[item]

    def __repr__(self):
        return f'{self.__class__.__name__}, job offers - {self.__len__()}'
