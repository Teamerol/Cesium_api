from typing import Union
from aiohttp import web
from repository.storage import Database
from config import DB
from repository.Struve_lines import Struve_lines
from repository.Struve_points import Struve_points
from json import dumps
from decimal import Decimal


def create_database_session() -> tuple[Database, Database.session]:
    db = Database(DB.HOSTNAME, DB.PORT, DB.USERNAME, DB.PASSWORD, DB.NAME)
    db.connect_database()
    session = db.create_session()
    return db, session

def generate_json_struve_lines(feature: Struve_lines, session) -> dict:
    json = {
        "type": "FeatureCollection",
        "name": feature.__tablename__,
        "crs": {
            "type": "name",
            "properties": {
                "name": "urn:ogc:def:crs:OGC:1.3:CRS84"
            },
        "features": None
        }
    }

    features_list = []

    for feature in session.query(feature):
        features = {"type": "Feature"}
        non_geometry = {"id": feature.id, "uuid": feature.uuid, "tartu_spb": feature.tartu_spb}
        features["properties"] = non_geometry
        features["geometry"] = feature.geom_json
        features_list.append(features)
        
    json["features"] = features_list

    return json

def generate_json_struve_points(feature: Struve_points, session) -> dict:
    json = {
        "type": "FeatureCollection",
        "name": feature.__tablename__,
        "crs": {
            "type": "name",
            "properties": {
                "name": "urn:ogc:def:crs:OGC:1.3:CRS84"
            },
        "features": None
        }
    }

    features_list = []

    for feature in session.query(feature):
        features = {"type": "Feature"}
        non_geometry =  {"id": feature.id, "no": feature.no, "no_by_stru": feature.no_by_stru, "no_of_tria": feature.no_of_tria,
        "name_by_st": feature.name_by_st, "alt_names": feature.alt_names, "lat_dms": feature.lat_dms, "lat_dec": feature.lat_dec,
        "lon_dms": feature.lon_dms, "lon_dec": feature.lon_dec, "country_en": feature.country_en, "unesco": feature.unesco,
        "right_labe": feature.right_labe, "astronomic": feature.astronomic}
        features["properties"] = non_geometry
        features["geometry"] = feature.geom_json
        features_list.append(features)
        
    json["features"] = features_list

    return json

def json_default(obj: object) -> Union[float, str]:
    if isinstance(obj, Decimal):
        return float(obj)
    return str(obj)

def struve_lines(request: web.Request) -> web.Response:

    db, session = create_database_session()
    json = generate_json_struve_lines(feature = Struve_lines, session = session)
    db.close_connection()

    return web.json_response(json, headers = {"Access-Control-Allow-Origin" : "*"})

def struve_points(request: web.Request) -> web.Response:

    db, session = create_database_session()
    json = generate_json_struve_points(feature = Struve_points, session = session)

    db.close_connection()

    return web.json_response(json, headers = {"Access-Control-Allow-Origin" : "*"},
                            dumps = dumps(json, default = json_default))