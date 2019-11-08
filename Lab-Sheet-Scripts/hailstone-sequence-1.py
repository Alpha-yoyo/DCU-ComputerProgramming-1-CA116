#!/usr/bin/env python

i = 0
n = input()
m = input()
while i < n:
   print m
   if m % 2 == 0:
      m = m / 2
   else:
      m = m * 3 + 1
   i = i + 1
