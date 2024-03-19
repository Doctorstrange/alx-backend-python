#!/usr/bin/env python3

"""
    Defines  wait_random() asynchronous coroutine that takes
    an integer argument max_delay with default value of 10.
    Using the random.uniform(), it generates random float between
    0 and max_delay.
"""

import asyncio
import random


async def wait_random(max_delay=10) -> float:
    """
        An asynchronous coroutine that waits for
        a random delay between 0 and max_delay
        seconds and eventually returns it

    :param max_delay: maximum delay time
    :return: Return delay time
   """

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
