import abc
import logging

import requests
from bs4 import BeautifulSoup as soup
from job_offer import JobOffer
from selenium.webdriver.common.by import By


class Page(abc.ABC):
    """
    Parent class for all job offer pages
    """

    def __init__(self, driver=None):
        self.complete_url = None
        self.job_offers = []
        self.city = ""
        self.category = ""
        self.driver = driver
        logging.info(f'Creating {self.__class__.__name__}')

    def _get_page(self, url, locator=None):
        """
        Reads website url and returns parsed HTML code
        :param url: str
        :return: bs4 parsed HTML code
        """
        if self.driver is not None:
            r = self.driver.get_page_source(url, locator)
        else:
            r = requests.get(url).text
            logging.info(f'Parsing and returning HTML content of {self}')
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
        page = self._get_page(self.complete_url, (By.CSS_SELECTOR, 'div.list-item'))
        logging.info(f'Finding all elements with tag {tag} and classes {[*args]}')
        return page.find_all(tag, class_=[*args])

    @abc.abstractmethod
    def _get_job_offer_information(self, container) -> JobOffer:
        """This method is meant to be overwritten by extending classes"""
        ...

    def print_offers(self):
        """Prints job offers. Includes a nicely formatted header for every page"""
        if self.category:
            header = f'| {self.__class__.__name__} | {self.city.title()} | {self.category.title()} |'
        else:
            header = f'| {self.__class__.__name__} | {self.city.title()} |'

        total_length = 100
        padding = (total_length - len(header)) // 2

        print(padding * '-', header, padding * '-')

        if len(self.job_offers) != 0:
            for i, job_offer in enumerate(self.job_offers):
                print(f'{i + 1}. {job_offer}'.encode('utf-8'))

    def __len__(self):
        return len(self.job_offers)

    def __getitem__(self, item):
        return self.job_offers[item]

    def __repr__(self):
        return f'{self.__class__.__name__} with {vars(self)}'
