#!/usr/bin/env python3

import sys

try:
	inp = sys.argv[1]
except IndexError:
	sys.exit(0)  # no input given
try:
	print(inp[0].upper() + inp[1:].lower(), end='')
except IndexError:
	print(inp[0].upper(), end='')
