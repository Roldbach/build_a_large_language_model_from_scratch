#! /usr/bin/env python
"""
A script used to retrieve The Verdict text data.

Author: Roldbach
Date: 12/10/2024
"""
from urllib import request

from configuration import path_configuration

url = (
    'https://raw.githubusercontent.com/rasbt/LLMs-from-scratch/'
    'main/ch02/01_main-chapter-code/the-verdict.txt'
)
file_path = f'{path_configuration.DATA_DIRECTORY}/the_verdict.txt'
request.urlretrieve(url, file_path)
