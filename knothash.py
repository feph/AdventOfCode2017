#!/usr/bin/env python3

#lst = [x for x in range(0, 5)]

#inp = [3,4,1,5,0]
part2_input = u"197,97,204,108,1,29,5,71,0,50,2,255,248,78,254,63"
#inp = u"1,2,3"
#inp = ""
#inp = "1,2,3"

def reverse_part(lst, fr, num_elem):
    if num_elem == 0:
        return lst
    else:
        le = len(lst)
        f_idx = fr % le
        t_idx = (f_idx+num_elem-1) % le
        if f_idx + num_elem > le: # wrap
            wrapped_part = lst[f_idx:] + lst[:t_idx+1]
            wrapped_part = wrapped_part[::-1]
            lst = wrapped_part[-t_idx-1:] + lst[t_idx+1:f_idx] + wrapped_part[:-t_idx-1]
        else:
            #print("reversed part is: %s" % lst[f_idx:t_idx+1][::-1])
            lst = lst[:f_idx] + lst[f_idx:t_idx+1][::-1] + lst[t_idx+1:]
        return lst

def dense_hash(sparse):
    dhash = []
    for block_num in range(16):
        dh_part = sparse[block_num*16:block_num*16+16]
        x = 0
        for y in dh_part:
            x = x ^ y
        dhash.append(x)
    return dhash

def sparse_hash(hash_input, part2=True, LEN_NUM=256):
    if part2:
        lengths = [ord(x) for x in hash_input.strip()] + [17,31,73,47,23]
    else:
        lengths = hash_input
    numbers = [x for x in range(0, LEN_NUM)]
    skip_size = 0
    cur_pos = 0
    le = len(lengths)
    if part2:
        NUM_ROUNDS = 64
    else:
        NUM_ROUNDS = 1
    for round_num in range(NUM_ROUNDS):
        for i in lengths:
    #        print("length = %u" % i)
    #        print("reversing %u elements from index %u" % (i, cur_pos))
            numbers = reverse_part(numbers, cur_pos, i)
            cur_pos += (i + skip_size)
    #        print("current pos = %u" % cur_pos)
            skip_size += 1
     #       print("skip size = %u" % skip_size)
    return numbers 


def knot_hash(hash_input):
    numbers = sparse_hash(hash_input)
    return "".join(["%0.2x" % elem for elem in dense_hash(numbers)])

if __name__ == "__main__":
    ex = [3,4,1,5]
    print(sparse_hash(ex, part2=False, LEN_NUM=5))

    part1 = [197,97,204,108,1,29,5,71,0,50,2,255,248,78,254,63]
    r = sparse_hash(part1, part2=False)
    print(r[0]*r[1])

    #e = [65, 27, 9, 1, 4, 3, 40 , 50 , 91 , 7 , 6 , 0 , 2 , 5 , 68 , 22]
    #x = 0
    #for y in e:
    #    x = x ^ y
    #print(x)
    #print("%0.2x, %0.2x, %0.2x" % (x, 7, 255))
    for s in ["", "AoC 2017", "1,2,3", "1,2,4", part2_input]:
        #print("sparse('%s'): %s" % (s, sparse_hash(s)))
        print("'%s' => %s" % (s, knot_hash(s)))


