from setuptools import setup, find_packages


setup(
    name='celery_redis_sync',
    version='1.0.0.dev0',
    author='Zeit Online',
    author_email='zon-backend@zeit.de',
    url='http://www.zeit.de/',
    description="Synchronous Redis result store backend",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    license='BSD',
    install_requires=[
        'celery',
        'redis',
        'setuptools',
    ],
    extras_require={'test': [
        'mock',
        'pytest',
        'testing.redis',
    ]},
    entry_points={
        'console_scripts': [
            # 'binary-name = celery_redis_sync.module:function'
        ],
    }
)
