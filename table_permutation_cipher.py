# -*- coding: utf-8 -*-
from i_cipher_provider import ICipherProvider
from table_permutation_key_provider import TablePermutationKeyProvider


class TablePermutationCipher(ICipherProvider):
    """ Table Permutation cipher provider"""

    def __init__(self, key_provider):
        """ Initializes class with specific key

            @param key_provider IKeyProvider key for operation
        """
        self._key_provider = key_provider

    def encrypt(self, block):
        """ Encrypt given block with table permutation cipher

            @param block string data to encrypt
        """

        key_1 = self._key_provider.get_key(TablePermutationKeyProvider.KEY_1)
        key_2 = self._key_provider.get_key(TablePermutationKeyProvider.KEY_2)

        block_length = len(key_2)
        rows = len(key_1)

        tbl = [None] * rows

        # fill table
        for i in range(rows):
            tbl[key_1[i] - 1] = block[i * block_length: (i + 1) * block_length]

        res = ""
        # write cypher
        for i in range(block_length):
            for j in range(rows):
                res += tbl[j][key_2[i] - 1]

        return res

    def decrypt(self, cipher):
        """ Decrypt given cipher with table permutation cipher

            @param cipher string data to decrypt
        """
        key_1 = self._key_provider.get_key(TablePermutationKeyProvider.KEY_1)
        key_2 = self._key_provider.get_key(TablePermutationKeyProvider.KEY_2)

        block_length = len(key_2)
        rows = len(key_1)

        tbl = [[None for i in range(block_length)] for j in range(rows)]

        # fill table
        for j in range(block_length):
            for i in range(rows):
                tbl[i][key_2[j] - 1] = cipher[j * rows + i]

        res = ""
        # read table
        for i in range(rows):
            res += "".join(tbl[key_1[i] -1])

        return res

