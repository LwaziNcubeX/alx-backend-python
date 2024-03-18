#!/usr/bin/env python3
"""
<---------- The basics of async ---------->
"""
import asyncio
from random import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits random delay between 0 and max_delay
    (included and float value) seconds and eventually returns it
    :param max_delay:
    :return:
    """
    delay = random() * max_delay
    await asyncio.sleep(delay)
    return delay
