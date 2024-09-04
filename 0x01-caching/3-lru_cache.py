#!/usr/bin/env python3
"""
LRUCache module
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache is a caching system that inherits from BaseCaching
    and follows the LRU (Least Recently Used) caching strategy.
    """

    def __init__(self):
        """
        Initialize the cache with the parent class constructor.
        """
        super().__init__()
        self.lru_order = []

    def put(self, key, item):
        """
        Add an item to the cache following the LRU strategy.

        Args:
            key (str): The key under which to store the item.
            item (Any): The item to be stored in the cache.

        If the cache exceeds MAX_ITEMS, the least recently used item is discarded.
        If key or item is None, this method does nothing.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.lru_order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lru_key = self.lru_order.pop(0)
                del self.cache_data[lru_key]
                print(f"DISCARD: {lru_key}")

            self.cache_data[key] = item
            self.lru_order.append(key)

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
            self.lru_order.remove(key)
            self.lru_order.append(key)
            return self.cache_data[key]
        return None

