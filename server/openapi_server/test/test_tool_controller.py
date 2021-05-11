# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.tool import Tool  # noqa: E501
from openapi_server.models.tool_dependencies import ToolDependencies  # noqa: E501
from openapi_server.test import BaseTestCase


class TestToolController(BaseTestCase):
    """ToolController integration test stubs"""

    def test_get_tool(self):
        """Test case for get_tool

        Get tool information
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/tool',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_tool_dependencies(self):
        """Test case for get_tool_dependencies

        Get tool dependencies
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/tool/dependencies',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
