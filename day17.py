#!/usr/bin/env python3
import sys
buffer = [0]
num_steps = 304
pos = 0

for i in range(1,2018):
    pos = (pos + num_steps) % len(buffer) + 1
    buffer.insert(pos, i)
print(buffer[pos+1])

pos = 0
l = 1
second = None
for i in range(1,50000000):
    pos = (pos + num_steps) % l
    if pos == 0:
        second = i
    pos += 1
    l += 1
#    if i % 1000000 == 0:
#        print(i)
#        sys.stdout.flush()
print(second)
