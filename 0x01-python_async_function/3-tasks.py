#!/usr/bin/env python3
"""
<----- Tasks ----->
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    task_wait_random that takes an integer max_delay
    and returns an asyncio.Task
    :param max_delay:
    :return:
    """
    return asyncio.Task(wait_random(max_delay))
