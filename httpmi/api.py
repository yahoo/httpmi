from flask import Flask
from flask import jsonify
from flask import request

from httpmi import ipmi


app = Flask(__name__)


@app.route('/power')
def power():
    if request.method == 'GET':
        bmc = request.form['bmc']
        user = request.form['user']
        password = request.form['password']
        return jsonify({'state': ipmi.get_power(bmc, user, password)})
