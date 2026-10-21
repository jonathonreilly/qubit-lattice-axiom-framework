"""Reviewer's independent GF(2)/Pauli engine (numpy, packed uint64 rows). Does not import c6_lib."""
import numpy as np

class Pauli:
    """i^ph * X^x Z^z  with x, z boolean numpy arrays of length n."""
    __slots__ = ('x', 'z', 'ph')
    def __init__(self, n, x=None, z=None, ph=0):
        self.x = np.zeros(n, bool) if x is None else x
        self.z = np.zeros(n, bool) if z is None else z
        self.ph = ph % 4
    def copy(self):
        return Pauli(len(self.x), self.x.copy(), self.z.copy(), self.ph)
    def __mul__(self, o):
        # X^x1 Z^z1 X^x2 Z^z2 = (-1)^{z1.x2} X^{x1+x2} Z^{z1+z2}
        s = int(np.count_nonzero(self.z & o.x))
        return Pauli(len(self.x), self.x ^ o.x, self.z ^ o.z, self.ph + o.ph + 2 * s)
    def inv(self):
        # (i^p X^x Z^z)^{-1} = i^{-p} Z^z X^x = i^{-p} (-1)^{x.z} X^x Z^z
        s = int(np.count_nonzero(self.x & self.z))
        return Pauli(len(self.x), self.x.copy(), self.z.copy(), -self.ph + 2 * s)
    def comm(self, o):
        return (int(np.count_nonzero(self.x & o.z)) + int(np.count_nonzero(self.z & o.x))) % 2 == 0
    def is_identity(self):
        return not self.x.any() and not self.z.any()
    def weight(self):
        return int(np.count_nonzero(self.x | self.z))
    def hermitian(self):
        # i^p X^x Z^z hermitian iff p + |x.z| even
        return (self.ph + int(np.count_nonzero(self.x & self.z))) % 2 == 0

def X_on(n, qs):
    P = Pauli(n); P.x[list(qs)] = True if len(qs) else P.x[[]]; return P
def Z_on(n, qs):
    P = Pauli(n)
    for q in qs: P.z[q] ^= True
    return P
def Xs(n, qs):
    P = Pauli(n)
    for q in qs: P.x[q] ^= True
    return P
def Y_on(n, q):
    P = Pauli(n); P.x[q] = True; P.z[q] = True; P.ph = 1   # Y = i X Z
    return P
def prod(ps, n):
    out = Pauli(n)
    for p in ps: out = out * p
    return out

def vec(P):
    return np.concatenate([P.x, P.z])

def pack(M):
    """bool matrix rows x cols -> uint64 rows x words"""
    M = np.asarray(M, bool)
    r, c = M.shape
    w = (c + 63) // 64
    pad = np.zeros((r, w * 64), bool); pad[:, :c] = M
    b = np.packbits(pad.reshape(r, w, 64)[:, :, ::-1], axis=2, bitorder='big')  # 8 bytes per word
    return b.view('>u8').reshape(r, w).astype(np.uint64)

def rank_packed(P, ncols):
    P = P.copy(); r = 0; nrows = P.shape[0]
    for col in range(ncols):
        w, b = divmod(col, 64)
        bitcol = (P[r:, w] >> np.uint64(b)) & np.uint64(1)
        nz = np.nonzero(bitcol)[0]
        if len(nz) == 0: continue
        p = r + nz[0]
        if p != r: P[[r, p]] = P[[p, r]]
        rows = r + 1 + np.nonzero(((P[r+1:, w] >> np.uint64(b)) & np.uint64(1)))[0]
        if len(rows): P[rows] ^= P[r]
        r += 1
        if r == nrows: break
    return r

def rank(M):
    M = np.asarray(M, bool)
    if M.shape[0] == 0: return 0
    return rank_packed(pack(M), M.shape[1])

def left_kernel(M):
    """Basis (bool rows over the row index) of {c : c^T M = 0}. Dense elimination with tracking."""
    M = np.asarray(M, bool).copy(); m, n = M.shape
    T = np.eye(m, dtype=bool)
    r = 0
    for col in range(n):
        nz = np.nonzero(M[r:, col])[0]
        if len(nz) == 0: continue
        p = r + nz[0]
        if p != r:
            M[[r, p]] = M[[p, r]]; T[[r, p]] = T[[p, r]]
        rows = np.nonzero(M[:, col])[0]; rows = rows[rows != r]
        M[rows] ^= M[r]; T[rows] ^= T[r]
        r += 1
        if r == m: break
    return T[r:]

def nullspace(M):
    """right nullspace of bool matrix M (rows x n): basis of {x : M x = 0}."""
    M = np.asarray(M, bool).copy(); m, n = M.shape
    piv = []; r = 0
    for col in range(n):
        if r == m: break
        nz = np.nonzero(M[r:, col])[0]
        if len(nz) == 0: continue
        p = r + nz[0]
        if p != r: M[[r, p]] = M[[p, r]]
        rows = np.nonzero(M[:, col])[0]; rows = rows[rows != r]
        M[rows] ^= M[r]
        piv.append(col); r += 1
    free = [c for c in range(n) if c not in set(piv)]
    out = []
    for f in free:
        x = np.zeros(n, bool); x[f] = True
        for i, pc_ in enumerate(piv):
            if M[i, f]: x[pc_] = True
        out.append(x)
    return np.array(out, bool).reshape(len(out), n)
