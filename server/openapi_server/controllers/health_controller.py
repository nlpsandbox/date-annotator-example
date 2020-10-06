import connexion
import six

from openapi_server.models.health import Health  # noqa: E501
from openapi_server import util


def health():  # noqa: E501
    """Get Health

    Get the health of the API # noqa: E501


    :rtype: Health
    """
    return 'do some magic!'
