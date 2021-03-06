from setuptools import setup, find_packages

tests_require = [
    'nose',
    'nose-cov',
    'mock',
]

version = '0.0.0'
try:
    import sftpproxy
    version = sftpproxy.__version__
except ImportError:
    pass

setup(
    name='sftpproxy',
    version=version,
    packages=find_packages(),
    url='https://github.com/balanced/sftpproxy',
    author='victorlin',
    author_email='victorlin@balancedpayments.com',
    install_requires=[
        'paramiko >=1.12,<2.0',
        'pycrypto >=2.6.1,<3.0',
        'pwho >=0.1.0,<0.2',
        'netaddr >=0.7.10,<0.8',
    ],
    extras_require=dict(
        tests=tests_require,
    ),
    tests_require=tests_require,
    test_suite='nose.collector',
    entry_points="""\
    """
)
