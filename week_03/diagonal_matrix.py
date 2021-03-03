number = 4
matrix = []

for row in range(len(matrix)):
    for i in range(row):
        if i==row :
            matrix[row][i] += 1
        else:
            matrix[row][i] += 0

print(matrix)