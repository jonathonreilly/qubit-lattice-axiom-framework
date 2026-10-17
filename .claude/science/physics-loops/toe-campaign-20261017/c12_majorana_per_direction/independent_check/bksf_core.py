"""Independent BKSF cubic-code core (qubit on each edge), written from the
definition:  A_(v,a) = X_(v,a) * prod Z(edges at v ordered before +a)
                                * prod Z(edges at v+e_a ordered before -a),
B_v = Z on the six edges at v,  hop plaquette (C8 convention)
S^o_p = A(v,b) A(v+b,a) A(v+a,b) A(v,a)  (exact product with phase),
signed generator s * S^o_p.  Rotations act by the bare edge permutation P_R.
Pauli format (x, z, k) from mpd_core."""
import itertools
from mpd_core import mul, dag, anticommute, is_identity, Tableau, rotations, dir_perm, apply, perm_sign, DIRS

E = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]


class BKSF:
    def __init__(self, L, order):
        self.L, self.order = L, tuple(order)
        self.n = 3 * L ** 3
        self.pos = {d: i for i, d in enumerate(order)}

    def site(self, v):
        L = self.L
        return ((v[0] % L) * L + (v[1] % L)) * L + (v[2] % L)

    def q(self, v, a):
        return 3 * self.site(v) + a

    @staticmethod
    def add(v, w, s=1):
        return tuple(v[i] + s * w[i] for i in range(3))

    def edge_at(self, v, d):
        a = d % 3
        return (v, a) if d < 3 else (self.add(v, E[a], -1), a)

    def A(self, v, a):
        x = 1 << self.q(v, a)
        z = 0
        w = self.add(v, E[a])
        for d in range(6):
            if self.pos[d] < self.pos[a]:
                z ^= 1 << self.q(*self.edge_at(v, d))
            if self.pos[d] < self.pos[a + 3]:
                z ^= 1 << self.q(*self.edge_at(w, d))
        # X on edge e and Z on other edges: Hermitian, phase 0
        return (x, z, 0)

    def B(self, v):
        z = 0
        for d in range(6):
            z ^= 1 << self.q(*self.edge_at(v, d))
        return (0, z, 0)

    def plaq(self, v, c, sign=1):
        a, b = [k for k in range(3) if k != c]
        va, vb = self.add(v, E[a]), self.add(v, E[b])
        P = (0, 0, 0)
        for Q in (self.A(v, b), self.A(vb, a), self.A(va, b), self.A(v, a)):
            P = mul(P, Q)
        if sign < 0:
            P = (P[0], P[1], (P[2] + 2) % 4)
        return P

    def sites(self):
        return list(itertools.product(range(self.L), repeat=3))

    def gens(self, sign):
        out = []
        for v in self.sites():
            out.append(("B", v, None, self.B(v)))
        for v in self.sites():
            for c in range(3):
                out.append(("S", v, c, self.plaq(v, c, sign)))
        return out


def edge_perm_map(L, M):
    """bare permutation P_R on edge qubits: returns list img[q] = q'."""
    lat = BKSF(L, range(6))
    dp = dir_perm(M)
    img = [0] * lat.n
    for v in lat.sites():
        for a in range(3):
            w = apply(M, v)
            img[lat.q(v, a)] = lat.q(*lat.edge_at(w, dp[a]))
    return img


def permute(P, img):
    x, z, k = P
    nx = nz = 0
    m = x
    while m:
        b = m & -m
        nx |= 1 << img[b.bit_length() - 1]
        m ^= b
    m = z
    while m:
        b = m & -m
        nz |= 1 << img[b.bit_length() - 1]
        m ^= b
    return (nx, nz, k)


def kind(M):
    tr = M[0][0] + M[1][1] + M[2][2]
    if tr == 3:
        return "E"
    if tr == 0:
        return "C3"
    if tr == 1:
        return "C4"
    # tr == -1: C2
    return "C2axis" if all(M[i][i] != 0 for i in range(3)) else "C2edge"
