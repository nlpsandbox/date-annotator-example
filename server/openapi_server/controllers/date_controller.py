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





    counter = 1  # TODO: Do not use counter as the note id
    returnList = []
    if connexion.request.is_json:
        note = [Note.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
        logging.info(f"NOTE TEXTA : { note[0]._text}")

        # match on https://stackoverflow.com/questions/4709652/python-regex-to-match-dates

        match = re.finditer('([1-9]|0[1-9]|1[0-9]|2[0-9]|3[0-1])(/)([1-9]|0[1-9]|1[0-2])(/)([0-9][0-9]|19[0-9][0-9]|20[0-9][0-9])', note[0]._text)
        add_match(counter, match, note, returnList, "MM/DD/YYYY")

        match = re.finditer('([1-9]|0[1-9]|1[0-9]|2[0-9]|3[0-1])(-)([1-9]|0[1-9]|1[0-2])(-)([0-9][0-9]|19[0-9][0-9]|20[0-9][0-9])', note[0]._text)
        add_match(counter, match, note, returnList, "MM-DD-YYYY")

        match = re.finditer('([1-9]|0[1-9]|1[0-9]|2[0-9]|3[0-1])(\.)([1-9]|0[1-9]|1[0-2])(\.)([0-9][0-9]|19[0-9][0-9]|20[0-9][0-9])', note[0]._text)
        add_match(counter, match, note, returnList, "MM.DD.YYYY")

        match = re.finditer('([1-9][1-9][0-9][0-9]|2[0-9][0-9][0-9])', note[0]._text)
        add_match(counter, match, note, returnList, "YYYY")

        match = re.finditer('(January|February|March|April|May|June|July|August|September|October|November|December)', note[0]._text, re.IGNORECASE)
        add_match(counter, match, note, returnList, "MMMM")

    return jsonify([])


def add_match(counter, match, note, returnList, date_format=None):
    if match is not None:
        for m in match:
            logging.info(f"Date : {m[0]} found at {m.start()}")
            da = DateAnnotation(format=format, id=counter, created_by="Date Annotation Example",
                                created_at=gkdate.today(), updated_by="Date Annotation Example",
                                updated_at=gkdate.today())
            da.text = m[0]
            da.note_id = note[0].id
            da.start = m.start()
            da.length = 10
            returnList.append(da)
            counter = counter + 1
    else:
        logging.info(f"No Dates found")
