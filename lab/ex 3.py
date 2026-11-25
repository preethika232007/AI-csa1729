
r = int(input("Enter rows: "))
c = int(input("Enter columns: "))

A = []
print("Enter matrix:")
for i in range(r):
    A.append(list(map(int, input().split())))

print("Transpose of matrix:")
for j in range(c):
    for i in range(r):
        print(A[i][j], end=" ")
    print()
