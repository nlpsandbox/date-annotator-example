#!/usr/bin/env python3

import connexion

from openapi_server import encoder
from logging.config import dictConfig



def main():
    # Set up logging
    dictConfig({
        'version': 1,
        'formatters': {'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }},
        'handlers': {'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        }},
        'root': {
            'level': 'INFO',
            'handlers': ['wsgi']
        }
    })
    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.app.logger.warning("Startup of Server...")
    app.add_api('openapi.yaml',
                arguments={'title': 'NLP Sandbox Date Annotator API'},
                pythonic_params=True)
    app.run(port=8080)
    app.app.logger.warning("Stopping of Server...")


if __name__ == '__main__':
    main()
