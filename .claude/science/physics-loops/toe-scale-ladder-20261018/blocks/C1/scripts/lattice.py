"""Cubic L^3 torus geometry for the supplied spin-1/2 link ring model (rho_v = 0).

Conventions (match docs/RING_MODEL_* runners): vertex v=(x,y,z), vid = (x*L+y)*L+z;
link l = 3*vid + a (from v to v+e_a), sigma_l = +1 means arrow along +e_a, E_l = sigma_l/2.
Plaquette p = 3*vid + o with o in 0:(x,y), 1:(y,z), 2:(x,z); for (a,b) its links are
(v,a)+, (v+e_a,b)+, (v+e_b,a)-, (v,b)-; circulation = sum sign*sigma; flippable iff |circ| = 4.
Gauss law: div sigma = 0 at every vertex (3 out / 3 in).
"""
import numpy as np

ORI = ((0, 1), (1, 2), (0, 2))


class Lattice:
    def __init__(self, L):
        self.L = L
        self.nv = L ** 3
        self.nl = 3 * self.nv
        self.np = 3 * self.nv
        coords = np.array([(x, y, z) for x in range(L) for y in range(L) for z in range(L)])
        self.coords = coords

        def vid(c):
            c = np.asarray(c) % L
            return (c[..., 0] * L + c[..., 1]) * L + c[..., 2]

        self.vid = vid
        E = np.eye(3, dtype=int)
        self.tail = np.repeat(np.arange(self.nv), 3)
        self.head = np.array([vid(coords[v] + E[a]) for v in range(self.nv) for a in range(3)])
        pl = np.zeros((self.np, 4), dtype=np.int64)
        for v in range(self.nv):
            for o, (a, b) in enumerate(ORI):
                c = coords[v]
                pl[3 * v + o] = [3 * v + a, 3 * vid(c + E[a]) + b, 3 * vid(c + E[b]) + a, 3 * v + b]
        self.plinks = pl
        self.psign = np.array([1, 1, -1, -1], dtype=np.int64)
        # plaquettes containing each link (4 in 3D)
        lp = [[] for _ in range(self.nl)]
        for p in range(self.np):
            for l in pl[p]:
                lp[l].append(p)
        self.lplaqs = np.array(lp, dtype=np.int64)
        # neighbourhood of p: p first, then the distinct plaquettes sharing >= 1 link
        nb = []
        for p in range(self.np):
            s = []
            for l in pl[p]:
                for q in lp[l]:
                    if q != p and q not in s:
                        s.append(q)
            nb.append([p] + s)
        m = max(len(x) for x in nb)
        self.nbh = -np.ones((self.np, m), dtype=np.int64)
        self.nnb = np.zeros(self.np, dtype=np.int64)
        for p, x in enumerate(nb):
            self.nbh[p, :len(x)] = x
            self.nnb[p] = len(x)
        # link midpoints and plaquette base positions
        self.lpos = np.array([coords[v] + 0.5 * E[a] for v in range(self.nv) for a in range(3)])
        self.ppos = np.repeat(coords, 3, axis=0).astype(float)
        self.lori = np.tile(np.arange(3), self.nv)
        self.pori = np.tile(np.arange(3), self.nv)

    def div(self, sigma):
        d = np.zeros(self.nv, dtype=np.int64)
        np.add.at(d, self.tail, sigma)
        np.add.at(d, self.head, -sigma)
        return d

    def circ(self, sigma):
        return (sigma[self.plinks] * self.psign).sum(axis=1)

    def flippable(self, sigma):
        return np.abs(self.circ(sigma)) == 4

    def winding(self, sigma):
        """W_a = sum over links (v,a) with v_a = 0 of sigma/2 (repo convention, units of e)."""
        w = []
        for a in range(3):
            sel = (self.lori == a) & (self.coords[self.tail][:, a] == 0)
            w.append(int(sigma[sel].sum()))
        return np.array(w) // 2 if all(x % 2 == 0 for x in w) else np.array(w) / 2

    def canonical(self):
        """Repo canonical zero-winding ice state: sigma_x=(-1)^y, sigma_y=sigma_z=(-1)^x."""
        s = np.zeros(self.nl, dtype=np.int64)
        for v in range(self.nv):
            x, y, z = self.coords[v]
            s[3 * v + 0] = (-1) ** y
            s[3 * v + 1] = (-1) ** x
            s[3 * v + 2] = (-1) ** x
        return s

    def gauge_set(self):
        """Lambda = {x-links with y+z even} U {y-links with z even} (even L)."""
        lam = np.zeros(self.nl, dtype=bool)
        for v in range(self.nv):
            x, y, z = self.coords[v]
            lam[3 * v + 0] = (y + z) % 2 == 0
            lam[3 * v + 1] = z % 2 == 0
        return lam
