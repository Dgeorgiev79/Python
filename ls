#!/usr/bin/python3.6

import os

list = os.popen("ls").read()

print(f"{list}")
