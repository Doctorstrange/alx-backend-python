#!/usr/bin/env python3
"""Waits for a random delay between 0 and
max_delay seconds (inclusive) and returns it"""

import asyncio
import random


async def wait_random(max_delay=10):
    """Waits for a random delay between 0 and
    max_delay seconds (inclusive) and returns it.

    Args:
        max_delay (float, optional): The maximum
        delay in seconds. Defaults to 10.

    Yields:
        float: The random delay that was waited for.
    """
    delay = random.uniform(0, max_delay)
    yield await asyncio.sleep(delay)
    return delay
