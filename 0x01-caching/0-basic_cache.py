#!/usr/bin/env python3
"""
BasicCache module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache is a caching system that inherits from BaseCaching
    with no limit on the number of items stored.
    """

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key (str): The key under which to store the item.
            item (Any): The item to be stored in the cache.

        If either key or item is None, this method does nothing.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

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

