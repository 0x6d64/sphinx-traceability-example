#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
implements a minimal example of an implemenation of some software
"""

class Exemplum(object):
    def __init__(self):
        """
        creates the object with internal data storage (:py:class:`list`).
        """
        self._data = list()

    def add_data(self, data):
        """
        :param data: the data to add to the storage
        """
        self._data.append(data)

    def clear(self):
        """
        empties the internal data storage
        :return: None
        """
        self._data = list()

    def __len__(self):
        """
        :return: elements in the data storage
        """
        return len(self._data)
