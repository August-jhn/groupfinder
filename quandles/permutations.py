import itertools
import numpy as np
import math

n = 4
numbers = [i for i in range(1,n+1)]

permutations = list(itertools.permutations(numbers))

P = [[] for i in range(n)]

for i in range(n):
    for p in permutations:
        if p[i] == i + 1:
            P[i].append(list(p))

indices = list(itertools.product([i for i in range(math.factorial(n-1))],repeat = n))

matrices = []

good_matrices = []

for ind in indices:
    m = []
    i = 0
    for p in P:
        
        m.append(p[ind[i]])
        i += 1
    matrices.append(m)
        


def check(matrix):
    for i in range(n):
        for j in range(n):
            for k in range(n): #note that it is columns x rows, not rows x columns as usual
                if matrix[k][matrix[j][i] -1] != matrix[matrix[k][j]-1][matrix[k][i]-1]:
                    return False
    return True

def find_permutation_matrices_and_inverses(n):
    """returns a list of tuples (permutation matrix, inverse of)"""
    def find_permutation_matrices(n):
        permutation_matrices = []
        bases = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            bases[i][i] = 1

        ps = list(itertools.permutations(bases))
        permutations = [[] for i in range(len(ps))]
        for i in range(len(permutations)):
            for j in range(n):
                permutations[i].append(ps[i][j])

        for p in permutations:
            
            permutation_matrices.append(np.array(p))
        return permutation_matrices

    #some debuging
    permutation_matrices = find_permutation_matrices(n)
    matrices_and_inverses = []
    for m in permutation_matrices:
        inv_m = np.linalg.inv(m).astype(int)
        matrices_and_inverses.append((m, inv_m)) 

    return matrices_and_inverses

permutations_and_inverses = find_permutation_matrices_and_inverses(n)

for matrix in matrices:
    if check(matrix):
        
        good_matrices.append(matrix)
      #  rho_matrix = np.matmul(np.matmul(inv, matrix), perm)

print("there are this many matrices",len(good_matrices))
for matrix in good_matrices:
    for perms in permutations_and_inverses:
        perm = perms[0]
        inv = perms[1]

        number_vec = np.matrix([[i+1] for i in range(n)])

        number_vec_permuted = np.matmul(perm, number_vec)

        matrix_permuted = np.zeros((n,n))

        for i in range(n):
            for j in range(n):
                
                matrix_permuted[i][j] = number_vec_permuted[matrix[i][j]-1]
                

        rho_matrix = np.matmul(np.matmul(inv, matrix_permuted), perm)
        i = 0
        for m in good_matrices:
            
            if not np.array_equal(matrix, rho_matrix) and np.array_equal(m, rho_matrix):
                good_matrices.remove(good_matrices[i])
                print(i)
            
            i += 1

print(np.array_equal(good_matrices[0], np.matmul(permutations_and_inverses[0][0],good_matrices[0])))
print(good_matrices)
#debuging stuff
print(len(good_matrices),len(permutations_and_inverses))
for m in good_matrices:
    print(m)

print([p[0] for p in permutations_and_inverses])
k = 3