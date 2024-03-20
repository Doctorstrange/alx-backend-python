#!/usr/bin/env python3

"""
Import async_comprehension from the previous file and write a
measure_runtime coroutine that will execute async_comprehension
four times in parallel using asyncio.gather.

measure_runtime should measure the total runtime and return it.
"""

import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Execute async_comprehension four times in parallel using
    asyncio.gather.

    :return: Total runtime of async_comprehension
    """
    start_time = asyncio.get_event_loop().time()
    awaitables = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*awaitables)

    end_time = asyncio.get_event_loop().time()
    total_runtime = end_time - start_time
    return total_runtime