import celery
import pytest
import redis
import testing.redis


@pytest.fixture(scope='session')
def redis_server():
    server = testing.redis.RedisServer()
    yield server
    server.stop()


@pytest.fixture('function')
def eager_celery_app(redis_server):
    redis_client = redis.Redis(**redis_server.dsn())
    app = celery.Celery(
        __name__,
        broker=redis_client,
        backend='celery_redis_sync.redis_sync.RedisBackend')
    app.conf.update(task_always_eager=True)
    app.conf.update(task_eager_propagates=True)
    with celery.contrib.testing.app.setup_default_app(app):
        app.set_current()
        yield app
