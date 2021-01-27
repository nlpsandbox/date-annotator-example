from openapi_server.models.health_check import HealthCheck  # noqa: E501


def get_health_check():  # noqa: E501
    """Get health check information

    Get information about the health of the service # noqa: E501


    :rtype: HealthCheck
    """
    return HealthCheck(status="pass"), 200
