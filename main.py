from aiohttp import web
from config import APP
from api.geodata import borders

def start_app():
    app = web.Application()
    app.add_routes([web.get('/borders', borders)])
    
    web.run_app(app, host = APP.ADDRESS, port = APP.PORT)

if __name__ == '__main__':
    start_app()