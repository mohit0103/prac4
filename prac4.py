m1=[]
m = int(input("Enter no of columns in 1st matrix: "))
n = int(input("Enter no of rows in 1st matrix: "))
for i in range(n):
    row = []
    for j in range(m):
        no = int(input("Enter elements:"))
        row.append(no)
    m1.append(row)
print(m1)
m2=[]
a = int(input("Enter no of columns in 2nd matrix: "))
b = int(input("Enter no of rows in 2nd matrix: "))
for i in range(b):
    row = []
    for j in range(a):
        no = int(input("Enter elements:"))
        row.append(no)
    m2.append(row)
print(m2)

for i in range(len(m1)):
  
   for j in range(len(m1[0])):
       result[i][j] = m1[i][j] + m2[i][j]

for r in result:
   print("Addition of two matrices is : ",r)

for i in range(len(m1)):
      
   for j in range(len(m1[0])):
       result1[i][j] = m1[i][j] - m2[i][j]

for r in result1:
   print("subtraction  of two matrices is : ",r)

for i in range(len(m1)):
      
   for j in range(len(m1[0])):
       result2[i][j] = m1[i][j] * m2[i][j]

for r in result2:
   print("Multiplication  of two matrices is : ",r)
