#!/usr/bin/env python3

instrs = open("day18.txt", "r").readlines()

cp = 0
ip = 0
ips = [0, 0]
registers = {}
registerss = [ {'p': 0}, {'p': 1} ]
queue = [ [], [] ]
snd_counter = [0, 0]

def task_switch():
    global ips
    global ip
    global cp
    global registers
    ips[cp] = ip
    registerss[cp] = registers
    if cp == 0:
        cp = 1
    else:
        cp = 0
    registers = registerss[cp]
    ip = ips[cp]
    if len(queue[cp]) == 0:
        return True
    else:
        return False


def snd(i):
    if cp == 0:
        queue[1].insert(0,i)
    else:
        queue[0].insert(0,i)
    snd_counter[cp] += 1

def rcv():
    try:
        r = queue[cp].pop()
    except IndexError:
        r = None
    return r

def get_rhs(s):
    try:
        b = int(s)
    except ValueError:
        b = registers.get(s, 0)
    return b

while ip < len(instrs):
    ins, *op = instrs[ip].strip().split(" ")
    #print("(%u) %u: %s %s" % (cp, ip, ins, op))
    if ins == "snd":
        freq = get_rhs(op[0])
        snd(freq)
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
        #print("(%u) rcv" % cp)
        #print("trying to rcv from queue %s" % queue[cp])
        r = rcv()
        if r is not None:
            #print("(%u) received %u!" % (cp, r))
            registers[op[0]] = r
            ip += 1
        else:
            print("switching task from state (%u) %u: %s" % (cp, ip, registers))
            res = task_switch()
            print("switched to task state (%u) %u: %s" % (cp, ip, registers))
            if res:
                print("deadlock detected, terminating!")
                print(snd_counter)
                break
    elif ins == "jgz":
        if get_rhs(op[0]) > 0:
            ip += get_rhs(op[1])
#            print("jumping to ip = %u" % ip)
        else:
            ip += 1
#    print(registers)
#print("last state (%u) %u: %s" % (cp, ip, registers))
#print(snd_counter)
