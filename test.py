#! /usr/bin/env python
from configuration import path_configuration
from core import tokenisation

with open(f'{path_configuration.DATA_DIRECTORY}/the_verdict.txt', 'r') as file:
    text_raw = file.read()

tokeniser = tokenisation.Tokeniser(text_raw)
text_1 = 'Hello, do you like tea?'
text_2 = 'In the sunlit terraces of the palace.'
text = '<|endoftext|> '.join((text_1, text_2))
ids = tokeniser.encode(text)
print(ids)
output = tokeniser.decode(ids)
print(output)
