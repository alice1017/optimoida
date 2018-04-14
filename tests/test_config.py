#!/usr/bin/env python
# coding: utf-8

import os

from unittest import TestCase
from optimoida.config import get_api_key


class ConfigureTestCase(TestCase):

    def test_ioerror(self):

        _file = "/tmp/optimoida.ini"
        _key = "testapikey"
        content = "[tinypng]\n"
        content += "key = {0}".format(_key)

        with self.assertRaises(IOError):
            get_api_key(_file)

        with open(_file, "w") as fp:
            fp.write(content)

        self.assertEqual(
            get_api_key(_file), _key)

        os.remove(_file)
