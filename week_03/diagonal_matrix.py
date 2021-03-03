number = 4

matrix = []

for row in range(number):
    matrix.append([0]*number)
    for i in range(number):
        if i==row :
            matrix[row][i] += 1
        #else:
            #matrix[row][i] += 0

print(matrix)