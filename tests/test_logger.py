#!/usr/bin/env python
# coding: utf-8

from unittest import TestCase
from optimoida.logging import (
    SUCCESS, FAILURE, logger)


class LoggerTestCase(TestCase):

    def test_flag_value(self):

        self.assertEqual(SUCCESS, "\x1b[34mSUCCESS\x1b[0m")
        self.assertEqual(FAILURE, "\x1b[31mFAILURE\x1b[0m")

    def test_logger(self):

        msg = "test"

        self.assertEqual(logger.info(msg), "\x1b[97m[~] \x1b[0mtest")
        self.assertEqual(
            logger.info(msg, SUCCESS),
            "\x1b[97m[~] \x1b[0m\x1b[34mSUCCESS\x1b[0m test")

        self.assertEqual(logger.warn(msg), "\x1b[33m[!] \x1b[0mtest")

        self.assertEqual(logger.error(msg), "\x1b[31m[-] \x1b[0mtest")
        self.assertEqual(
            logger.error(msg, FAILURE),
            "\x1b[31m[-] \x1b[0m\x1b[31mFAILURE\x1b[0m test")
