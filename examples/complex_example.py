#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Comprehensive example of using the compoundfiles library.

This example demonstrates all main capabilities of the library:
- Reading existing files
- Creating new files
- Editing existing files
"""

import compoundfiles as cf
import tempfile
import os

def demo_reading():
    """Demonstration of file reading"""
    print("=" * 50)
    print("READING DEMONSTRATION")
    print("=" * 50)
    
    # Create a temporary file for demonstration
    with tempfile.NamedTemporaryFile(suffix='.cfb', delete=False) as temp_file:
        temp_filename = temp_file.name

    try:
        # First, create a file for reading
        with cf.CompoundFileWriter(temp_filename) as writer:
            writer.create_stream(writer.root, "DemoFile.txt", "Demo file".encode('utf-8'))
            storage = writer.create_storage(writer.root, "DemoStorage")
            writer.create_stream(storage, "NestedFile.txt", "Nested file".encode('utf-8'))

        # Now read it
        with cf.CompoundFileReader(temp_filename) as reader:
            print(f"Structure of file {temp_filename}:")
            for item in reader.root:
                if item.isdir:
                    print(f"  [STORAGE] {item.name}")
                    for subitem in item:
                        print(f"    [FILE] {subitem.name} (size: {subitem.size})")
                else:
                    print(f"  [FILE] {item.name} (size: {item.size})")

                # Read file contents
                if item.isfile:
                    with reader.open(item) as stream:
                        content = stream.read()
                        print(f"    Content: {content}")

    finally:
        # Remove temporary file
        if os.path.exists(temp_filename):
            os.unlink(temp_filename)

def demo_writing():
    """Demonstration of file writing"""
    print("\n" + "=" * 50)
    print("WRITING DEMONSTRATION")
    print("=" * 50)

    demo_filename = "demo_output.cfb"

    with cf.CompoundFileWriter(demo_filename) as writer:
        # Create complex structure
        writer.create_stream(writer.root, "RootFile.txt", "File in root".encode('utf-8'))

        config_storage = writer.create_storage(writer.root, "Configuration")
        writer.create_stream(config_storage, "settings.ini", "[config]\nenabled=true\n".encode('utf-8'))

        data_storage = writer.create_storage(writer.root, "Data")
        writer.create_stream(data_storage, "data.bin", b"\x00\x01\x02\x03")

        nested_storage = writer.create_storage(data_storage, "NestedData")
        writer.create_stream(nested_storage, "deep_data.txt", "Deep data".encode('utf-8'))

        print(f"Created file {demo_filename} with following structure:")
        print("├── RootFile.txt")
        print("├── Configuration/")
        print("│   └── settings.ini")
        print("└── Data/")
        print("    ├── data.bin")
        print("    └── NestedData/")
        print("        └── deep_data.txt")

    # Check the created file
    with cf.CompoundFileReader(demo_filename) as reader:
        print(f"\nChecking created file {demo_filename}:")
        print(f"Number of items in root: {len(reader.root)}")

    # Remove demo file
    if os.path.exists(demo_filename):
        os.unlink(demo_filename)
        print(f"\nDemo file {demo_filename} removed")

def demo_editing():
    """Demonstration of file editing"""
    print("\n" + "=" * 50)
    print("EDITING DEMONSTRATION")
    print("=" * 50)

    # Create a file for editing
    edit_demo_file = "edit_demo.cfb"

    with cf.CompoundFileWriter(edit_demo_file) as writer:
        writer.create_stream(writer.root, "OriginalFile.txt", "Original content".encode('utf-8'))
        storage = writer.create_storage(writer.root, "OriginalStorage")
        writer.create_stream(storage, "OriginalNested.txt", "Original nested file".encode('utf-8'))

    print(f"Original file {edit_demo_file} created")

    # Edit the file
    with cf.CompoundFileEditor(edit_demo_file) as editor:
        # Add a new file
        editor.create_stream(editor.root, "AddedFile.txt", "Added content".encode('utf-8'))

        # Add a new storage
        new_storage = editor.create_storage(editor.root, "NewStorage")
        editor.create_stream(new_storage, "NewFile.txt", "New file".encode('utf-8'))

        # Rename existing file
        original_file = editor.root["OriginalFile.txt"]
        editor.rename(original_file, "RenamedOriginal.txt")

        # Save changes
        editor.save()
        print("File edited and saved")

    # Check the result
    with cf.CompoundFileReader(edit_demo_file) as reader:
        print(f"\nStructure after editing {edit_demo_file}:")
        for item in reader.root:
            if item.isdir:
                print(f"  [STORAGE] {item.name}")
                if item.name == "OriginalStorage":
                    for subitem in item:
                        print(f"    [FILE] {subitem.name}")
            else:
                print(f"  [FILE] {item.name}")

    # Remove demo file
    if os.path.exists(edit_demo_file):
        os.unlink(edit_demo_file)
        print(f"\nDemo file {edit_demo_file} removed")

def main():
    """Main demonstration function"""
    print("Comprehensive demonstration of compoundfiles library capabilities")
    print("This demonstration shows all main capabilities:")
    print("- Reading OLE Compound files")
    print("- Creating new files")
    print("- Editing existing files")

    demo_reading()
    demo_writing()
    demo_editing()

    print("\n" + "=" * 50)
    print("DEMONSTRATION COMPLETE")
    print("=" * 50)

if __name__ == "__main__":
    main()