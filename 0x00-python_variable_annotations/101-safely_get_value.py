#!/usr/bin/env python3
"""Returns the string representation of the given float `n`."""
from typing import Mapping, Any, Union, TypeVar


T = TypeVar("T")  # Generic type variable for values in the dictionary


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """Safely retrieves a value from a dictionary"""

    if key in dct:
        return dct[key]
    else:
        return default
