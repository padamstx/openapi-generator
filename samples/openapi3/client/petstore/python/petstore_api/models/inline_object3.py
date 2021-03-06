# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from petstore_api.configuration import Configuration


class InlineObject3(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'integer': 'int',
        'int32': 'int',
        'int64': 'int',
        'number': 'float',
        'float': 'float',
        'double': 'float',
        'string': 'str',
        'pattern_without_delimiter': 'str',
        'byte': 'str',
        'binary': 'file',
        'date': 'date',
        'date_time': 'datetime',
        'password': 'str',
        'callback': 'str'
    }

    attribute_map = {
        'integer': 'integer',
        'int32': 'int32',
        'int64': 'int64',
        'number': 'number',
        'float': 'float',
        'double': 'double',
        'string': 'string',
        'pattern_without_delimiter': 'pattern_without_delimiter',
        'byte': 'byte',
        'binary': 'binary',
        'date': 'date',
        'date_time': 'dateTime',
        'password': 'password',
        'callback': 'callback'
    }

    def __init__(self, integer=None, int32=None, int64=None, number=None, float=None, double=None, string=None, pattern_without_delimiter=None, byte=None, binary=None, date=None, date_time=None, password=None, callback=None, local_vars_configuration=None):  # noqa: E501
        """InlineObject3 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._integer = None
        self._int32 = None
        self._int64 = None
        self._number = None
        self._float = None
        self._double = None
        self._string = None
        self._pattern_without_delimiter = None
        self._byte = None
        self._binary = None
        self._date = None
        self._date_time = None
        self._password = None
        self._callback = None
        self.discriminator = None

        if integer is not None:
            self.integer = integer
        if int32 is not None:
            self.int32 = int32
        if int64 is not None:
            self.int64 = int64
        self.number = number
        if float is not None:
            self.float = float
        self.double = double
        if string is not None:
            self.string = string
        self.pattern_without_delimiter = pattern_without_delimiter
        self.byte = byte
        if binary is not None:
            self.binary = binary
        if date is not None:
            self.date = date
        if date_time is not None:
            self.date_time = date_time
        if password is not None:
            self.password = password
        if callback is not None:
            self.callback = callback

    @property
    def integer(self):
        """Gets the integer of this InlineObject3.  # noqa: E501

        None  # noqa: E501

        :return: The integer of this InlineObject3.  # noqa: E501
        :rtype: int
        """
        return self._integer

    @integer.setter
    def integer(self, integer):
        """Sets the integer of this InlineObject3.

        None  # noqa: E501

        :param integer: The integer of this InlineObject3.  # noqa: E501
        :type integer: int
        """
        if (self.local_vars_configuration.client_side_validation and
                integer is not None and integer > 100):  # noqa: E501
            raise ValueError("Invalid value for `integer`, must be a value less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                integer is not None and integer < 10):  # noqa: E501
            raise ValueError("Invalid value for `integer`, must be a value greater than or equal to `10`")  # noqa: E501

        self._integer = integer

    @property
    def int32(self):
        """Gets the int32 of this InlineObject3.  # noqa: E501

        None  # noqa: E501

        :return: The int32 of this InlineObject3.  # noqa: E501
        :rtype: int
        """
        return self._int32

    @int32.setter
    def int32(self, int32):
        """Sets the int32 of this InlineObject3.

        None  # noqa: E501

        :param int32: The int32 of this InlineObject3.  # noqa: E501
        :type int32: int
        """
        if (self.local_vars_configuration.client_side_validation and
                int32 is not None and int32 > 200):  # noqa: E501
            raise ValueError("Invalid value for `int32`, must be a value less than or equal to `200`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                int32 is not None and int32 < 20):  # noqa: E501
            raise ValueError("Invalid value for `int32`, must be a value greater than or equal to `20`")  # noqa: E501

        self._int32 = int32

    @property
    def int64(self):
        """Gets the int64 of this InlineObject3.  # noqa: E501

        None  # noqa: E501

        :return: The int64 of this InlineObject3.  # noqa: E501
        :rtype: int
        """
        return self._int64

    @int64.setter
    def int64(self, int64):
        """Sets the int64 of this InlineObject3.

        None  # noqa: E501

        :param int64: The int64 of this InlineObject3.  # noqa: E501
        :type int64: int
        """

        self._int64 = int64

    @property
    def number(self):
        """Gets the number of this InlineObject3.  # noqa: E501

        None  # noqa: E501

        :return: The number of this InlineObject3.  # noqa: E501
        :rtype: float
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this InlineObject3.

        None  # noqa: E501

        :param number: The number of this InlineObject3.  # noqa: E501
        :type number: float
        """
        if self.local_vars_configuration.client_side_validation and number is None:  # noqa: E501
            raise ValueError("Invalid value for `number`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                number is not None and number > 543.2):  # noqa: E501
            raise ValueError("Invalid value for `number`, must be a value less than or equal to `543.2`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                number is not None and number < 32.1):  # noqa: E501
            raise ValueError("Invalid value for `number`, must be a value greater than or equal to `32.1`")  # noqa: E501

        self._number = number

    @property
    def float(self):
        """Gets the float of this InlineObject3.  # noqa: E501

        None  # noqa: E501

        :return: The float of this InlineObject3.  # noqa: E501
        :rtype: float
        """
        return self._float

    @float.setter
    def float(self, float):
        """Sets the float of this InlineObject3.

        None  # noqa: E501

        :param float: The float of this InlineObject3.  # noqa: E501
        :type float: float
        """
        if (self.local_vars_configuration.client_side_validation and
                float is not None and float > 987.6):  # noqa: E501
            raise ValueError("Invalid value for `float`, must be a value less than or equal to `987.6`")  # noqa: E501

        self._float = float

    @property
    def double(self):
        """Gets the double of this InlineObject3.  # noqa: E501

        None  # noqa: E501

        :return: The double of this InlineObject3.  # noqa: E501
        :rtype: float
        """
        return self._double

    @double.setter
    def double(self, double):
        """Sets the double of this InlineObject3.

        None  # noqa: E501

        :param double: The double of this InlineObject3.  # noqa: E501
        :type double: float
        """
        if self.local_vars_configuration.client_side_validation and double is None:  # noqa: E501
            raise ValueError("Invalid value for `double`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                double is not None and double > 123.4):  # noqa: E501
            raise ValueError("Invalid value for `double`, must be a value less than or equal to `123.4`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                double is not None and double < 67.8):  # noqa: E501
            raise ValueError("Invalid value for `double`, must be a value greater than or equal to `67.8`")  # noqa: E501

        self._double = double

    @property
    def string(self):
        """Gets the string of this InlineObject3.  # noqa: E501

        None  # noqa: E501

        :return: The string of this InlineObject3.  # noqa: E501
        :rtype: str
        """
        return self._string

    @string.setter
    def string(self, string):
        """Sets the string of this InlineObject3.

        None  # noqa: E501

        :param string: The string of this InlineObject3.  # noqa: E501
        :type string: str
        """
        if (self.local_vars_configuration.client_side_validation and
                string is not None and not re.search(r'[a-z]', string, flags=re.IGNORECASE)):  # noqa: E501
            raise ValueError(r"Invalid value for `string`, must be a follow pattern or equal to `/[a-z]/i`")  # noqa: E501

        self._string = string

    @property
    def pattern_without_delimiter(self):
        """Gets the pattern_without_delimiter of this InlineObject3.  # noqa: E501

        None  # noqa: E501

        :return: The pattern_without_delimiter of this InlineObject3.  # noqa: E501
        :rtype: str
        """
        return self._pattern_without_delimiter

    @pattern_without_delimiter.setter
    def pattern_without_delimiter(self, pattern_without_delimiter):
        """Sets the pattern_without_delimiter of this InlineObject3.

        None  # noqa: E501

        :param pattern_without_delimiter: The pattern_without_delimiter of this InlineObject3.  # noqa: E501
        :type pattern_without_delimiter: str
        """
        if self.local_vars_configuration.client_side_validation and pattern_without_delimiter is None:  # noqa: E501
            raise ValueError("Invalid value for `pattern_without_delimiter`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                pattern_without_delimiter is not None and not re.search(r'^[A-Z].*', pattern_without_delimiter)):  # noqa: E501
            raise ValueError(r"Invalid value for `pattern_without_delimiter`, must be a follow pattern or equal to `/^[A-Z].*/`")  # noqa: E501

        self._pattern_without_delimiter = pattern_without_delimiter

    @property
    def byte(self):
        """Gets the byte of this InlineObject3.  # noqa: E501

        None  # noqa: E501

        :return: The byte of this InlineObject3.  # noqa: E501
        :rtype: str
        """
        return self._byte

    @byte.setter
    def byte(self, byte):
        """Sets the byte of this InlineObject3.

        None  # noqa: E501

        :param byte: The byte of this InlineObject3.  # noqa: E501
        :type byte: str
        """
        if self.local_vars_configuration.client_side_validation and byte is None:  # noqa: E501
            raise ValueError("Invalid value for `byte`, must not be `None`")  # noqa: E501

        self._byte = byte

    @property
    def binary(self):
        """Gets the binary of this InlineObject3.  # noqa: E501

        None  # noqa: E501

        :return: The binary of this InlineObject3.  # noqa: E501
        :rtype: file
        """
        return self._binary

    @binary.setter
    def binary(self, binary):
        """Sets the binary of this InlineObject3.

        None  # noqa: E501

        :param binary: The binary of this InlineObject3.  # noqa: E501
        :type binary: file
        """

        self._binary = binary

    @property
    def date(self):
        """Gets the date of this InlineObject3.  # noqa: E501

        None  # noqa: E501

        :return: The date of this InlineObject3.  # noqa: E501
        :rtype: date
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this InlineObject3.

        None  # noqa: E501

        :param date: The date of this InlineObject3.  # noqa: E501
        :type date: date
        """

        self._date = date

    @property
    def date_time(self):
        """Gets the date_time of this InlineObject3.  # noqa: E501

        None  # noqa: E501

        :return: The date_time of this InlineObject3.  # noqa: E501
        :rtype: datetime
        """
        return self._date_time

    @date_time.setter
    def date_time(self, date_time):
        """Sets the date_time of this InlineObject3.

        None  # noqa: E501

        :param date_time: The date_time of this InlineObject3.  # noqa: E501
        :type date_time: datetime
        """

        self._date_time = date_time

    @property
    def password(self):
        """Gets the password of this InlineObject3.  # noqa: E501

        None  # noqa: E501

        :return: The password of this InlineObject3.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this InlineObject3.

        None  # noqa: E501

        :param password: The password of this InlineObject3.  # noqa: E501
        :type password: str
        """
        if (self.local_vars_configuration.client_side_validation and
                password is not None and len(password) > 64):
            raise ValueError("Invalid value for `password`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                password is not None and len(password) < 10):
            raise ValueError("Invalid value for `password`, length must be greater than or equal to `10`")  # noqa: E501

        self._password = password

    @property
    def callback(self):
        """Gets the callback of this InlineObject3.  # noqa: E501

        None  # noqa: E501

        :return: The callback of this InlineObject3.  # noqa: E501
        :rtype: str
        """
        return self._callback

    @callback.setter
    def callback(self, callback):
        """Sets the callback of this InlineObject3.

        None  # noqa: E501

        :param callback: The callback of this InlineObject3.  # noqa: E501
        :type callback: str
        """

        self._callback = callback

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineObject3):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineObject3):
            return True

        return self.to_dict() != other.to_dict()
