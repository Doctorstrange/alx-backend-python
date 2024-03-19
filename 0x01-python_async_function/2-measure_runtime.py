#!/usr/bin/env python3
"""Measures the active time of the wait_n coroutine"""

import asyncio
import time

try:
    wait = __import__('1-concurrent_coroutines').wait_n
except ImportError:
    pass


def measure_time(n: int, max_delay: int) -> float:
    """Measures the active time of the wait_n coroutine

    Args:
        max_delay arguments that measures the total execution time

    Yields:
        float: Use the time module
    """
    start_time = time.time()
    asyncio.run(wait(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
