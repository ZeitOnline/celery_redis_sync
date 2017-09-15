import celery.contrib.testing.app
import pytest
import testing.redis


@pytest.fixture(scope='session')
def redis_server():
    server = testing.redis.RedisServer()
    yield server
    server.stop()


@pytest.fixture('session')
def celery_test_app(redis_server):
    dsn = redis_server.dsn()
    app = celery.contrib.testing.app.TestApp(
        __name__,
        backend='celery_redis_sync.redis_sync.SynchronousRedisBackend')
    app.conf.update(redis_host=dsn['host'])
    app.conf.update(redis_port=dsn['port'])
    app.conf.update(redis_db=dsn['db'])
    # XXX commented for debugging
    # worker = celery.contrib.testing.worker.start_worker(app)
    # worker.__enter__()
    with celery.contrib.testing.app.setup_default_app(app):
        app.set_current()
        yield app
        # XXX cleanup needs to be placed somewhere else
        # worker.__exit__(None, None, None)
