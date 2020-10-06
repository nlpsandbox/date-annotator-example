#!/usr/bin/env python3

import json
from logging.config import dictConfig

import connexion

from openapi_server.models.date_annotation import DateAnnotation


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

    class AnnotationDateEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, DateAnnotation):
                text = obj.text;  # From Parent Class, out of the box connexion only returns fields on the child class
                date_format = obj.date_format or ""
                created_date_str = obj.created_at.strftime("%y%m%d")
                note_id = obj.note_id
                start = obj.start
                return {'id': obj.id, 'note_id': note_id, 'createdBy': obj.created_by, 'text': text,
                        'date_format': date_format, 'created_at': created_date_str, "start" : start}

            return json.JSONEncoder.default(self,
                                            obj)  # default, if not Delivery object. Caller's problem if this is not serialziable.

    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_encoder = AnnotationDateEncoder
    app.add_api('openapi.yaml',
                arguments={'title': 'NLP Sandbox Date Annotator API'},
                pythonic_params=True)
    app.run(port=8080)


if __name__ == '__main__':
    main()
