#!/usr/bin/env python3
"""Basic cache"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """basic cache"""

    def put(self, key, item):
        """Add item to cache data with the given key."""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Get item from cache data based on the given key."""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
