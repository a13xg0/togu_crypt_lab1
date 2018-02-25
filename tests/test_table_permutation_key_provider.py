# -*- coding: utf-8 -*-

import unittest
from mock import patch, mock_open
from table_permutation_key_provider import TablePermutationKeyProvider


class PermutationKeyProviderTestCase(unittest.TestCase):
    def test_init_creation_initializationCorrect(self):
        key_provider = TablePermutationKeyProvider("some file name")

        self.assertEqual(key_provider._file_name, "some file name", "invalid file name assignment")

    @patch("table_permutation_key_provider.open", new_callable=mock_open, create=True, read_data="{\"key_1\": [1, 2]}")
    def test_get_key_AnyParameter_fileOpens(self, fake_open):

        key_provider = TablePermutationKeyProvider("some.file")
        key_provider.get_key(TablePermutationKeyProvider.KEY_1)

        fake_open.assert_called_with("some.file", "r")

    @patch("json.load", return_value={'key_1': '1234456', 'key_2': '5662345'})
    @patch("table_permutation_key_provider.open", new_callable=mock_open, create=True, read_data="{\"key_1\": [1, 2]}")
    def test_get_key_AnyParameter_key1(self, fake_open, fake_json_load):
        key_provider = TablePermutationKeyProvider("some.file")

        result = key_provider.get_key(TablePermutationKeyProvider.KEY_1)

        self.assertEqual('1234456', result, 'invalid key value response')

    @patch("json.load", return_value={'key_1': '1234456', 'key_2': '5662345'})
    @patch("table_permutation_key_provider.open", new_callable=mock_open, create=True, read_data="{\"key_1\": [1, 2]}")
    def test_get_key_AnyParameter_key2(self, fake_open, fake_json_load):
        key_provider = TablePermutationKeyProvider("some.file")

        result = key_provider.get_key(TablePermutationKeyProvider.KEY_2)

        self.assertEqual('5662345', result, 'invalid key value response')


if __name__ == '__main__':
    unittest.main()