#!/usr/bin/env python3
"""
The code is nearly identical to wait_n except
task_wait_random is being called.
"""

import asyncio
from typing import List, Any

try:
    task_wait = __import__('3-tasks').task_wait_random
except ImportError:
    pass


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    The code is nearly identical to wait_n
    except task_wait_random is being called.
    :return: A list of asyncio.Tasks
    """
    dos = []
    for _ in range(n):
        do = await task_wait(max_delay)
        dos.append(do)
    return sorted(dos)
