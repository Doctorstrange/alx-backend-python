#!/usr/bin/env python3
"""Returns the string representation of the given float `n`."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by the given `multiplier`."""

    def inner(number: float) -> float:
        """Multiplies a float by the `multiplier`."""
        return number * multiplier

    return inner
