#!/usr/bin/python3
"""
Initialization module for the models package.
"""
from models.engine.file_storage import FileStorage

# Create a unique FileStorage instance for the application
storage = FileStorage()
# Call reload() method on this variable
storage.reload()
