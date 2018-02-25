# -*- coding: utf-8 -*-
import abc


class IKeyProvider():
    """ Key providers classes interface """
    @abc.abstractmethod
    def get_key(self, key_property):
        """ get key for specified property

            @param: key_property int Describes which key part should be returned
        """
        raise NotImplementedError
