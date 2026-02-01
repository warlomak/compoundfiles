.. _install:

============
Installation
============

The library has no dependencies in and of itself, and consists entirely of
Python code, so installation should be trivial on most platforms.
Installation from source via git is recommended.


.. _git_install:

Git installation
================

To install from git::

    $ git clone https://github.com/warlomak/compoundfiles.git
    $ cd compoundfiles
    $ pip install -e .

To upgrade the installation::

    $ cd compoundfiles
    $ git pull
    $ pip install -e .

To remove the installation::

    $ pip uninstall compoundfiles

The library is tested and compatible with Python 3.13.2. Installation should work on any Python 3.2+ version.


Development installation
========================

If you wish to develop the library yourself, you are best off doing so within
a virtualenv with source checked out from `GitHub`_ (fork repository), like so::

    $ pip install virtualenv
    $ virtualenv sandbox
    $ source sandbox/bin/activate  # On Windows: sandbox\Scripts\activate
    $ git clone https://github.com/warlomak/compoundfiles.git
    $ cd compoundfiles
    $ pip install -e .

The above uses the included setup.py to perform a development installation
into the constructed virtualenv. The fork repository contains additional
functionality for writing and editing compound files.


.. _GitHub: https://github.com/warlomak/compoundfiles
