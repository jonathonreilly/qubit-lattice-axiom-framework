"""TW-3 helper: Majorana operators by Jordan-Wigner, as sparse signed permutations.

gamma_{2j}   = Z...Z X_j
gamma_{2j+1} = Z...Z Y_j
Basis states are integers s in [0, 2^n); bit j (value 1<<j) is qubit j.
Each Majorana is stored as (flip_mask, phase vector); products are cheap.
"""
import numpy as np
import scipy.sparse as sp


class Maj:
    def __init__(self, nq):
        self.nq = nq
        self.dim = 1 << nq
        s = np.arange(self.dim, dtype=np.int64)
        self.s = s
        # parity of bits below j
        self._below = []
        for j in range(nq):
            mask = (1 << j) - 1
            pc = np.zeros(self.dim, dtype=np.int64)
            x = s & mask
            while np.any(x):
                pc += x & 1
                x >>= 1
            self._below.append(pc & 1)
        self.n_maj = 2 * nq

    def op(self, a):
        """Return (flip, phase) for gamma_a acting as gamma|s> = phase[s] |s^flip>.
        Represented in 'column' convention: (gamma v)[s^flip] = phase[s] v[s]."""
        j, typ = divmod(a, 2)
        bit = (self.s >> j) & 1
        zsign = 1 - 2 * self._below[j]  # Z string
        if typ == 0:   # X
            ph = zsign.astype(complex)
        else:          # Y: Y|0> = i|1>, Y|1> = -i|0>
            ph = zsign * np.where(bit == 0, 1j, -1j)
        return (1 << j, ph)

    def mat(self, a):
        f, ph = self.op(a)
        rows = self.s ^ f
        return sp.csr_matrix((ph, (rows, self.s)), shape=(self.dim, self.dim))

    def string(self, idx):
        """Product gamma_{i1} gamma_{i2} ... as (flip, phase) in column convention."""
        flip = 0
        ph = np.ones(self.dim, dtype=complex)
        # apply rightmost first
        cur = self.s.copy()
        for a in reversed(idx):
            f, p = self.op(a)
            ph = ph * p[cur]
            cur = cur ^ f
            flip ^= f
        return flip, ph

    def string_mat(self, idx, coeff=1.0):
        flip, ph = self.string(idx)
        rows = self.s ^ flip
        return sp.csr_matrix((coeff * ph, (rows, self.s)), shape=(self.dim, self.dim))

    def parity(self):
        pc = np.zeros(self.dim, dtype=np.int64)
        x = self.s.copy()
        while np.any(x):
            pc += x & 1
            x >>= 1
        return 1 - 2 * (pc & 1)


def cayley_terms():
    """Cayley 4-form on R^8 (indices 0..7), Spin(7)-invariant, 14 terms.
    phi = e123 + e145 + e167 + e246 - e257 - e347 - e356 (indices 1..7)
    Omega = e0 ^ phi + *_7 phi.  Signs verified numerically by the commutant test."""
    phi = [((1, 2, 3), 1), ((1, 4, 5), 1), ((1, 6, 7), 1), ((2, 4, 6), 1),
           ((2, 5, 7), -1), ((3, 4, 7), -1), ((3, 5, 6), -1)]
    terms = []
    for (t, sg) in phi:
        terms.append(((0,) + t, sg))
    # Hodge dual in 7D: *(e_abc) = sign * e_{complement}, with e_abc ^ *e_abc = vol
    for (t, sg) in phi:
        comp = tuple(sorted(set(range(1, 8)) - set(t)))
        perm = list(t) + list(comp)
        # sign of permutation perm relative to (1..7)
        p = [x - 1 for x in perm]
        sgn = 1
        p = p[:]
        for i in range(len(p)):
            while p[i] != i:
                k = p[i]
                p[i], p[k] = p[k], p[i]
                sgn = -sgn
        terms.append((comp, sg * sgn))
    return terms
