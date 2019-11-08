#!/usr/bin/env python

if __name__ == "__main__":
   a = ["mountain", "montagne", "mont", "mo", "montages", "zebra", "monthly"]
   s = "mont"

i = 0
while i < len(a) and a[i][0:len(s)] != s[0:len(s)]:
   i = i + 1

if i < len(a):
   print a[i]
