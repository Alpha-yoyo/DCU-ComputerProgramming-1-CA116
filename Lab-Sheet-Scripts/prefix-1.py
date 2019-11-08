#!/usr/bin/env python

if __name__ == "__main__":
   a = ["mountain", "montagne", "mont", "mo", "montages", "zebra", "monthly"]
   s = "mont"

i = 0
while i < len(a):
   s1 = a[i]
   if s1[0:len(s)] == s[0:len(s)]:
      print s1
   i = i + 1
