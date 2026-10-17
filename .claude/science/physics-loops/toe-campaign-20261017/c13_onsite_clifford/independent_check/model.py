"""Half-edge (six qubits per site) and edge BKSF models, written from the
definitions in the C11/C13 task statement (independent check)."""
import itertools
import numpy as np
from paulialg import (mul, prod, dag, is_herm, commutes, X, Z, Y, IDENT, bits,
                      apply_clifford, SignedGroup, proper_rotations, pc)

DIRS = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]
DIDX = {d: i for i, d in enumerate(DIRS)}
ROTS = proper_rotations()


def rot_dir(M, d):
    return DIDX[tuple(int(c) for c in M @ np.array(DIRS[d]))]


def rot_order(M, o):
    return tuple(rot_dir(M, d) for d in o)


def classify_rotation(M):
    if np.array_equal(M, np.eye(3, dtype=int)):
        return "id"
    tr = int(np.trace(M))
    if tr == 0:
        return "C3"
    if tr == 1:
        return "C4"
    # tr == -1: C2; axis C2 iff diagonal
    if all(M[i, j] == 0 for i in range(3) for j in range(3) if i != j):
        return "C2axis"
    return "C2edge"


class Lattice:
    def __init__(self, L):
        self.L = L
        self.N = L ** 3

    def site(self, r):
        L = self.L
        return (r[0] % L) + L * ((r[1] % L) + L * (r[2] % L))

    def coord(self, s):
        L = self.L
        return (s % L, (s // L) % L, s // (L * L))

    def shift(self, s, d):
        c = self.coord(s)
        return self.site(tuple(c[i] + DIRS[d][i] for i in range(3)))

    def rot_site(self, M, s):
        c = np.array(self.coord(s))
        return self.site(tuple(int(t) for t in M @ c))

    def trans_site(self, s, t):
        c = self.coord(s)
        return self.site(tuple(c[i] + t[i] for i in range(3)))


# ---------------------------------------------------------------- half-edge
class HalfEdge:
    """Qubit index q = 6*site + d."""

    def __init__(self, L, o):
        self.lat = Lattice(L)
        self.L = L
        self.o = tuple(o)
        self.pos = {d: i for i, d in enumerate(o)}
        self.n = 6 * self.lat.N

    def q(self, s, d):
        return 6 * s + d

    def before(self, d):
        return [e for e in range(6) if self.pos[e] < self.pos[d]]

    def mu(self, s, d):
        return prod([X(self.q(s, d))] + [Z(self.q(s, e)) for e in self.before(d)])

    def nu(self, s, d):
        return prod([Y(self.q(s, d))] + [Z(self.q(s, e)) for e in self.before(d)])

    def B(self, s):
        return prod([Z(self.q(s, d)) for d in range(6)])

    def R(self, s, a):
        t = self.lat.shift(s, a)
        return mul(Z(self.q(s, a)), Z(self.q(t, a + 3)))

    def A(self, s, a):
        t = self.lat.shift(s, a)
        ops = [X(self.q(s, a)), X(self.q(t, a + 3))]
        ops += [Z(self.q(s, e)) for e in self.before(a)]
        ops += [Z(self.q(t, e)) for e in self.before(a + 3)]
        return prod(ops)

    def S(self, s, a, b, sign):
        lat = self.lat
        sa, sb = lat.shift(s, a), lat.shift(s, b)
        p = prod([self.A(s, a), self.A(sa, b), self.A(sb, a), self.A(s, b)])
        if not is_herm(p):
            p = (p[0], p[1], (p[2] + 1) % 4)
        assert is_herm(p)
        return (p[0], p[1], (p[2] + 2 * sign) % 4)

    def generators(self, sector, sites=None):
        """sector = (s_x, s_y, s_z): sign of plaquette normal to axis c."""
        gens = []
        rng = range(self.lat.N) if sites is None else sites
        for s in rng:
            gens.append(("B", s, self.B(s)))
            for a in range(3):
                gens.append(("R", (s, a), self.R(s, a)))
            for c in range(3):
                a, b = [t for t in range(3) if t != c]
                gens.append(("S", (s, c), self.S(s, a, b, sector[c])))
        return gens

    def group(self, sector):
        G = SignedGroup(self.n)
        for _, _, g in self.generators(sector):
            G.add(g)
        return G

    # ---- maps
    def bare_images(self, M):
        imgX, imgZ = [None] * self.n, [None] * self.n
        for s in range(self.lat.N):
            rs = self.lat.rot_site(M, s)
            for d in range(6):
                rd = rot_dir(M, d)
                imgX[self.q(s, d)] = X(self.q(rs, rd))
                imgZ[self.q(s, d)] = Z(self.q(rs, rd))
        return imgX, imgZ

    def majorana_images(self, M, eps=None, epsp=None):
        """On-site map mu_{s,d} -> eps_d mu_{Rs,Rd}, nu_{s,d} -> eps'_d nu_{Rs,Rd}
        (same ordering o on both sides), translated into X/Z images via
        Z_d = -i mu_d nu_d,  X_d = mu_d prod_{d' before d} Z_{d'}."""
        eps = eps or [1] * 6
        epsp = epsp or [1] * 6
        imgX, imgZ = [None] * self.n, [None] * self.n
        for s in range(self.lat.N):
            rs = self.lat.rot_site(M, s)
            mu_img, nu_img, z_img = {}, {}, {}
            for d in range(6):
                rd = rot_dir(M, d)
                m = self.mu(rs, rd)
                v = self.nu(rs, rd)
                if eps[d] < 0:
                    m = (m[0], m[1], (m[2] + 2) % 4)
                if epsp[d] < 0:
                    v = (v[0], v[1], (v[2] + 2) % 4)
                mu_img[d], nu_img[d] = m, v
            for d in range(6):
                zz = mul(mu_img[d], nu_img[d])
                z_img[d] = (zz[0], zz[1], (zz[2] + 3) % 4)  # times -i
            for d in range(6):
                imgZ[self.q(s, d)] = z_img[d]
                imgX[self.q(s, d)] = prod([mu_img[d]] + [z_img[e] for e in self.before(d)])
        return imgX, imgZ

    def translation(self, P, t):
        x, z, k = P
        nx = nz = 0
        for qq in bits(x):
            s, d = divmod(qq, 6)
            nx |= 1 << self.q(self.lat.trans_site(s, t), d)
        for qq in bits(z):
            s, d = divmod(qq, 6)
            nz |= 1 << self.q(self.lat.trans_site(s, t), d)
        return (nx, nz, k)


# ---------------------------------------------------------------- edge model
class Edge:
    """Qubit index 3*site + a for edge (site, site+e_a)."""

    def __init__(self, L, o):
        self.lat = Lattice(L)
        self.L = L
        self.o = tuple(o)
        self.pos = {d: i for i, d in enumerate(o)}
        self.n = 3 * self.lat.N

    def e(self, s, d):
        if d < 3:
            return 3 * s + d
        return 3 * self.lat.shift(s, d) + (d - 3)

    def before(self, d):
        return [e for e in range(6) if self.pos[e] < self.pos[d]]

    def B(self, s):
        return prod([Z(self.e(s, d)) for d in range(6)])

    def A(self, s, a):
        t = self.lat.shift(s, a)
        ops = [X(3 * s + a)]
        ops += [Z(self.e(s, d)) for d in self.before(a)]
        ops += [Z(self.e(t, d)) for d in self.before(a + 3)]
        return prod(ops)

    def S(self, s, a, b, sign):
        lat = self.lat
        sa, sb = lat.shift(s, a), lat.shift(s, b)
        p = prod([self.A(s, a), self.A(sa, b), self.A(sb, a), self.A(s, b)])
        if not is_herm(p):
            p = (p[0], p[1], (p[2] + 1) % 4)
        return (p[0], p[1], (p[2] + 2 * sign) % 4)

    def generators(self, sector, sites=None):
        gens = []
        rng = range(self.lat.N) if sites is None else sites
        for s in rng:
            gens.append(("B", s, self.B(s)))
            for c in range(3):
                a, b = [t for t in range(3) if t != c]
                gens.append(("S", (s, c), self.S(s, a, b, sector[c])))
        return gens

    def group(self, sector):
        G = SignedGroup(self.n)
        for _, _, g in self.generators(sector):
            G.add(g)
        return G

    def bare_images(self, M):
        imgX, imgZ = [None] * self.n, [None] * self.n
        for s in range(self.lat.N):
            rs = self.lat.rot_site(M, s)
            for a in range(3):
                q2 = self.e(rs, rot_dir(M, a))
                imgX[3 * s + a] = X(q2)
                imgZ[3 * s + a] = Z(q2)
        return imgX, imgZ

    def cz_partners(self, o_from, o_to):
        """Vertex-centred CZ network: at every vertex, CZ between the edges in
        directions d, d' whose relative order differs between o_from, o_to."""
        pf = {d: i for i, d in enumerate(o_from)}
        pt = {d: i for i, d in enumerate(o_to)}
        inv = [(d, e) for d in range(6) for e in range(d + 1, 6)
               if (pf[d] < pf[e]) != (pt[d] < pt[e])]
        partners = [0] * self.n
        for s in range(self.lat.N):
            for d, e in inv:
                q1, q2 = self.e(s, d), self.e(s, e)
                partners[q1] ^= 1 << q2
                partners[q2] ^= 1 << q1
        return partners, inv

    def cz_images(self, partners):
        imgX = [(1 << q, partners[q], 0) for q in range(self.n)]
        imgZ = [Z(q) for q in range(self.n)]
        return imgX, imgZ


def compose_images(first, second, n):
    """Images of the Clifford 'second o first' (apply first, then second)."""
    fX, fZ = first
    sX, sZ = second
    return ([apply_clifford(fX[q], sX, sZ) for q in range(n)],
            [apply_clifford(fZ[q], sX, sZ) for q in range(n)])
