from aiohttp import web
from config import APP
from api.geodata import struve_lines, struve_points

def start_app():
    app = web.Application()
    app.add_routes([web.get('/struve_lines', struve_lines),
                    web.get('/struve_points', struve_points)])
    
    web.run_app(app, host = APP.ADDRESS, port = APP.PORT)

if __name__ == '__main__':
    start_app()