=================
celery_redis_sync
=================

Synchronous Redis result store backend.

This may be of use when utilizing a redis result backend as a simple data store
without establishing a Pub/Sub connection, thus providing multiple, independent
applications to access, edit and remove stored data.


Usage
=====

* Configure the provided backend `SynchronousRedisBackend` as your celery result backend


Run tests
=========

Using `tox`_ and `py.test`_. Maybe install ``tox`` (e.g. via ``pip install tox``)
and then simply run ``tox``.

.. _`tox`: http://tox.readthedocs.io/
.. _`py.test`: http://pytest.org/
