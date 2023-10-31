import random
class Matrix():
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matrix = []
        for _ in range(n):
            row = []
            for _ in range(m):
                random_value = random.randint(1, 50)
                row.append(random_value)
            self.matrix.append(row)

    def print_matrix(self):
        for row in self.matrix:
            print(row)

    def calculate_mean(self):
        total = 0
        for row in self.matrix:
            total+=sum(row)
        return total/(self.n * self.m)
    def calculate_row(self,row_index):
        if 0<=row_index<=self.n:
            return sum(self.matrix[row_index])
        else:
            return None
    def calculate_col_average(self, col_index):
        if 0<=col_index<=self.m:
            col_sum = 0
            for row in self.matrix:
                col_sum += row[col_index]
            return col_sum / self.n
        else:
            return None
    
    def submatrix(self, row1, row2, col1, col2):
        if 0 <= row1 <= row2 < self.n and 0 <= col1 <= col2 < self.m:
            sub_mat = [row[col1:col2 + 1] for row in self.matrix[row1:row2 + 1]]
            
            for row in sub_mat:
                print(row)
        else:
            print("Invalid submatrix dimensions.")


matrix = Matrix(6,5)
print("\nMatrix:")
matrix.print_matrix()
print("\nMean of matrix =", matrix.calculate_mean())
print("\nSum of row 2 =", matrix.calculate_row(1))
print("\nAverage of column 3 =", matrix.calculate_col_average(2))
print("\nSubmatrix: ")
matrix.submatrix(0,2,2,4)
