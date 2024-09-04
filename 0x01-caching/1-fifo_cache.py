#!/usr/bin/env python3
"""
FIFOCache module
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache is a caching system that inherits from BaseCaching
    and follows the FIFO (First-In, First-Out) caching strategy.
    """

    def __init__(self):
        """
        Initialize the cache with the parent class constructor.
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add an item to the cache following the FIFO strategy.

        Args:
            key (str): The key under which to store the item.
            item (Any): The item to be stored in the cache.

        If the cache exceeds MAX_ITEMS, the first added item is discarded.
        If key or item is None, this method does nothing.
        """
        if key is not None and item is not None:
            if key not in self.cache_data:
                self.order.append(key)
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                oldest_key = self.order.pop(0)
                del self.cache_data[oldest_key]
                print(f"DISCARD: {oldest_key}")

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

