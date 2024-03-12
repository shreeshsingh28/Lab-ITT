r = int(input("Enter rows: "))
c = int(input("Enter cols: "))

# Input matrix
mat = []
for i in range(r):
    a = []
    for j in range(c):
        a.append(int(input("Enter element: ")))
    mat.append(a)

# Display original matrix
print("Original Matrix:")
for i in range(r):
    for j in range(c):
        print(mat[i][j], end=" ")
    print()


# Transpose matrix
mat2 = [[0] * r for _ in range(c)]  # Correct initialization
for i in range(r):
    for j in range(c):
        mat2[j][i] = mat[i][j]

# Display transposed matrix
print("\nTransposed Matrix:")
for i in range(c):
    for j in range(r):
        print(mat2[i][j], end=" ")
    print()
