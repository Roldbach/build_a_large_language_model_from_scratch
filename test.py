#! /usr/bin/env python
from configuration import path_configuration
from core import tokenisation

with open(f'{path_configuration.DATA_DIRECTORY}/the_verdict.txt', 'r') as file:
    text_raw = file.read()

tokeniser = tokenisation.Tokeniser(text_raw)
text = """"It's the last he painted, you know,"
 Mrs. Gisburn said with pardonable pride."""
ids = tokeniser.encode(text)
output = tokeniser.decode(ids)
print(output)
