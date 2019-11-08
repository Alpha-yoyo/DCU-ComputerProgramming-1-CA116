#!/usr/bin/env python

n = input()
i = 0
prev = 1
curr = 0
while i < n:
  tmp = curr
  curr = prev + curr
  prev = tmp
  print prev
  i = i + 1
