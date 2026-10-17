"""Independent core for the Majorana-per-direction cubic code check.

Written from the definitions only (no reference to the campaign runner).

Pauli convention: a Pauli is (x, z, k) with Python-int bitsets x, z over the
n qubits, meaning  i^k * prod_q X_q^{x_q} * prod_q Z_q^{z_q}  (all X's to the
left of all Z's).  Then
  (i^a X^x1 Z^z1)(i^b X^x2 Z^z2) = i^{a+b+2|z1&x2|} X^{x1^x2} Z^{z1^z2}.
Everything below is exact (phases mod 4).

Sites v of the L^3 torus carry qubits 3v, 3v+1, 3v+2.  Directions
d = 0..5 = (+x,+y,+z,-x,-y,-z).  Majorana gamma_{v,d} = JW index d inside the
site: X1, Y1, Z1X2, Z1Y2, Z1Z2X3, Z1Z2Y3.  Majoranas at different sites commute
(no inter-site string).
"""
import itertools

DIRS = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]
DIR_INDEX = {v: i for i, v in enumerate(DIRS)}


def pc(a):
    return a.bit_count()


def mul(p, q):
    return (p[0] ^ q[0], p[1] ^ q[1], (p[2] + q[2] + 2 * pc(p[1] & q[0])) % 4)


def dag(p):
    x, z, k = p
    return (x, z, (-k + 2 * pc(x & z)) % 4)


def anticommute(p, q):
    return (pc(p[0] & q[1]) + pc(p[1] & q[0])) & 1


def is_identity(p):
    return p[0] == 0 and p[1] == 0


# single-site Majoranas on local qubits 0,1,2 (bits)
_LOCAL = [
    (0b001, 0b000, 0),  # X1
    (0b001, 0b001, 1),  # Y1 = i X1 Z1
    (0b010, 0b001, 0),  # Z1 X2
    (0b010, 0b011, 1),  # Z1 Y2
    (0b100, 0b011, 0),  # Z1 Z2 X3
    (0b100, 0b111, 1),  # Z1 Z2 Y3
]


