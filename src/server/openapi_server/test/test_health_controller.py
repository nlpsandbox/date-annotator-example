# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.health import Health  # noqa: E501
from openapi_server.test import BaseTestCase


class TestHealthController(BaseTestCase):
    """HealthController integration test stubs"""

    def test_health(self):
        """Test case for health

        Get Health
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/health',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
