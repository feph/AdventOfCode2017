#!/usr/bin/env python3

input_lines = open("day19.txt", "r").readlines()
maze = [ [c for c in line] for line in input_lines]

start = maze[0].index("|")
dir = (0, 1)
pos = (start, 0)

letters = [chr(65+i) for i in range(26)]
at_end = False
st = ""

max_step = 120
i = 1
while not at_end:
    pos = (pos[0] + dir[0], pos[1] + dir[1])
    i += 1
    def m(t):
        return maze[t[1]][t[0]]
    peek = m( ( pos[0]+dir[0], pos[1]+dir[1] ) )
    c = m( pos ) 
    lc = (pos[0] + dir[1] , pos[1]-dir[0])
    l = m(lc)
    rc = (pos[0]-dir[1], pos[1]+dir[0])
    r = m(rc)
    print("pos: %s c: %s" % (pos, c))
    if c == " ":
        raise ValueError("stepped onto empty field at ", pos)
    if c in letters:
        st += c
        if peek == " ":
            at_end = True
            continue
    elif (c == "|" or c == "-"): #step over or walk on
        pass
    elif (c == "+"): # switch dir
        if l != " ":
            dir = (dir[1], -dir[0])
        elif r != " ":
            dir = (-dir[1], dir[0])

print(st)
print(i)
