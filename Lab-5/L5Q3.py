r1 = int(input("enter rows- "))
c1 = int(input("enter cols- "))

mat1 = []

for i in range(r1):
    a = []
    for j in range(c1):
        a.append(int(input("element- ")))
    mat1.append(a)

for i in range(r1):
    for j in range(c1):
        print(mat1[i][j], end=" ")
    print()

r2 = int(input("enter rows- "))
c2 = int(input("enter cols- "))

mat2 = []

for i in range(r2):
    a = []
    for j in range(c2):
        a.append(int(input("element- ")))
    mat2.append(a)

for i in range(r2):
    for j in range(c2):
        print(mat2[i][j], end=" ")
    print()

mat3 = [[0]*c2 for _ in range(r1)]

for i in range(r1):
    for j in range(c2):
        for k in range(c1):
            mat3[i][j] = mat3[i][j] + mat1[i][k] * mat2[k][j]

for i in range(r1):
    for j in range(c2):
        print(mat3[i][j], end=" ")
    print()