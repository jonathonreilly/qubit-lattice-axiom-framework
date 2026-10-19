"""Reviewer's own implementation of C4f's U = L2 o L1, written from the NOTE.md definitions only.
Torus L^3, L even (parity of sites must be well defined).
Unit = (type, base point). Each unit: S (4 sites, ordered), patD (4 bits: 1 if site in D),
Gamma (4 sites or none), ctrl: 0 none, 1 Gamma must be empty, 2 Gamma must be full."""
import itertools, numpy as np

E = [np.array(v) for v in ((1,0,0),(0,1,0),(0,0,1))]

def templates():
    """unit types as offset templates: list of dicts with S, patD, G, ctrl; layer 1 or 2"""
    T1, T2 = [], []
    for a, b in ((0,1),(0,2),(1,2)):
        S = [(0,0,0), tuple(E[a]+E[b]), tuple(E[a]), tuple(E[b])]
        T1.append(dict(S=S, patD=[1,1,0,0], G=None, ctrl=0, name=f'sq{a}{b}'))
    cube = list(itertools.product((0,1), repeat=3))
    Bo = [o for o in cube if sum(o) % 2 == 1]   # par z != par k
    Ao = [o for o in cube if sum(o) % 2 == 0]
    for kind, Sset, Gset, ctrl in (('B', Bo, Ao, 1), ('A', Ao, Bo, 2)):
        for j in range(3):
            S = sorted(Sset, key=lambda o: (o[j], o))
            patD = [1 if o[j] == 0 else 0 for o in S]
            T2.append(dict(S=S, patD=patD, G=list(Gset), ctrl=ctrl, name=f'{kind}{j}'))
    return T1, T2

def add(p, o): return tuple(int(p[i]) + int(o[i]) for i in range(3))

def neighbour_templates(T):
    """N1 / N2 of the unit (t, origin) as sets of (t', offset), per the C4f definition:
    N1(u) = {w != u : F_w cap S_u != 0 or F_u cap S_w != 0},  F = S u Gamma."""
    def F(t): return T[t]['S'] + (T[t]['G'] or [])
    R = 6
    def N1(t, p):
        Su = {add(p, o) for o in T[t]['S']}; Fu = {add(p, o) for o in F(t)}
        out = set()
        for t2 in range(len(T)):
            for q in itertools.product(range(-R, R+1), repeat=3):
                q = add(p, q)
                if (t2, q) == (t, p): continue
                Sw = {add(q, o) for o in T[t2]['S']}; Fw = {add(q, o) for o in F(t2)}
                if (Fw & Su) or (Fu & Sw): out.add((t2, q))
        return out
    # brute-force is O(units*window); fine once (window small); use relative translation
    n1 = {t: N1(t, (0,0,0)) for t in range(len(T))}
    n2 = {}
    for t in range(len(T)):
        acc = set()
        for (t2, q) in n1[t]:
            for (t3, r) in n1[t2]:
                acc.add((t3, add(q, r)))
        n2[t] = acc - n1[t] - {(t, (0,0,0))}
    return n1, n2

