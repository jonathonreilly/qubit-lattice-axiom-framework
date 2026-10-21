"""Independent reviewer implementation of the C4e construction U = L2 o L1.

Written from the NOTE.md definitions only (no author code imported or copied).

Sparse implementation on the infinite lattice Z^3: a configuration is a frozenset of
occupied (magnon) sites.  Units:
  L1 ('S'): unit plaquettes base + {0, ea, eb, ea+eb}, D = {0, ea+eb}, D' = {ea, eb}.
  L2 ('T'): for cube k, B(k) = k + {odd offsets} = k + {e1, e2, e3, (1,1,1)};
            axis j: D = B ∩ {x_j = k_j}, D' = B ∩ {x_j = k_j + 1}.
Rule: u active iff (a) candidate (c ∩ S_u equals D_u or D'_u exactly);
  (b) for both states of u (rest fixed) no unit of N1(u) is a candidate;
  (c) no unit of N2(u) \\ (N1(u) ∪ {u}) is a candidate in c.
N1, N2 are taken within the layer's own unit family.
"""
import itertools

E = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
PLANES = [(0, 1), (0, 2), (1, 2)]


def add(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def cheb(a, b):
    return max(abs(a[0] - b[0]), abs(a[1] - b[1]), abs(a[2] - b[2]))


ODD = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 1)]


def unit_offsets(kind, idx):
    """Return (D offsets, D' offsets) relative to base."""
    if kind == 'S':
        a, b = PLANES[idx]
        ea, eb = E[a], E[b]
        return [(0, 0, 0), add(ea, eb)], [ea, eb]
    else:
        j = idx
        D = [o for o in ODD if o[j] == 0]
        Dp = [o for o in ODD if o[j] == 1]
        return D, Dp


OFFS = {(k, i): unit_offsets(k, i) for k in 'ST' for i in range(3)}


def unit_sites(u):
    kind, base, idx = u
    D, Dp = OFFS[(kind, idx)]
    return [add(base, o) for o in D], [add(base, o) for o in Dp]


def units_containing(site, kind):
    out = []
    for idx in range(3):
        D, Dp = OFFS[(kind, idx)]
        for o in D + Dp:
            out.append((kind, sub(site, o), idx))
    return out


def _rel(u, base):
    return (u[0], sub(u[1], base), u[2])


def _neighbour_tables(kind):
    N1, N2o = {}, {}
    for idx in range(3):
        u = (kind, (0, 0, 0), idx)
        D, Dp = unit_sites(u)
        n1 = set()
        for s in D + Dp:
            n1.update(units_containing(s, kind))
        n1.discard(u)
        n2 = set()
        for w in n1:
            Dw, Dpw = unit_sites(w)
            for s in Dw + Dpw:
                n2.update(units_containing(s, kind))
        n2 -= n1
        n2.discard(u)
        N1[idx] = sorted(n1)
        N2o[idx] = sorted(n2)
    return N1, N2o


NB = {k: _neighbour_tables(k) for k in 'ST'}


def translate_unit(u, t):
    return (u[0], add(u[1], t), u[2])


def is_candidate(u, occ):
    """occ: callable site -> bool."""
    D, Dp = unit_sites(u)
    cD = [occ(s) for s in D]
    cDp = [occ(s) for s in Dp]
    return (all(cD) and not any(cDp)) or (all(cDp) and not any(cD))


def layer(c, kind):
    c = frozenset(c)
    occ0 = c.__contains__
    # candidates (must contain an occupied site)
    cands = set()
    for s in c:
        for u in units_containing(s, kind):
            if u not in cands and is_candidate(u, occ0):
                cands.add(u)
    N1, N2o = NB[kind]
    active = []
    for u in cands:
        base, idx = u[1], u[2]
        # (c)
        bad = False
        for w in N2o[idx]:
            if translate_unit(w, base) in cands:
                bad = True
                break
        if bad:
            continue
        D, Dp = unit_sites(u)
        Sset = set(D) | set(Dp)
        for state in (D, Dp):
            st = set(state)
            occ = (lambda s, st=st: (s in st) if s in Sset else (s in c))
            for w in N1[idx]:
                if is_candidate(translate_unit(w, base), occ):
                    bad = True
                    break
            if bad:
                break
        if not bad:
            active.append(u)
    # cross
    new = set(c)
    used = set()
    for u in active:
        D, Dp = unit_sites(u)
        for s in D + Dp:
            assert s not in used, "active units overlap"
            used.add(s)
        if all(s in c for s in D):
            for s in D:
                new.discard(s)
            new.update(Dp)
        else:
            for s in Dp:
                new.discard(s)
            new.update(D)
    return frozenset(new)


def L1(c):
    return layer(c, 'S')


def L2(c):
    return layer(c, 'T')


def U(c):
    return L2(L1(c))


def Uinv(c):
    return L1(L2(c))


# ---------- symmetry group ----------
def signed_perms():
    out = []
    for p in itertools.permutations(range(3)):
        for s in itertools.product([1, -1], repeat=3):
            M = [[0] * 3 for _ in range(3)]
            for i in range(3):
                M[i][p[i]] = s[i]
            out.append(tuple(tuple(r) for r in M))
    return out


def det3(M):
    a = M
    return (a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
            - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
            + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0]))


def perm_sign(M):
    # sign of underlying permutation
    p = [next(j for j in range(3) if M[i][j] != 0) for i in range(3)]
    inv = sum(1 for i in range(3) for j in range(i + 1, 3) if p[i] > p[j])
    return -1 if inv % 2 else 1


O24 = [M for M in signed_perms() if det3(M) == 1]
# T: even permutation with an even number of sign flips  (det=+1 and perm even)
T12 = [M for M in O24 if perm_sign(M) == 1]
ODD12 = [M for M in O24 if perm_sign(M) == -1]
assert len(O24) == 24 and len(T12) == 12 and len(ODD12) == 12


def apply(M, x):
    return tuple(sum(M[i][j] * x[j] for j in range(3)) for i in range(3))


def act(M, c):
    return frozenset(apply(M, x) for x in c)


def tr(c, t):
    return frozenset(add(x, t) for x in c)


def normalize(c):
    """translation normal form"""
    m = min(c)
    return frozenset(sub(x, m) for x in c)


def canon_T(c):
    """canonical rep under translations + T"""
    best = None
    for M in T12:
        r = act(M, c)
        mn = min(r)
        key = tuple(sorted(sub(x, mn) for x in r))
        if best is None or key < best:
            best = key
    return best


class Check:
    def __init__(self, logf=None):
        self.p = 0
        self.f = 0
        self.logf = logf

    def __call__(self, cond, msg):
        if cond:
            self.p += 1
        else:
            self.f += 1
        line = ("PASS " if cond else "FAIL ") + msg
        print(line, flush=True)
        if self.logf:
            self.logf.write(line + "\n")
            self.logf.flush()

    def info(self, msg):
        line = "INFO " + msg
        print(line, flush=True)
        if self.logf:
            self.logf.write(line + "\n")
            self.logf.flush()

    def total(self):
        line = f"TOTAL: PASS={self.p} FAIL={self.f}"
        print(line, flush=True)
        if self.logf:
            self.logf.write(line + "\n")
            self.logf.flush()
