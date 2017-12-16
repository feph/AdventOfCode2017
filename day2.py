#!/usr/bin/env python

import numpy as np
data = np.genfromtxt("day2.txt", delimiter="\t")
checksum = sum( [np.max(x) - np.min(x) for x in data ])
print(checksum)

## part2 

sum = 0
for row in data:
    for i, x in enumerate(row):
        for y in row[i+1:]:
            if x%y == 0:
                sum = sum+x//y
            if y%x == 0:
                sum = sum+y//x

print(sum)
