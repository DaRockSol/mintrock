from asyncio.subprocess import PIPE
import subprocess
from sys import stdout
from tokenize import String

message = {}
cmnd = "echo More Output"
try:
    output = subprocess.check_output(
        cmnd, stderr=subprocess.STDOUT, shell=True, timeout=3,
        universal_newlines=True)
except subprocess.CalledProcessError as e:
    message["WTF"] = "metaboss process failed"
    message["error"] = str(e.returncode) + " - " + e.output
    print(message)
else:
    message["message"] = output
    print(message)