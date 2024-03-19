#!/usr/bin/env python3
"""
A coroutine called async_comprehension that takes no arguments.
"""
import typing

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """
    A coroutine called async_comprehension that collects 10 numbers
    from the async_generator function
    """
    mylist = []
    async for item in async_generator():
        mylist.append(item)
    return mylist
