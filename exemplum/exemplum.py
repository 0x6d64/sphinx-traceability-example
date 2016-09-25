#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Exemplum(object):
    def __init__(self):
        """
        creates the object with internal data storage (:py:class:`list`).
        """
        self._data = list()
        pass

    def add_data(self, data):
        """
        :param data: the data to add to the storage
        """
        self._data.append(data)

    def __len__(self):
        """
        :return: elements in the data storage
        """
        return len(self._data)
