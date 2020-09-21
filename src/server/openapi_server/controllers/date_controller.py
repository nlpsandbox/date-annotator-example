import connexion
import six

from openapi_server.models.date_annotation import DateAnnotation  # noqa: E501
from openapi_server.models.note import Note  # noqa: E501
from openapi_server import util
from datetime import date
import logging


def dates_read_all(note=None):  # noqa: E501
    """Get all date annotations

    Returns the date annotations # noqa: E501

    :param note: 
    :type note: list | bytes

    :rtype: List[DateAnnotation]
    """
    print("in dates_read_all ")
    returnList = []
    if connexion.request.is_json:
        note = [Note.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
        logging.info(f"NOTE TEXT : { note[0]._text}")
        returnList.append(DateAnnotation( date_format=None, id=2, created_by="George", created_at=date.today(), updated_by="Demo System", updated_at=date.today()))
        return returnList

    return 'do some magic!'
