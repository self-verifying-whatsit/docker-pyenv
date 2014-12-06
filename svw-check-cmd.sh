#!/usr/bin/env bash

docker run -t -a stdout -a stderr -i docker-pyenv:latest pyenv whence python
