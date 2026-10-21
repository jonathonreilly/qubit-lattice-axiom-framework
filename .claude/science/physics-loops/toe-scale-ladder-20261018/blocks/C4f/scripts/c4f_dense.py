"""Second (dense, torus) implementation of the C4f layers, written separately from c4f_core.

Sites of the L-torus are flat indices.  Every unit is stored as arrays: D (2 idx), Dp (2 idx),
G (control sites, 0 or 4 idx), ctl in {0 none, 1 empty, 2 full}.  N1 is built by brute force from
the incidence of read sets F and write sets S on the torus (sparse boolean matrices), N2 = N1.N1
minus N1 minus diagonal.  No offset tables from c4f_core are used.
"""
import itertools
import numpy as np
import scipy.sparse as sp

CUBE = list(itertools.product((0, 1), repeat=3))


class Torus:
    def __init__(self, L):
        self.L = L
        self.V = L ** 3
        g = np.indices((L, L, L)).reshape(3, -1).T
        self.coords = g

    def idx(self, z):
        L = self.L
        z = np.asarray(z) % L
        return (z[..., 0] * L + z[..., 1]) * L + z[..., 2]


def build_layer(T, kinds):
    L = T.L
    Ds, Dps, Gs, ctls = [], [], [], []
    for k in itertools.product(range(L), repeat=3):
        k = np.array(k)
        for kind in kinds:
            for a in range(3):
                if kind == 'sq':
                    b, c = [i for i in range(3) if i != a]
                    eb = np.eye(3, dtype=int)[b]; ec = np.eye(3, dtype=int)[c]
                    D = [k, k + eb + ec]; Dp = [k + eb, k + ec]; G = []; ctl = 0
                else:
                    cube = [k + np.array(d) for d in CUBE]
                    odd = [z for z in cube if (z - k).sum() % 2 == 1]
                    even = [z for z in cube if (z - k).sum() % 2 == 0]
                    if kind == 'B':
                        S, G, ctl = odd, even, 1
                    elif kind == 'A':
                        S, G, ctl = even, odd, 2
                    else:  # 'B0': C4e uncontrolled
                        S, G, ctl = odd, [], 0
                    D = [z for z in S if z[a] == k[a]]
                    Dp = [z for z in S if z[a] == k[a] + 1]
                Ds.append([T.idx(z) for z in D]); Dps.append([T.idx(z) for z in Dp])
                Gs.append([T.idx(z) for z in G] if G else [-1, -1, -1, -1]); ctls.append(ctl)
    lay = dict(D=np.array(Ds), Dp=np.array(Dps), G=np.array(Gs), ctl=np.array(ctls))
    n = len(ctls)
    S = np.concatenate([lay['D'], lay['Dp']], axis=1)
    rows = np.repeat(np.arange(n), 4)
    MS = sp.csr_matrix((np.ones(4 * n, bool), (rows, S.ravel())), shape=(n, T.V))
    Gv = lay['G']; m = Gv[:, 0] >= 0
    rr = np.repeat(np.arange(n)[m], 4)
    MG = sp.csr_matrix((np.ones(len(rr), bool), (rr, Gv[m].ravel())), shape=(n, T.V))
    MF = ((MS + MG) > 0).astype(np.int32)
    MSi = MS.astype(np.int32)
    A = (MF @ MSi.T) + (MSi @ MF.T)            # A[u,w] > 0  iff  F_u n S_w or S_u n F_w
    A = (A > 0).astype(np.int32).tolil(); A.setdiag(0); A = A.tocsr(); A.eliminate_zeros()
    A2 = (A @ A > 0).astype(np.int32).tolil(); A2.setdiag(0); A2 = A2.tocsr()
    A2 = A2 - A2.multiply(A)
    A2.eliminate_zeros(); A2 = (A2 > 0).astype(np.int32).tocsr()
    lay['N1'] = A; lay['N2'] = A2; lay['n'] = n
    return lay


def cand(lay, c):
    """c: bool array over sites.  vector of candidacy."""
    dD = c[lay['D']].all(1) & ~c[lay['Dp']].any(1)
    dP = c[lay['Dp']].all(1) & ~c[lay['D']].any(1)
    ok = dD | dP
    G = lay['G']; ctl = lay['ctl']
    g = c[np.where(G >= 0, G, 0)]
    ok &= np.where(ctl == 1, ~g.any(1), True)
    ok &= np.where(ctl == 2, g.all(1), True)
    return ok


def cand_one(lay, c, w):
    D = lay['D'][w]; Dp = lay['Dp'][w]
    s = c[D]; t = c[Dp]
    if not ((s.all() and not t.any()) or (t.all() and not s.any())): return False
    ctl = lay['ctl'][w]
    if ctl == 1: return not c[lay['G'][w]].any()
    if ctl == 2: return bool(c[lay['G'][w]].all())
    return True


def active(lay, c):
    cd = cand(lay, c)
    ci = cd.astype(np.int32)
    bad = (lay['N1'] @ ci > 0) | (lay['N2'] @ ci > 0)
    pre = np.nonzero(cd & ~bad)[0]
    act = []
    N1 = lay['N1']
    for u in pre:
        D = lay['D'][u]; Dp = lay['Dp'][u]
        c2 = c.copy()
        if c[D].all(): c2[D] = False; c2[Dp] = True
        else: c2[Dp] = False; c2[D] = True
        nb = N1.indices[N1.indptr[u]:N1.indptr[u + 1]]
        if any(cand_one(lay, c2, w) for w in nb): continue
        act.append(u)
    return np.array(act, int)


def apply(lay, c, return_active=False):
    act = active(lay, c)
    out = c.copy()
    for u in act:
        D = lay['D'][u]; Dp = lay['Dp'][u]
        if c[D].all(): out[D] = False; out[Dp] = True
        else: out[Dp] = False; out[D] = True
    return (out, act) if return_active else out


class DenseU:
    def __init__(self, L, variant='C4f'):
        self.T = Torus(L)
        self.L1 = build_layer(self.T, ('sq',))
        self.L2 = build_layer(self.T, ('B', 'A') if variant == 'C4f' else ('B0',))
    def __call__(self, c): return apply(self.L2, apply(self.L1, c))
    def inv(self, c): return apply(self.L1, apply(self.L2, c))
