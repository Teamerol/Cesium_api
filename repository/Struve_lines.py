from sqlalchemy import Column, Integer
from geoalchemy2 import Geometry
from sqlalchemy.ext.declarative import declarative_base
from geoalchemy2.functions import ST_AsGeoJSON
from sqlalchemy.dialects.postgresql import JSON


Base = declarative_base()

class Struve_lines(Base):
    __tablename__ = "Struve_lines"
    
    id = Column("id", Integer, primary_key=True)
    geom = Column("geom", Geometry("LINESTRING", srid=4326))
    uuid = Column("uuid", Integer)
    tartu_spb = Column("tartu_spb", Integer)
    geom_json = Column("geom_json", JSON)