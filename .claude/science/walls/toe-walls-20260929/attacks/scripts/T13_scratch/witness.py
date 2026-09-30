"""Test 1: the N5 two-clock witness in a chain whose single time is not in doubt.

Open critical-Ising chain L=8: H = sum ZZ + sum X.  A = site 0, B = site 7.
"""
import numpy as np
from scipy.linalg import expm

L = 8
I2 = np.eye(2); X = np.array([[0, 1], [1, 0]], complex); Z = np.diag([1., -1.]).astype(complex)


def op(single, j):
    mats = [I2] * L
    mats[j] = single
    out = mats[0]
    for m in mats[1:]:
        out = np.kron(out, m)
    return out


def op2(a, j, b, k):
    mats = [I2] * L
    mats[j] = a
    mats[k] = b
    out = mats[0]
    for m in mats[1:]:
        out = np.kron(out, m)
    return out


def ham(cut_bonds=()):
    H = np.zeros((2 ** L, 2 ** L), complex)
    for j in range(L - 1):
        if j in cut_bonds:
            continue
        H += op2(Z, j, Z, j + 1)
    for j in range(L):
        H += op(X, j)
    return H


def comm(a, b):
    return a @ b - b @ a


def nrm(a):
    return np.linalg.norm(a)


Id = np.eye(2 ** L)
HA = Id + op(X, 0)
HB = Id + op(X, L - 1)
H = ham()
Hdec = ham(cut_bonds=(0, L - 2))   # bonds (0,1) and (6,7) removed

print("[H_A,H_B] norm           :", nrm(comm(HA, HB)))
print("H_A >= 0, H_B >= 0       :", np.linalg.eigvalsh(HA).min() >= -1e-12, np.linalg.eigvalsh(HB).min() >= -1e-12)
# linear independence of generators (Frobenius Gram determinant)
g = np.array([[np.vdot(a, b).real for b in (HA, HB)] for a in (HA, HB)])
print("Gram det (independent if >0):", np.linalg.det(g))


def U(s, t):
    return expm(-1j * (s * HA + t * HB))


rng = np.random.default_rng(1)
err = 0
for _ in range(5):
    s, t, s2, t2 = rng.normal(size=4)
    err = max(err, nrm(U(s, t) @ U(s2, t2) - U(s + s2, t + t2)))
print("R^2 homomorphism residual:", err)
# is U(1,0) on the one-parameter orbit exp(-i tau (H_A+H_B))?  test: min over tau
Ssum = HA + HB
best = min(nrm(U(1, 0) - expm(-1j * tau * Ssum)) for tau in np.linspace(-6, 6, 2401))
print("min_tau ||U(1,0) - exp(-i tau (HA+HB))|| :", best)

print("--- dynamics")
print("connected chain:  ||[H_A,H]|| =", nrm(comm(HA, H)), " ||[H_B,H]|| =", nrm(comm(HB, H)))
print("decoupled chain:  ||[H_A,Hdec]|| =", nrm(comm(HA, Hdec)), " ||[H_B,Hdec]|| =", nrm(comm(HB, Hdec)))
# same for a block Hamiltonian on 3 end sites
def block(sites):
    Hb = np.zeros_like(H)
    for j in sites:
        Hb += op(X, j)
    for j in sites[:-1]:
        Hb += op2(Z, j, Z, j + 1)
    return Hb
BA = block([0, 1, 2]); BB = block([5, 6, 7])
print("block A={0,1,2}, B={5,6,7}: ||[BA,BB]|| =", nrm(comm(BA, BB)),
      " ||[BA,H]|| =", nrm(comm(BA, H)), " ||[BB,H]|| =", nrm(comm(BB, H)))
