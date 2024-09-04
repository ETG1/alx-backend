#!/usr/bin/env python3
"""
LFUCache module
"""

from base_caching import BaseCaching
from collections import defaultdict


class LFUCache(BaseCaching):
    """
    LFUCache is a caching system that inherits from BaseCaching
    and follows the LFU (Least Frequently Used) caching strategy.
    """

    def __init__(self):
        """
        Initialize the cache with the parent class constructor.
        """
        super().__init__()
        self.frequency = defaultdict(int)  # Tracks the frequency of access
        self.lru_order = defaultdict(list)  # Tracks the order of keys with same frequency
        self.min_freq = 0  # Tracks the minimum frequency of any item in the cache

    def put(self, key, item):
        """
        Add an item to the cache following the LFU strategy.

        Args:
            key (str): The key under which to store the item.
            item (Any): The item to be stored in the cache.

        If the cache exceeds MAX_ITEMS, the least frequently used item
        is discarded. If there's a tie in frequency, the least recently
        used item is discarded.
        If key or item is None, this method does nothing.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.get(key)  # Update frequency and order
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Get the least frequently used keys
            least_freq_keys = self.lru_order[self.min_freq]
            lru_key = least_freq_keys.pop(0)  # LRU item among those with least frequency
            del self.cache_data[lru_key]
            del self.frequency[lru_key]
            if not least_freq_keys:
                del self.lru_order[self.min_freq]
            print(f"DISCARD: {lru_key}")

        # Add new item
        self.cache_data[key] = item
        self.frequency[key] = 1
        self.lru_order[1].append(key)
        self.min_freq = 1

    def get(self, key):
        """
        Retrieve an item from the cache by key.

        Args:
            key (str): The key corresponding to the desired item.

        Returns:
            The value associated with the key, or None if the key
            is None or does not exist in the cache.
        """
        if key is None or key not in self.cache_data:
            return None

        # Update frequency and LRU order
        freq = self.frequency[key]
        self.lru_order[freq].remove(key)
        if not self.lru_order[freq]:
            del self.lru_order[freq]
            if self.min_freq == freq:
                self.min_freq += 1

        self.frequency[key] += 1
        new_freq = self.frequency[key]
        self.lru_order[new_freq].append(key)

        return self.cache_data[key]

