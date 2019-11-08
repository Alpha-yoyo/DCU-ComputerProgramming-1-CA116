#!/usr/bin/env python

s = raw_input()
x = 0
y = 0
while y < len(s):
  if s[y] == "0":
    x = x * 2
  else:
    x = x * 2 + 1
  y = y + 1
print x
