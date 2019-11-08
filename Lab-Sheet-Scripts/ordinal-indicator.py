#!/usr/bin/env python

s = raw_input()
if s[len(s) - 2:len(s)] == "11":
   print "th"
elif s[len(s) - 2:len(s)] == "12":
   print "th"
elif s[len(s) - 2:len(s)] == "13":
   print "th"
elif s[len(s) - 1] == "1":
   print "st"
elif s[len(s) - 1] == "2":
   print "nd"
elif s[len(s) - 1] == "3":
   print "rd"
else:
   print "th"
