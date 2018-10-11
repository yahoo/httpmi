# Copyright 2018, Oath Inc
# Licensed under the terms of the Apache 2.0 license. See LICENSE file in
# https://github.com/yahoo/httpmi

from pyghmi.ipmi import command

from httpmi import exception


VALID_POWER_STATES = ('on', 'off')
VALID_BOOT_DEVICES = ('network', 'hd')


def _connect(credentials):
    return command.Command(bmc=credentials['bmc'],
                           port=int(credentials.get('port', 623)),
                           userid=credentials['user'],
                           password=credentials['password'])


def get_power(credentials):
    return _connect(credentials).get_power()['powerstate']


def set_power(credentials, state):
    if state not in VALID_POWER_STATES:
        raise exception.InvalidPowerState(state=state)
    res = _connect(credentials).set_power(state)
    if 'powerstate' in res:
        # already in the desired state, return immediately
        return res['powerstate']
    elif 'pendingpowerstate' in res:
        # for now, just return the pending state
        # consider adding an optional wait here, to wait for the actual change
        return res['pendingpowerstate']


def get_boot_device(credentials):
    data = _connect(credentials).get_bootdev()
    return data['bootdev']


def set_boot_device(credentials, device, persist=False, uefiboot=False):
    if device not in VALID_BOOT_DEVICES:
        raise exception.InvalidBootDevice(device=device)
    return _connect(credentials).set_bootdev(device,
                                             persist=persist,
                                             uefiboot=uefiboot)['bootdev']


# TODO(jroll) ironic also supports:
# get sensors data
# inject nmi
