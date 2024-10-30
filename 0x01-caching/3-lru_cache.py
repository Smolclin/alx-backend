#!/usr/bin/env python3
"""
class LIFOCache that inherits from BaseCaching and is a caching system
"""


from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    You must use self.cache_data - dictionary from
    the parent class BaseCaching
    """

    def __init__(self):
        """
        Must assign to the dictionary self.cache_data
        the item value for the key key
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        If key or item is None, this method should not do anything
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lru_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", lru_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Must return the value in self.cache_data linked to key
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
