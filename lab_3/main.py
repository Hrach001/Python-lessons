def vector_matrix_multiply(vector, matrix):
    if len(vector) != len(matrix):
        raise ValueError("Number of columns in the matrix must be equal to the length of the vector.")
    
    result = []
    for row in matrix:
        row_result = sum(v * m for v, m in zip(vector, row))
        result.append(row_result)
    
    return result

def write_matrix_to_file(matrix, filename):
    with open(filename, 'w') as file:
        for value in matrix:
            file.write(str(value) + '\n')

# Example usage:
vector = [1, 2, 3]
matrix = [[4, 5, 6],
          [7, 8, 9],
          [10, 11, 12]]

result = vector_matrix_multiply(vector, matrix)

output_filename = "output_matrix.txt"
write_matrix_to_file(result, output_filename)

print(f"The result of the vector-matrix multiplication has been written to {output_filename}.")