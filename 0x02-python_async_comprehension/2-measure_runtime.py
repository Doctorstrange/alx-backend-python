#!/usr/bin/env python3

"""
coroutine that will execute async_comprehension
four times in parallel using asyncio.gather.
"""

import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    coroutine that will execute
    async_comprehension four times in parallel using asyncio.gather.
    """
    start_time = asyncio.get_event_loop().time()
    wait = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*wait)

    end_time = asyncio.get_event_loop().time()
    total_time = end_time - start_time
    return total_time
