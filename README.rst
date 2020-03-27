=============================
pyontruck
=============================

.. image:: https://user-images.githubusercontent.com/4689706/77090966-3504a180-6a08-11ea-8cfb-7ac145d65d43.png
    :target: https://ontruck.com

|build-status| |coverage| |docs| |license|



Django extended by Ontruck-ers

Documentation
-------------

The full documentation is at https://pyontruck.readthedocs.io.

Quickstart
----------

Install pyontruck::

    pip install pyontruck


Features
------------

* Context manager to edit dict
* Retry decorator
* Sequence utils
* Time utils

Running Tests
-------------

Does the code actually work?

Prepare test env

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install -r requirements/test.txt


Run tests

::

    (myenv) $ make test

Run tests in several python versions using tox

::

    (myenv) $ make test-all


Run tests getting code coverage


::

    (myenv) $ make coverage


Generate documentation
----------------------

::

    (myenv) $ pip install -r requirements/dev.txt
    (myenv) $ make docs


.. |build-status| image:: https://travis-ci.org/ontruck/pyontruck.svg?branch=master
    :target: https://travis-ci.org/ontruck/pyontruck
    :alt: Build status

.. |coverage| image:: https://codecov.io/gh/ontruck/pyontruck/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/ontruck/pyontruck
    :alt: Coverage status

.. |docs| image:: https://readthedocs.org/projects/pyontruck/badge/?version=latest
    :target: https://pyontruck.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. |license| image:: https://img.shields.io/pypi/l/celery.svg
    :alt: BSD License
    :target: https://opensource.org/licenses/BSD-3-Clause
