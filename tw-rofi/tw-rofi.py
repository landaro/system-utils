#!/usr/bin/env python

# Simple rofi frontend for handling taskwarrior tasks

import sys
import subprocess
from rofi import Rofi

def main():
    r = Rofi()
    options = ['New Task', 'Planned', 'Triage', 'All']
    index, key = r.select('TW', options)
    if (key == -1):
        sys.exit()
    match index:
        case 0:
            create_new_task(r)
        case 1:
            subprocess.run(["notify-send", "Task", "E: not implemented"])
        case 2:
            subprocess.run(["notify-send", "Task", "E: not implemented"])
        case 3:
            subprocess.run(["notify-send", "Task", "E: not implemented"])
        case _:
            sys.exit(10)

def create_new_task(rf):
    task = rf.text_entry('New task')
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

if __name__ == "__main__":
    main()
