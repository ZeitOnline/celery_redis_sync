import celery.backends.base
import celery.backends.redis


def select_backend(**kw):
    """Override the built-in redis:// backend URL to also support redis+sync://
    """
    url = kw.get('url', '')
    # See celery.app.backends.by_url
    if url.startswith('sync'):
        cls = SynchronousRedisBackend
    else:
        cls = celery.backends.redis.RedisBackend
    return cls(**kw)


class SynchronousRedisBackend(
        celery.backends.base.SyncBackendMixin,
        celery.backends.redis.RedisBackend):
    """Synchronous Redis result backend."""

    def ResultConsumer(self, *args, **kw):
        return None

    def on_task_call(self, *args, **kw):
        pass

    def _set(self, key, value):
        # We omit the self.client.publish() call.
        if self.expires:
            self.client.setex(key, self.expires, value)
        else:
            self.client.set(key, value)
