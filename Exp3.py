row = int(input("Enter the row count:"))
col = int(input("Enter the column count:"))

m1= [[0 for i in range(col)] for i in range(row)]
m2= [[0 for i in range(col)] for i in range(row)]    
ans= [[0 for i in range(col)] for i in range(row)]

print("Enter data for matrix:")
for i in range (row):
    for j in range (col):
        m1[i][j]=int(input(f"Enter value for row{i+1} and col{j+1}:"))

print("Enter data for matrix2:")
for i in range(row):
    for j in range(col):
        m2[i][j]=int(input(f"Enter value for row{i+1} and col{j+1}:"))

#m1= [[2,3],[4,5]]
#m2= [[2,3],[8,9]]
#ans= [[0,0],[0,0]]
#row=2
#col=2

#Addtion
for i in range(row):
    for j in range(col):
        ans[i][j]= m1[i][j]+m2[i][j]

print(ans) 

#Subtraction
for i in range (row):
    for j in range (col):
        ans[i][j]= m1[i][j]-m2[i][j]

print(ans)

#Transpose
ans=[[0 for i in range(row)] for j in range(col)]
for i in range(row):
    for j in range(col):
        ans[i][j] = m1[j][i]

print("Transpose:",ans)

#Multiplication
if(len(m1[0])==len(m2)):
    print("Multiplication possible")

    ans= [[0 for i in range(len(m2[0]))] for i in range(len(m1))]

    for i in range(row):
        for j in range(col):
            for k in range(row):
                ans[i][j] += m1[i][k]*m2[k][j]
else:
    print("Multiplication not possible")

print("Multiplication:",ans)            