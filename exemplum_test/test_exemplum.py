#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""tests for exemplum module"""

from unittest import TestCase
from exemplum import Exemplum

class TestExemplum(TestCase):
    """test cases for class Exemplum"""
    def test_add_data(self):
        """
        .. testcase:: tc_1
            :tests: req_3

            initalize an :py:class:`Exemplum` object and add an element.
            Inspect the data storage if added data is there.
        """
        test_inst = Exemplum()
        test_inst.add_data('some data')
        self.assertIn('some data', test_inst._data)  # pylint: disable=protected-access

    def test_len_method(self):
        """
        .. testcase:: tc_2
            :tests: req_4 req_2

            initialize an exemplum object and check if :py:meth:`exemplum.Exemplum.__len__` returns 0.
            Add several elements and check each time that the count increases by 1.
        """
        test_inst = Exemplum()
        self.assertEqual(0, len(test_inst))

        for idx in range(1, 1000):
            test_inst.add_data(idx * idx)
            self.assertEqual(idx, len(test_inst))

    def test_usecase(self):
        """
        .. testcase:: tc_3
            :tests: req_2 req_4 req_3

            This testcase tests several requirements at once using a typical use case.
        """
        test_inst = Exemplum()

        test_inst.add_data('some data')
        self.assertIn('some data', test_inst._data)  # pylint: disable=protected-access

        test_inst.clear()
        self.assertEqual(0, len(test_inst))

    def test_nothing(self):
        """
        .. testcase:: tc_4
            :tests:

            This test does nothing.
        """
