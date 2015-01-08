#!/usr/bin/env python

import os
import sys
import uuid
from pip.req import parse_requirements
from codecs import open


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

packages = [
    'python-kafka-logging',
]

install_requirements = parse_requirements('requirements.txt', None, None, None, uuid.uuid1())
requirements = [str(ir.req) for ir in install_requirements]

with open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()

setup(
    name='python-kafka-logging',
    version=0.2,
    description='Simple python logging handler for forwarding logs to a kafka server.',
    long_description=readme + '\n\n',
    maintainer="Taykey INC",
    maintainer_email="github@taykey.com",
    author='Avihoo Mamka',
    author_email='avihoo@taykey.com',
    url='https://github.com/taykey/python-kafka-logging',
    packages=packages,
    package_data={'': ['LICENSE.txt', 'README.rst']},
    include_package_data=True,
    install_requires=requirements,
    license='Apache 2.0',
    zip_safe=False,
    keywords=['python', 'logging', 'handler', 'example', 'kafka', 'logs', 'logstash', 'formatter'],
    classifiers=(
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ),
)
