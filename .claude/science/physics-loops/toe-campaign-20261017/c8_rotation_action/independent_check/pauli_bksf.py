"""Independent re-implementation (written from the definitions in the note,
without reading the C8 runner) of the translation-invariant BKSF codes on the
L-torus, with exact Pauli algebra including phases.

Pauli convention: (x, z, ph) means i^ph * X^x Z^z, x and z are Python ints used
as bit sets over the qubits. Hermitian "canonical" form of a support (x, z) is
i^{|x&z|} X^x Z^z  (= tensor product of single-qubit X, Y, Z with Y = iXZ).
"""
import itertools

DIRS = [(0, +1), (1, +1), (2, +1), (0, -1), (1, -1), (2, -1)]


def popcount(n):
    return n.bit_count()


def pmul(P, Q):
    x1, z1, p1 = P
    x2, z2, p2 = Q
    return (x1 ^ x2, z1 ^ z2, (p1 + p2 + 2 * popcount(z1 & x2)) % 4)


def sign_vs_canonical(P):
    """Return s with P = s * canonical(P.x, P.z); s in {1,-1,1j,-1j}."""
    x, z, p = P
    k = (p - popcount(x & z)) % 4
    return [1, 1j, -1, -1j][k]


def canonical(x, z, sgn=1):
    k = popcount(x & z) % 4
    if sgn == -1:
        k = (k + 2) % 4
    return (x, z, k)


