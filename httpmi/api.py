from flask import Flask
from flask import jsonify
from flask import request

from httpmi import ipmi


app = Flask(__name__)

CREDS_KEYS = ['bmc', 'user', 'password']


def _get_bmc_credentials():
    return {k: request.form[k] for k in CREDS_KEYS}


@app.route('/power')
def power():
    creds = _get_bmc_credentials()
    if request.method == 'GET':
        return jsonify({'state': ipmi.get_power(creds)})
