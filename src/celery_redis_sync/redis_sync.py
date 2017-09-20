# -*- coding: utf-8 -*-
"""Synchronous Redis result store backend."""

from kombu.utils.objects import cached_property
import celery.backends.base
import celery.exceptions

try:
    import redis
    from kombu.transport.redis import get_redis_error_classes
except ImportError:                 # pragma: no cover
    redis = None                    # noqa
    get_redis_error_classes = None  # noqa

E_REDIS_MISSING = """
You need to install the redis library in order to use \
the Redis result store backend.
"""


class SynchronousRedisBackend(celery.backends.base.KeyValueStoreBackend):
    """Synchronous Redis result backend."""

    #: :pypi:`redis` client module.
    redis = redis

    def __init__(self, url=None, connection_pool=None, *args, **kwargs):
        super(SynchronousRedisBackend, self).__init__(*args, **kwargs)
        self.url = url
        _get = self.app.conf.get
        if self.redis is None:
            raise celery.exceptions.ImproperlyConfigured(
                E_REDIS_MISSING.strip())

        self._ConnectionPool = connection_pool

        self.connparams = {
            'host': _get('redis_host') or 'localhost',
            'port': _get('redis_port') or 6379,
            'db': _get('redis_db') or 0,
            # 'password': _get('redis_password'),
            # 'max_connections': self.max_connections,
            # 'socket_timeout': socket_timeout and float(socket_timeout),
            # 'socket_connect_timeout':
            #    socket_connect_timeout and float(socket_connect_timeout),
        }

    def _create_client(self, **params):
        return self.redis.StrictRedis(
            connection_pool=self.ConnectionPool(**params),
        )

    @property
    def ConnectionPool(self):
        if self._ConnectionPool is None:
            self._ConnectionPool = self.redis.ConnectionPool
        return self._ConnectionPool

    @cached_property
    def client(self):
        return self._create_client(**self.connparams)

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
