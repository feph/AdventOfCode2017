#!/usr/bin/env python3
import binascii
from knothash import knot_hash

inp = "hfdlxzhv"

rowstrings = ["%s-%u" % (inp,i) for i in range(128)]

def hexchar_to_binstr(c):
    return bin(int(c,16))[2:]

hashes = [knot_hash(s) for s in rowstrings]
bits = [ [hexchar_to_binstr(c).zfill(4) for c in row] for row in hashes]
bits = [ [c for c in "".join(row)] for row in bits ]
print(sum(["".join(row).count('1') for row in bits]))
next_k = 2

bits = [ [ int(c) for c in row] for row in bits]

def neighbors(i,j):
    n = []
    if i > 0:
        n.append(bits[i-1][j])
    if i < 127:
        n.append(bits[i+1][j])
    if j > 0:
        n.append(bits[i][j-1])
    if j < 127:
        n.append(bits[i][j+1])
    return n

def neighbor_coords(i,j):
    n = []
    if i > 0:
        n.append((i-1, j))
    if i < 127:
        n.append((i+1, j))
    if j > 0:
        n.append((i, j-1))
    if j < 127:
        n.append((i, j+1))
    return n

def remove_group(i,j):
    bits[i][j] = 0
    ns = neighbor_coords(i,j)
    for ix, jx in ns:
        if bits[ix][jx] == 1:
            remove_group(ix,jx)

groups = 0
for i in range(128):
    for j in range(128):
        if bits[i][j] == 1: #untouched
            remove_group(i,j)
            groups += 1

print(groups)
