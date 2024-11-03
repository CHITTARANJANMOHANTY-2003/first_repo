# python program to swap 2 nums without taking third variable
def swap(num1, num2):
    num1 = num1 + num2
    num2 = num1 - num2
    num1 = num1 - num2
    # i have not the process but don't print
    print("after swapping: ")
    print(num1, num2)
swap(4.4, 8.4)