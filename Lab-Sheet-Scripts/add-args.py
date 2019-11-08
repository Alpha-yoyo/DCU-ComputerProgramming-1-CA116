#!/usr/bin/env python

import sys
args = sys.argv[1:]
i = 0
total = 0

while i < len(args):
   total = total + int(args[i])
   i = i + 1
print total
