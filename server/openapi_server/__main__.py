#!/usr/bin/env python3

import connexion

from openapi_server import encoder


def main():
    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': 'NLP Sandbox Date Annotator API'},
                pythonic_params=True)
    # TODO: Consider using param host="0.0.0.0", debug=True,
    app.run(port=8080)


if __name__ == '__main__':
    main()
