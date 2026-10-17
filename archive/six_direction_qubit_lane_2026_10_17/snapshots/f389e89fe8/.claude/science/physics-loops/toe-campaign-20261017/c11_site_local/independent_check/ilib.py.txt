"""Independent library: edge and half-edge BKSF codes on the L^3 torus.

Written from the definitions only (did not read the c11 runner or c11 scratch scripts).

Pauli = (x, z, k) meaning i^k X^x Z^z with x, z python-int bit vectors.
"""
import itertools

DIRS = [(0, 1), (1, 1), (2, 1), (0, -1), (1, -1), (2, -1)]
DIDX = {d: i for i, d in enumerate(DIRS)}


def popc(a):
    return a.bit_count()


def pmul(P, Q):
    x1, z1, k1 = P
    x2, z2, k2 = Q
    return (x1 ^ x2, z1 ^ z2, (k1 + k2 + 2 * popc(z1 & x2)) % 4)


def pdag(P):
    x, z, k = P
    # (i^k X^x Z^z)^dag = i^-k Z^z X^x = i^-k (-1)^{x.z} X^x Z^z
    return (x, z, (-k + 2 * popc(x & z)) % 4)


def commute(P, Q):
    return (popc(P[0] & Q[1]) + popc(P[1] & Q[0])) % 2 == 0


# ---------------------------------------------------------------- rotations
def rotations():
    mats = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product([1, -1], repeat=3):
            M = [[0] * 3 for _ in range(3)]
            for i in range(3):
                M[i][perm[i]] = signs[i]
            # det
            d = (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
                 - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
                 + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))
            if d == 1:
                mats.append(tuple(tuple(r) for r in M))
    assert len(mats) == 24
    return mats


def mvec(M, v):
    return tuple(sum(M[i][j] * v[j] for j in range(3)) for i in range(3))


def rot_dir(M, d):
    a, s = DIRS[d]
    e = [0, 0, 0]
    e[a] = s
    w = mvec(M, e)
    for b in range(3):
        if w[b] != 0:
            return DIDX[(b, w[b])]


def mmul(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)) for i in range(3))


def rot_type(M):
    tr = M[0][0] + M[1][1] + M[2][2]
    # identity 3, C2: -1, C3: 0, C4: 1
    order = {3: 1, -1: 2, 0: 3, 1: 4}[tr]
    if order == 2:
        # axis C2 if diagonal matrix
        diag = all(M[i][j] == 0 for i in range(3) for j in range(3) if i != j)
        return 'C2axis' if diag else 'C2edge'
    return {1: 'E', 3: 'C3', 4: 'C4'}[order]


