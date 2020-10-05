import psycopg2

class DatabaseConnection(object):
    """
    Class for creating instances of Database connection object
    """
    def __init__(self, host, port, db, user, password):
        self.host = host
        self.port = port
        self.db = db
        self.user = user
        self.password = password


    def get_connection(self):
        try:
            db = psycopg2.connect(
                host=self.host,
                port=self.port,
                database=self.db,
                user=self.user,
                password=self.password
                )
            cursor = db.cursor()
        except(Exception, psycopg2.Error):
            print("Encounter exception while attempting to connect to PostgreSQL")
        return db, cursor
    
    def close_connection(self, cursor, db):
        cursor.close()
        db.close()