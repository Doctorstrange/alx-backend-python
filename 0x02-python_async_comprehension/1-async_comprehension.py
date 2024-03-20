#!/usr/bin/env python3
"""
coroutine will collect 10 random numbers using
an async comprehensing over async_generator
"""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    coroutine will collect 10 random numbers
    using an async comprehensing over async_generator
    """
    generated_list = []
    async for value in async_generator():
        generated_list.append(value)
    return generated_list
