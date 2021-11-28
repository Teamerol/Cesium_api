from psycopg2 import connect
from psycopg2.errors import ConnectionException


class Database:

    connection = None
    cursor = None
    borders = None

    def __init__(self, host: str, port: int, username: str, password: str, dbname: str):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.dbname = dbname

    def connect_database(self):
        try:
            connection = connect(
            host = self.host,
            port = self.port,
            user = self.username,
            password = self.password,
            dbname = self.dbname
            )

        except ConnectionError as e:
            raise ConnectionException("Trying to connect to PostgreSQL aborted.")
        finally:
            self.connection = connection
    
    def create_cursor(self):
        if self.connection:
            cur = self.connection.cursor()
            self.cursor = cur
    
    def close_connection(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
    
    def fetch_borders(self):
        if self.cursor:
            self.cursor.execute("""
    SELECT jsonb_build_object(
    'type',     'FeatureCollection',
    'features', jsonb_agg(features.feature)
    )
    FROM (
	  SELECT jsonb_build_object(
		'type',       'Feature',
		'id',         id,
		'geometry',   ST_AsGeoJSON(geom)::jsonb,
		'properties', to_jsonb(inputs) - 'id' - 'geom'
	  ) AS feature
	  FROM (SELECT id, geom, name, admin_lvl FROM "Komi_district_borders") 
	inputs) 
	features
        """)
    
            
            return self.cursor.fetchone()