#!/usr/bin/env python

import os
import subprocess
import pytest


def test_svb(capfd):
    here = os.path.dirname(__file__)
    scriptPath = os.path.join(here, 'svb-check-cmd.sh')
    process = subprocess.Popen(scriptPath)
    process.communicate()
    assert process.returncode == 0, process.returncode
    out, err = capfd.readouterr()
    assert "2.7.8" in out and '3.4.2' in out

if __name__ == '__main__':
    pytest.main()
