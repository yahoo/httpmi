from pyghmi.ipmi import command


def _connect(credentials):
    return command.Command(bmc=credentials['bmc'],
                           userid=credentials['user'],
                           password=credentials['password'])


def get_power(credentials):
    return _connect(credentials).get_power()['powerstate']
