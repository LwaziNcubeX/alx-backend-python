#!/usr/bin/env python3
"""A function that returns values safely with type annotations."""
import typing


def safely_get_value(dct: typing.Mapping, key: typing.Any,
                     default: typing.Union[typing.TypeVar, None] = None
                     ) -> typing.Union[typing.Any, typing.TypeVar]:
    """
    Safely retrieves a value from a mapping.

    Retrieves a value associated with the given key from the provided mapping.
    If the key exists in the mapping, the corresponding value is returned. If
    the key does not exist, the specified default value is returned instead.

    Args:
        dct (typing.Mapping): The mapping (e.g., dictionary) to retrieve
            the value from.
        key (typing.Any): The key whose associated value is to be retrieved.
        default (typing.Union[typing.TypeVar, None], optional): The value to
            return if the key is not found in the mapping. Defaults to None.

    Returns:
        typing.Union[typing.Any, typing.TypeVar]: The value associated with the
        key if found in the mapping, or the default value otherwise.
    """
    if key in dct:
        return dct[key]
    else:
        return default
