from abc import ABC, abstractmethod
from re import I

from repository.Borders import Borders
from repository.storage import Database


class BordersDAO(ABC):

    db: Database;
    id: int
    geom: str
    name: str
    admin_lvl: int

    def build_borders(self):
        return Borders(id, self.geom, self.name, self.admin_lvl)
    
    def query_borders(self):
        self.db.cursor.execute("""
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