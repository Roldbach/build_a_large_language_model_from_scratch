"""
A script used to setup customised packages and modules used in the project.

Author: Roldbach
Date: 12/10/2024
"""
import setuptools

setuptools.setup(
    name = 'build_a_large_language_model_from_scratch',
    version = '0.0.1',
    author = 'Roldbach',
    packages = setuptools.find_packages(exclude=['tests', 'tests.*']),
)
