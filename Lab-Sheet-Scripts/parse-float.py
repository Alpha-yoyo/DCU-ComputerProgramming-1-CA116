#!/usr/bin/env python

s = raw_input()
i = 0

while i < len(s) and s[i] != ".":
   i = i + 1

if i < len(s):
   print s[0:i]
   print s[i + 1:len(s)]
