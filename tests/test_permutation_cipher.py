# -*- coding: utf-8 -*-

import unittest
from mock import patch, mock_open
from permutation_cipher import PermutationCipher
from i_key_provider import IKeyProvider


class FakeKeyProvider(IKeyProvider):
    def __init__(self, key):
        self._key = key

    def get_key(self, key_property):
        return self._key


class PermutationCipherTestCase(unittest.TestCase):
    def getKey(self):
        return FakeKeyProvider([8, 7, 5, 6, 3, 1, 2, 4])

    def test_init_creation_initializationCorrect(self):
        cipher = PermutationCipher("some provider")

        self.assertEqual(cipher._key_provider, "some provider", "invalid provider assignment")

    def test_encrypt_FIO_TruncatedCipher(self):

        cipher = PermutationCipher(self.getKey())
        res = cipher.encrypt(u"ГОРБАЧ_АЛЕКСАНДР_ВИТАЛЬЕВИЧ")

        self.assertEqual(u"А_АЧРГОБРДАНКЛЕСЕЬАЛИ_ВТ", res, "error in cypher algorithm")

    def test_decrypt_Cipher_RightResponse(self):

        cipher = PermutationCipher(self.getKey())
        res = cipher.decrypt(u"А_АЧРГОБРДАНКЛЕСЕЬАЛИ_ВТ")

        self.assertEqual(u"ГОРБАЧ_АЛЕКСАНДР_ВИТАЛЬЕ", res, "error in cypher algorithm")

    def test_encrypt_chunk_Part_Cipher(self):

        cipher = PermutationCipher(self.getKey())
        res = cipher.encrypt_chunk(u"ГОРБАЧ_А")

        self.assertEqual(u"А_АЧРГОБ", res, "error in cypher algorithm")

    def test_decrypt_chunk_Part_Cipher(self):

        cipher = PermutationCipher(self.getKey())
        res = cipher.decrypt_chunk(u"А_АЧРГОБ")

        self.assertEqual(u"ГОРБАЧ_А", res, "error in cypher algorithm")


if __name__ == '__main__':
    unittest.main()