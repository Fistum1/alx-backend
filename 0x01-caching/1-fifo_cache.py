#!/usr/bin/python3

'''
Task 1: FIFO caching.
'''


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    A class that inherits from BaseCaching and is a caching system
    """
    def __init__(self):
        """
        It initializes the cache.
        """
        super().__init__()
        self.data = {}
        self.next_in, self.next_out = 0, 0

    def _pop(self):
        """
        FIFO algorithm, remove element
        """
        self.next_out += 1
        key = self.data[self.next_out]
        del self.data[self.next_out], self.cache_data[key]

    def _push(self, key, item):
        """
        FIFO algorithm, add element
        """
        if len(self.cache_data) > BaseCaching.MAX_ITEMS - 1:
            print("DISCARD: {}".format(self.data[self.next_out + 1]))
            self._pop()
        self.cache_data[key] = item
        self.next_in += 1
        self.data[self.next_in] = key

    def put(self, key, item):
        """
        It assigns to the dictionary
        """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
            else:
                self._push(key, item)

    def get(self, key):
        """
        It returns the value linked
        """
        if key is None or self.cache_data.get(key) is None:
            return None
        if key in self.cache_data:
            value = self.cache_data[key]
            return value
