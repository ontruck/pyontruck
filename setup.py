#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pip

try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

parsed_requirements = parse_requirements(
    'requirements/prod.txt',
    session=pip.download.PipSession()
)

parsed_test_requirements = parse_requirements(
    'requirements/test.txt',
    session=pip.download.PipSession()
)


requirements = [str(ir.req) for ir in parsed_requirements]
test_requirements = [str(tr.req) for tr in parsed_test_requirements]


setup(
    name='pyontruck',
    version='0.1.0',
    description="Python utils for Ontruck projects",
    long_description=readme + '\n\n' + history,
    author="Jorge Arevalo",
    author_email='jorge.arevalo@ontruck.com',
    url='https://github.com/jorgeas80/pyontruck',
    packages=[
        'pyontruck',
    ],
    package_dir={'pyontruck':
                 'pyontruck'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='pyontruck',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License (MIT)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
