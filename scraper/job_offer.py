import datetime
import logging


class JobOffer:
    """
    Represents single job offer. May differ depending on the site it comes from
    """

    def __init__(self, title, source, link, minimal_salary=0, maximal_salary=0, employer="", address="", city="",
                 category=""):
        self.title = title
        self.source = source
        self.minimal_salary = minimal_salary
        self.maximal_salary = maximal_salary
        self.link = link
        self.employer = employer
        self.address = address
        self.city = city
        self.category = category
        self.posted = datetime.datetime.now().strftime('%d-%m-%Y')
        logging.info(f'Creating new instance of {self}')

    def __repr__(self):
        return f'{self.__class__.__name__}(title={self.title!r}, source={self.source!r} min_salary={self.minimal_salary!r}, ' \
               f'max_salary={self.maximal_salary!r}, link={self.link!r}, employer={self.employer!r}, address={self.address!r}, ' \
               f'city={self.city!r}, category={self.category!r})'

    def __getitem__(self, item):
        if item in vars(self).keys():
            return vars(self)[item]
        else:
            raise KeyError
