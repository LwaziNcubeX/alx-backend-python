#!/usr/bin/env python3
"""
Run time for four parallel comprehensions
"""
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    calculate runtime for four parallel and return it
    :return:
    """
    start_time = time.time()
    await async_comprehension()
    end_time = time.time()

    return end_time - start_time
