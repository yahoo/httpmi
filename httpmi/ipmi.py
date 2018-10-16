# Copyright 2018, Oath Inc
# Licensed under the terms of the Apache 2.0 license. See LICENSE file in
# https://github.com/yahoo/httpmi

from pyghmi.ipmi import command

from httpmi import exception


VALID_POWER_STATES = ('power on', 'power off')
VALID_BOOT_DEVICES = ('pxe', 'disk')
IRONIC_TO_PYGHMI = {
    'power on': 'on',
    'power off': 'off',
    'pxe': 'network',
    'disk': 'hd',
}
PYGHMI_TO_IRONIC = {v: k for k, v in IRONIC_TO_PYGHMI.items()}


def _connect(credentials):
    return command.Command(bmc=credentials['bmc'],
                           port=int(credentials.get('port', 623)),
                           userid=credentials['user'],
                           password=credentials['password'])


def get_power(credentials):
    state = _connect(credentials).get_power()['powerstate']
    return PYGHMI_TO_IRONIC[state]


def set_power(credentials, state):
    if state not in VALID_POWER_STATES:
        raise exception.InvalidPowerState(state=state)
    state = IRONIC_TO_PYGHMI[state]
    res = _connect(credentials).set_power(state)
    if 'powerstate' in res:
        # already in the desired state, return immediately
        return PYGHMI_TO_IRONIC[res['powerstate']]
    elif 'pendingpowerstate' in res:
        # for now, just return the pending state
        # consider adding an optional wait here, to wait for the actual change
        return PYGHMI_TO_IRONIC[res['pendingpowerstate']]


def get_boot_device(credentials):
    data = _connect(credentials).get_bootdev()
    return PYGHMI_TO_IRONIC[data['bootdev']]


def set_boot_device(credentials, device, persist=False, uefiboot=False):
    if device not in VALID_BOOT_DEVICES:
        raise exception.InvalidBootDevice(device=device)
    device = IRONIC_TO_PYGHMI[device]
    new_device = _connect(credentials).set_bootdev(
        device, persist=persist, uefiboot=uefiboot)['bootdev']
    return PYGHMI_TO_IRONIC[new_device]


# TODO(jroll) ironic also supports:
# get sensors data
# inject nmi
