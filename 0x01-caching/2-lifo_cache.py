#!/usr/bin/env python3
"""
LIFOCache module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache is a caching system that inherits from BaseCaching
    and follows the LIFO (Last-In, First-Out) caching strategy.
    """

    def __init__(self):
        """
        Initialize the cache with the parent class constructor.
        """
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """
        Add an item to the cache following the LIFO strategy.

        Args:
            key (str): The key under which to store the item.
            item (Any): The item to be stored in the cache.

        If the cache exceeds MAX_ITEMS, the last added item is discarded.
        If key or item is None, this method does nothing.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                if self.last_key is not None:
                    del self.cache_data[self.last_key]
                    print(f"DISCARD: {self.last_key}")

            self.last_key = key

    def get(self, key):
        """
        Retrieve an item from the cache by key.

        Args:
            key (str): The key corresponding to the desired item.

        Returns:
            The value associated with the key, or None if the key
            is None or does not exist in the cache.
        """
        return self.cache_data.get(key)

