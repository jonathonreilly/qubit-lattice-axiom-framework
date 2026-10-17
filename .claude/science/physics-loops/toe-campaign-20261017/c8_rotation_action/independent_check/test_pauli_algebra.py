"""Unit test of the phase-tracked Pauli algebra against dense matrices."""
import random
import numpy as np
from pauli_bksf import pmul, sign_vs_canonical, canonical, permute_pauli
from pair_test import dagger

I = np.eye(2); X = np.array([[0, 1], [1, 0]]); Z = np.diag([1, -1]); Y = 1j * X @ Z

def mat(P, n):
    x, z, p = P
    M = np.array([[1]])
    for q in range(n):
        f = I
        if (x >> q) & 1 and (z >> q) & 1:
            f = X @ Z
        elif (x >> q) & 1:
            f = X
        elif (z >> q) & 1:
            f = Z
        M = np.kron(f, M)  # qubit q is the more significant factor
    return (1j) ** p * M

random.seed(1)
n = 4
for _ in range(500):
    P = (random.randrange(16), random.randrange(16), random.randrange(4))
    Q = (random.randrange(16), random.randrange(16), random.randrange(4))
    assert np.allclose(mat(pmul(P, Q), n), mat(P, n) @ mat(Q, n))
    assert np.allclose(mat(dagger(P), n), mat(P, n).conj().T)
    C = canonical(P[0], P[1])
    Cm = mat(C, n)
    assert np.allclose(Cm, Cm.conj().T)  # canonical is Hermitian
    # canonical = tensor product of X, Y, Z
    T = np.array([[1]])
    for q in range(n):
        xb, zb = (P[0] >> q) & 1, (P[1] >> q) & 1
        T = np.kron([I, X, Z, Y][xb + 2 * zb], T)
    assert np.allclose(Cm, T)
    s = sign_vs_canonical(P)
    assert np.allclose(mat(P, n), s * Cm)
    perm = random.sample(range(n), n)
    # permutation matrix action
    PermM = np.zeros((2 ** n, 2 ** n))
    for b in range(2 ** n):
        nb = 0
        for q in range(n):
            if (b >> q) & 1:
                nb |= 1 << perm[q]
        PermM[nb, b] = 1
    assert np.allclose(mat(permute_pauli(P, perm), n), PermM @ mat(P, n) @ PermM.T)
print("Pauli algebra unit test: PASS (500 random products, daggers, canonical forms, permutations)")
