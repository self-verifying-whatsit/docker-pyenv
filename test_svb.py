import os
import subprocess


def test_svb():
    here = os.path.dirname(__file__)
    scriptPath = os.path.join(here, 'docker_check.sh')
    process = subprocess.Popen(scriptPath)
    stdout, stderr = process.communicate()
    assert process.returncode == 0, process.returncode
    assert stdout != None  # fixme WHY?
