import connexion
import six

from openapi_server.models.date_annotation import DateAnnotation  # noqa: E501
from openapi_server.models.note import Note  # noqa: E501
from openapi_server import util


def dates_read_all(note=None):  # noqa: E501
    """Get all date annotations

    Returns the date annotations # noqa: E501

    :param note: 
    :type note: list | bytes

    :rtype: List[DateAnnotation]
    """
    if connexion.request.is_json:
        note = [Note.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return 'do some magic!'
