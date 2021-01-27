# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class TextDateAnnotation(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, start=None, length=None, text=None, confidence=None, date_format=None):  # noqa: E501
        """TextDateAnnotation - a model defined in OpenAPI

        :param start: The start of this TextDateAnnotation.  # noqa: E501
        :type start: int
        :param length: The length of this TextDateAnnotation.  # noqa: E501
        :type length: int
        :param text: The text of this TextDateAnnotation.  # noqa: E501
        :type text: str
        :param confidence: The confidence of this TextDateAnnotation.  # noqa: E501
        :type confidence: float
        :param date_format: The date_format of this TextDateAnnotation.  # noqa: E501
        :type date_format: str
        """
        self.openapi_types = {
            'start': int,
            'length': int,
            'text': str,
            'confidence': float,
            'date_format': str
        }

        self.attribute_map = {
            'start': 'start',
            'length': 'length',
            'text': 'text',
            'confidence': 'confidence',
            'date_format': 'dateFormat'
        }

        self._start = start
        self._length = length
        self._text = text
        self._confidence = confidence
        self._date_format = date_format

    @classmethod
    def from_dict(cls, dikt) -> 'TextDateAnnotation':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TextDateAnnotation of this TextDateAnnotation.  # noqa: E501
        :rtype: TextDateAnnotation
        """
        return util.deserialize_model(dikt, cls)

    @property
    def start(self):
        """Gets the start of this TextDateAnnotation.

        The position of the first character  # noqa: E501

        :return: The start of this TextDateAnnotation.
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this TextDateAnnotation.

        The position of the first character  # noqa: E501

        :param start: The start of this TextDateAnnotation.
        :type start: int
        """
        if start is None:
            raise ValueError("Invalid value for `start`, must not be `None`")  # noqa: E501

        self._start = start

    @property
    def length(self):
        """Gets the length of this TextDateAnnotation.

        The length of the annotation  # noqa: E501

        :return: The length of this TextDateAnnotation.
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this TextDateAnnotation.

        The length of the annotation  # noqa: E501

        :param length: The length of this TextDateAnnotation.
        :type length: int
        """
        if length is None:
            raise ValueError("Invalid value for `length`, must not be `None`")  # noqa: E501

        self._length = length

    @property
    def text(self):
        """Gets the text of this TextDateAnnotation.

        The string annotated  # noqa: E501

        :return: The text of this TextDateAnnotation.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this TextDateAnnotation.

        The string annotated  # noqa: E501

        :param text: The text of this TextDateAnnotation.
        :type text: str
        """
        if text is None:
            raise ValueError("Invalid value for `text`, must not be `None`")  # noqa: E501

        self._text = text

    @property
    def confidence(self):
        """Gets the confidence of this TextDateAnnotation.

        The confidence in the accuracy of the annotation  # noqa: E501

        :return: The confidence of this TextDateAnnotation.
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this TextDateAnnotation.

        The confidence in the accuracy of the annotation  # noqa: E501

        :param confidence: The confidence of this TextDateAnnotation.
        :type confidence: float
        """
        if confidence is not None and confidence > 100:  # noqa: E501
            raise ValueError("Invalid value for `confidence`, must be a value less than or equal to `100`")  # noqa: E501
        if confidence is not None and confidence < 0:  # noqa: E501
            raise ValueError("Invalid value for `confidence`, must be a value greater than or equal to `0`")  # noqa: E501

        self._confidence = confidence

    @property
    def date_format(self):
        """Gets the date_format of this TextDateAnnotation.

        Date format (ISO 8601)  # noqa: E501

        :return: The date_format of this TextDateAnnotation.
        :rtype: str
        """
        return self._date_format

    @date_format.setter
    def date_format(self, date_format):
        """Sets the date_format of this TextDateAnnotation.

        Date format (ISO 8601)  # noqa: E501

        :param date_format: The date_format of this TextDateAnnotation.
        :type date_format: str
        """

        self._date_format = date_format
