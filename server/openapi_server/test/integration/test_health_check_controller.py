# coding: utf-8

from __future__ import absolute_import
import unittest

from openapi_server.test.integration import BaseTestCase


class TestHealthCheckController(BaseTestCase):
    """HealthCheckController integration test stubs"""

    def test_get_health_check(self):
        """Test case for get_health_check

        Get health check information
        """
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/healthCheck',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
