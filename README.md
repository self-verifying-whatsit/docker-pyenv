# Docker-Pyenv

### Install pyenv and two different Pythons in userspace

## Build instructions

* cd into your clone of this project
* `./svb-build.sh`

## Validate

* cd into your clone of this project
* `pip install -r requirements.txt`
* `./svb-check.py`

[Docker](https://www.docker.com/) provides lightweight containers not quite like virtual machines using [Linux container technology (LXC)](https://linuxcontainers.org).

[Pyenv](https://github.com/yyuu/pyenv) builds different Python versions in Userspace and makes them easily manageable in combination with virtualenvs.

## TODO
use [docker bindings](http://docker-py.readthedocs.org/en/latest/api/) to check result

## What is this?

This repository is part of the Self Validating Blueprint (SVB) project as introduced in [here](https://self-validating-blueprint.github.io/introduction/).
