#!/usr/bin/env python3
"""A type-annotated function make_multiplier that takes a
float multiplier as argument and
returns a function that multiplies a float by multiplier"""
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """make_multiplier takes a float multiplier and
    returns a function that multiplies a float by multiplier"""

    def multiplier_func(num: float) -> float:
        """multiplies num by multiplier"""
        return num * multiplier

    return multiplier_func
