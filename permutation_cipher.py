# -*- coding: utf-8 -*-
from i_cipher_provider import ICipherProvider


class PermutationCipher(ICipherProvider):
    """ Permutation cipher provider"""

    def __init__(self, key_provider):
        """ Initializes class with specific key

            @param key_provider IKeyProvider key for operation
        """
        self._key_provider = key_provider

    def encrypt(self, block):
        pass

    def decrypt(self, cipher):
        pass

