# -*- coding: utf-8 -*-
from i_key_provider import IKeyProvider
import json


class PermutationKeyProvider(IKeyProvider):
    """ Permutation key provider"""

    KEY_SIMPLE = 1

    def __init__(self, file_name):
        """ Initializes class with specific file with key

            @param file_name string file with this key
        """
        self._file_name = file_name

    def get_key(self, key_property):
        """ because there is only one key, we will not check key_property passed """
        with open(self._file_name, "r") as f:
            data = json.load(f)
            return data["key"]
