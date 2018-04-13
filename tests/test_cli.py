#!/usr/bin/env python
# coding: utf-8

from unittest import TestCase
from optimoida.cli import parser


class ParserTestCase(TestCase):

    def test_positional_args(self):

        cmd = [".", "..", "../.."]
        args = parser.parse_args(cmd)

        self.assertEqual(args.path, cmd)

    def test_optional_args(self):

        args = parser.parse_args(["--dev"])
        self.assertTrue(args.dev)