class Layer:
    def __init__(self, T, n1, n2, L):
        self.L = L; V = L**3; self.V = V; nT = len(T)
        idx = lambda p: ((p[0] % L)*L + p[1] % L)*L + p[2] % L
        self.idx = idx
        bases = list(itertools.product(range(L), repeat=3))
        self.uid = {}
        units = []
        for t in range(nT):
            for p in bases:
                self.uid[(t, p)] = len(units); units.append((t, p))
        self.units = units; nU = len(units)
        S = np.zeros((nU, 4), np.int64); G = np.full((nU, 4), V, np.int64)
        pat = np.zeros((nU, 4), np.uint8); ctrl = np.zeros(nU, np.int8)
        for u, (t, p) in enumerate(units):
            S[u] = [idx(add(p, o)) for o in T[t]['S']]
            pat[u] = T[t]['patD']; ctrl[u] = T[t]['ctrl']
            if T[t]['G']: G[u] = [idx(add(p, o)) for o in T[t]['G']]
        self.S, self.G, self.pat, self.ctrl = S, G, pat, ctrl
        def uofs(t, p, rel):
            t2, q = rel; return self.uid[(t2, tuple(int(x) % L for x in add(p, q)))]
        # N1 lists (padded) and N2 lists
        m1 = max(len(n1[t]) for t in range(nT)); m2 = max(len(n2[t]) for t in range(nT))
        N1 = np.full((nU, m1), -1, np.int64); N2 = np.full((nU, m2), -1, np.int64)
        for u, (t, p) in enumerate(units):
            l1 = sorted({uofs(t, p, r) for r in n1[t]}); l2 = sorted({uofs(t, p, r) for r in n2[t]})
            assert len(l1) == len(n1[t]) and len(l2) == len(n2[t]), 'torus too small: neighbour wrap'
            N1[u, :len(l1)] = l1; N2[u, :len(l2)] = l2
        self.N1, self.N2 = N1, N2
        self.n1size = {T[t]['name']: len(n1[t]) for t in range(nT)}
        self.n2size = {T[t]['name']: len(n2[t]) for t in range(nT)}

    def cand_from(self, sv, gv, u):
        """sv,gv: (...,4) values of S and Gamma; u: unit indices broadcastable"""
        pat = self.pat[u]; ctrl = self.ctrl[u]
        isD = np.all(sv == pat, axis=-1); isDp = np.all(sv == 1 - pat, axis=-1)
        ok = np.where(ctrl == 0, True, np.where(ctrl == 1, np.all(gv == 0, axis=-1), np.all(gv == 1, axis=-1)))
        return (isD | isDp) & ok

    def active(self, c):
        cc = np.append(c, 0).astype(np.uint8)
        allu = np.arange(len(self.units))
        cand = self.cand_from(cc[self.S], cc[self.G], allu)
        A = []
        for u in np.nonzero(cand)[0]:
            ok = True
            # (c) no unit of N2(u) is a candidate (in c)
            n2 = self.N2[u]; n2 = n2[n2 >= 0]
            if cand[n2].any(): continue
            # (b) for both states of u, no unit of N1(u) is a candidate
            n1 = self.N1[u]; n1 = n1[n1 >= 0]
            Su = self.S[u]
            for st in (self.pat[u], 1 - self.pat[u]):
                c2 = cc.copy(); c2[Su] = st
                if self.cand_from(c2[self.S[n1]], c2[self.G[n1]], n1).any():
                    ok = False; break
            if ok: A.append(u)
        return A

    def apply(self, c, return_active=False):
        A = self.active(c)
        out = c.copy()
        if A:
            sites = self.S[A].ravel()
            assert len(set(sites.tolist())) == len(sites), 'active units not site-disjoint'
            out[sites] ^= 1
        return (out, A) if return_active else out

_cache = {}
def build(L):
    if L in _cache: return _cache[L]
    T1, T2 = templates()
    a1 = neighbour_templates(T1); a2 = neighbour_templates(T2)
    l1 = Layer(T1, *a1, L); l2 = Layer(T2, *a2, L)
    _cache[L] = (l1, l2); return l1, l2

def U(l1, l2, c): return l2.apply(l1.apply(c))
def Uinv(l1, l2, c): return l1.apply(l2.apply(c))

# ---------- symmetry ----------
def group_O():
    O = []
    for p in itertools.permutations(range(3)):
        for s in itertools.product((1, -1), repeat=3):
            M = np.zeros((3, 3), int)
            for i in range(3): M[p[i], i] = s[i]
            if round(np.linalg.det(M)) == 1: O.append(M)
    return O
psign = lambda M: int(round(np.linalg.det(np.abs(M))))

def site_perm(M, L, centre2=(0,0,0)):
    """permutation array P with new[P[x]] = old[x], x -> M x about the point centre2/2 (half-integer allowed)"""
    pts = np.array(list(itertools.product(range(L), repeat=3)))
    c2 = np.array(centre2)
    img2 = (M @ (2*pts - c2).T).T + c2
    assert np.all(img2 % 2 == 0)
    img = (img2 // 2) % L
    return (img[:, 0]*L + img[:, 1])*L + img[:, 2]

def act(M, P, c):
    out = np.empty_like(c); out[P] = c
    if psign(M) == -1: out = 1 - out
    return out
