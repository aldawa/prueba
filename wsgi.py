# aiohttpdemo_polls/main.py
from aiohttp import web
from routes import setup_routes
import argparse
import logging
if __name__ == "__main__":
    app = web.Application()
    setup_routes(app)
    web.run_app(app)