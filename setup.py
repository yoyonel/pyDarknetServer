#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    README = readme_file.read()

with open('HISTORY.rst') as history_file:
    HISTORY = history_file.read()

REQUIREMENTS = []

SETUP_REQUIREMENTS = ['pytest-runner', ]

TEST_REQUIREMENTS = ['pytest', ]

setup(
    author="Lionel Atty",
    author_email='yoyonel@hotmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    python_requires='>=3.6',
    description="Python Darknet Server",
    install_requires=REQUIREMENTS,
    license="MIT license",
    long_description=README + '\n\n' + HISTORY,
    include_package_data=True,
    keywords='pydarknetserver',
    name='pydarknetserver',
    packages=find_packages(include=['pydarknetserver']),
    setup_requires=SETUP_REQUIREMENTS,
    test_suite='tests',
    tests_require=TEST_REQUIREMENTS,
    url='https://github.com/yoyonel/pydarknetserver',
    version='0.2.0',
    zip_safe=False,
)
