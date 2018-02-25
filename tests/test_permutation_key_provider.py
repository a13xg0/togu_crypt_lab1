# -*- coding: utf-8 -*-

import unittest
from mock import patch, mock_open
from permutation_key_provider import PermutationKeyProvider


class PermutationKeyProviderTestCase(unittest.TestCase):
    def test_init_creation_initializationCorrect(self):
        key_provider = PermutationKeyProvider("some file name")

        self.assertEqual(key_provider._file_name, "some file name", "invalid file name assignment")

    @patch("permutation_key_provider.open", new_callable=mock_open, create=True, read_data="{\"key\": [1, 2]}")
    def test_get_key_AnyParameter_fileOpens(self, fake_open):

        key_provider = PermutationKeyProvider("some.file")
        key_provider.get_key(PermutationKeyProvider.KEY_SIMPLE)

        fake_open.assert_called_with("some.file", "r")

    @patch("json.load", return_value={'key': '1234456'})
    @patch("permutation_key_provider.open", new_callable=mock_open, create=True, read_data="{\"key\": [1, 2]}")
    def test_get_key_AnyParameter_rightResponse(self, fake_open, fake_json_load):
        key_provider = PermutationKeyProvider("some.file")

        result = key_provider.get_key(PermutationKeyProvider.KEY_SIMPLE)

        self.assertEqual('1234456', result, 'invalid key value response')


if __name__ == '__main__':
    unittest.main()