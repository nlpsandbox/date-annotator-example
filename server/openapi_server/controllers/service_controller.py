import connexion
import six

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.service import Service  # noqa: E501
from openapi_server import util


def service():  # noqa: E501
    """Get service information

    Get information about the service # noqa: E501


    :rtype: Service
    """
    return 'do some magic!'
