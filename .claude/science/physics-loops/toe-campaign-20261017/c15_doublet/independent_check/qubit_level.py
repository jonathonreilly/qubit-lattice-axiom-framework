"""Qubit-level checks of the site-local JW encoding (explicit matrices)."""
AUDIT_TIMEOUT_SEC = 1800
import itertools, numpy as np
from functools import reduce
from scipy.linalg import expm
I = np.eye(2); X = np.array([[0, 1], [1, 0]], complex); Y = np.array([[0, -1j], [1j, 0]]); Z = np.diag([1, -1]).astype(complex)
def kron(*a): return reduce(np.kron, a)
def site_majoranas(nq=5):
    chis = []
    for j in range(nq):
        for P in (X, Y):
            ops = [Z] * j + [P] + [I] * (nq - j - 1)
            chis.append(kron(*ops))
    return chis
chi = site_majoranas()
d = 32
ok = all(np.allclose(chi[a] @ chi[b] + chi[b] @ chi[a], 2 * (a == b) * np.eye(d)) for a in range(10) for b in range(10))
print('10 Majoranas per site, Clifford relations:', ok)
D = (-1j) ** 5 * reduce(np.matmul, chi)
print('D_v = Z1Z2Z3Z4Z5:', np.allclose(D, kron(Z, Z, Z, Z, Z)))
B = (-1j) ** 3 * reduce(np.matmul, chi[:6])
print('link parity B = Z1Z2Z3:', np.allclose(B, kron(Z, Z, Z, I, I)))
Pu = -1j * chi[6] @ chi[7]; Pd = -1j * chi[8] @ chi[9]
print('P_up = Z4, P_dn = Z5:', np.allclose(Pu, kron(I, I, I, Z, I)), np.allclose(Pd, kron(I, I, I, I, Z)))
print('D = B P_up P_dn:', np.allclose(D, B @ Pu @ Pd))
cu = (chi[6] + 1j * chi[7]) / 2
sm = np.array([[0, 1], [0, 0]], complex)  # |0><1|
print('c_up = B (x) sigma(4):', np.allclose(cu, B @ kron(I, I, I, sm, I)))
# even link bilinears act only on qubits 1-3, even matter bilinears only on 4-5
def acts_only_on(M, qubits):
    # check M commutes with all Paulis on the complement
    comp = [q for q in range(5) if q not in qubits]
    for q in comp:
        for P in (X, Y, Z):
            ops = [I] * 5; ops[q] = P; Pq = kron(*ops)
            if not np.allclose(M @ Pq, Pq @ M): return False
    return True
print('link bilinears act only on qubits 1-3:', all(acts_only_on(chi[a] @ chi[b], [0, 1, 2]) for a in range(6) for b in range(a + 1, 6)))
print('matter bilinears act only on qubits 4-5:', all(acts_only_on(chi[a] @ chi[b], [3, 4]) for a in range(6, 10) for b in range(a + 1, 10)))
# two sites: Majoranas at different sites commute
chi2a = [np.kron(c, np.eye(32)) for c in chi]; chi2b = [np.kron(np.eye(32), c) for c in chi]
print('Majoranas at different sites commute:', all(np.allclose(a @ b, b @ a) for a in chi2a for b in chi2b))
# so c^dag(x), c^dag(y) commute: matter partons are hard-core bosons at the operator level
cdx = chi2a[6] - 1j * chi2a[7]; cdy = chi2b[6] - 1j * chi2b[7]
print('[c_up^dag(x), c_up^dag(y)] = 0:', np.allclose(cdx @ cdy, cdy @ cdx))
# A link signed permutation with prod eps = sign(perm) is implemented by an even link unitary:
# e.g. C4z on directions: +x->+y->-x->-y->+x ; build from exp(pi/4 chi_a chi_b) rotations
def rot90(a, b):  # chi_a -> chi_b, chi_b -> -chi_a  (or reversed sign)
    return expm(np.pi / 4 * chi[a] @ chi[b])
U = rot90(0, 1) @ rot90(3, 4)
imgs = [U @ chi[k] @ U.conj().T for k in range(10)]
def ident(M):
    for k in range(10):
        for s in (1, -1):
            if np.allclose(M, s * chi[k]): return (s, k)
print('example even link unitary (C4z type): images of chi_0..9 =', [ident(M) for M in imgs])
print('  acts only on qubits 1-3:', acts_only_on(U, [0, 1, 2]))
