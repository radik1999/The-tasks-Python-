##У списку випадкових цілих чисел поміняти місцями мінімальний і максимальний елементи.

import random
list1 = []

for item in range (10):
    list1.append (random.randint (0,100))
print ("The first List: ", list1)

temp = []
index_max_value = list1.index(max (list1))
index_min_value = list1.index(min (list1))
temp = max (list1)
list1 [index_max_value] = list1 [index_min_value]
list1 [index_min_value] = temp
print ("The second List: ", list1)
