from psycopg2 import connect
from psycopg2.errors import ConnectionException
from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Database:

    url = None
    connection = None
    session = None

    def __init__(self, host: str, port: int, username: str, password: str, dbname: str):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.dbname = dbname
    
    def _create_URL_for_connection(self) -> str:
        self.url = URL(drivername = 'postgresql',
        username = self.username, 
        password=self.password,
        host = self.host,
        port = self.port,
        database = self.dbname)
        return self.url

    def connect_database(self):
        try:
            connection = create_engine(self._create_URL_for_connection())

        except ConnectionError as e:
            raise ConnectionException("Trying to connect to PostgreSQL aborted.")
        finally:
            self.connection = connection
    
    def create_session(self):
        if self.connection:
            Session = sessionmaker(self.connection)
            session = Session()
            self.session = session
            return self.session
    
    def close_connection(self):
        if self.session:
            self.session.close()
        if self.connection:
            self.connection.dispose()