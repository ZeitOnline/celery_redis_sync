# -*- coding: utf-8 -*-
"""Synchronous Redis result store backend."""
import celery.backends.base


class RedisBackend(celery.backends.base.BaseKeyValueStoreBackend):
    """Synchronous Redis result backend."""

    def __init__(self, url=None, *args, **kwargs):
        super(RedisBackend, self).__init__(*args, **kwargs)
        self.url = url

    def get(self, key):
        return self.client.get(key)

    def mget(self, keys):
        return self.client.get_multi(keys)

    def set(self, key, value):
        return self.client.set(key, value, self.expires)

    def delete(self, key):
        return self.client.delete(key)

    def incr(self, key):
        return self.client.incr(key)
