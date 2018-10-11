# httpmi
> An HTTP proxy for IPMI commands.

[![Build Status](https://travis-ci.org/yahoo/httpmi.svg?branch=master)](https://travis-ci.org/yahoo/httpmi)

IPMI is an unencrypted protocol that works over UDP. httpmi provides an
HTTP proxy to arbitrary IPMI hosts, as securing HTTP is well-understood. This
provides infrastructure operators the ability to perform IPMI control between
locations more securely.

## Table of Contents

- [Background](#background)
- [Install](#install)
- [Usage](#usage)
- [Contribute](#contribute)
- [License](#license)

## Background

Oath runs a number of edge sites which we wish to control from a central
location.  Instead of keeping credentials in the edge site and controlling
servers from there, we use httpmi to proxy credentials and commands into the
site.

## Install

Install httpmi via pip. As it isn't currently on PyPI, just clone the
repository and run `pip install .` from the root.

We recommend running the app with uWSGI, which looks something like::

    $ uwsgi --http 127.0.0.1:5000 --wsgi httpmi.api --callable app --master

For whatever reason, this doesn't currently work from inside the repository,
so `cd` somewhere else first.

## Usage

Every API call uses form data for command parameters and credentials. Every
API call must pass the BMC IP address and credentials in the keys
`bmc`, `user`, and `password`. Some API calls have additional parameters.

* `GET /power` - returns the current power state of the machine. No additional
  parameters required. Example response:

      {"state": "on"}

  Response value may be "on" or "off".

* `POST /power` - set the power state for the machine. Returns immediately with
  the pending power state of the machine if it is changing, or the current
  state if the machine is already in the requested state. Takes one parameter,
  "state", which may be "on" or "off". Example response:

      {"state": "on"}

  Response value may be "on" or "off".

Some examples in curl::

    $ curl -X POST \
           --form user=admin --form password=password \
           --form bmc=10.88.209.247 --form port=6230
           --form state=off \
           http://localhost:5000/power

    {"state":"off"}

    $ curl -X GET \
           --form user=admin --form password=password \
           --form bmc=10.88.209.247 --form port=6230 \
           http://localhost:5000/power

    {"state":"off"}

    $ curl -X POST \
           --form user=admin --form password=password \
           --form bmc=10.88.209.247 --form port=6230 \
           --form device=hd \
           http://localhost:5000/boot-device

    {"device":"hd"}

    $ curl -X GET \
           --form user=admin --form password=password \
           --form bmc=10.88.209.247 --form port=6230 \
           http://localhost:5000/boot-device

    {"device":"hd"}

## Contribute

Please refer to [the contributing.md file](Contributing.md) for information
about how to get involved. We welcome issues, questions, and pull requests.
Pull Requests are welcome.

## License

This project is licensed under the terms of the Apache 2.0 open source license.
Please refer to [LICENSE](LICENSE) for the full terms.
