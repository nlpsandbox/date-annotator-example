#!/usr/bin/env python3

import connexion
import flask

from openapi_server import encoder

app = connexion.App(__name__, specification_dir='./openapi/')
app.app.json_encoder = encoder.JSONEncoder
app.add_api('openapi.yaml', pythonic_params=True)

# Redirections required by the NLP Sandbox
app.add_url_rule('/', 'root', lambda: flask.redirect('/api/v1/tool'))
app.add_url_rule('/ui', 'ui', lambda: flask.redirect('/api/v1/ui'))


def main():
    app.run(port=8080)


if __name__ == '__main__':
    main()
