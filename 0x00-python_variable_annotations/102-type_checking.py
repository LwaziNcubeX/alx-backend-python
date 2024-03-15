#!/usr/bin/env python3
"""An updated zoom array with Type Checking"""
import typing


def zoom_array(lst: typing.Tuple, factor: int = 2) -> typing.List:
    """Returns a new zoom array with specified factor"""
    zoomed_in: typing.List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array: typing.Tuple[int, int, int] = (12, 72, 91)

zoom_2x: typing.List[int] = zoom_array(array)

zoom_3x: typing.List[int] = zoom_array(array, 3)
