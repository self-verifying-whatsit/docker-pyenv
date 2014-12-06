# Docker-Pyenv

### Install pyenv and two different Pythons in userspace

## To sudo or not to sudo

if your user is in the `docker` group, you don't have to use sudo, otherwise you do.

## Build instructions

* cd into your clone of this project
* `./svw-build.sh`

## Validate

** You might want to do this in a virtualenv. If you have virtualenvwrapper installed you can just type `mktmpenv` and you are in a throw away wirtualenv, that will be deleted when you call `deactivate`.**

* cd into your clone of this project
* `pip install -r requirements.txt`
* `./svw-check.py`

[Docker](https://www.docker.com/) provides lightweight containers not quite like virtual machines using [Linux container technology (LXC)](https://linuxcontainers.org).

[Pyenv](https://github.com/yyuu/pyenv) builds different Python versions in Userspace and makes them easily manageable in combination with virtualenvs.

## TODO
use [docker bindings](http://docker-py.readthedocs.org/en/latest/api/) to check result

## What is this?

This repository is part of the Self Validating Whatsit (SVW) project as introduced in [here](https://self-validating-whatsit.github.io/introduction/).
