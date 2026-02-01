.. _root:

compoundfiles - Python library for reading/writing OLE Compound Files (CFB)
===========================================================================

A pure Python library for reading, writing, and editing Microsoft's
Compound File Binary (CFB) format (also known as OLE Compound Documents),
used in legacy Microsoft Office files, certain media systems, and scientific applications.

The library supports Python 3.2+ through Python 3.13.2 (Python 2 support has been dropped in this fork).
It emphasizes correctness, performing extensive validity checks on opened files.
By default, non-fatal errors trigger warnings, which developers can manage via Python's ``warnings`` module.

This is a fork of the original project with added writing and editing capabilities:

* **Full Writing Support**: Create new compound files with a compliant Red-Black tree directory structure.
* **Editing Support**: Rename, delete, or add streams and storages in existing files.
* **Enhanced Validation**: Detect and handle corrupted or non-standard files more reliably.
* **Improved Memory Management**: Optimized for large files and MiniFAT streams.
* **Better Compatibility**: Handles edge cases and differences between CFB versions.
* **Git Installation**: Available for installation directly from the git repository.

Original project (forked from): https://github.com/waveform-computing/compoundfiles
Original author: Dave Hughes <dave@waveform.org.uk>
Fork author: warlomak <warlomak@gmail.com>
Fork repository: https://github.com/warlomak/compoundfiles
Bug tracker: https://github.com/warlomak/compoundfiles/issues

Table of Contents
=================

.. toctree::
   :maxdepth: 2
   :numbered:

   install
   quickstart
   examples
   compliance
   api
   changelog
   license


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
