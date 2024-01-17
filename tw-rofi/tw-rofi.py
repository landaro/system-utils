#!/usr/bin/env python

# Simple rofi frontend for capturing new taskwarrior tasks

import sys
import subprocess
from rofi import Rofi

r = Rofi()

task = r.text_entry('New task')

if task == None:
    sys.exit()

try:
    result = subprocess.run(
        ["task", "add", "+TRIAGE", repr(task)],
        capture_output = True,
        text = True,
        check = True
    )
    subprocess.run(["notify-send", "Task", result.stdout])
except subprocess.CalledProcessError as e:
    subprocess.run(["notify-send", f"Task Error (ret: {e.returncode})", e.stderr])
