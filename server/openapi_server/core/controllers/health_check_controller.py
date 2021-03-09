from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.health_check import HealthCheck  # noqa: E501


def get_health_check():  # noqa: E501
    """Get health check information

    Get information about the health of the service # noqa: E501


    :rtype: HealthCheck
    """
    try:
        res = HealthCheck(status="pass")
        status = 200
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))
    return res, status
