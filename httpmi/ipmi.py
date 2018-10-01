# Copyright 2018, Oath Inc
# Licensed under the terms of the Apache 2.0 license. See LICENSE file in
# https://github.com/yahoo/httpmi

from pyghmi.ipmi import command

from httpmi import exception


VALID_POWER_STATES = ('on', 'off')


def _connect(credentials):
    return command.Command(bmc=credentials['bmc'],
                           userid=credentials['user'],
                           password=credentials['password'])


def get_power(credentials):
    return _connect(credentials).get_power()['powerstate']


def set_power(credentials, state):
    if state not in VALID_POWER_STATES:
        raise exception.InvalidPowerState(state)
    connection = _connect(credentials).set_power(state)['powerstate']
    if 'powerstate' in res:
        # already in the desired state, return immediately
        return res['powerstate']
    elif 'pendingpowerstate' in res:
        # for now, just return the pending state
        # consider adding an optional wait here, to wait for the actual change
        return res['pendingpowerstate']


# TODO ironic also supports:
# reboot (off then on)
# get boot device
# set boot device
# get sensors data
# inject nmi
