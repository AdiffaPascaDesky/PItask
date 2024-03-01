import math

numbers = []
sum_of_numbers = 0
while True:
    num = int(input("Enter a number): "))
    if num == -1:
        break
    numbers.append(num)
    sum_of_numbers += num

print("sum of number:", sum_of_numbers)
