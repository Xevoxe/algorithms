import math


#  Calculate a^exp mod b
def calc_expo_modulo(a, exp, b):
    #  Check to see if exp is a power of 2
    if neive_check_power_2(exp):
        return calc_modulo_pow2(a, exp, b)
    else:
        #  Not a power of 2 so break up exponent into binary
        int_to_binary = convert_to_binary(exp)
        for index in range(len(int_to_binary)):
            if int_to_binary[index] == 1:
                pass


    #  Quotient Remainder Thoerem


def calc_mod(a, b):
    return a - math.floor(a / b) * b


#  Determine if a is a power of 2
#  O(Log n)
def neive_check_power_2(a):
    while a > 1:
        a = a / 2
        if a == 1:
            return True
    return False


#  Calculate modulo with exponent of power of 2
#  This is a divide and conquer algorithm that solves a small portion of the problem
#  and then combines the results to find the final answer.
def calc_modulo_pow2(a, exp, b):
    pow2 = 1
    result = calc_mod(pow(a, pow2), b)
    while pow2 < exp:
        result = calc_mod(result * result, b)
        pow2 = pow2 * 2
    return result


def convert_to_binary(number):
    result = []
    while (number > 0):
        if number % 2 == 1:
            result.append(1)
        else:
            result.append(0)
        number = math.floor(number / 2)
    print(result)
    return result
