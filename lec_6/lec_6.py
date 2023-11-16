import random

def generate_random_matrix(rows, cols):
    matrix = []
    for _ in range(rows):
        row = []
        for _ in range(cols):
            random_value = random.randint(1, 100)
            row.append(random_value)
        matrix.append(row)
    return matrix

def get_column_sum(matrix, column_index):
    if not matrix:
        print("Matrix is empty.")
    elif not matrix[0]:
        print("Matrix is empty.")
    elif column_index < 0 or column_index >= len(matrix[0]):
        print("Invalid column index.")
    else:
        column_sum = 0
        for row in matrix:
            column_sum += row[column_index]
        return column_sum

def get_row_average(matrix, row_index):
    if not matrix:
        print("Matrix is empty.")
    elif row_index < 0 or row_index >= len(matrix):
        print("Invalid row index.")
    elif not matrix[row_index]:
        print("Row is empty.")
    else:
        row = matrix[row_index]
        row_sum = sum(row)
        row_average = row_sum / len(row)
        return row_average

matrix = generate_random_matrix(3, 4)
for row in matrix:
    print(row)

col_index = int(input("Enter column index: "))
row_index = int(input("Enter row index: "))

column_sum = get_column_sum(matrix, col_index)
if column_sum is not None:
    print(f"Sum of column {col_index + 1} is {column_sum}.")

row_average = get_row_average(matrix, row_index)
if row_average is not None:
    print(f"Average of row {row_index + 1} is {row_average}.")
