import logging

from pymongo import MongoClient

from job_offer import JobOffer


class Database:
    def __init__(self, database_name, collection):
        self.client = MongoClient()
        self.db = self.client.get_database(database_name)
        self.collection = self.db.get_collection(collection)
        self.counters = self.db.get_collection('counters')
        logging.info(f'Creating connection to the database')

    def get_collection(self):
        return self.collection

    def increment_id(self):
        doc = self.counters.find_and_modify(query={'_id': 'offer_id'}, update={'$inc': {'id_value': 1}})
        return doc['id_value']

    def insert_job_offer(self, job_offer: JobOffer):
        logging.info(f'Inserting {str(job_offer)} into database')
        in_table = self.get_collection().find({'link': job_offer['link']}).count()
        if in_table > 0:
            logging.info(f'This offer is already in database')
        else:
            offer = {
                '_id': self.increment_id(),
                'title': job_offer['title'],
                'source': job_offer['source'],
                'link': job_offer['link'],
                'minimal_salary': job_offer['minimal_salary'],
                'maximal_salary': job_offer['maximal_salary'],
                'employer': job_offer['employer'],
                'address': job_offer['address'],
                'city': job_offer['city'].lower(),
                'category': job_offer['category'],
                'posted': job_offer['posted']
            }
            self.get_collection().insert_one(offer)
