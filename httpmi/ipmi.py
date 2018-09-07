from pyghmi.ipmi import command


def _connect(bmc, user, password):
    return command.Command(bmc=bmc, userid=user, password=password)


def get_power(bmc, user, password):
    return _connect(bmc, user, password).get_power()['powerstate']
