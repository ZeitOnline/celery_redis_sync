import celery.backends.base
import celery.backends.redis


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
