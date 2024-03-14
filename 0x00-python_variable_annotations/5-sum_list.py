#!/usr/bin/env python3
"""A type-annotated function sum_list which takes a list input_list of floats
as argument and returns their sum as a float."""
import typing


def sum_list(input_list: typing.List[float]) -> float:
    """sum_list takes a list input_list of floats
    and returns the sum as a float"""
    total: float = 0.0

    for n in input_list:
        total += n
    return total
