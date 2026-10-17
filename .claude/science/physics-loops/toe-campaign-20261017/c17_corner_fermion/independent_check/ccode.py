"""Independent BKSF corner-graph code with repetition halves (own construction).

Pauli = (x, z, p) meaning i^p X^x Z^z (X-part written to the left).
"""
import numpy as np
from geom import Lattice, DIRS, CTYPES, CTIDX, neg, add, perp, rot_vec, rotations


def pmul(P, Q):
    x1, z1, p1 = P
    x2, z2, p2 = Q
    return (x1 ^ x2, z1 ^ z2, (p1 + p2 + 2 * bin(z1 & x2).count('1')) % 4)


def pdag(P):
    x, z, p = P
    return (x, z, (-p + 2 * bin(x & z).count('1')) % 4)


def commute(P, Q):
    return (bin(P[0] & Q[1]).count('1') + bin(P[1] & Q[0]).count('1')) % 2 == 0


def hermitian(P):
    x, z, p = P
    return (p - bin(x & z).count('1')) % 2 == 0


def lexpos(d):
    for a in d:
        if a > 0:
            return True
        if a < 0:
            return False
    raise ValueError


class CornerCode:
    def __init__(self, L, flux=None, ordering_seed=None):
        # flux: dict type -> +1 (0) / -1 (pi)
        if flux is None:
            flux = {'square': -1, 'triangle': +1, 'plaquette': -1, 'tube': +1}
        self.flux = flux
        self.lat = lat = Lattice(L)
        self.L = L
        nc = lat.ncorner
        # edges: for each corner list of (nbr corner, kind, disp4)
        self.nbrs = [None] * nc
        edges = {}
        for v in lat.sites:
            for ct in CTYPES:
                c = lat.corner(v, ct)
                p0 = lat.corner_pos4(v, ct)
                lst = []
                for (v2, ct2, kind) in lat.neighbours(v, ct):
                    c2 = lat.corner(v2, ct2)
                    disp = tuple(b - a for a, b in zip(p0, lat.corner_pos4(v2, ct2)))
                    lst.append((c2, kind, disp))
                    e = frozenset([c, c2])
                    edges.setdefault(e, kind)
                self.nbrs[c] = lst
        self.edges = list(edges)
        self.ekind = edges
        assert len(self.edges) == 36 * len(lat.sites)
        # qubits: per site 48 = 24 onsite edges + 24 halves (corner, link)
        self.Q = {}
        nq = 0
        site_of = []
        for si, v in enumerate(lat.sites):
            loc = []
            for ct in CTYPES:
                c = lat.corner(v, ct)
                for (c2, kind, disp) in self.nbrs[c]:
                    e = frozenset([c, c2])
                    if kind == 'onsite':
                        if (e, None) not in self.Q:
                            self.Q[(e, None)] = nq
                            nq += 1
                            site_of.append(si)
                    else:
                        self.Q[(e, c)] = nq
                        nq += 1
                        site_of.append(si)
        self.nq = nq
        self.site_of = site_of
        assert nq == 48 * len(lat.sites)
        # ordering at each corner: sort its 6 edges by displacement (translation-invariant)
        rng = np.random.default_rng(ordering_seed) if ordering_seed is not None else None
        self.order = []
        for c in range(nc):
            lst = sorted(self.nbrs[c], key=lambda t: t[2])
            if rng is not None:
                # per-corner-TYPE random ordering, still translation invariant
                pass
            self.order.append([frozenset([c, t[0]]) for t in lst])
        if ordering_seed is not None:
            perms = {ct: rng.permutation(6) for ct in range(12)}
            self.order = [[self.order[c][i] for i in perms[c % 12]] for c in range(nc)]
        self.rank = [{e: i for i, e in enumerate(self.order[c])} for c in range(nc)]
        self.disp = {}
        for c in range(nc):
            for (c2, kind, disp) in self.nbrs[c]:
                self.disp[(c, c2)] = disp

    # qubit holding Z of edge e at corner c (the half at c's site for links)
    def zq(self, e, c):
        if self.ekind[e] == 'onsite':
            return self.Q[(e, None)]
        return self.Q[(e, c)]

    def xmask(self, e):
        if self.ekind[e] == 'onsite':
            return 1 << self.Q[(e, None)]
        a, b = tuple(e)
        return (1 << self.Q[(e, a)]) | (1 << self.Q[(e, b)])

    def hop(self, j, k):
        e = frozenset([j, k])
        x = self.xmask(e)
        z = 0
        for c in (j, k):
            r = self.rank[c][e]
            for l in self.order[c][:r]:
                z |= 1 << self.zq(l, c)
        eps = 1 if lexpos(self.disp[(j, k)]) else -1
        return (x, z, 0 if eps == 1 else 2)

    def Bq(self, c):
        z = 0
        for e in self.order[c]:
            z |= 1 << self.zq(e, c)
        return (0, z, 0)

    def links(self):
        return [e for e in self.edges if self.ekind[e] == 'link']

    def Rl(self, e):
        a, b = tuple(e)
        return (0, (1 << self.Q[(e, a)]) | (1 << self.Q[(e, b)]), 0)

    def loop(self, cyc, F):
        P = (0, 0, 0)
        n = len(cyc)
        for i in range(n):
            P = pmul(P, self.hop(cyc[i], cyc[(i + 1) % n]))
        x, z, p = P
        p = (p + n + (0 if F == 1 else 2)) % 4
        return (x, z, p)

    # faces as cyclic corner lists
    def faces(self):
        lat = self.lat
        out = []
        ax = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
        for v in lat.sites:
            for a in DIRS:
                b = next(d for d in DIRS if perp(d, a))
                c = tuple(int(t) for t in np.cross(a, b))
                cyc = [lat.corner(v, (a, e)) for e in (b, c, neg(b), neg(c))]
                out.append(('square', cyc))
            for s in [(sx, sy, sz) for sx in (1, -1) for sy in (1, -1) for sz in (1, -1)]:
                dx, dy, dz = (s[0], 0, 0), (0, s[1], 0), (0, 0, s[2])
                cyc = [lat.corner(v, (dx, dy)), lat.corner(v, (dy, dz)), lat.corner(v, (dz, dx))]
                out.append(('triangle', cyc))
            for i in range(3):
                for j in range(i + 1, 3):
                    a, b = ax[i], ax[j]
                    cyc = [lat.corner(v, (a, b)), lat.corner(add(v, a), (neg(a), b)),
                           lat.corner(add(add(v, a), b), (neg(a), neg(b))), lat.corner(add(v, b), (a, neg(b)))]
                    out.append(('plaquette', cyc))
            for a in ax:
                b = next(d for d in DIRS if perp(d, a))
                c = tuple(int(t) for t in np.cross(a, b))
                ring = [b, c, neg(b), neg(c)]
                for t in range(4):
                    e, e2 = ring[t], ring[(t + 1) % 4]
                    cyc = [lat.corner(v, (a, e)), lat.corner(add(v, a), (neg(a), e)),
                           lat.corner(add(v, a), (neg(a), e2)), lat.corner(v, (a, e2))]
                    out.append(('tube', cyc))
        return out

    def generators(self):
        gens = []
        for c in range(self.lat.ncorner):
            gens.append(('B', c, self.Bq(c)))
        for e in self.links():
            gens.append(('R', e, self.Rl(e)))
        for (t, cyc) in self.faces():
            gens.append((t, tuple(cyc), self.loop(cyc, self.flux[t])))
        return gens

    # ---- rotations about the origin site ----
    def rot_corner(self, M, c):
        v, ct = self.lat.corner_info(c)
        return self.lat.corner(rot_vec(M, v), [rot_vec(M, d) for d in ct])

    def rot_edge(self, M, e):
        return frozenset(self.rot_corner(M, c) for c in e)

    def perm(self, M):
        """qubit permutation pi: qubit i -> pi[i]."""
        pi = [None] * self.nq
        for (e, c), q in self.Q.items():
            e2 = self.rot_edge(M, e)
            c2 = None if c is None else self.rot_corner(M, c)
            pi[q] = self.Q[(e2, c2)]
        assert sorted(pi) == list(range(self.nq))
        return pi


