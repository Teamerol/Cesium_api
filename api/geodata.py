from aiohttp import web
from repository.storage import Database
from config import DB


def borders(request: web.Request) -> web.Response:
    db = Database(DB.HOSTNAME, DB.PORT, DB.USERNAME, DB.PASSWORD, DB.NAME)
    connection = db.connect_database()
    cursor = db.create_cursor()

    borders = db.fetch_borders()

    db.close_connection()
    return web.json_response(borders)