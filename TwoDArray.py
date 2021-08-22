"""
   * Author - Shardul Khapke
   * Date - 18-AUG-2021
   * Time - 6:38 PM
   * Title - Print 2D Array.
"""
Rows = int(input("Enter the number of rows:"))
Col = int(input("Enter the number of columns:"))

matrix = []
print("Enter the entries in row wise:")

for M in range(Rows):
    array = []
    for N in range(Col):
        array.append(int(input()))  # ---->ADDING INPUT IN ARRAY
    matrix.append(array)
print("The 2D array is given below:")
for M in range(Rows):
    for N in range(Col):
        print(matrix[M][N], end=" ")
    print()