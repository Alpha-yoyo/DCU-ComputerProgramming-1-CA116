#!/usr/bin/env python

i = 1
n = input()
counts = 0
while counts < n:
  if i % 3 == 0 and i % 5 == 0:
    print "fizz-buzz"
  elif i % 5 == 0:
    print "buzz"
  elif i % 3 == 0:
    print "fizz"
  else:
    print i
  i = i + 1
  counts = counts + 1
