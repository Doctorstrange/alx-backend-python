#!/usr/bin/env python3
"""Returns the string representation of the given float `n`."""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns the first element of a sequence"""

    if lst:
        return lst[0]
    else:
        return None
