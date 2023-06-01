# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
import math


def letter_conbinations(value):
    #Doc String
    """This function to xxx....."""
    ds_kq = []
    l2 = ['a', 'b', 'c']
    l3 = ['d', 'e', 'f']
    l4 = ['g', 'h', 'i']
    l5 = ['j', 'k', 'l']
    l6 = ['m', 'n', 'o']
    l7 = ['p', 'q', 'r', 's']
    l8 = ['t', 'u', 'v']
    l9 = ['w', 'x', 'y', 'z']
    ds_mapping = {'2': l2, '3': l3, '4': l4, '5': l5, '6': l6, '7': l7, '8': l8, '9': l9}
    v1 = value[0] # '5'
    v2 = value[1] # '6'
    pt1 = ds_mapping.get(v1)
    pt2 = ds_mapping.get(v2)
    for c1 in pt1:
        for c2 in pt2:
            ds_kq.append(c1+c2)
    return ds_kq

kq = letter_conbinations("56")
print(kq)
#them 1 doan code
math.sqrt()

print("Xin chao 1234")
