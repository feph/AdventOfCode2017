#!/usr/bin/env python3
import numpy as np

inp = 361527

pos = np.array((0,0))
dir = np.array((1,0))
used_pos = set()
used_pos.add((0,0))
values = {}
right = np.array((1,0))
left = np.array((-1,0))
up = np.array([0,1])
down = np.array([0,-1])

for c in range(2,inp+1):
    pos = pos + dir
    used_pos.add(tuple(pos))
#    print("%u is at %u,%u" % (c,pos[0], pos[1]))
    if all(dir == right):
        left_neigh = up
    elif all(dir == up):
        left_neigh = left
    elif all(dir == left):
        left_neigh = down
    elif all(dir == down):
        left_neigh = right
    if tuple(pos + left_neigh) in used_pos:
        dir = dir # continue
    else:
        dir = left_neigh

print(sum(abs(pos)))

# part2
print(" ==== part 2 ==== ")

inp = 361527
#inp = 30
pos = np.array((0,0))
dir = np.array((1,0))
used_pos = set()
used_pos.add((0,0))
values = {}
right = np.array((1,0))
left = np.array((-1,0))
up = np.array([0,1])
down = np.array([0,-1])


def sum_neighbors(pos, values):
    x = np.arange(-1,2,1)
    y = np.arange(-1,2,1)
    xx,yy = np.meshgrid(x,y)
    result = 0
    for dx,dy in zip(xx.flatten(),yy.flatten()):
        if dx == 0 and dy == 0:
            continue
        result += values.get("%u,%u" % (pos[0]+dx,pos[1]+dy),0)
    return result
pos_s = "0,0"
values[pos_s] = 1
while values[pos_s] < inp:
    pos = pos + dir
    pos_s = "%s,%s" % (pos[0], pos[1])
    used_pos.add(tuple(pos))
    values[pos_s] = sum_neighbors(pos,values)
    print("%u is at %u,%u" % (values[pos_s], pos[0], pos[1]))
    if all(dir == right):
        left_neigh = up
    elif all(dir == up):
        left_neigh = left
    elif all(dir == left):
        left_neigh = down
    elif all(dir == down):
        left_neigh = right
    if tuple(pos + left_neigh) in used_pos:
        dir = dir # continue
    else:
        dir = left_neigh



