#!/usr/bin/env python
# coding: utf-8

import os


def roundstr(size):

    return str(round(size, 1))


def convert_size(byte):

    if byte < 1024:
        return str(byte) + 'B'

    elif byte < 1024 ** 2:
        return roundstr(byte / 1024.0) + 'KB'

    elif byte < 1024 ** 3:
        return roundstr(byte / (1024.0 ** 2)) + 'MB'

    elif byte < 1024 ** 4:
        return roundstr(byte / (1024.0 ** 3)) + 'GB'

    else:
        return str(byte) + 'B'


def getsize(_file):

    rawsize = os.path.getsize(_file)
    return convert_size(rawsize)
