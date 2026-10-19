"""Independent dense (torus) implementation of the C4e layers, vectorised with numpy.

Neighbourhoods N1, N2 are computed here by brute force from site-unit incidence on the torus,
independently of rv_core's offset tables.  Requires L even (parity) and L >= 8 (no wrap of
neighbourhoods, radius 3).
"""
import numpy as np

E = np.eye(3, dtype=int)
ODD = np.array([(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 1)])


class Layer:
    def __init__(self, L, kind):
        self.L = L
        V = L ** 3
        coords = np.array(np.unravel_index(np.arange(V), (L, L, L))).T  # (V,3)
        self.coords = coords
        offs = []  # per idx: 4 offsets (D0, D1, D'0, D'1)
        if kind == 'S':
            for a, b in [(0, 1), (0, 2), (1, 2)]:
                offs.append([np.zeros(3, int), E[a] + E[b], E[a], E[b]])
        else:
            for j in range(3):
                D = [o for o in ODD if o[j] == 0]
                Dp = [o for o in ODD if o[j] == 1]
                offs.append(D + Dp)
        Sx = []
        for idx in range(3):
            cols = []
            for o in offs[idx]:
                cc = (coords + o) % L
                cols.append(np.ravel_multi_index(cc.T, (L, L, L)))
            Sx.append(np.stack(cols, 1))
        Sx = np.concatenate(Sx, 0)  # (nU,4)
        self.Sx = Sx
        nU = Sx.shape[0]
        self.nU = nU
        # site -> units
        site_units = [[] for _ in range(V)]
        for u in range(nU):
            for s in Sx[u]:
                site_units[s].append(u)
        N1 = []
        for u in range(nU):
            st = set()
            for s in Sx[u]:
                st.update(site_units[s])
            st.discard(u)
            N1.append(sorted(st))
        N2o = []
        for u in range(nU):
            st = set()
            for w in N1[u]:
                for s in Sx[w]:
                    st.update(site_units[s])
            st -= set(N1[u])
            st.discard(u)
            N2o.append(sorted(st))
        n1 = max(len(x) for x in N1)
        n2 = max(len(x) for x in N2o)
        assert min(len(x) for x in N1) == n1 and min(len(x) for x in N2o) == n2
        self.N1 = np.array(N1)
        self.N2o = np.array(N2o)
        # override map: for u, slot i of N1, column q of w: which column of u has same site (-1)
        W = Sx[self.N1]  # (nU,n1,4)
        ov = -np.ones(W.shape, dtype=int)
        for p in range(4):
            ov[W == Sx[:, p][:, None, None]] = p
        self.ov = ov
        # radius of dependency region per site (exact, from the definition)
        rad = 0
        x0 = 0
        for u in site_units[x0]:
            reg = set(Sx[u])
            for w in list(N1[u]) + list(N2o[u]):
                reg.update(Sx[w])
            for s in reg:
                d = (coords[s] - coords[x0] + L // 2) % L - L // 2
                rad = max(rad, int(np.abs(d).max()))
        self.radius = rad
        self.n1, self.n2 = n1, n2

    def cand(self, content):
        a = content
        return ((a[..., 0] & a[..., 1] & ~a[..., 2] & ~a[..., 3])
                | (~a[..., 0] & ~a[..., 1] & a[..., 2] & a[..., 3]))

    def __call__(self, c, return_active=False):
        c = c.astype(bool)
        cont = c[self.Sx]
        cand = self.cand(cont)
        ok = cand & ~cand[self.N2o].any(1)
        W = c[self.Sx[self.N1]]  # (nU,n1,4)
        for pat in (np.array([1, 1, 0, 0], bool), np.array([0, 0, 1, 1], bool)):
            Wm = W.copy()
            m = self.ov >= 0
            Wm[m] = pat[self.ov[m]]
            ok &= ~self.cand(Wm).any(1)
        act = np.nonzero(ok)[0]
        new = c.copy()
        S = self.Sx[act]
        flat = S.ravel()
        assert len(np.unique(flat)) == len(flat), "active overlap"
        new[S] = ~c[S]  # crossing a candidate = complementing its 4 sites
        if return_active:
            return new, act
        return new


class Dyn:
    def __init__(self, L):
        self.L = L
        self.l1 = Layer(L, 'S')
        self.l2 = Layer(L, 'T')

    def U(self, c):
        return self.l2(self.l1(c))

    def Uinv(self, c):
        return self.l1(self.l2(c))
