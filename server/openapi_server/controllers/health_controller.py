from flask import jsonify

from openapi_server.models.health import Health  # noqa: E501


def health():  # noqa: E501
    """Get Health
    Get the health of the API # noqa: E501
    :rtype: Health
    """
    # return jsonify(Health("pass"))
    return jsonify({'status': 'pass'})