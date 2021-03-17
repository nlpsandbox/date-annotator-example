import connexion
import six

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.text_date_annotation_request import TextDateAnnotationRequest  # noqa: E501
from openapi_server.models.text_date_annotation_response import TextDateAnnotationResponse  # noqa: E501
from openapi_server import util
from openapi_server.core.controllers import text_date_annotation_controller as controller


def create_text_date_annotations(text_date_annotation_request=None):  # noqa: E501
    """Annotate dates in a clinical note

    Return the date annotations found in a clinical note # noqa: E501

    :param text_date_annotation_request: 
    :type text_date_annotation_request: dict | bytes

    :rtype: TextDateAnnotationResponse
    """
    if connexion.request.is_json:
        text_date_annotation_request = TextDateAnnotationRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return controller.create_text_date_annotations(
        text_date_annotation_request=text_date_annotation_request
    )
