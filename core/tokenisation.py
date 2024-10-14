"""
A module that contains customised objects and functions for word tokenisation.

Author: Roldbach
Date: 12/10/2024
"""
from collections import abc
import re

DELIMITER = r'([,.?_!"()\']|--|\s)'

# {{{ Tokeniser
class Tokeniser:
    """A class that can encode/decode texts into IDs and vice versa."""
    
    # {{{ __init__
    def __init__(self, text: str, delimiter: str = DELIMITER) -> None:
        self._delimiter = delimiter
        self._vocabulary = self._construct_vocabulary(text)
        self._vocabulary_inverse = self._construct_vocabulary_inverse()
    # }}}

    # {{{ _construct_vocabulary
    def _construct_vocabulary(self, text: str) -> dict[str,int]:
        token_all = self._tokenise(text)
        token_set = set(token_all)
        token_set = sorted(token_set)
        token_set = self._add_special_tokens(token_set)
        vocabulary = {token:token_id for token_id, token in enumerate(token_set)}
        return vocabulary
    # }}}

    # {{{ _construct_vocabulary_inverse
    def _construct_vocabulary_inverse(self) -> dict[int,str]:
        return {token_id:token for token, token_id in self._vocabulary.items()}
    # }}}

    # {{{ _tokenise
    def _tokenise(self, text: str) -> tuple[str,...]:
        token_all = re.split(self._delimiter, text)
        token_all = tuple(token.strip() for token in token_all if token.strip())
        return token_all
    # }}}

    # {{{ _add_special_tokens
    def _add_special_tokens(self, token_set: set[str]) -> set[str]:
        token_special_all = ('<|endoftext|>', '<|unknown|>')
        token_set.extend(token_special_all)
        return token_set
    # }}}

    # {{{ encode
    def encode(self, text: str) -> tuple[int,...]:
        token_all = self._tokenise(text)
        token_all = tuple(
            token if token in self._vocabulary else '<|unknown|>'
            for token in token_all
        )
        token_id_all = tuple(self._vocabulary[token] for token in token_all)
        return token_id_all
    # }}}

    # {{{ decode
    def decode(self, token_id_all: tuple[int,...]) -> str:
        token_all = tuple(
            self._vocabulary_inverse[token_id] for token_id in token_id_all)
        text = ' '.join(token_all)
        text = re.sub(r'\s+([,.:;?!"()\'])', r'\1', text)
        return text
    # }}}
# }}}
