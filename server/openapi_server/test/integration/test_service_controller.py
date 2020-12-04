# coding: utf-8

from __future__ import absolute_import
import unittest

from openapi_server.test.integration import BaseTestCase


class TestServiceController(BaseTestCase):
    """ServiceController integration test stubs"""

    def test_service(self):
        """Test case for service

        Get service information
        """
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/service',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
