#!/usr/bin/env python3

instrs = open("day18.txt", "r").readlines()

ip = 0
freq = None
registers = {}

def get_rhs(s):
    try:
        b = int(s)
    except ValueError:
        b = registers.get(s, 0)
    return b

while ip < len(instrs):
    ins, *op = instrs[ip].strip().split(" ")
    print("%u: %s %s" % (ip, ins, op))
    if ins == "snd":
        freq = get_rhs(op[0])
        ip += 1
    elif ins == "set":
        registers[op[0]] = get_rhs(op[1])
        ip += 1
    elif ins == "add":
        registers[op[0]] = registers.get(op[0], 0) + get_rhs(op[1])
        ip += 1
    elif ins == "mul":
        registers[op[0]] = registers.get(op[0],0) * get_rhs(op[1])
        ip += 1
    elif ins == "mod":
        registers[op[0]] = registers.get(op[0],0) % get_rhs(op[1])
        ip += 1
    elif ins == "rcv":
        if freq != 0:
            print("recovered %s" % freq)
            break
        else:
            ip += 1
    elif ins == "jgz":
        if get_rhs(op[0]) > 0:
            ip += get_rhs(op[1])
            print("jumping to ip = %u" % ip)
        else:
            ip += 1
    print(registers)



