#!/usr/bin/env python

a = []
s = raw_input()
while s != "end":
   a.append(s)
   s = raw_input()

i = 0
while i < len(a):
   p = i
   j = i + 1
   while j < len(a):
      if a[j] < a[p]:
         p = j
      j = j + 1
   tmp = a[i]
   a[i] = a[p]
   a[p] = tmp
   print a[i]
   i = i + 1
