import os
from math import prod

matrix = [[1,2,3,3],[4,5,6,6],[7,8,9,9]]

def matrix_maximus(matrix:list[list[int], list[int]]) -> tuple[list[int], list[int]]:
    transpose_matrix = [list(line) for line in zip(*matrix)]

    sum_column = [sum(column) for column in transpose_matrix]
    prod_column = [prod(column) for column in transpose_matrix]

    index_max_sum = [index for index, value in enumerate(sum_column) if value == max(sum_column)]
    index_max_prod = [index for index, value in enumerate(prod_column) if value == max(prod_column)]

    print(f"Índices das colunas com maior soma: {index_max_sum}")
    print(f"Índices das colunas com maior multiplicação: {index_max_prod}")
    
    return (index_max_sum, index_max_prod)

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    matrix_maximus(matrix)