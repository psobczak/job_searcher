import sqlite3

from job_offer import JobOffer


class DatabaseConnector:
    """
    Responsible for all database related things
    """

    DATABASE_PATH = "job_searcher.sqlite"
    CONNECTION = None

    def __init__(self):
        self.path = self.DATABASE_PATH
        self.connection = self.create_connection()

    def create_connection(self):
        if self.CONNECTION is None:
            try:
                self.CONNECTION = sqlite3.connect(self.DATABASE_PATH)
                print('Connection established')
            except ConnectionError:
                print('Connection could not be established')
        return self.CONNECTION

    def close_connection(self):
        if self.CONNECTION is not None:
            self.CONNECTION.close()
            self.CONNECTION = None
            print('Connection closed')
        return self.CONNECTION

    def insert_into_offers(self, job_offer):
        sql = 'INSERT INTO offers(title, source, minimum_salary, maximum_salary, link) VALUES (?, ?, ?, ?, ?)'
        with self.CONNECTION as conn:
            try:
                if isinstance(job_offer, JobOffer):
                    job_offer_atrs = vars(job_offer)
                    job_offer_sql = (job_offer_atrs['title'],
                                     job_offer_atrs['source'],
                                     job_offer_atrs['min'],
                                     job_offer_atrs['max'],
                                     job_offer_atrs['link'])
                    cur = conn.cursor()
                    cur.execute(sql, job_offer_sql)
            except sqlite3.IntegrityError:
                print('This job offer is already in database!')
                pass
