import connexion
import re

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.note import Note  # noqa: E501
from openapi_server.models.text_date_annotations import TextDateAnnotations  # noqa: E501


def create_text_date_annotations(note=None):  # noqa: E501
    """Annotate dates in a clinical note

    Return the date annotations found in a clinical note # noqa: E501

    :param note:
    :type note: dict | bytes

    :rtype: TextDateAnnotations
    """
    res = None
    status = None

    if connexion.request.is_json:
        try:
            note = Note.from_dict(connexion.request.get_json())  # noqa: E501

            annotations = []
            # Adapted from https://stackoverflow.com/a/61234139
            matches = re.finditer(
                "([1-9]|0[1-9]|1[0-2])(/)([1-9]|0[1-9]|1[0-9]|2[0-9]|3[0-1])" +
                "(/)(19[0-9][0-9]|20[0-9][0-9])", note._text)
            add_date_annotation(annotations, matches, "MM/DD/YYYY")

            matches = re.finditer(
                "([1-9]|0[1-9]|1[0-2])(-)([1-9]|0[1-9]|1[0-9]|2[0-9]|3[0-1])" +
                "(-)(19[0-9][0-9]|20[0-9][0-9])", note._text)
            add_date_annotation(annotations, matches, "MM-DD-YYYY")

            matches = re.finditer(
                "([1-9]|0[1-9]|1[0-2])(\\.)([1-9]|0[1-9]|1[0-9]|2[0-9]|" +
                "3[0-1])(\\.)(19[0-9][0-9]|20[0-9][0-9])", note._text)
            add_date_annotation(annotations, matches, "MM.DD.YYYY")

            matches = re.finditer(
                "([1-9][1-9][0-9][0-9]|2[0-9][0-9][0-9])", note._text)
            add_date_annotation(annotations, matches, "YYYY")

            matches = re.finditer(
                "(January|February|March|April|May|June|July|August|" +
                "September|October|November|December)",
                note._text, re.IGNORECASE)
            add_date_annotation(annotations, matches, "MMMM")

            res = TextDateAnnotations(annotations)
            status = 200
        except Exception as error:
            status = 500
            res = Error("Internal error", status, str(error))

    return res, status


def add_date_annotation(annotations, matches, format):
    """
    Converts matches to TextDateAnnotation objects and adds them to the
    annotations array specified.
    """
    for match in matches:
        annotations.append({
            'start': match.start(),
            'length': len(match[0]),
            'text':  match[0],
            'format': format,
        })
