#!/usr/bin/env python3
from operator import xor

a = 634
b = 301

count = 0
for i in range(40*10**6):
    a = (a* 16807) % 2147483647
    b = (b* 48271) % 2147483647
    if (xor(a,b) & ((1<<16)-1) == 0):
        count += 1

print(count)
