import sys
from math import pow

FILE_NAME = 'in.in'
OUTPUT_NAME = 'tidy-numbers-out.out'

FILE = open(FILE_NAME)

NUM_CASES = int(FILE.readline())
ANSWERS = []
# to solve for big problems, have to clear all lower numbers, from right to left, to satisfy furthest left numbers
# def is_tidy(x):
#     digit = None
#     while x > 0:
#         tmp = x % 10
#         if digit is not None and tmp > digit:
#             return False
#         digit = tmp
#         x /= 10
#     return True

def is_tidy(x):
    for i in range(0, len(x)):
        if i + 1 < len(x):
            if x[i] < x[i + 1]:
                return False
    return True

def get_digits(x):
    ret = []
    while x > 0:
        ret.append(x % 10)
        x /= 10
    return ret

def get_int(digits):
    num_str = ""
    i = len(digits) - 1
    while i >= 0:
        num_str += str(digits[i])
        i -= 1
    return int(num_str)
    # num = long(0)
    # for i in range(0, len(digits)):
    #     num += (digits[i] * pow(10, i))
    #     print str(num)
    # return long(num)

# works for n <= 1000, but not efficient enough
# def solve(n):
#     while n > 0:
#         if (is_tidy(n)):
#             return n
#         n -= 1
#     return n

def solve(n):
    digits = get_digits(n)
    for i in range(0, len(digits)):
        if i + 1 < len(digits):
            if digits[i] < digits[i + 1]:
                target_change = i + 1
                while digits[target_change] == 0:
                    target_change += 1
                for j in range(0, target_change):
                    digits[j] = 9
                digits[target_change] -= 1
    return get_int(digits)


for z in range(0, NUM_CASES):
    case = int(FILE.readline())
    ANSWERS.append(solve(case))
FILE.close()

OUT_FILE = open(OUTPUT_NAME, 'w')
for i in range(0, NUM_CASES):
    #print('Case #{0}: {1}\n'.format(i + 1, ANSWERS[i]))
    OUT_FILE.write('Case #{0}: {1}\n'.format(i + 1, ANSWERS[i]))
OUT_FILE.close()
