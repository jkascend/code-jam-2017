import sys
from math import pow

FILE_NAME = 'in.in'
OUTPUT_NAME = 'pancakes-out.out'

FILE = open(FILE_NAME)

NUM_CASES = int(FILE.readline())
ANSWERS = []

def is_set(val, bit):
    return val & 1 << bit > 0

def flip_range(start, length, val):
    for k in range(0, length):
        val ^= 1 << k + start
    return val

def set_bits(s):
    ret = 0
    for i in range(0, len(s)):
        if s[i] == "+":
            ret |= 1 << i
    return ret

def solve(s, k):
    bits = set_bits(s)
    num_flips = 0

    i = 0
    while i < len(s):
        if is_set(bits, i) is not True:
            if k + i > len(s):
                return "IMPOSSIBLE"
            else:
                bits = flip_range(i, k, bits)
                num_flips += 1
                i = 0
        else:
            i += 1
    return num_flips

for z in range(0, NUM_CASES):
    case = FILE.readline().split()
    ANSWERS.append(solve(case[0], int(case[1])))
FILE.close()

OUT_FILE = open(OUTPUT_NAME, 'w')
for i in range(0, NUM_CASES):
    OUT_FILE.write('Case #{0}: {1}\n'.format(i + 1, ANSWERS[i]))
OUT_FILE.close()
