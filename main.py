# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from sorting import bubblesort
from discretemath import divisionalgorithm, primefactorizer
from discretemath.gcflcm import get_gcd, get_lcm, get_gcd_euclid
from discretemath.exponentialmodulo import calc_expo_modulo


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(get_gcd(34, 47))
    print(get_gcd_euclid(34, 47))

    a = 98765
    b = 13

    print(calc_expo_modulo(5, 117, 19))
    print(pow(7, 256) % b)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
