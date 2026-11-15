#!/usr/bin/env python3
# checks/bb11_bgd.py -- BFT_B session 11, check bb11.
# Criteria: checks/bb11_criteria.md (born 13:59:43 UTC, amendment 14:02:18 UTC), both written before this script.
# Exact rational arithmetic only: fractions.Fraction and Python int. No numpy, no BLAS, no scipy.
# DRIVE_BRIEF rule 6 exempts this from the numeric lock; no lock is taken.
#
# Model: d = 2, L = 3, k = 2, gauge group SU(2) IN THE ADJOINT (3x3 rational rotations).
# The abelian model of checks/bb9b_rtcc.py and checks/bb10_cof.py cannot be reused: for an abelian group Ad == 1 and
# every statement of BFT_B section 38.3 is vacuous. Those two scripts are not edited.

from fractions import Fraction as F
import itertools, sys

d = 2
L = 3
K = 2

# ---------------------------------------------------------------- rational rotations (adjoint SU(2))
C, S = F(3, 5), F(4, 5)        # 3-4-5: exact in Q


def mat(rows):
    return tuple(tuple(F(x) for x in r) for r in rows)


I3 = mat([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
RZ = mat([[C, -S, 0], [S, C, 0], [0, 0, 1]])
RX = mat([[1, 0, 0], [0, C, -S], [0, S, C]])
RY = mat([[C, 0, S], [0, 1, 0], [-S, 0, C]])


def mm(A, B):
    return tuple(tuple(sum(A[i][t] * B[t][j] for t in range(3)) for j in range(3)) for i in range(3))


def mt(A):
    return tuple(tuple(A[j][i] for j in range(3)) for i in range(3))


def mv(A, v):
    return tuple(sum(A[i][t] * v[t] for t in range(3)) for i in range(3))


def vsub(u, v):
    return tuple(a - b for a, b in zip(u, v))


def vadd(u, v):
    return tuple(a + b for a, b in zip(u, v))


def vzero(v):
    return all(a == 0 for a in v)


def n2sq(v):                      # squared Euclidean norm, exact
    return sum(a * a for a in v)


def frob_sq(A):                   # squared Frobenius norm, exact
    return sum(A[i][j] * A[i][j] for i in range(3) for j in range(3))


def msub(A, B):
    return tuple(tuple(A[i][j] - B[i][j] for j in range(3)) for i in range(3))


def is_I(A):
    return A == I3


# ---------------------------------------------------------------- lattices
class Lev:
    """periodic level lattice of side s in d dimensions"""

    def __init__(self, s):
        self.s = s
        self.sites = list(itertools.product(range(s), repeat=d))
        self.links = [(z, mu) for z in self.sites for mu in range(d)]
        self.plaqs = [(z, 0, 1) for z in self.sites]      # d = 2: one plane

    def shift(self, z, mu, t=1):
        w = list(z)
        w[mu] = (w[mu] + t) % self.s
        return tuple(w)


def rng(seed):
    """deterministic LCG; returns a function giving small ints"""
    st = [seed]

    def nxt(lo, hi):
        st[0] = (1103515245 * st[0] + 12345) % (2 ** 31)
        return lo + st[0] % (hi - lo + 1)
    return nxt


def rand_fun(lev, nxt):
    return {z: tuple(F(nxt(-4, 4), nxt(1, 3)) for _ in range(3)) for z in lev.sites}


def rand_form1(lev, nxt):
    return {b: tuple(F(nxt(-4, 4), nxt(1, 3)) for _ in range(3)) for b in lev.links}


def rand_form2(lev, nxt):
    return {p: tuple(F(nxt(-4, 4), nxt(1, 3)) for _ in range(3)) for p in lev.plaqs}


# ---------------------------------------------------------------- covariant operators
def dZ_fun(lev, A, lam):
    """level-j function -> level-j 1-form: (d_Z lam)(y,mu) = A(y,mu) lam(y+e_mu) - lam(y)"""
    out = {}
    for (z, mu) in lev.links:
        out[(z, mu)] = vsub(mv(A[(z, mu)], lam[lev.shift(z, mu)]), lam[z])
    return out


def dZs_form1(lev, A, j1):
    """1-form -> function (transpose of dZ_fun): (d_Z^* j)(z) = sum_mu [A(z-e_mu,mu)^T j(z-e_mu,mu) - j(z,mu)]"""
    out = {z: (F(0), F(0), F(0)) for z in lev.sites}
    for (z, mu) in lev.links:
        w = lev.shift(z, mu, -1)
        out[z] = vadd(out[z], mv(mt(A[(w, mu)]), j1[(w, mu)]))
        out[z] = vsub(out[z], j1[(z, mu)])
    return out


def dZ_form1(lev, A, v):
    """1-form -> 2-form (covariant curl based at the plaquette's first corner)"""
    out = {}
    for (z, mu, nu) in lev.plaqs:
        zm, zn = lev.shift(z, mu), lev.shift(z, nu)
        t = vsub(v[(z, mu)], v[(z, nu)])
        t = vadd(t, mv(A[(z, mu)], v[(zm, nu)]))
        t = vsub(t, mv(A[(z, nu)], v[(zn, mu)]))
        out[(z, mu, nu)] = t
    return out


def dZs_form2(lev, A, Fm):
    """2-form -> 1-form, transpose of dZ_form1 (d = 2, plane (0,1))"""
    out = {b: (F(0), F(0), F(0)) for b in lev.links}
    for (z, mu, nu) in lev.plaqs:
        zm, zn = lev.shift(z, mu), lev.shift(z, nu)
        g = Fm[(z, mu, nu)]
        out[(z, mu)] = vadd(out[(z, mu)], g)
        out[(z, nu)] = vsub(out[(z, nu)], g)
        out[(zm, nu)] = vadd(out[(zm, nu)], mv(mt(A[(z, mu)]), g))
        out[(zn, mu)] = vsub(out[(zn, mu)], mv(mt(A[(z, nu)]), g))
    return out


def corner_transports(lev, A, p):
    z, mu, nu = p
    zm, zn = lev.shift(z, mu), lev.shift(z, nu)
    U1 = mm(A[(z, mu)], A[(zm, nu)])
    U2 = mm(A[(z, nu)], A[(zn, mu)])
    return U1, U2


# ---------------------------------------------------------------- backgrounds
def bg_abelian(lev):
    return {b: I3 for b in lev.links}


def gauge_sites(lev, nxt):
    """a site-wise rational rotation G"""
    gens = [I3, RZ, RX, RY, mm(RZ, RX), mm(RX, RY), mt(RZ), mt(RX)]
    return {z: gens[nxt(0, len(gens) - 1)] for z in lev.sites}


def bg_flat(lev, G):
    """A(b) = G(y) G(y')^{-1} for b = (y, y') -- a pure gauge, every plaquette holonomy exactly 1"""
    return {(z, mu): mm(G[z], mt(G[lev.shift(z, mu)])) for (z, mu) in lev.links}


def bg_curved(lev, nxt):
    gens = [RZ, RX, RY, mm(RZ, RX), mm(RX, RZ), mt(RY)]
    return {b: gens[nxt(0, len(gens) - 1)] for b in lev.links}


# ---------------------------------------------------------------- the L = 3, K = 2 tower (for A4)
class Tower:
    def __init__(self, T, nxt, straight=True, break_link=None):
        self.T = T
        self.lev = [Lev(T * L ** (K - j)) for j in range(K + 1)]
        self.A = [None] * K
        self.A[0] = bg_curved(self.lev[0], nxt)
        for j in range(1, K):
            self.A[j] = {}
            for (X, mu) in self.lev[j].links:
                self.A[j][(X, mu)] = self.row(j - 1, X, mu)
            if not straight and break_link is not None and j == break_link[0]:
                self.A[j][break_link[1]] = mm(self.A[j][break_link[1]], RX)

    def root(self, j, X):
        """level-0 root of the level-j site X (block centres: r(X) = L*X + (L-1)/2)"""
        off = (L - 1) // 2
        z = X
        for _ in range(j):
            z = tuple((L * c + off) for c in z)
        return tuple(c % self.lev[0].s for c in z)

    def root_one(self, j, X):
        """level-(j-1) root of the level-j site X"""
        off = (L - 1) // 2
        return tuple((L * c + off) % self.lev[j - 1].s for c in X)

    def row(self, j, X, mu):
        """straight level-j row product from c_X to c_{X+e_mu} (c at level j)"""
        c = self.root_one(j + 1, X)
        M = I3
        z = c
        for _ in range(L):
            M = mm(M, self.A[j][(z, mu)])
            z = self.lev[j].shift(z, mu)
        return M

    def Qstr(self, j, v):
        """covariant straight root map: level-j 1-form -> level-(j+1) 1-form"""
        out = {}
        for (X, mu) in self.lev[j + 1].links:
            c = self.root_one(j + 1, X)
            T_i = I3
            acc = (F(0), F(0), F(0))
            z = c
            for _ in range(L):
                acc = vadd(acc, mv(T_i, v[(z, mu)]))
                T_i = mm(T_i, self.A[j][(z, mu)])
                z = self.lev[j].shift(z, mu)
            out[(X, mu)] = acc
        return out

    def ev(self, j, lam0):
        """level-0 function -> level-j function by evaluation at the level-j roots"""
        return {X: lam0[self.root(j, X)] for X in self.lev[j].sites}


# ---------------------------------------------------------------- exact linear algebra
def gauss_solve(M, rhs):
    """exact Gaussian elimination; M a list of rows (lists of Fraction), rhs a list. Returns None if singular."""
    n = len(M)
    Aug = [list(M[i]) + [rhs[i]] for i in range(n)]
    for col in range(n):
        piv = None
        for r in range(col, n):
            if Aug[r][col] != 0:
                piv = r
                break
        if piv is None:
            return None
        Aug[col], Aug[piv] = Aug[piv], Aug[col]
        pv = Aug[col][col]
        Aug[col] = [x / pv for x in Aug[col]]
        for r in range(n):
            if r != col and Aug[r][col] != 0:
                f = Aug[r][col]
                Aug[r] = [a - f * b for a, b in zip(Aug[r], Aug[col])]
    return [Aug[i][n] for i in range(n)]


def rank(M):
    """exact rank of a list of rows"""
    if not M:
        return 0
    A = [list(r) for r in M]
    nr, nc = len(A), len(A[0])
    r = 0
    for c in range(nc):
        piv = None
        for i in range(r, nr):
            if A[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        pv = A[r][c]
        A[r] = [x / pv for x in A[r]]
        for i in range(nr):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [a - f * b for a, b in zip(A[i], A[r])]
        r += 1
        if r == nr:
            break
    return r


# ---------------------------------------------------------------- the covariant box-Coulomb problem
class Box:
    """connected box of level-0 sites of own half-width h around c, on the side-s torus (no wrap: 2h+1 <= s)"""

    def __init__(self, lev, c, h):
        self.lev, self.c, self.h = lev, c, h
        rngs = [range(c[nu] - h, c[nu] + h + 1) for nu in range(d)]
        self.sites = [tuple(x % lev.s for x in z) for z in itertools.product(*rngs)]
        sset = set(self.sites)
        self.links = [(z, mu) for z in self.sites for mu in range(d) if lev.shift(z, mu) in sset]
        self.idx = {z: i for i, z in enumerate(self.sites)}

    def dmat(self, A):
        """matrix of lam -> (d_Z lam)|_links, in the basis (site, component); rows = (link, component)"""
        n = 3 * len(self.sites)
        rows = []
        for (z, mu) in self.links:
            w = self.lev.shift(z, mu)
            Am = A[(z, mu)]
            for a in range(3):
                r = [F(0)] * n
                for t in range(3):
                    r[3 * self.idx[w] + t] += Am[a][t]
                r[3 * self.idx[z] + a] -= 1
                rows.append(r)
        return rows

    def nullity(self, A, pin):
        rows = self.dmat(A)
        n = 3 * len(self.sites)
        if pin:
            for a in range(3):
                r = [F(0)] * n
                r[3 * self.idx[self.c] + a] = F(1)
                rows.append(r)
        return n - rank(rows)

    def coulomb(self, A, x0):
        """minimise sum_{b in links} |x0(b) + (d_Z lam)(b)|^2 over lam with lam(c) = 0; returns dict site -> vec"""
        D = self.dmat(A)
        n = 3 * len(self.sites)
        b = []
        for (z, mu) in self.links:
            for a in range(3):
                b.append(x0[(z, mu)][a])
        # normal equations D^T D lam = -D^T b, with the pinned block removed
        free = [i for i in range(n) if i // 3 != self.idx[self.c]]
        fidx = {i: j for j, i in enumerate(free)}
        m = len(free)
        M = [[F(0)] * m for _ in range(m)]
        R = [F(0)] * m
        for ri, row in enumerate(D):
            nzs = [(i, row[i]) for i in free if row[i] != 0]
            for (i, vi) in nzs:
                for (j, vj) in nzs:
                    M[fidx[i]][fidx[j]] += vi * vj
                R[fidx[i]] -= vi * b[ri]
        sol = gauss_solve(M, R)
        if sol is None:
            return None
        lam = {z: [F(0), F(0), F(0)] for z in self.sites}
        for i in free:
            lam[self.sites[i // 3]][i % 3] = sol[fidx[i]]
        return {z: tuple(v) for z, v in lam.items()}


# ---------------------------------------------------------------- quintic tents
def sigma5(t):
    if t >= 1:
        return F(0)
    if t <= 0:
        return F(1)
    return 1 - 10 * t ** 3 + 15 * t ** 4 - 6 * t ** 5


def tent(lev, c, z, spacing):
    w = F(1)
    for nu in range(d):
        dd = (z[nu] - c[nu]) % lev.s
        dd = min(dd, lev.s - dd)
        w *= sigma5(F(dd, spacing))
    return w


# ================================================================ TESTS
res = {}


def record(tag, ok, note=""):
    res[tag] = (bool(ok), note)
    print("%-6s %s  %s" % (tag, "PASS" if ok else "FAIL", note))


print("bb11 -- BFT_B session 11, nonabelian background defects (d=2, L=3, K=2, SU(2) adjoint, exact Q)")
print()

# ---- Part A: operator identities on a side-6 level-0 torus, and the L=3,K=2 tower for A4
lev6 = Lev(6)
nxt = rng(20261028)
Gs = gauge_sites(lev6, nxt)
A_flat = bg_flat(lev6, Gs)
A_curv = bg_curved(lev6, nxt)
A_ab = bg_abelian(lev6)

# A1 / A1n: d_Z d_Z = (U1 - U2) at the far corner, and ||U1-U2||_F = ||Ad_W - 1||_F
ok1, ok1n, ok1f = True, False, True
for A in (A_curv, A_flat):
    for _ in range(8):
        lam = rand_fun(lev6, nxt)
        dd = dZ_form1(lev6, A, dZ_fun(lev6, A, lam))
        for p in lev6.plaqs:
            z, mu, nu = p
            cfar = lev6.shift(lev6.shift(z, mu), nu)
            U1, U2 = corner_transports(lev6, A, p)
            pred = mv(msub(U1, U2), lam[cfar])
            if not vzero(vsub(dd[p], pred)):
                ok1 = False
            if A is A_curv and not vzero(dd[p]):
                ok1n = True
for p in lev6.plaqs:
    U1, U2 = corner_transports(lev6, A_curv, p)
    if frob_sq(msub(U1, U2)) != frob_sq(msub(mm(mt(U1), U2), I3)):
        ok1f = False
record("A1", ok1, "exact identity (d_Z d_Z lam)(p) = (U1-U2) lam(far corner), curved and flat")
record("A1n", ok1n, "non-vacuity: d_Z d_Z lam exactly nonzero on the curved background")
record("A1f", ok1f, "||U1-U2||_F^2 = ||Ad_W - 1||_F^2 exactly on every plaquette")

# A2: adjointness
ok2 = True
for _ in range(8):
    lam = rand_fun(lev6, nxt)
    j1 = rand_form1(lev6, nxt)
    lhs = sum(sum(a * b for a, b in zip(j1[bb], dZ_fun(lev6, A_curv, lam)[bb])) for bb in lev6.links)
    ds = dZs_form1(lev6, A_curv, j1)
    rhs = sum(sum(a * b for a, b in zip(ds[z], lam[z])) for z in lev6.sites)
    if lhs != rhs:
        ok2 = False
record("A2", ok2, "<j, d_Z lam> = <d_Z^* j, lam> exactly (Tier A: adjointness)")

# A3 / A3n: the size claim for d_Z^* d_Z^*, Frobenius form, constant 1
maxdef = max(frob_sq(msub(mm(mt(U1), U2), I3)) for U1, U2 in (corner_transports(lev6, A_curv, p) for p in lev6.plaqs))
ok3, ok3n = True, False
worst = F(0)
for _ in range(8):
    Gm = rand_form2(lev6, nxt)
    out = dZs_form1(lev6, A_curv, dZs_form2(lev6, A_curv, Gm))
    mg = max(n2sq(Gm[p]) for p in lev6.plaqs)
    for z in lev6.sites:
        if n2sq(out[z]) > maxdef * mg:
            ok3 = False
        if not vzero(out[z]):
            ok3n = True
        if mg != 0 and n2sq(out[z]) * 1 > worst * mg:
            worst = F(n2sq(out[z]), 1) / mg
record("A3", ok3, "|d_Z^* d_Z^* G|_2^2 <= max_p ||Ad_W-1||_F^2 * max|G|_2^2 (bound %s, worst ratio %s)"
       % (maxdef, worst))
record("A3n", ok3n, "non-vacuity: d_Z^* d_Z^* G exactly nonzero")

# A4a / A4b: root covariance on the tower, T = 2
nxt4 = rng(777)
tw = Tower(2, nxt4, straight=True)
ok4a = True
for _ in range(8):
    lam0 = rand_fun(tw.lev[0], nxt4)
    for l in range(K - 1, -1, -1):
        lam_l = tw.ev(l, lam0)
        lam_l1 = tw.ev(l + 1, lam0)
        lhs = tw.Qstr(l, dZ_fun(tw.lev[l], tw.A[l], lam_l))
        if l + 1 < K:
            rhs = dZ_fun(tw.lev[l + 1], tw.A[l + 1], lam_l1)
        else:
            # top: level-K links carry the data; compare against the row product (A_K is not part of the chain)
            rhs = {bb: vsub(mv(tw.row(l, bb[0], bb[1]), lam_l1[tw.lev[l + 1].shift(bb[0], bb[1])]), lam_l1[bb[0]])
                   for bb in tw.lev[l + 1].links}
        for bb in tw.lev[l + 1].links:
            if not vzero(vsub(lhs[bb], rhs[bb])):
                ok4a = False
record("A4a", ok4a, "Q_str^Z d_Z ev^{(l)} = d_Z ev^{(l+1)} exactly on a straight-row tower (l = 0, 1)")

nxt4b = rng(777)
bl = (1, (((0, 0)), 0))
tw2 = Tower(2, nxt4b, straight=False, break_link=(1, ((0, 0), 0)))
ok4b, ok4bn = True, False
for _ in range(8):
    lam0 = rand_fun(tw2.lev[0], nxt4b)
    l = 0
    lam_l = tw2.ev(l, lam0)
    lam_l1 = tw2.ev(l + 1, lam0)
    lhs = tw2.Qstr(l, dZ_fun(tw2.lev[l], tw2.A[l], lam_l))
    rhs = dZ_fun(tw2.lev[l + 1], tw2.A[l + 1], lam_l1)
    for (X, mu) in tw2.lev[l + 1].links:
        diff = vsub(lhs[(X, mu)], rhs[(X, mu)])
        pred = mv(msub(tw2.row(l, X, mu), tw2.A[l + 1][(X, mu)]), lam_l1[tw2.lev[l + 1].shift(X, mu)])
        if not vzero(vsub(diff, pred)):
            ok4b = False
        if not vzero(diff):
            ok4bn = True
record("A4b", ok4b and ok4bn, "defect = (Row_l - A_{l+1}) lam_{l+1}(Y+e_mu) exactly, and nonzero (non-vacuous: %s)"
       % ok4bn)

# A5: the gauge shift of the covariant box-Coulomb minimiser
box = Box(lev6, (2, 2), 2)
ok5 = True
for _ in range(4):
    x0 = rand_form1(lev6, nxt)
    mu_f = rand_fun(lev6, nxt)
    dmu = dZ_fun(lev6, A_curv, mu_f)
    xs = {bb: vadd(x0[bb], dmu[bb]) for bb in lev6.links}
    la = box.coulomb(A_curv, x0)
    lb = box.coulomb(A_curv, xs)
    if la is None or lb is None:
        ok5 = False
        break
    for z in box.sites:
        pred = vadd(vsub(la[z], mu_f[z]), mu_f[box.c])
        if not vzero(vsub(lb[z], pred)):
            ok5 = False
record("A5", ok5, "lam^{E,Z}(x + d_Z mu) = lam^{E,Z}(x) - mu + mu(c_X) exactly (curved background)")

# A6: nullity
n_curv_pin = box.nullity(A_curv, pin=True)
n_curv_nopin = box.nullity(A_curv, pin=False)
n_ab_nopin = box.nullity(A_ab, pin=False)
n_ab_pin = box.nullity(A_ab, pin=True)
record("A6", n_curv_pin == 0 and n_ab_nopin == 3,
       "nullity of d_Z on the box: curved %d (pinned) / %d (unpinned); abelian %d (unpinned) / %d (pinned)"
       % (n_curv_pin, n_curv_nopin, n_ab_nopin, n_ab_pin))

# ---- Part B
# B1a: the two tent properties; B1: idempotence of Pi_E^Z at a curved background
roots = [(0, 0), (3, 0), (0, 3), (3, 3)]
ok_b1a = True
for z in lev6.sites:
    if sum(tent(lev6, c, z, 3) for c in roots) != 1:
        ok_b1a = False
for c in roots:
    for c2 in roots:
        if tent(lev6, c, c2, 3) != (1 if c == c2 else 0):
            ok_b1a = False
record("B1a", ok_b1a, "sum_X chi_X = 1 and chi_X(c_Y) = delta_XY exactly (quintic tents, spacing 3)")

boxes = {c: Box(lev6, c, 2) for c in roots}


def Lambda_Z(A, x0):
    out = {z: (F(0), F(0), F(0)) for z in lev6.sites}
    for c in roots:
        la = boxes[c].coulomb(A, x0)
        if la is None:
            return None
        for z in boxes[c].sites:
            w = tent(lev6, c, z, 3)
            if w != 0:
                out[z] = vadd(out[z], tuple(w * a for a in la[z]))
    return out


def PiE_Z(A, x0):
    lam = Lambda_Z(A, x0)
    if lam is None:
        return None
    dl = dZ_fun(lev6, A, lam)
    return {bb: vadd(x0[bb], dl[bb]) for bb in lev6.links}


ok_b1 = True
for _ in range(4):
    x0 = rand_form1(lev6, nxt)
    p1 = PiE_Z(A_curv, x0)
    if p1 is None:
        ok_b1 = False
        break
    lam1 = Lambda_Z(A_curv, p1)
    if any(not vzero(lam1[z]) for z in lev6.sites):
        ok_b1 = False
    p2 = PiE_Z(A_curv, p1)
    if any(not vzero(vsub(p2[bb], p1[bb])) for bb in lev6.links):
        ok_b1 = False
record("B1", ok_b1, "Lambda_Z(Pi_E^Z x) = 0 and Pi_E^Z Pi_E^Z = Pi_E^Z exactly at a curved background")

# B2: Lemma CONJ at a flat nonabelian background -- the three pointwise intertwinings
ok_b2a = True
for _ in range(4):
    lt = rand_fun(lev6, nxt)
    lam = {z: mv(Gs[z], lt[z]) for z in lev6.sites}
    lhs = dZ_fun(lev6, A_flat, lam)
    rhs = {(z, mu): mv(Gs[z], vsub(lt[lev6.shift(z, mu)], lt[z])) for (z, mu) in lev6.links}
    for bb in lev6.links:
        if not vzero(vsub(lhs[bb], rhs[bb])):
            ok_b2a = False

nxt5 = rng(31337)
twf = Tower(2, nxt5, straight=True)
Gt = gauge_sites(twf.lev[0], nxt5)
twf.A[0] = bg_flat(twf.lev[0], Gt)
for (X, mu) in twf.lev[1].links:
    twf.A[1][(X, mu)] = twf.row(0, X, mu)
ok_b2b = True
for _ in range(4):
    vt = rand_form1(twf.lev[0], nxt5)
    v = {(z, mu): mv(Gt[z], vt[(z, mu)]) for (z, mu) in twf.lev[0].links}
    lhs = twf.Qstr(0, v)
    for (X, mu) in twf.lev[1].links:
        c = twf.root_one(1, X)
        acc = (F(0), F(0), F(0))
        z = c
        for _ in range(L):
            acc = vadd(acc, vt[(z, mu)])
            z = twf.lev[0].shift(z, mu)
        if not vzero(vsub(lhs[(X, mu)], mv(Gt[c], acc))):
            ok_b2b = False

ok_b2c = True
for _ in range(4):
    xt = rand_form1(lev6, nxt)
    x = {(z, mu): mv(Gs[z], xt[(z, mu)]) for (z, mu) in lev6.links}
    lz = box.coulomb(A_flat, x)
    l0 = box.coulomb(A_ab, xt)
    if lz is None or l0 is None:
        ok_b2c = False
        break
    for z in box.sites:
        if not vzero(vsub(lz[z], mv(Gs[z], l0[z]))):
            ok_b2c = False
record("B2", ok_b2a and ok_b2b and ok_b2c,
       "flat background: d_Z M_G = M_G^base d (%s), Q_str^Z M_G = M_G^root Q_str (%s), lam^{E,Z} M_G = M_G lam^E (%s)"
       % (ok_b2a, ok_b2b, ok_b2c))

# ---- Controls
ok_c1 = True
for _ in range(4):
    lam = rand_fun(lev6, nxt)
    dd = dZ_form1(lev6, A_ab, dZ_fun(lev6, A_ab, lam))
    if any(not vzero(dd[p]) for p in lev6.plaqs):
        ok_c1 = False
    Gm = rand_form2(lev6, nxt)
    out = dZs_form1(lev6, A_ab, dZs_form2(lev6, A_ab, Gm))
    if any(not vzero(out[z]) for z in lev6.sites):
        ok_c1 = False
nxt6 = rng(4242)
twa = Tower(2, nxt6, straight=True)
twa.A[0] = bg_abelian(twa.lev[0])
for (X, mu) in twa.lev[1].links:
    twa.A[1][(X, mu)] = twa.row(0, X, mu)
for _ in range(2):
    lam0 = rand_fun(twa.lev[0], nxt6)
    lhs = twa.Qstr(0, dZ_fun(twa.lev[0], twa.A[0], twa.ev(0, lam0)))
    rhs = dZ_fun(twa.lev[1], twa.A[1], twa.ev(1, lam0))
    for bb in twa.lev[1].links:
        if not vzero(vsub(lhs[bb], rhs[bb])):
            ok_c1 = False
record("C1", ok_c1, "abelian control: d_Z d_Z = 0, d_Z^* d_Z^* = 0, root-covariance defect = 0, all exactly")

b0 = ((1, 1), 0)
A_pert = dict(A_flat)
A_pert[b0] = mm(A_flat[b0], RX)
ok_c2, ok_c2s = False, True
for _ in range(2):
    lt = rand_fun(lev6, nxt)
    lam = {z: mv(Gs[z], lt[z]) for z in lev6.sites}
    lhs = dZ_fun(lev6, A_pert, lam)
    rhs = {(z, mu): mv(Gs[z], vsub(lt[lev6.shift(z, mu)], lt[z])) for (z, mu) in lev6.links}
    for bb in lev6.links:
        diff = vsub(lhs[bb], rhs[bb])
        if not vzero(diff):
            if bb == b0:
                ok_c2 = True
            else:
                ok_c2s = False
nplaq_broken = sum(1 for p in lev6.plaqs
                   if not is_I(mm(mt(corner_transports(lev6, A_pert, p)[0]), corner_transports(lev6, A_pert, p)[1])))
record("C2", ok_c2 and ok_c2s,
       "perturbed-flat control: intertwining defect exactly nonzero and supported exactly on b_0 "
       "(%d plaquettes of A' have holonomy != 1)" % nplaq_broken)

print()
allok = all(v[0] for v in res.values())
print("VERDICT bb11: %s" % ("ALL PASS" if allok else "NOT ALL PASS -- FAILED: "
                            + ", ".join(t for t, v in res.items() if not v[0])))
sys.exit(0)
