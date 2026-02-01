#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Example of using the compoundfiles library for reading OLE Compound files.

This example demonstrates:
- Opening an existing compound file
- Viewing file structure
- Reading stream contents
"""

import compoundfiles as cf

def read_compound_file(filename):
    """
    Example of reading an OLE Compound file

    Args:
        filename (str): Path to the file to read
    """
    print(f"Opening file: {filename}")

    with cf.CompoundFileReader(filename) as doc:
        print("\nContents of root directory:")
        for entry in doc.root:
            if entry.isfile:
                print(f"  File: {entry.name} (size: {entry.size} bytes)")
            else:
                print(f"  Directory: {entry.name}")

        print("\nReading content of first stream (if any):")
        for entry in doc.root:
            if entry.isfile:
                print(f"\nReading stream: {entry.name}")
                with doc.open(entry) as stream:
                    data = stream.read()
                    print(f"  First 100 bytes: {data[:100]}")
                break

if __name__ == "__main__":
    # Usage example (replace with actual file)
    # read_compound_file("path/to/your/compound_file.doc")
    print("OLE Compound file reading example")
    print("To run the example, specify path to an existing compound file")