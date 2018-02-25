# -*- coding: utf-8 -*-
import abc


class ICipherProvider():
    """ Cypher classes interface """
    @abc.abstractmethod
    def encrypt(self, block):
        """ Encrypts block, returns encrypted data

            @param: block string The block with data to encrypt
        """
        raise NotImplementedError

    def decrypt(self, cipher):
        """ Decrypts block, returns decrypted data

            @param: block string The block with cipher text
        """
        raise NotImplementedError
