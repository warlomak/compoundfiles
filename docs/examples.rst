.. _examples:

========
Examples
========

This section provides practical examples demonstrating how to use the compoundfiles library for various tasks.

Reading Files
=============

The following example demonstrates how to read an existing OLE Compound file:

.. code-block:: python

    import compoundfiles as cf

    # Open an existing compound file
    with cf.CompoundFileReader('example.cfb') as doc:
        # List contents of the root directory
        for entry in doc.root:
            if entry.isfile:
                print(f"File: {entry.name} (size: {entry.size})")
            else:
                print(f"Storage: {entry.name}")
        
        # Read content of a specific stream
        with doc.open('Storage1/File1.txt') as stream:
            content = stream.read()
            print(content)

Creating New Files
==================

The following example demonstrates how to create a new OLE Compound file:

.. code-block:: python

    import compoundfiles as cf

    # Create a new compound file
    with cf.CompoundFileWriter('new_file.cfb') as writer:
        # Create a storage (directory-like structure)
        storage = writer.create_storage(writer.root, "MyStorage")
        
        # Create a stream in the root
        writer.create_stream(writer.root, "RootFile.txt", b"Content of root file")
        
        # Create a stream in the storage
        writer.create_stream(storage, "NestedFile.txt", b"Content of nested file")

Editing Existing Files
======================

The following example demonstrates how to edit an existing OLE Compound file:

.. code-block:: python

    import compoundfiles as cf

    # Edit an existing compound file
    with cf.CompoundFileEditor('existing_file.cfb') as editor:
        # Add a new stream
        editor.create_stream(editor.root, "NewFile.txt", b"New content")
        
        # Add a new storage
        new_storage = editor.create_storage(editor.root, "NewStorage")
        
        # Rename an existing entity
        if "OldName.txt" in editor.root:
            editor.rename(editor.root["OldName.txt"], "NewName.txt")
        
        # Save changes
        editor.save()

Complete Examples
=================

For complete working examples, see the `examples` directory in the source repository:

- `reading_example.py` - Demonstrates reading compound files
- `writing_example.py` - Demonstrates creating new compound files
- `editing_example.py` - Demonstrates editing existing compound files
- `complex_example.py` - Comprehensive example showing all capabilities

You can run these examples directly to see the library in action:

.. code-block:: bash

    python examples/reading_example.py
    python examples/writing_example.py
    python examples/editing_example.py
    python examples/complex_example.py