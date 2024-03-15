#!/usr/bin/env python3
"""Returns the string representation of the given float `n`."""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple contains
            a sequence from the input list and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
