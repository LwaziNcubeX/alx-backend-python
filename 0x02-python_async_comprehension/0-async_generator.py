#!/usr/bin/env python3
"""
A coroutine called async_generator that takes no arguments.
"""
import asyncio
from random import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Loops 10 times and sleeps 1 sec per loop then yields them
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random() * 10
