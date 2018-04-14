#!/usr/bin/env python
# coding: utf-8

from unittest import TestCase
from optimoida.core import check_extension


class CoreTestCase(TestCase):

    def test_extension(self):

        testcase = {
            "sample.jpg": True,
            "test.JPG": True,
            "sample.png": True,
            "test.PNG": True,
            "sample.gif": False,
            "test.psd": False
        }

        for path, valid_value in testcase.iteritems():

            if valid_value:
                self.assertEqual(check_extension(path), valid_value)

            else:
                with self.assertRaises(IOError):
                    check_extension(path)
