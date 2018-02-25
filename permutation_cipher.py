# -*- coding: utf-8 -*-
from i_cipher_provider import ICipherProvider
from permutation_key_provider import PermutationKeyProvider


class PermutationCipher(ICipherProvider):
    """ Permutation cipher provider"""

    def __init__(self, key_provider):
        """ Initializes class with specific key

            @param key_provider IKeyProvider key for operation
        """
        self._key_provider = key_provider

    def encrypt_chunk(self, chunk):
        """ Encrypt chunk of code with length equals to key length

            @param chunk string string with data
        """
        res = ""
        for position in self._key_provider.get_key(PermutationKeyProvider.KEY_SIMPLE):
            res += chunk[position - 1]

        return res

    def decrypt_chunk(self, chunk):
        """ Decrypt chunk of code with length equals to key length

            @param chunk string string with cipher
        """
        block_length = len(self._key_provider.get_key(PermutationKeyProvider.KEY_SIMPLE))

        res = [None] * block_length
        for i in range(block_length):
            res[self._key_provider.get_key(PermutationKeyProvider.KEY_SIMPLE)[i] - 1] = chunk[i]

        return "".join(res)

    def encrypt(self, block):
        """ Encrypt given block with permutation cipher

            @param block string data to encrypt
        """
        block_length = len(self._key_provider.get_key(PermutationKeyProvider.KEY_SIMPLE))

        res = ""

        for i in range(len(block) // block_length):
            res += self.encrypt_chunk(block[i * block_length: (i + 1) * block_length])

        return res

    def decrypt(self, cipher):
        """ Decrypt given cipher with permutation cipher

            @param cipher string data to decrypt
        """
        block_length = len(self._key_provider.get_key(PermutationKeyProvider.KEY_SIMPLE))
        number_of_parts = len(cipher) // block_length

        res = ""

        for i in range(number_of_parts):
            res += self.decrypt_chunk(cipher[i * block_length: (i + 1) * block_length])

        return res

