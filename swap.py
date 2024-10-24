# python program to swap 2 nums without taking third variable
def swap(num1, num2):
    num1 = num1 + num2
    num2 = num1 - num2
    num1 = num1 - num2
swap(4, 8)