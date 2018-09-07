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