class Lattice:
    def __init__(self, L):
        self.L = L
        self.N = L ** 3
        self.n = 3 * self.N

    def site(self, v):
        L = self.L
        return ((v[0] % L) * L + (v[1] % L)) * L + (v[2] % L)

    def coords(self, s):
        L = self.L
        return (s // (L * L), (s // L) % L, s % L)

    def gamma(self, v, d):
        s = self.site(v)
        x, z, k = _LOCAL[d]
        return (x << (3 * s), z << (3 * s), k)

    def mono(self, labels, k=0):
        """Pauli for i^k * gamma_{l1} gamma_{l2} ... (ordered), labels=(v,d)."""
        p = (0, 0, k % 4)
        for (v, d) in labels:
            p = mul(p, self.gamma(v, d))
        return p

    # ---- generators as Majorana monomials (k, [labels]) -------------------
    @staticmethod
    def add(v, w):
        return (v[0] + w[0], v[1] + w[1], v[2] + w[2])

    def edge_labels(self, v, a):
        """A_(v,a) = gamma_{v,+a} gamma_{v+e_a,-a}, a in 0,1,2."""
        return [(v, a), (self.add(v, DIRS[a]), a + 3)]

    def B_mono(self, v):
        return (1, [(v, d) for d in range(6)])  # (-i)^3 = i

    def plaq_mono(self, v, a, b, sign=+1):
        """ordered product around v -> v+a -> v+a+b -> v+b -> v."""
        va = self.add(v, DIRS[a])
        vb = self.add(v, DIRS[b])
        labs = (self.edge_labels(v, a) + self.edge_labels(va, b)
                + self.edge_labels(vb, a) + self.edge_labels(v, b))
        return (0 if sign > 0 else 2, labs)

    def all_sites(self):
        L = self.L
        return list(itertools.product(range(L), repeat=3))

    def generators(self, sector):
        """sector = dict {(a,b): +-1} for (a,b) in (1,2),(2,0),(0,1)
        i.e. orientations yz, zx, xy.  Returns list of (k,labels)."""
        gens = []
        for v in self.all_sites():
            gens.append(self.B_mono(v))
        for v in self.all_sites():
            for (a, b), s in sector.items():
                gens.append(self.plaq_mono(v, a, b, s))
        return gens

    def to_pauli(self, m):
        return self.mono(m[1], m[0])


ORIENTS = [(1, 2), (2, 0), (0, 1)]


def all_sectors():
    out = []
    for signs in itertools.product([1, -1], repeat=3):
        out.append(dict(zip(ORIENTS, signs)))
    return out


class Tableau:
    """Echelon form of a set of commuting Paulis with exact phases.
    vec = x | (z << n); rows keyed by leading bit."""

    def __init__(self, n):
        self.n = n
        self.rows = {}
        self.consistent = True  # becomes False if -I is generated

    def _vec(self, p):
        return p[0] | (p[1] << self.n)

    def reduce(self, p):
        while True:
            v = self._vec(p)
            if v == 0:
                return p
            h = v.bit_length() - 1
            r = self.rows.get(h)
            if r is None:
                return p
            p = mul(r, p)

    def insert(self, p):
        q = self.reduce(p)
        if is_identity(q):
            if q[2] != 0:
                self.consistent = False
            return False
        self.rows[self._vec(q).bit_length() - 1] = q
        return True

    def rank(self):
        return len(self.rows)

    def sign_of(self, p):
        """+1 if p in group, -1 if -p in group, 0 if neither, None if +-i."""
        q = self.reduce(p)
        if not is_identity(q):
            return 0
        # p * (product of rows) = q  => p = q * prod^-1 ; group elt g = prod
        # with q = i^k I: p = i^k g^{-1} = i^k g (g Hermitian, g^2=I)
        return {0: 1, 2: -1}.get(q[2], None)


def rotations():
    """24 proper rotations as 3x3 signed permutation matrices (tuples)."""
    out = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product([1, -1], repeat=3):
            M = [[0] * 3 for _ in range(3)]
            for i in range(3):
                M[i][perm[i]] = signs[i]
            # determinant
            det = signs[0] * signs[1] * signs[2] * perm_sign(perm)
            if det == 1:
                out.append(tuple(tuple(r) for r in M))
    return out


def improper():
    out = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product([1, -1], repeat=3):
            M = [[0] * 3 for _ in range(3)]
            for i in range(3):
                M[i][perm[i]] = signs[i]
            det = signs[0] * signs[1] * signs[2] * perm_sign(perm)
            if det == -1:
                out.append(tuple(tuple(r) for r in M))
    return out


def perm_sign(p):
    p = list(p)
    s = 1
    seen = [False] * len(p)
    for i in range(len(p)):
        if not seen[i]:
            j, c = i, 0
            while not seen[j]:
                seen[j] = True
                j = p[j]
                c += 1
            if c % 2 == 0:
                s = -s
    return s


def apply(M, v):
    return tuple(sum(M[i][j] * v[j] for j in range(3)) for i in range(3))


def dir_perm(M):
    return tuple(DIR_INDEX[apply(M, DIRS[d])] for d in range(6))


def admissible_eps(M):
    s = perm_sign(dir_perm(M))
    return [e for e in itertools.product([1, -1], repeat=6)
            if (e[0] * e[1] * e[2] * e[3] * e[4] * e[5]) == s]


def act_mono(lat, M, eps, m):
    """gamma_{v,d} -> eps(d) gamma_{Mv, Md}."""
    k, labs = m
    dp = dir_perm(M)
    sgn = 1
    new = []
    for (v, d) in labs:
        sgn *= eps[d]
        new.append((apply(M, v), dp[d]))
    return ((k + (0 if sgn > 0 else 2)) % 4, new)


def act_pauli_via_mono(lat, M, eps, m):
    return lat.to_pauli(act_mono(lat, M, eps, m))
