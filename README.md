# httpmi
> An HTTP proxy for IPMI commands.

IPMI is an unencrypted protocol that works over UDP. httpmi provides an
HTTP proxy to arbitrary IPMI hosts, as securing HTTP is well-understood. This
provides infrastructure operators the ability to perform IPMI control between
locations more securely.

## Table of Contents

- [Background](#background)
- [Install](#install)
- [Configuration](#configuration)
- [Usage](#usage)
- [Security](#security)
- [Contribute](#contribute)
- [License](#license)

## Background

Oath runs a number of edge sites which we wish to control from a central
location.  Instead of keeping credentials in the edge site and controlling
servers from there, we use httpmi to proxy credentials and commands into the
site.

## Install

Install httpmi via pip.

TODO insert more words about virtualenvs and such.

## Configuration

TODO some words about fronting with a web server providing TLS and such.

## Usage

TODO quick API overview here.

## Security

TODO some words about securing the httpmi host and communication here.

## Contribute

Please refer to [the contributing.md file](Contributing.md) for information
about how to get involved. We welcome issues, questions, and pull requests.
Pull Requests are welcome.

## License

This project is licensed under the terms of the Apache 2.0 open source license.
Please refer to [LICENSE](LICENSE) for the full terms.
