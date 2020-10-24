# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.date_annotation import DateAnnotation  # noqa: E501
from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.note import Note  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDateController(BaseTestCase):
    """DateController integration test stubs"""

    def test_dates_read_all(self):
        """Test case for dates_read_all

        Get all date annotations
        """

        note = [Note(id=None, created_by=None, created_at=None,
                updated_by=None, updated_at=None, text="text", type=None)]
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v1/dates',
            method='POST',
            headers=headers,
            data=json.dumps(note),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
