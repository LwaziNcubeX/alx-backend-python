#!/usr/bin/env python3
"""A function that return values,
add type annotations to the function """
import typing
from types import NoneType


def safely_get_value(dct: typing.Mapping, key: typing.Any,
                     default: typing.Union[TypeError, NoneType] = None
                     ) -> typing.Union[typing.Any, TypeError]:
    """A function that return values,
    add type annotations to the function """
    if key in dct:
        return dct[key]
    else:
        return default
