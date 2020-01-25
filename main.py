from itertools import product

from config.database_connector import DatabaseConnector
from pages.alten import Alten, ALTEN_CITIES
from pages.just_join_it import JustJoinIT, JUST_CITIES, JUST_CATEGORIES
from pages.nbc import NBC

if __name__ == '__main__':

    # Prepare database
    db = DatabaseConnector()
    db.create_connection()

    # # Just join IT
    for city, category in product(JUST_CITIES, JUST_CATEGORIES):
        just = JustJoinIT(city, category)
        just.create_job_offers()
        just.print_offers()
        for offer in just.job_offers:
            db.insert_into_offers(offer)

    # Alten
    for city in ALTEN_CITIES:
        alten = Alten(city)
        alten.create_job_offers()
        alten.print_offers()
        for offer in alten.job_offers:
            db.insert_into_offers(offer)

    # NBC
    nbc = NBC('Wrocław')
    nbc.create_job_offers()
    nbc.print_offers()
    for offer in nbc.job_offers:
        db.insert_into_offers(offer)

    db.close_connection()
