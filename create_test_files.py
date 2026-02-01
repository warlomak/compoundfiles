#!/usr/bin/env python
"""
Script to create test files for the compound file library
"""
import os
from compoundfiles.writer import CompoundFileWriter

def create_small_with_dirs():
    """Create a small compound file with directories"""
    filename = os.path.join('data', 'small_with_dirs.ert')
    
    with CompoundFileWriter(filename) as writer:
        # Create a storage
        storage = writer.create_storage(writer.root, "TestStorage")
        
        # Create a stream inside the storage
        writer.create_stream(storage, "TestStream", b"Test data inside storage")
        
        # Create another stream in root
        writer.create_stream(writer.root, "RootStream", b"Root level data")
    
    print(f"Created {filename}")

def create_small_without_dirs():
    """Create a small compound file without directories"""
    filename = os.path.join('data', 'small_without_dirs.ert')
    
    with CompoundFileWriter(filename) as writer:
        # Create a single stream in root
        writer.create_stream(writer.root, "SimpleStream", b"Just some simple data")
    
    print(f"Created {filename}")

def create_big_with_dirs():
    """Create a bigger compound file with directories"""
    filename = os.path.join('data', 'big_with_dirs.MD')
    
    with CompoundFileWriter(filename) as writer:
        # Create multiple storages
        storage1 = writer.create_storage(writer.root, "Documents")
        storage2 = writer.create_storage(writer.root, "Images")
        
        # Create streams in first storage
        writer.create_stream(storage1, "doc1.txt", b"Document 1 content")
        writer.create_stream(storage1, "doc2.txt", b"Document 2 content")
        
        # Create streams in second storage
        writer.create_stream(storage2, "img1.jpg", b"Image 1 binary data" + b"\x00" * 100)
        writer.create_stream(storage2, "img2.png", b"Image 2 binary data" + b"\x00" * 200)
        
        # Create some streams in root
        writer.create_stream(writer.root, "config.xml", b"<config><setting>value</setting></config>")
        writer.create_stream(writer.root, "readme.txt", b"This is a readme file")
    
    print(f"Created {filename}")

if __name__ == "__main__":
    # Create the data directory if it doesn't exist
    os.makedirs('data', exist_ok=True)
    
    create_small_with_dirs()
    create_small_without_dirs()
    create_big_with_dirs()
    
    print("All test files created successfully!")