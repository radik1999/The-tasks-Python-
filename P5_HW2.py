##Вводяться десять натуральних чисел більше 2. Порахувати, скільки серед них чисел, що кратні 5-ти.

print ("This program calculates how many numbers are multiples of 5 in the list.")
import random
list_numbers = []
countNumbers = 0

for i in range (10):
    numbers = random.randint (2, 100)
    list_numbers.append (numbers)
    if numbers % 5 == 0:
        countNumbers += 1
    
print ("Numbers : ", list_numbers)
print ("Count of numbers that are multiples of 5 is: %2d" %countNumbers)
