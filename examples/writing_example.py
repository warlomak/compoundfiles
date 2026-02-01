#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Example of using the compoundfiles library for writing OLE Compound files.

This example demonstrates:
- Creating a new compound file
- Creating directory structure
- Writing data to streams
"""

import compoundfiles as cf

def create_compound_file(filename):
    """
    Example of creating a new OLE Compound file

    Args:
        filename (str): Path to the file to create
    """
    print(f"Creating new file: {filename}")

    with cf.CompoundFileWriter(filename) as writer:
        # Create a storage (directory)
        storage = writer.create_storage(writer.root, "MyStorage")

        # Create a stream in the root
        writer.create_stream(writer.root, "RootLevelFile.txt", "This is a file in root".encode('utf-8'))

        # Create a stream inside the storage
        writer.create_stream(storage, "NestedFile.txt", "This is a file inside storage".encode('utf-8'))

        # Create nested storages
        nested_storage = writer.create_storage(storage, "NestedStorage")
        writer.create_stream(nested_storage, "DeepFile.txt", "File deep in structure".encode('utf-8'))

        print("File successfully created with this structure:")
        print("├── RootLevelFile.txt")
        print("└── MyStorage/")
        print("    ├── NestedFile.txt")
        print("    └── NestedStorage/")
        print("        └── DeepFile.txt")

if __name__ == "__main__":
    # Usage example
    # create_compound_file("example_output.cfb")
    print("OLE Compound file creation example")
    print("To run the example, uncomment the function call")