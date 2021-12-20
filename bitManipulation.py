# AND, OR, NOT, XOR
"""
AND: &: For each pair of corresponding bits, both need to be one for 1 to be returned
OR: |: For each pair of corresponding bits, either need to be one for 1 to be returned
NOT: ~: Flips each bit, 1's are changed to 0's and 0's are changed to 1's
XOR: ^: For each pair of corresponding bits, if both are 1 - 0 is returned, if both are 0 - 0 is returned
                                            if one bit not both bits are 1 - 1 is returned
"""


def and_op(a, b):
    result = a & b
    return result


def or_op(a, b):
    result = a | b
    return result


def xor_op(a, b):
    result = a ^ b
    return result


def not_op(a):
    result = ~a
    return result


def single_number_using_xor(a: list):
    result = a[0]
    for num in a[1:]:
        result ^= num
    return result


# main body
x = 1
y = 2
z = [4, 1, 2, 1, 2]
print(and_op(x, y))
print(or_op(x, y))
print(xor_op(x, y))
print(not_op(y))
print(single_number_using_xor(z))
