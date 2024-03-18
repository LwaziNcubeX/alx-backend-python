#!/usr/bin/env python3
"""
<----- Python Multiple Concurrent Coroutines ----->
"""
import typing

task_wait_random = __import__('0-basic_async_syntax').wait_random


def selection_sort(arr: typing.List) -> None:
    """
    Selection sort for an array
    :param arr:
    :return:
    """
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """
    runs wait_random n times with the specified max_delay.
    and stores them in a list.

    :param n:
    :param max_delay:
    :return: list of floats
    """
    my_list = []
    for i in range(n):
        a = await task_wait_random(max_delay)
        my_list.append(a)

    selection_sort(my_list)
    return my_list
