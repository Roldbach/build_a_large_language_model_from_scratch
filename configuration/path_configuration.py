"""
A module that contains directory/file paths used in the project.

Author: Roldbach
Date: 12/10/2024
"""
import pathlib

# Root Directory
ROOT_DIRECTORY = pathlib.Path.cwd()
for parent in ROOT_DIRECTORY.parents:
    if (parent/'setup.py').exists():
        ROOT_DIRECTORY = parent

# Other Directories
DATA_DIRECTORY = f'{ROOT_DIRECTORY}/data'
