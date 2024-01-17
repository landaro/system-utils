#!/usr/bin/env python

import sys
import subprocess
from rofi import Rofi

r = Rofi()

options = ['cancel', 'shutdown', 'suspend', 'hibernate', 'reboot', 'logout']
index, key = r.select('Bye?', options)

if (key == -1 or index == 0):
    sys.exit()

match index:
    case 1:
        subprocess.call(["systemctl", "poweroff"])
    case 2:
        subprocess.call(["systemctl", "suspend"])
    case 3:
        subprocess.call(["systemctl", "hibernate"])
    case 4:
        subprocess.call(["systemctl", "reboot"])
    case 5:
        subprocess.call(["i3-msg", "exit"])
    case _:
        sys.exit(10)
