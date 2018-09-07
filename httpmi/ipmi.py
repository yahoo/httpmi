from pyghmi.ipmi import command


def _connect(credentials):
    return command.Command(bmc=credentials['bmc'],
                           userid=credentials['user'],
                           password=credentials['password'])


def get_power(credentials):
    return _connect(credentials).get_power()['powerstate']


def set_power(credentials, state):
    res = _connect(credentials).set_power()['powerstate']
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
