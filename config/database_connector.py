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
        sql = f'INSERT INTO offers(' \
              f'title, ' \
              f'source, ' \
              f'minimum_salary, ' \
              f'maximum_salary, ' \
              f'link, ' \
              f'employer, ' \
              f'address) ' \
              f'VALUES (?, ?, ?, ?, ?, ?, ?)'
        with self.CONNECTION as conn:
            try:
                if isinstance(job_offer, JobOffer):
                    aaa = tuple(attribute for attribute in vars(job_offer).values())
                    cur = conn.cursor()
                    cur.execute(sql, aaa)
            except sqlite3.IntegrityError:
                print('This job offer is already in database!')
                pass

    def create_table(self, table_name='offers'):
        sql = f'CREATE TABLE IF NOT EXISTS {table_name} (' \
              f'title TEXT NOT NULL, ' \
              f'source TEXT NOT NULL, ' \
              f'minimum_salary NUMERIC DEFAULT 0,' \
              f'maximum_salary	NUMERIC DEFAULT 0, ' \
              f'link TEXT NOT NULL, ' \
              f'employer TEXT, ' \
              f'address TEXT, ' \
              f'PRIMARY KEY("link")' \
              f')'
        with self.CONNECTION as conn:
            try:
                cursor = conn.cursor()
                cursor.execute(sql)
                print(f'Table {table_name} successfully created!')
            except sqlite3.Error:
                pass
