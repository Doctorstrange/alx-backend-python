#!/usr/bin/env python3

"""Defines asynchronous coroutines takes in 2 int arguments (in this order)"""

from typing import List

try:
    wait = __import__('0-basic_async_syntax').wait_random
except ImportError:
    pass


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    takes in 2 int arguments (in this order)
    :return: the list of all the delays (float values)
    """
    delays = []
    for _ in range(n):
        delay = await wait(max_delay)
        delays.append(delay)
    return sorted(delays)
