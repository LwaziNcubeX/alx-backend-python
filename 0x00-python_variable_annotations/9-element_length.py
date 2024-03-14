#!/usr/bin/env python3
"""A variable length:
Let's duck type an iterable object"""
import typing


def element_length(lst: typing.Iterable[typing.Sequence]) -> (
        typing.List)[typing.Tuple[typing.Sequence, int]]:
    """Returns the length of an iterable object"""
    return [(i, len(i)) for i in lst]
