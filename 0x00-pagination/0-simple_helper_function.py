#!/usr/bin/env python3
"""
 function named index_range that takes two
 integer arguments page and page_size
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    function should return a tuple of size two
    containing a start index and an end index
    """

    return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)
