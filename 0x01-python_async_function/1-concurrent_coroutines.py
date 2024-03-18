#!/usr/bin/env python3
"""
<----- Python Multiple Concurrent Coroutines ----->
"""
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    runs wait_random n times with the specified max_delay.
    and stores them in a list.

    :param n:
    :param max_delay:
    :return: list of floats
    """
    my_list = []
    for i in range(n):
        a = await wait_random(max_delay)
        my_list.append(a)
    return my_list
