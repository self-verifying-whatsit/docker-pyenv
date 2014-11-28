#!/usr/bin/env python

import os
import subprocess
import pytest


def test_svb(capfd):
    here = os.path.dirname(__file__)
    scriptPath = os.path.join(here, 'svb-check-cmd.sh')
    process = subprocess.Popen(scriptPath)
    process.communicate()
    out, err = capfd.readouterr()
    if process.returncode:
        pytest.fail("%s (exitcode %s)" % (err, process.returncode))
    assert "2.7.8" in out and '3.4.2' in out

if __name__ == '__main__':
    pytest.main()
