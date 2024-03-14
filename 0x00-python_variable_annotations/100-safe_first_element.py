#!/usr/bin/env python3
"""A safe first element:
Duck typing - first element of a sequence"""
import typing


def safe_first_element(lst: typing.Sequence[typing.Any]
                       ) -> typing.Union[typing.Any, None]:
    """A safe first element:
    Duck typing - first element of a sequence"""
    if lst:
        return lst[0]
    else:
        return None
