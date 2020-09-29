# aiohttpdemo_polls/main.py
from aiohttp import web
from routes import setup_routes
import argparse
import logging
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Demo Mouth Detection"
    )

    parser.add_argument(
        "--port", type=int, default=8080, help="Port for HTTP server (default: 8080)"
    )
    parser.add_argument("--verbose", "-v", action="count")

    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    app = web.Application()
    setup_routes(app)
    web.run_app(app, access_log=None, port=args.port, ssl_context=None)