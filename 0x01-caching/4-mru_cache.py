#!/usr/bin/env python3
"""
MRUCache module
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache is a caching system that inherits from BaseCaching
    and follows the MRU (Most Recently Used) caching strategy.
    """

    def __init__(self):
        """
        Initialize the cache with the parent class constructor.
        """
        super().__init__()
        self.mru_key = None

    def put(self, key, item):
        """
        Add an item to the cache following the MRU strategy.

        Args:
            key (str): The key under which to store the item.
            item (Any): The item to be stored in the cache.

        If the cache exceeds MAX_ITEMS, the most recently used item is discarded.
        If key or item is None, this method does nothing.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key not in self.cache_data:
                    if self.mru_key is not None:
                        del self.cache_data[self.mru_key]
                        print(f"DISCARD: {self.mru_key}")
            self.cache_data[key] = item
            self.mru_key = key

    def get(self, key):
        """
        Retrieve an item from the cache by key.

        Args:
            key (str): The key corresponding to the desired item.

        Returns:
            The value associated with the key, or None if the key
            is None or does not exist in the cache.
        """
        if key is not None and key in self.cache_data:
            self.mru_key = key
            return self.cache_data[key]
        return None