def permute_mask(m, pi):
    out = 0
    while m:
        low = m & -m
        i = low.bit_length() - 1
        out |= 1 << pi[i]
        m ^= low
    return out


def bits(m):
    out = []
    while m:
        low = m & -m
        out.append(low.bit_length() - 1)
        m ^= low
    return out


class StabGroup:
    """Phase-tracking GF(2) elimination for a commuting Pauli group."""

    def __init__(self, n):
        self.n = n
        self.piv = {}  # pivot bit -> Pauli
        self.minus_identity = False

    def key(self, P):
        return P[0] | (P[1] << self.n)

    def reduce(self, P):
        while True:
            k = self.key(P)
            if k == 0:
                return P
            hb = k.bit_length() - 1
            if hb not in self.piv:
                return P
            P = pmul(P, self.piv[hb])

    def add(self, P):
        R = self.reduce(P)
        k = self.key(R)
        if k == 0:
            if R[2] != 0:
                self.minus_identity = True
            return False
        self.piv[k.bit_length() - 1] = R
        return True

    def member_sign(self, P):
        """Return +1/-1 (or complex phase) if P = phase * element of group, else None."""
        R = self.reduce(P)
        if self.key(R) != 0:
            return None
        return {0: 1, 1: 1j, 2: -1, 3: -1j}[R[2]]
