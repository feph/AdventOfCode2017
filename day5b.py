#!/usr/bin/env python3

inp = [int(x) for x in open("day5.txt", "r").readlines()]

cnt = 0
pos = 0

while pos >= 0 and pos < len(inp):
    offset = inp[pos]
    if offset >= 3:
        inp[pos] -= 1
    else:
        inp[pos] += 1
    pos = pos + offset
    cnt = cnt + 1

print(cnt)
