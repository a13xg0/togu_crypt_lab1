# -*- coding: utf-8 -*-
from i_key_provider import IKeyProvider
import json


class TablePermutationKeyProvider(IKeyProvider):
    """ Table Permutation key provider"""

    KEY_1 = 1
    KEY_2 = 2

    def __init__(self, file_name):
        """ Initializes class with specific file with key

            @param file_name string file with this key
        """
        self._file_name = file_name

    def get_key(self, key_property):
        with open(self._file_name, "r") as f:
            data = json.load(f)

            if key_property == self.KEY_1:
                return data["key_1"]

            if key_property == self.KEY_2:
                return data["key_2"]
