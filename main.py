from database_connector import DatabaseConnector
from pages.alten import Alten
from pages.just_join_it import JustJoinIT
from pages.nbc import NBC
from webdriver import WebDriver

if __name__ == '__main__':

    # Prepare database
    db = DatabaseConnector()
    db.create_connection()

    # Just join IT
    driver = WebDriver()
    just = JustJoinIT('wroclaw', 'testing', driver=driver)
    just.create_job_offers()

    # Alten
    alten = Alten('wroclaw')
    alten.create_job_offers()

    # NBC
    nbc = NBC('Wroclaw')
    nbc.create_job_offers()

    for offer in just.job_offers:
        db.insert_into_offers(offer)

    for offer in alten.job_offers:
        db.insert_into_offers(offer)

    for offer in nbc.job_offers:
        db.insert_into_offers(offer)

    db.close_connection()
