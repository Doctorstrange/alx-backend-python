#!/usr/bin/env python3

"""that takes an integer max_delay and returns a asyncio.Task"""

# from typing import Any
import asyncio

try:
    wait = __import__('0-basic_async_syntax').wait_random
except ImportError:
    pass


def task_wait_random(max_delay: int) -> asyncio.Task:
    """that takes an integer max_delay and returns a asyncio.Task

    :time module to measure an approximate elapsed time
    :return: An asyncio.Task
    """
    return asyncio.create_task(wait(max_delay))
