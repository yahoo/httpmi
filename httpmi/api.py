# Copyright 2018, Oath Inc
# Licensed under the terms of the Apache 2.0 license. See LICENSE file in
# https://github.com/yahoo/httpmi

from flask import Flask
from flask import jsonify
from flask import request

from httpmi import ipmi


app = Flask(__name__)

CREDS_KEYS = ['bmc', 'user', 'password']


def _get_bmc_credentials():
    return {k: request.form[k] for k in CREDS_KEYS}


@app.route('/power', methods=['GET', 'POST'])
def power():
    creds = _get_bmc_credentials()
    if request.method == 'GET':
        return jsonify({'state': ipmi.get_power(creds)})

    # TODO(jroll) add a wait parameter here or make it feel like real IPMI?
    new_state = request.form['state']
    return jsonify({'state': ipmi.set_power(creds, new_state)})


@app.route('/boot-device', methods=['GET', 'POST'])
def boot_device():
    creds = _get_bmc_credentials()
    if request.method == 'GET':
        return jsonify({'device': ipmi.get_boot_device(creds)})

    new_device = request.form['device']
    return jsonify({'device': ipmi.set_boot_device(creds, new_device)})
