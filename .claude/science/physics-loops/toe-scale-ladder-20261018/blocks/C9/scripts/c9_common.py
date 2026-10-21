"""C9 shared helpers: dense qubit operators on small site lists.

Conventions: a 'site list' is an ordered list of distinct hashable labels (lattice points as
tuples).  Operators on a site list of length n are 2^n x 2^n dense numpy arrays, tensor factor
order = list order.  Pure numpy, no randomness unless an RNG is passed.
"""
from __future__ import annotations

import itertools
import numpy as np

I2 = np.eye(2, dtype=complex)
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
PAULI = [SX, SY, SZ]


class Counter:
    def __init__(self, fh):
        self.p = 0
        self.f = 0
        self.fh = fh

    def check(self, ok, msg):
        line = ("PASS " if ok else "FAIL ") + msg
        if ok:
            self.p += 1
        else:
            self.f += 1
        self.log(line)
        return ok

    def log(self, line):
        print(line, flush=True)
        self.fh.write(line + "\n")
        self.fh.flush()

    def total(self):
        self.log(f"TOTAL: PASS={self.p} FAIL={self.f}")


def op_on(n, site_ops):
    """Tensor product on n qubits; site_ops: dict index -> 2x2."""
    out = np.array([[1.0 + 0j]])
    for i in range(n):
        out = np.kron(out, site_ops.get(i, I2))
    return out


def perm_op(n, perm):
    """Unitary permuting tensor factors: qubit at position i is moved to position perm[i]."""
    dim = 2 ** n
    P = np.zeros((dim, dim), dtype=complex)
    for b in range(dim):
        bits = [(b >> (n - 1 - i)) & 1 for i in range(n)]
        nb = [0] * n
        for i in range(n):
            nb[perm[i]] = bits[i]
        c = 0
        for i in range(n):
            c = (c << 1) | nb[i]
        P[c, b] = 1.0
    return P


def swap_op(n, i, j):
    perm = list(range(n))
    perm[i], perm[j] = j, i
    return perm_op(n, perm)


def all_perm_ops(n):
    return [perm_op(n, p) for p in itertools.permutations(range(n))]


def embed(op, sub, full):
    """Embed operator `op` on ordered site list `sub` into ordered site list `full` (sub subset)."""
    n = len(full)
    k = len(sub)
    pos = [full.index(s) for s in sub]
    rest = [i for i in range(n) if i not in pos]
    # build op (x) I on order pos+rest, then permute to full order
    big = np.kron(op, np.eye(2 ** (n - k), dtype=complex))
    order = pos + rest  # tensor slot t holds full-site order[t]
    # permutation operator moving slot t -> position order[t]
    Pm = perm_op(n, order)
    return Pm @ big @ Pm.conj().T


def random_su2_invariant(n, rng, hermitian=False):
    """Random element of the image of C[S_n] (= SU(2) commutant on n qubits, Schur-Weyl)."""
    ops = all_perm_ops(n)
    c = rng.normal(size=len(ops)) + 1j * rng.normal(size=len(ops))
    g = sum(ci * P for ci, P in zip(c, ops))
    if hermitian:
        g = g + g.conj().T
    return g


def global_rot(n, U):
    out = np.array([[1.0 + 0j]])
    for _ in range(n):
        out = np.kron(out, U)
    return out


def random_su2(rng):
    a = rng.normal(size=4)
    a /= np.linalg.norm(a)
    return np.array([[a[0] + 1j * a[1], a[2] + 1j * a[3]], [-a[2] + 1j * a[3], a[0] - 1j * a[1]]])


def vector_channel(g, n, a):
    """Decompose g on n qubits at qubit a: g = X0 (x) 1_a + sum_j Xj (x) sigma^j_a.
    Returns list [X0, X1, X2, X3] as operators on the other n-1 qubits (original order)."""
    others = [i for i in range(n) if i != a]
    order = others + [a]
    Pm = perm_op(n, order)  # slot t -> position order[t]
    gp = Pm.conj().T @ g @ Pm  # now qubit a is last slot
    d = 2 ** (n - 1)
    G = gp.reshape(d, 2, d, 2)
    res = []
    for s in [I2, SX, SY, SZ]:
        # X = (1/2) tr_a [ g (1 (x) s) ]
        res.append(0.5 * np.einsum('iajb,ba->ij', G, s))
    return res


def min_support(g, n, tol=1e-9):
    """Indices of qubits on which g acts nontrivially."""
    sup = []
    for a in range(n):
        X = vector_channel(g, n, a)
        if max(np.abs(X[j]).max() for j in (1, 2, 3)) > tol:
            sup.append(a)
    return sup
