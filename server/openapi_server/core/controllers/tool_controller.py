from openapi_server.models.tool import Tool
from openapi_server.models.tool_dependencies import ToolDependencies
from openapi_server.models.license import License


def get_tool():
    """Get tool information

    Get information about the tool

    :rtype: Tool
    """
    tool = Tool(
        name="date-annotator-example",
        version="1.0.1",
        license=License.APACHE_2_0,
        repository="github:nlpsandbox/date-annotator-example",
        description="Example implementation of the NLP Sandbox Date Annotator",
        author="The NLP Sandbox Team",
        author_email="thomas.schaffter@sagebionetworks.org",
        url="https://github.com/nlpsandbox/date-annotator-example",
        tool_type="nlpsandbox:date-annotator",
        tool_api_version="1.0.1"
    )
    return tool, 200


def get_tool_dependencies():
    """Get tool dependencies

    Get the dependencies of this tool

    :rtype: ToolDependencies
    """
    return ToolDependencies(tool_dependencies=[]), 200
