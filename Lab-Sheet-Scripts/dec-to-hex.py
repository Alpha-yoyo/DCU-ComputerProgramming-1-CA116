#!/usr/bin/env python

hex = ""
base = 16

digits = "0123456789abcdef"

n = input()
while n != 0:
   hex = digits[n % base] + hex
   n = n / base
print hex
