# Copyright 2018, Oath Inc
# Licensed under the terms of the Apache 2.0 license. See LICENSE file in
# https://github.com/yahoo/httpmi


class BaseException(Exception):
    _msg_fmt = 'An unknown error occurred.'

    def __init__(self, message=None, **kwargs):
        if not message:
            try:
                message = self._msg_fmt % kwargs
            except Exception as e:
                # get what we can out if something went wrong
                message = self._msg_fmt

        super(BaseException, self).__init__(message)


class InvalidPowerState(BaseException):
    _msg_fmt = ('Invalid power state: %(state)s. Acceptable values are '
                '"on", "off".')


class InvalidBootDevice(BaseException):
    _msg_fmt = ('Invalid boot device: %(device)s. Acceptable values are '
                '"network", "hd".')
