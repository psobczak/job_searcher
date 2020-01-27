import logging
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
        self.create_table()
        self.skipped = 0

    def create_connection(self):
        if self.CONNECTION is None:
            try:
                self.CONNECTION = sqlite3.connect(self.DATABASE_PATH)
                logging.info(f'Connection to database established')
            except ConnectionError:
                logging.info('Connection could not be established')
        return self.CONNECTION

    def close_connection(self):
        if self.CONNECTION is not None:
            self.CONNECTION.close()
            self.CONNECTION = None
            logging.info('Connection closed')
        return self.CONNECTION

    def insert_into_offers(self, job_offer):
        sql = f'INSERT INTO offers(' \
              f'title, ' \
              f'source, ' \
              f'minimum_salary, ' \
              f'maximum_salary, ' \
              f'link, ' \
              f'employer, ' \
              f'address,' \
              f'city,' \
              f'category,' \
              f'posted) ' \
              f'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
        with self.CONNECTION as conn:
            try:
                if isinstance(job_offer, JobOffer):
                    job_offer = tuple(attribute for attribute in vars(job_offer).values())
                    cur = conn.cursor()
                    cur.execute('SELECT rowid FROM offers where link = ? and city = ? and category = ?',
                                (job_offer[4], job_offer[7], job_offer[8]))
                    data = cur.fetchone()
                    if data is None:
                        cur.execute(sql, job_offer)
                    else:
                        logging.info(
                            f'Row with link={job_offer[4]}, city={job_offer[7]} and category={job_offer[8]} is'
                            f' already in database')
                        pass
            except sqlite3.IntegrityError:
                logging.info(f'{job_offer} is already in database!')
                pass

    def create_table(self, table_name='offers'):
        sql = f'CREATE TABLE IF NOT EXISTS {table_name} (' \
              f'title TEXT NOT NULL, ' \
              f'source TEXT NOT NULL, ' \
              f'minimum_salary NUMERIC DEFAULT 0,' \
              f'maximum_salary	NUMERIC DEFAULT 0, ' \
              f'link TEXT NOT NULL, ' \
              f'employer TEXT, ' \
              f'address TEXT,' \
              f'city TEXT,' \
              f'category TEXT,' \
              f'posted DATE,' \
              f'PRIMARY KEY("link")' \
              f')'
        with self.CONNECTION as conn:
            try:
                cursor = conn.cursor()
                cursor.execute(sql)
                logging.info(f'Table {table_name} successfully created!')
            except sqlite3.Error:
                pass
