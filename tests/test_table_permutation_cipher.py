# -*- coding: utf-8 -*-

import unittest
from mock import patch, mock_open
from table_permutation_cipher import TablePermutationCipher
from table_permutation_key_provider import TablePermutationKeyProvider
from i_key_provider import IKeyProvider


class FakeKeyProvider(IKeyProvider):
    def __init__(self, key1, key2):
        self._key1 = key1
        self._key2 = key2

    def get_key(self, key_property):
        if key_property == TablePermutationKeyProvider.KEY_1:
            return self._key1

        if key_property == TablePermutationKeyProvider.KEY_2:
            return self._key2


class PermutationCipherTestCase(unittest.TestCase):
    def getKey(self):
        return FakeKeyProvider([5, 3, 1, 2, 4, 6], [3, 4, 1, 2])

    def test_init_creation_initializationCorrect(self):
        cipher = TablePermutationCipher("some provider")

        self.assertEqual(cipher._key_provider, "some provider", "invalid provider assignment")

    def test_encrypt_FIO_TruncatedCipher(self):

        cipher = TablePermutationCipher(self.getKey())
        res = cipher.encrypt(u"ГОРБАЧ_АЛЕКСАНДР_ВИТАЛЬЕВИЧ")

        self.assertEqual(u"КД_ИРЬСРАТБЕЛАА_ГАЕНЧВОЛ", res, "error in cypher algorithm")

    def test_decrypt_Cipher_RightResponse(self):

        cipher = TablePermutationCipher(self.getKey())
        res = cipher.decrypt(u"КД_ИРЬСРАТБЕЛАА_ГАЕНЧВОЛ")

        self.assertEqual(u"ГОРБАЧ_АЛЕКСАНДР_ВИТАЛЬЕ", res, "error in cypher algorithm")


if __name__ == '__main__':
    unittest.main()