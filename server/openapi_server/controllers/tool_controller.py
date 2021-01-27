import connexion
import six

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.tool import Tool  # noqa: E501
from openapi_server.models.tool_dependencies import ToolDependencies  # noqa: E501
from openapi_server import util


def get_tool():  # noqa: E501
    """Get tool information

    Get information about the tool # noqa: E501


    :rtype: Tool
    """
    return 'do some magic!'


def get_tool_dependencies():  # noqa: E501
    """Get tool dependencies

    Get the dependencies of this tool # noqa: E501


    :rtype: ToolDependencies
    """
    return 'do some magic!'
