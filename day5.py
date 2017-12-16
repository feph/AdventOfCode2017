#!/usr/bin/env python3

inp = [int(x) for x in open("day5.txt", "r").readlines()]

cnt = 0
pos = 0

while pos >= 0 and pos < len(inp):
    jump = inp[pos]
    inp[pos] += 1
    pos = pos + jump
    cnt = cnt + 1

print(cnt)
