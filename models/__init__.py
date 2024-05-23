#!/usr/bin/python3
"""This module links the base model and storage engine.
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
