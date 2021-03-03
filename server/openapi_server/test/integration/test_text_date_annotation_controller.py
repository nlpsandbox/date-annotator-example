# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json

from openapi_server.test.integration import BaseTestCase


class TestTextDateAnnotationController(BaseTestCase):
    """TextDateAnnotationController integration test stubs"""

    def test_create_text_date_annotations(self):
        """Test case for create_text_date_annotations

        Annotate dates in a clinical note
        """
        text_date_annotation_request = {
            "note": {
                "identifier": "awesome-note",
                "noteType": "loinc:LP29684-5",
                "patientId": "awesome-patient",
                "text":
                    "On 12/26/2020, Ms. Chloe Price met with Dr. Prescott. She"
                    " mentioned that she was born in May of 1987. "
                    "Specifically, she was born on 11.4.1987."
            }
        }
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v1/textDateAnnotations',
            method='POST',
            headers=headers,
            data=json.dumps(text_date_annotation_request),
            content_type='application/json')
        annotations = response.json['textDateAnnotations']
        self.assertTrue(
            any(annotation['date'] == '2020' and
                annotation['dateFormat'] == 'YYYY'
                for annotation in annotations))
        self.assertTrue(
            any(annotation['date'] == '2020-12-26' and
                annotation['dateFormat'] == 'MM/DD/YYYY'
                for annotation in annotations))
        self.assertTrue(
            any(annotation['date'] == '--05' and
                annotation['text'] == 'May'
                for annotation in annotations))
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
