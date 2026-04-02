import numpy as np
from utils import *

#renvoie la matrice du nombre de chemins de longueur exactement k
#M[i][j] = nombre de chemin de longueur exactement k entre i et j
def chemins(matrice, k):
    return np.linalg.matrix_power(matrice,k)

def normalize_laplacian(L):
    n = len(L)
    D = np.zeros((n, n))
    for i in range(0, len(D)):
        if(L[i][i] != 0):
            D[i][i] = np.power(float(L[i][i]), -0.5)
    return np.matmul(D, np.matmul(L, D))

def create_permutation_matrix(permu):
    n = len(permu)
    m = [[0 for i in range(0, n)] for j in range(0,n)]
    for i in range(0, n):
        m[i][permu[i]] = 1
    return m

# M : an adjacency matrix
# S : a (bi)partitioning, in the for of a list of nodes belonging to S
# it returns the conductance of such a S/Sc partitioning
def conductance(M, S):
    n = len(M)
    SC = []
    SS = sorted(S)
    j = 0
    for i in range(0,n):
        if j >= len(SS):
            SC.append(i)
        elif i < SS[j]:
            SC.append(i)
        else:
            j+=1
    e = 0.
    for i in S:
        for j in SC:
            e += M[i][j]
    if e == 0:
        return 0.
    L = adj_to_lap(M)
    d1, d2 = 0,0
    for i in S:
        d1 += L[i][i]
    for i in SC:
        d2 += L[i][i]
    mini = min(d1, d2)
    if mini == 0:
        return float('inf')
    return e/mini

# takes an adjacency matrix as input
def spectral_partition(M):
    n = len(M)
    L0 = adj_to_lap(M)
    L = normalize_laplacian(L0)
    eigens = np.linalg.eig(L)
    eigenvectors = []
    # REGARDEZ !!! LES EIGENVECTORS SONT CHIFFRES DANS NUMPY, IL FAUT LES DECHIFFRER 
    for i in range(0,n):
        eigenvectors.append(eigens.eigenvectors[:,i])
    lam2 = sorted(eigens.eigenvalues)[1]
    fiedler = None
    for i in range(0, len(eigens.eigenvalues)):
        if lam2 == eigens.eigenvalues[i]:
            fiedler = eigenvectors[i]
            break
    fiedler_ord = [(fiedler[i], i) for i in range(0, len(fiedler))]
    permu = [id for (_, id) in sorted(fiedler_ord)]
    S = []
    meilleur_score = float('inf')
    # finalement on peut améliorer cette partie en modifiant petit à petit E(S,SC) et Vol(S) Vol(SC)
    # comme ça le bottleneck redevient l'obtention des valeurs propres
    # visiblement les valeurs propres de trouvent en O(n^2), mais potentiellement encore plus vite sous forme de matrices creuses non ? 
    for eta in range(0,n-1):
        S.append(permu[eta])
        current_score = conductance(M, S)
        if current_score < meilleur_score:
            S_final = S.copy()
            meilleur_score = current_score
    return S_final

# takes an adjacency matrix as input
def bruteforce_partition(M):
    L = adj_to_lap(M)
    bruteforce_partition.n = len(M)
    bruteforce_partition.S_opti, bruteforce_partition.score_opti = [], float('inf')
    def aux(p, S):
        if p == bruteforce_partition.n:
            score = conductance(M, S)
            if(score < bruteforce_partition.score_opti and S != [] and len(S) != bruteforce_partition.n):
                bruteforce_partition.score_opti = score
                bruteforce_partition.S_opti = S.copy()
        else:
            aux(p+1, S)
            S.append(p)
            aux(p+1, S)
            del S[-1]
    aux(0, [])
    return bruteforce_partition.S_opti

def spectral_partition_fast(M):
    n = len(M)
    L0 = adj_to_lap(M)
    L = normalize_laplacian(L0)
    eigens = np.linalg.eig(L)
    eigenvectors = []
    for i in range(0,n):
        eigenvectors.append(eigens.eigenvectors[:,i])
    lam2 = sorted(eigens.eigenvalues)[1]
    fiedler = None
    for i in range(0, len(eigens.eigenvalues)):
        if lam2 == eigens.eigenvalues[i]:
            fiedler = eigenvectors[i]
            break
    fiedler_ord = [(fiedler[i], i) for i in range(0, len(fiedler))]
    permu = [id for (_, id) in sorted(fiedler_ord)]
    permuinv = inverse_permutation(permu)
    S = []
    meilleur_score = float('inf')
    volS, volSC, e = 0, 0, 0
    for i in range(0,n):
        volSC += L0[i][i]
    for eta in range(0,n-1):
        node = permu[eta]
        S.append(node)
        volSC -= L0[node][node]
        volS += L0[node][node]
        for i in range(0, n):
            j = permuinv[i]
            if j < eta:
                e -= M[node][i]
            elif j > eta:
                e += M[node][i]
        if min(volS, volSC) == 0:
            current_score = float('inf')
        else:
            current_score = e/min(volS, volSC)
        if current_score < meilleur_score:
            S_final = S.copy()
            meilleur_score = current_score
    return S_final