import logging
from itertools import product

from config.mongo import Database
from pages.alten import Alten, ALTEN_CITIES
from pages.just_join_it import JustJoinIT, JUST_CITIES, JUST_CATEGORIES
from pages.nbc import NBC

# Logging config
log_format = '[%(asctime)s]: {%(module)s, %(funcName)s:%(lineno)d - %(message)s}'
logging.basicConfig(format=log_format, level=logging.DEBUG,
                    handlers=[logging.FileHandler('job_offers.log', 'w', 'utf-8')])

if __name__ == '__main__':

    # Prepare database
    d = Database('job', 'offers')

    # # Just join IT
    for city, category in product(JUST_CITIES, JUST_CATEGORIES):
        just = JustJoinIT(city, category)
        just.create_job_offers()
        just.print_offers()
        for offer in just.job_offers:
            d.insert_job_offer(offer)

    # Alten
    for city in ALTEN_CITIES:
        alten = Alten(city)
        alten.create_job_offers()
        alten.print_offers()
        for offer in alten.job_offers:
            d.insert_job_offer(offer)

    # NBC
    nbc = NBC('Wrocław'.encode('utf-8'))
    nbc.create_job_offers()
    nbc.print_offers()
    for offer in nbc.job_offers:
        d.insert_job_offer(offer)
