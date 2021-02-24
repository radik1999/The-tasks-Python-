##Заповнити матрицю розмірності MxN (введеними користувачем) і вивести її на екран
##Знайти мінімальний елемент 3-го рядочка та максимальний елемент 2-го стовпчика і вивести їх на екран


row = int (input ("Input the count of the rows: "))
column = int (input ("Input the count of the columns: "))
table = [[0] * column] * row

i = 0
j = 0
for i in range (row):
    for j in range (column):
        table[i][j] = i * j 
        print ("%3d" %table[i][j], end = "")
    print ()
print ()
 
temp1 = []
for j in range (column):
    temp1.append(table[2][j])
print ("Min Element of 3rd row is: %5d" %min(temp1))

print ()
temp1 = []
for i in range (row):
    temp1.append(table[i][1])
print ("Max Element of 2nd column is: ", max(temp1))
  