# ---------------------------------------------------------------- lattice
class Lat:
    def __init__(self, L):
        self.L = L
        self.N = L ** 3

    def vid(self, v):
        L = self.L
        return (v[0] % L) + L * (v[1] % L) + L * L * (v[2] % L)

    def vec(self, i):
        L = self.L
        return (i % L, (i // L) % L, i // (L * L))

    def add(self, v, d):
        a, s = DIRS[d]
        w = list(v)
        w[a] += s
        return tuple(w)

    def verts(self):
        return [self.vec(i) for i in range(self.N)]


# ---------------------------------------------------------------- edge model
class EdgeModel:
    """qubit on edge (v,a) from v to v+e_a; index 3*vid + a."""

    def __init__(self, L):
        self.lat = Lat(L)
        self.n = 3 * self.lat.N

    def edge_at(self, v, d):
        """the edge at vertex v in direction d"""
        a, s = DIRS[d]
        if s == 1:
            return 3 * self.lat.vid(v) + a
        w = list(v)
        w[a] -= 1
        return 3 * self.lat.vid(w) + a

    def A(self, o, v, a):
        rank = {d: i for i, d in enumerate(o)}
        w = self.lat.add(v, a)
        x = 1 << self.edge_at(v, a)
        z = 0
        for d in range(6):
            if rank[d] < rank[a]:
                z ^= 1 << self.edge_at(v, d)
            if rank[d] < rank[a + 3]:
                z ^= 1 << self.edge_at(w, d)
        return (x, z, 0)

    def B(self, v):
        z = 0
        for d in range(6):
            z ^= 1 << self.edge_at(v, d)
        return (0, z, 0)

    def rot_qubit_perm(self, M):
        lat = self.lat
        perm = [0] * self.n
        for i in range(lat.N):
            v = lat.vec(i)
            Rv = mvec(M, v)
            for a in range(3):
                d2 = rot_dir(M, a)
                perm[3 * i + a] = self.edge_at(Rv, d2)
        return perm

    def gens_extra(self, v):
        return []


# ---------------------------------------------------------------- half-edge model
class HalfModel:
    """six qubits per site: qubit (v,d) index 6*vid + d."""

    def __init__(self, L, rsign=1):
        self.lat = Lat(L)
        self.n = 6 * self.lat.N
        self.rsign = rsign

    def q(self, v, d):
        return 6 * self.lat.vid(v) + d

    def A(self, o, v, a):
        rank = {d: i for i, d in enumerate(o)}
        w = self.lat.add(v, a)
        x = (1 << self.q(v, a)) | (1 << self.q(w, a + 3))
        z = 0
        for d in range(6):
            if rank[d] < rank[a]:
                z ^= 1 << self.q(v, d)
            if rank[d] < rank[a + 3]:
                z ^= 1 << self.q(w, d)
        return (x, z, 0)

    def B(self, v):
        z = 0
        for d in range(6):
            z ^= 1 << self.q(v, d)
        return (0, z, 0)

    def R(self, v, a):
        w = self.lat.add(v, a)
        z = (1 << self.q(v, a)) | (1 << self.q(w, a + 3))
        return (0, z, 0 if self.rsign == 1 else 2)

    def rot_qubit_perm(self, M):
        """framework site rotation: site v -> Rv, qubit label d -> Rd."""
        lat = self.lat
        perm = [0] * self.n
        for i in range(lat.N):
            v = lat.vec(i)
            Rv = mvec(M, v)
            for d in range(6):
                perm[6 * i + d] = self.q(Rv, rot_dir(M, d))
        return perm

    def gens_extra(self, v):
        return [self.R(v, a) for a in range(3)]


# ---------------------------------------------------------------- common
def plaq_hops(model, v, a, b):
    """edges of plaquette at v in plane (a,b), a<b, in cyclic order v->v+a->v+a+b->v+b->v"""
    lat = model.lat
    return [(v, a), (lat.add(v, a), b), (lat.add(v, b), a), (v, b)]


def S(model, o, v, a, b, sign=1):
    P = (0, 0, 0)
    for (w, c) in plaq_hops(model, v, a, b):
        P = pmul(P, model.A(o, w, c))
    if sign == -1:
        P = (P[0], P[1], (P[2] + 2) % 4)
    return P


PLANES = [(0, 1), (0, 2), (1, 2)]  # normal axes 2, 1, 0


def normal(a, b):
    return 3 - a - b


def generators(model, o, sec=(1, 1, 1)):
    """sec[c] = sign of plaquettes normal to axis c"""
    g = []
    for v in model.lat.verts():
        g.append(model.B(v))
        g.extend(model.gens_extra(v))
        for (a, b) in PLANES:
            g.append(S(model, o, v, a, b, sec[normal(a, b)]))
    return g


def permute_bits(val, perm):
    out = 0
    while val:
        low = val & -val
        i = low.bit_length() - 1
        out |= 1 << perm[i]
        val ^= low
    return out


def permute_pauli(P, perm):
    return (permute_bits(P[0], perm), permute_bits(P[1], perm), P[2])


class SignedSpan:
    """Echelon basis keyed by leading bit of combined vector; tracks phases.
    All rows have eigenvalue +1 on the code space (if generators commute and are consistent)."""

    def __init__(self, n):
        self.n = n
        self.rows = {}
        self.consistent = True

    def comb(self, P):
        return P[0] | (P[1] << self.n)

    def reduce(self, P):
        c = self.comb(P)
        while c:
            hb = c.bit_length() - 1
            r = self.rows.get(hb)
            if r is None:
                return P, False
            P = pmul(P, r)
            c = self.comb(P)
        return P, True

    def add(self, P):
        R, inspan = self.reduce(P)
        if inspan:
            if R[2] != 0:
                self.consistent = False
            return False
        hb = self.comb(R).bit_length() - 1
        self.rows[hb] = R
        return True

    def rank(self):
        return len(self.rows)

    def eig(self, P):
        """returns phase c with P|code> = c|code> as i-power, or None if not in group up to phase"""
        R, inspan = self.reduce(P)
        if not inspan:
            return None
        return R[2]


def span_of(model, gens):
    sp = SignedSpan(model.n)
    for g in gens:
        sp.add(g)
    return sp


def all_commute(gens):
    # fast check: group by support locality is unnecessary at these sizes
    n = len(gens)
    for i in range(n):
        for j in range(i + 1, n):
            if not commute(gens[i], gens[j]):
                return False
    return True
