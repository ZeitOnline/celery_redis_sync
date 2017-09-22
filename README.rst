=================
celery_redis_sync
=================

Synchronous Redis result store backend.

This may be of use when utilizing a redis result backend as a simple data store
without establishing a Pub/Sub connection, thus providing multiple, independent
applications to access, edit and remove stored data.


Usage
=====

Make sure the ``celery_redis_sync`` module is importable, and then simply
specify a ``redis+sync://`` URL in your celery configuration ``result_backend``
setting instead of the built-in ``redis://`` URL scheme.


Run tests
=========

Using `tox`_ and `py.test`_. Maybe install ``tox`` (e.g. via ``pip install tox``)
and then simply run ``tox``.

For the integration tests you need to have the redis binary installed (tests
start `their own server`_).

.. _`tox`: http://tox.readthedocs.io/
.. _`py.test`: http://pytest.org/
.. _`their own server`: https://pypi.python.org/pypi/testing.redis
