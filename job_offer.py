import datetime
import logging


class JobOffer:
    """
    Represents single job offer. May differ depending on the site it comes from
    """

    def __init__(self, title, source, link, min_salary=0, max_salary=0, employer="", address="", city="", category=""):
        self.title = title
        self.source = source
        self.min = min_salary
        self.max = max_salary
        self.link = link
        self.employer = employer
        self.address = address
        self.city = city
        self.category = category
        self.posted = datetime.datetime.now().strftime('%d-%m-%Y')
        logging.info(f'Creating new instance of {self}')

    def __repr__(self):
        return f'{self.__class__.__name__}(title={self.title!r}, source={self.source!r} min_salary={self.min!r}, ' \
               f'max_salary={self.max!r}, link={self.link!r}, employer={self.employer!r}, address={self.address!r}, ' \
               f'city={self.city!r}, category={self.category!r}) '
