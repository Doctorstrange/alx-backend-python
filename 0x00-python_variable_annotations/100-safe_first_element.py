#!/usr/bin/env python3
"""Returns the string representation of the given float `n`."""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence) -> Union[Any, None]:
    """
    Returns:
        Union[Any, None]: The first element of the sequence.
    """
    if lst:
        return lst[0]
    else:
        return None
