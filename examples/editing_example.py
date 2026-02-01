#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Example of using the compoundfiles library for editing OLE Compound files.

This example demonstrates:
- Opening an existing compound file for editing
- Adding new streams and storages
- Renaming existing elements
- Deleting elements
"""

import compoundfiles as cf

def edit_compound_file(filename):
    """
    Example of editing an OLE Compound file

    Args:
        filename (str): Path to the file to edit
    """
    print(f"Editing file: {filename}")
    
    with cf.CompoundFileEditor(filename) as editor:
        # Add a new storage to the root
        editor.create_storage(editor.root, "NewStorage")

        # Add a new stream to the root
        editor.create_stream(editor.root, "NewFile.txt", "New file content".encode('utf-8'))

        # Add a stream to the newly created storage
        new_storage = editor.root["NewStorage"]
        editor.create_stream(new_storage, "NewNestedFile.txt", "Content in new storage".encode('utf-8'))
        
        # If there are existing elements, rename one of them
        # (assuming the file has at least one stream)
        for item in editor.root:
            if item.isfile:
                print(f"Renaming file: {item.name}")
                editor.rename(item, f"Renamed_{item.name}")
                break

        # Save changes
        editor.save()
        print("Changes saved")

def add_to_existing_file(filename):
    """
    Example of adding data to an existing file

    Args:
        filename (str): Path to the file to edit
    """
    print(f"Adding data to file: {filename}")

    with cf.CompoundFileEditor(filename) as editor:
        # Add a new stream with edit information
        edit_info = f"File edited by {__file__}"
        editor.create_stream(editor.root, "EditInfo.txt", edit_info.encode('utf-8'))

        # Save changes
        editor.save()
        print("Edit information added")

if __name__ == "__main__":
    # Usage examples (replace with actual file)
    # edit_compound_file("path/to/your/compound_file.cfb")
    # add_to_existing_file("path/to/your/compound_file.cfb")
    print("OLE Compound file editing examples")
    print("To run examples, specify path to an existing compound file")