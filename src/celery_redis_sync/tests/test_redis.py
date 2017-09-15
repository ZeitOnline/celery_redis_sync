import celery


@celery.shared_task
def test_task():
    return 42


def test_redis_should_set_job_id(celery_test_app):
    res = test_task.delay()
    res.state
