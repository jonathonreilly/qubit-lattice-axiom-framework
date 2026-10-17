"""Independent BKSF-on-Z^3 checker core. Paulis are Python ints: bit i = X on qubit i, bit n+i = Z on qubit i."""
import itertools
import numpy as np

DIRS = [(0, 1), (1, 1), (2, 1), (0, -1), (1, -1), (2, -1)]  # index d -> (axis, sign): +x,+y,+z,-x,-y,-z
DNAME = ['+x', '+y', '+z', '-x', '-y', '-z']


def dir_index(a, s):
    return a if s == 1 else a + 3


class Lattice:
    def __init__(self, L):
        self.L = L
        self.n = 3 * L ** 3

    def vid(self, v):
        L = self.L
        return ((v[0] % L) * L + (v[1] % L)) * L + (v[2] % L)

    def eid(self, v, a):
        return self.vid(v) * 3 + a

    def edge_at(self, v, d):
        a, s = DIRS[d]
        if s == 1:
            return self.eid(v, a)
        w = list(v); w[a] -= 1
        return self.eid(w, a)

    def X(self, q):
        return 1 << q

    def Z(self, q):
        return 1 << (self.n + q)

    def A(self, v, a, rank):
        """rank[d] = position of direction d in ordering. rank=None -> toric code A=X."""
        p = self.X(self.eid(v, a))
        if rank is None:
            return p
        w = list(v); w[a] += 1
        dp, dm = dir_index(a, 1), dir_index(a, -1)
        for d in range(6):
            if rank[d] < rank[dp]:
                p ^= self.Z(self.edge_at(v, d))
            if rank[d] < rank[dm]:
                p ^= self.Z(self.edge_at(w, d))
        return p

    def B(self, v):
        p = 0
        for d in range(6):
            p ^= self.Z(self.edge_at(v, d))
        return p

    def plaq(self, v, a, b, rank):
        va = list(v); va[a] += 1
        vb = list(v); vb[b] += 1
        return self.A(v, a, rank) ^ self.A(va, b, rank) ^ self.A(vb, a, rank) ^ self.A(v, b, rank)

    def verts(self):
        return itertools.product(range(self.L), repeat=3)

    def gens(self, rank):
        Bs = [self.B(v) for v in self.verts()]
        Ss = [self.plaq(v, a, b, rank) for v in self.verts() for (a, b) in [(0, 1), (1, 2), (0, 2)]]
        return Bs, Ss

    def comm(self, p, q):
        n = self.n
        m = (1 << n) - 1
        return bin(((p & m) & (q >> n)) ^ ((p >> n) & (q & m))).count('1') & 1


def rref(rows):
    basis = {}
    for r in rows:
        while r:
            p = r.bit_length() - 1
            if p in basis:
                r ^= basis[p]
            else:
                basis[p] = r
                break
    piv = sorted(basis)
    for p in piv:  # full reduction
        b = basis[p]
        for q in piv:
            if q != p and (basis[q] >> p) & 1:
                basis[q] ^= b
    return tuple(sorted(basis.values()))


def rank(rows):
    basis = {}
    for r in rows:
        while r:
            p = r.bit_length() - 1
            if p in basis:
                r ^= basis[p]
            else:
                basis[p] = r
                break
    return len(basis)


def rank_of_order(order):
    """order: tuple of direction indices, earliest first."""
    rk = [0] * 6
    for i, d in enumerate(order):
        rk[d] = i
    return rk


ORDERS = list(itertools.permutations(range(6)))

# proper rotations: signed permutation matrices det +1
ROTS = []
for perm in itertools.permutations(range(3)):
    for signs in itertools.product([1, -1], repeat=3):
        M = np.zeros((3, 3), dtype=int)
        for i in range(3):
            M[perm[i], i] = signs[i]  # M e_i = signs[i] e_perm[i]
        if round(np.linalg.det(M)) == 1:
            ROTS.append(M)
assert len(ROTS) == 24


def rot_dir(M, d):
    a, s = DIRS[d]
    col = M[:, a] * s
    b = int(np.nonzero(col)[0][0])
    return dir_index(b, int(col[b]))


def rot_order(M, order):
    return tuple(rot_dir(M, d) for d in order)


def qubit_perm(lat, M):
    """perm[q] = image qubit of qubit q under rotation M about origin."""
    perm = [0] * lat.n
    for v in lat.verts():
        Rv = tuple(int(t) for t in (M @ np.array(v)))
        for a in range(3):
            d = rot_dir(M, dir_index(a, 1))
            perm[lat.eid(v, a)] = int(lat.edge_at(Rv, d))
    assert sorted(perm) == list(range(lat.n))
    return perm


def apply_perm(lat, p, perm):
    n = lat.n
    out = 0
    q = 0
    x = p & ((1 << n) - 1)
    z = p >> n
    while x:
        lb = x & -x
        i = lb.bit_length() - 1
        out |= 1 << perm[i]
        x ^= lb
    while z:
        lb = z & -z
        i = lb.bit_length() - 1
        out |= 1 << (n + perm[i])
        z ^= lb
    return out