class Lattice:
    def __init__(self, L):
        self.L = L
        self.nv = L ** 3
        self.n = 3 * L ** 3

    def vid(self, v):
        L = self.L
        return (v[0] % L) + L * ((v[1] % L) + L * (v[2] % L))

    def vert(self, i):
        L = self.L
        return (i % L, (i // L) % L, i // (L * L))

    def edge(self, v, a):
        return 3 * self.vid(v) + a

    @staticmethod
    def add(v, a, s=1):
        w = list(v)
        w[a] += s
        return tuple(w)

    def edge_at(self, v, d):
        """Qubit index of the edge at vertex v in direction d=(a,s)."""
        a, s = d
        if s == +1:
            return self.edge(v, a)
        return self.edge(self.add(v, a, -1), a)

    def verts(self):
        L = self.L
        return [(x, y, z) for z in range(L) for y in range(L) for x in range(L)]


class Code:
    """BKSF code for one ordering (tuple of 6 indices into DIRS, earliest first)."""

    def __init__(self, lat, order):
        self.lat = lat
        self.order = tuple(order)
        self.rank = {DIRS[d]: i for i, d in enumerate(order)}
        self._A = {}

    def A(self, v, a):
        lat = self.lat
        key = (lat.vid(v), a)
        if key in self._A:
            return self._A[key]
        x = 1 << lat.edge(v, a)
        z = 0
        r_plus = self.rank[(a, +1)]
        r_minus = self.rank[(a, -1)]
        w = lat.add(v, a)
        for d in DIRS:
            if self.rank[d] < r_plus:
                z ^= 1 << lat.edge_at(v, d)
            if self.rank[d] < r_minus:
                z ^= 1 << lat.edge_at(w, d)
        P = (x, z, 0)  # X and Z on disjoint qubits -> Hermitian already
        assert x & z == 0
        self._A[key] = P
        return P

    def B(self, v):
        z = 0
        for d in DIRS:
            z ^= 1 << self.lat.edge_at(v, d)
        return (0, z, 0)

    @staticmethod
    def plane(c):
        a, b = [t for t in range(3) if t != c]
        return a, b

    def hop(self, v, c):
        """A(v,b) A(v+b,a) A(v+a,b) A(v,a) around the plaquette at v normal to c."""
        a, b = self.plane(c)
        add = self.lat.add
        Q = self.A(v, b)
        Q = pmul(Q, self.A(add(v, b), a))
        Q = pmul(Q, self.A(add(v, a), b))
        Q = pmul(Q, self.A(v, a))
        return Q

    def generators(self, s=(0, 0, 0)):
        """Signed generators: list of (label, Pauli). Plaquette generator =
        (-1)^{s_c} * canonical Hermitian Pauli on the hop product's support."""
        gens = []
        for v in self.lat.verts():
            gens.append((("B", v), self.B(v)))
        for v in self.lat.verts():
            for c in range(3):
                Q = self.hop(v, c)
                gens.append((("P", v, c), canonical(Q[0], Q[1], -1 if s[c] else 1)))
        return gens

    def hop_signs(self):
        """For each orientation c the set of signs hop/canonical over all v."""
        out = {}
        for c in range(3):
            out[c] = set(sign_vs_canonical(self.hop(v, c)) for v in self.lat.verts())
        return out


class Span:
    """GF(2) row reduction of a list of Paulis (as 2n-bit vectors) with
    tracking of which generators were combined."""

    def __init__(self, paulis, n):
        self.n = n
        self.paulis = paulis
        self.piv = {}  # pivot bit -> (vec, combo)
        self.relations = []
        for i, P in enumerate(paulis):
            vec = P[0] | (P[1] << n)
            combo = 1 << i
            vec, combo = self._reduce(vec, combo)
            if vec == 0:
                self.relations.append(combo)
            else:
                pb = vec.bit_length() - 1
                self.piv[pb] = (vec, combo)
        self.rank = len(self.piv)

    def _reduce(self, vec, combo):
        piv = self.piv
        while vec:
            pb = vec.bit_length() - 1
            if pb not in piv:
                return vec, combo
            pv, pc = piv[pb]
            vec ^= pv
            combo ^= pc
        return 0, combo

    def decompose(self, P):
        """Return combo bitmask with XOR of generator supports == support of P,
        or None if P is not in the span (up to phase)."""
        vec = P[0] | (P[1] << self.n)
        vec, combo = self._reduce(vec, 0)
        if vec != 0:
            return None
        return combo

    def product(self, combo, paulis=None):
        paulis = self.paulis if paulis is None else paulis
        R = (0, 0, 0)
        i = 0
        while combo:
            if combo & 1:
                R = pmul(R, paulis[i])
            combo >>= 1
            i += 1
        return R

    def canonical_basis(self):
        """Fully reduced row echelon form (frozenset) for span comparison."""
        rows = dict((k, v[0]) for k, v in self.piv.items())
        keys = sorted(rows, reverse=True)
        for k in keys:
            for k2 in keys:
                if k2 != k and (rows[k2] >> k) & 1:
                    rows[k2] ^= rows[k]
        return frozenset(rows.values())


def rotations():
    mats = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product([1, -1], repeat=3):
            M = [[0] * 3 for _ in range(3)]
            for i in range(3):
                M[i][perm[i]] = signs[i]
            # determinant
            det = (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
                   - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
                   + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))
            if det == 1:
                mats.append(tuple(tuple(r) for r in M))
    assert len(mats) == 24
    return mats


def matvec(M, v):
    return tuple(sum(M[i][j] * v[j] for j in range(3)) for i in range(3))


def order_of(M):
    I = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    P = M
    k = 1
    while P != I:
        P = tuple(tuple(sum(P[i][t] * M[t][j] for t in range(3)) for j in range(3)) for i in range(3))
        k += 1
    return k


def edge_perm(lat, M, t=(0, 0, 0)):
    """Qubit permutation induced by v -> M v + t (bare permutation)."""
    perm = [0] * lat.n
    for v in lat.verts():
        for a in range(3):
            e = [0, 0, 0]
            e[a] = 1
            w = tuple(matvec(M, v)[i] + t[i] for i in range(3))
            Re = matvec(M, tuple(e))
            b = [i for i in range(3) if Re[i] != 0][0]
            s = Re[b]
            if s == 1:
                perm[lat.edge(v, a)] = lat.edge(w, b)
            else:
                perm[lat.edge(v, a)] = lat.edge(lat.add(w, b, -1), b)
    assert sorted(perm) == list(range(lat.n))
    return perm


def permute_bits(xint, perm):
    out = 0
    while xint:
        low = xint & -xint
        i = low.bit_length() - 1
        out |= 1 << perm[i]
        xint ^= low
    return out


def permute_pauli(P, perm):
    return (permute_bits(P[0], perm), permute_bits(P[1], perm), P[2])
