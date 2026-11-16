from testcontainers.community.redis import RedisContainer
import celery.contrib.testing.app
import celery.contrib.testing.worker
import pytest


@pytest.fixture(scope='session')
def redis_server():
    with RedisContainer() as server:
        yield server


@pytest.fixture(scope='session')
def celery_test_app(redis_server):
    app = celery.contrib.testing.app.TestApp(__name__, set_as_current=True)
    port = redis_server.get_exposed_port(redis_server.port)
    app.conf['result_backend'] = f'redis+sync://localhost:{port}/0'
    with celery.contrib.testing.app.setup_default_app(
        app
    ), celery.contrib.testing.worker.start_worker(app):
        yield app


# celery.contrib.testing.worker expects a 'ping' task, so it can check that the
# worker is running properly.
@celery.shared_task(name='celery.ping')
def celery_ping():
    return 'pong'
