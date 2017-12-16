#!/usr/bin/env python3

lines = open("day4.txt","r").readlines()

print(len([1 for x in lines if len(x.strip().split(" ")) == len(set(x.strip().split(" ")))]))

# part2

print(len([1 for x in lines if 
           len    ([''.join(sorted(b)) for b in x.strip().split(" ")]) == 
           len(set([''.join(sorted(b)) for b in x.strip().split(" ")]))
           ]))
