from sqlalchemy import Column, Integer, String, Numeric
from geoalchemy2 import Geometry
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import JSON


Base = declarative_base()

class Struve_points(Base):
    __tablename__ = "Struve_points"

    id = Column("id", Integer, primary_key=True)
    geom = Column("geom", Geometry("POINT", srid=4326))
    no = Column("no", Integer)
    no_by_stru = Column("no_by_stru", Integer)
    no_of_tria = Column("no_of_tria", String)
    name_by_st = Column("name_by_st", String)
    alt_names = Column("alt_names", String)
    lat_dms = Column("lat_dms", String)
    lat_dec = Column("lat_dec", Numeric)
    lon_dms = Column("lon_dms", String)
    lon_dec = Column("lon_dec", Numeric)
    country_en = Column("country_en", String)
    unesco = Column("unesco", Integer)
    right_labe = Column("right_labe", Integer)
    astronomic = Column("astronomic", Integer)
    geom_json = Column("geom_json", JSON)