# Examples for compoundfiles library

This directory contains examples of using the compoundfiles library to work with OLE Compound files.

## Example structure

- `reading_example.py` - examples of reading OLE Compound files
- `writing_example.py` - examples of creating new OLE Compound files
- `editing_example.py` - examples of editing existing files
- `complex_example.py` - comprehensive example demonstrating all capabilities

## Main capabilities

### Reading files
- Opening and analyzing OLE Compound file structures
- Viewing directory and file contents
- Reading data from streams

### Writing files
- Creating new OLE Compound files
- Creating directory structures (storages)
- Writing data to streams
- Supporting nested structures

### Editing files
- Adding new files and directories
- Renaming existing elements
- Deleting elements
- Saving changes

## Running examples

To run examples, use the Python command:

```bash
python reading_example.py
python writing_example.py
python editing_example.py
python complex_example.py
```

Note that some examples require existing OLE Compound files for demonstration. For testing new file creation, no additional files are required.