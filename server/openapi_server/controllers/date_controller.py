import connexion
import six

from openapi_server.models.annotation import Annotation  # noqa: E501
from openapi_server.models.date_annotation import DateAnnotation
from openapi_server.models.note import Note  # noqa: E501
from openapi_server import util
from datetime import date as gkdate
import logging
import re
from flask import jsonify

def dates_read_all(note=None):  # noqa: E501
    """Get all date annotations

    Returns the date annotations # noqa: E501

    :param note:
    :type note: list | bytes

    :rtype: List[DateAnnotation]
    """

    # TODO: Why is note value set to None when passing an array of notes using
    # the interactive doc?
    # logging.info(note)

    res = []
    if connexion.request.is_json:
        notes = [Note.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501

        for note in notes:
            # Adapted from https://stackoverflow.com/a/61234139
            matches = re.finditer('([1-9]|0[1-9]|1[0-9]|2[0-9]|3[0-1])(/)([1-9]|0[1-9]|1[0-2])(/)(19[0-9][0-9]|20[0-9][0-9])', note._text)
            add_date_annotation(res, note, matches, "MM/DD/YYYY")

            matches = re.finditer('([1-9]|0[1-9]|1[0-9]|2[0-9]|3[0-1])(-)([1-9]|0[1-9]|1[0-2])(-)(19[0-9][0-9]|20[0-9][0-9])', note._text)
            add_date_annotation(res, note, matches, "MM-DD-YYYY")

            matches = re.finditer('([1-9]|0[1-9]|1[0-9]|2[0-9]|3[0-1])(\.)([1-9]|0[1-9]|1[0-2])(\.)(19[0-9][0-9]|20[0-9][0-9])', note._text)
            add_date_annotation(res, note, matches, "MM.DD.YYYY")

            matches = re.finditer('([1-9][1-9][0-9][0-9]|2[0-9][0-9][0-9])', note._text)
            add_date_annotation(res, note, matches, "YYYY")

            matches = re.finditer('(January|February|March|April|May|June|July|August|September|October|November|December)', note._text, re.IGNORECASE)
            add_date_annotation(res, note, matches, "MMMM")

            # TODO: Remove annotations that are fully included into another
            # annotation.

    return jsonify(res)


def add_date_annotation(res, note, matches, format):
    """
    Converts matches to DateAnnotation objects and adds them to res.
    """
    for match in matches:
        res.append({
            'noteId': note._id,
            'text':  match[0],
            'format': format,
            'start': match.start(),
            'length': len(match[0])
        })

