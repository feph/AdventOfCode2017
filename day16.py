#!/usr/bin/env python3

instrs = open("day16.txt","r").read().strip().split(",")

lst = [chr(97+i) for i in range(16)]
start_lst = lst.copy()

def s(lst, i):
    return lst[-i:] + lst[:-i]

def x(lst, a,b):
    ea = lst[a]
    eb = lst[b]
    lst[b] = ea
    lst[a] = eb
    return lst

def p(lst, a,b):
    ia = lst.index(a)
    ea = lst[ia]
    ib = lst.index(b)
    eb = lst[ib]
    lst[ia] = eb
    lst[ib] = ea
    return lst

for i in range(1000000000):
    for ins in instrs:
        f = ins[0]
        op = ins[1:].split("/")
        if len(op) > 1:
            a,b = op
        else:
            a = op[0]
        if f == "s":
            lst = s(lst, int(a))
        elif f == "x":
            lst = x(lst, int(a), int(b))
        elif f == "p":
            lst = p(lst, a, b)
    if i == 0:
        print("Part A:")
        print("".join(lst))
    if lst == start_lst:
        print("Part B:")
        print("found cycle after %u ops!" % (i+1))
        cycle = i+1
        break

n = 1000000000 % cycle
for i in range(n):
    for ins in instrs:
        f = ins[0]
        op = ins[1:].split("/")
        if len(op) > 1:
            a,b = op
        else:
            a = op[0]
        if f == "s":
            lst = s(lst, int(a))
        elif f == "x":
            lst = x(lst, int(a), int(b))
        elif f == "p":
            lst = p(lst, a, b)


print("".join(lst))
