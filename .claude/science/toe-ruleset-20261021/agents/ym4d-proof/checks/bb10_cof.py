#!/usr/bin/env python3
"""bb10_cof.py -- exact rational check of Lemma DF-cc (the funnel regrouping of the dual push-down),
Proposition COF-size and Proposition COF-res (BFT_B.md session 10, Sec 34.2 / 35).

Criteria: checks/bb10_criteria.md (written BEFORE this script, with one amendment also written before this
script: the dimension-dependent exponent L^{-(d-1)} and the added test A8).

The model and the whole operator construction (Lev, the sparse-matrix helpers, build(), solve_div, rnd, gauss)
are COPIED VERBATIM from checks/bb9b_rtcc.py, which is NOT edited: d = 2, L = 3, k = 2, kappa_0 = 1,
kappa_1 = 2, roots = block centres, axial order 0 then 1.  Only the tests below are new.

Exact arithmetic only (fractions.Fraction and Python ints). No numpy, no BLAS, single thread.
"""
from fractions import Fraction as F
import itertools, time, sys

d = 2
L = 3
K = 2
KAP = [F(1), F(2)]
t0 = time.time()

def side(l, T):
    return (L ** (K - l)) * T

# ---------- index helpers ----------
class Lev:
    def __init__(self, l, T):
        self.l = l
        self.n = side(l, T)
        n = self.n
        self.sites = list(itertools.product(range(n), repeat=d))
        self.si = {z: i for i, z in enumerate(self.sites)}
        self.links = [(z, mu) for z in self.sites for mu in range(d)]
        self.li = {b: i for i, b in enumerate(self.links)}
    def sh(self, z, mu, t=1):
        w = list(z); w[mu] = (w[mu] + t) % self.n; return tuple(w)

# ---------- sparse matrices: dict (row, col) -> Fraction ----------
def mat_from_fun(fun, ncol, basis_vec, nrow):
    """build sparse matrix of a linear map given as fun(vector dict) -> vector dict"""
    M = {}
    for j in range(ncol):
        out = fun(basis_vec(j))
        for i, v in out.items():
            if v != 0:
                M[(i, j)] = v
    return M

def mt(M):
    return {(j, i): v for (i, j), v in M.items()}

def mmul(A, B):
    """A (m x p) times B (p x q), sparse"""
    Bc = {}
    for (i, j), v in B.items():
        Bc.setdefault(i, []).append((j, v))
    C = {}
    for (i, p), v in A.items():
        for (j, w) in Bc.get(p, ()):
            key = (i, j)
            nv = C.get(key, 0) + v * w
            if nv == 0:
                C.pop(key, None)
            else:
                C[key] = nv
    return C

def msub(A, B):
    C = dict(A)
    for k, v in B.items():
        nv = C.get(k, 0) - v
        if nv == 0:
            C.pop(k, None)
        else:
            C[k] = nv
    return C

def mapply(M, x, n):
    y = [F(0)] * n
    for (i, j), v in M.items():
        if x[j] != 0:
            y[i] += v * x[j]
    return y

def eq(A, B):
    return len(msub(A, B)) == 0

def nz(v):
    return any(a != 0 for a in v)

def mx(v):
    return max([abs(a) for a in v], default=F(0))

# ---------- operators ----------
def build(T):
    lev = {l: Lev(l, T) for l in range(K + 1)}
    O = {}
    for l in range(K + 1):
        Lv = lev[l]
        nS, nL = len(Lv.sites), len(Lv.links)
        # d on functions: (dlam)(z,mu) = lam(z+e_mu) - lam(z)
        M = {}
        for (z, mu) in Lv.links:
            i = Lv.li[(z, mu)]
            M[(i, Lv.si[Lv.sh(z, mu)])] = M.get((i, Lv.si[Lv.sh(z, mu)]), 0) + 1
            k2 = (i, Lv.si[z]); M[k2] = M.get(k2, 0) - 1
        O[('dfun', l)] = {k: F(v) for k, v in M.items() if v != 0}
        # d* on 1-forms: (d*v)(z) = sum_mu [ v_mu(z-e_mu) - v_mu(z) ]
        M = {}
        for z in Lv.sites:
            i = Lv.si[z]
            for mu in range(d):
                k1 = (i, Lv.li[(Lv.sh(z, mu, -1), mu)]); M[k1] = M.get(k1, 0) + 1
                k2 = (i, Lv.li[(z, mu)]); M[k2] = M.get(k2, 0) - 1
        O[('dstar', l)] = {k: F(v) for k, v in M.items() if v != 0}
        # d on 1-forms -> 2-forms (d=2: one plaquette per site)
        M = {}
        for z in Lv.sites:
            i = Lv.si[z]
            for (b, s) in (((z, 0), 1), ((Lv.sh(z, 0), 1), 1), ((Lv.sh(z, 1), 0), -1), ((z, 1), -1)):
                k1 = (i, Lv.li[b]); M[k1] = M.get(k1, 0) + s
        O[('dform', l)] = {k: F(v) for k, v in M.items() if v != 0}
    for l in range(K):
        Lv, Up = lev[l], lev[l + 1]
        # ev: level-l functions -> level-(l+1) functions, (ev lam)(X) = lam(c_X), c_X = L*X + ((L-1)/2)(1,..,1)
        off = (L - 1) // 2
        M = {}
        for X in Up.sites:
            cX = tuple((L * X[a] + off) % Lv.n for a in range(d))
            M[(Up.si[X], Lv.si[cX])] = F(1)
        O[('ev', l)] = M
        # Q_str: (Q_str v)(X,mu) = L^{-d} sum_{y in B(X)} sum_{j<L} v_mu(y + j e_mu)
        M = {}
        c = F(1, L ** d)
        for X in Up.sites:
            base = [L * X[a] for a in range(d)]
            for mu in range(d):
                i = Up.li[(X, mu)]
                for a in itertools.product(range(L), repeat=d):
                    y = tuple((base[t] + a[t]) % Lv.n for t in range(d))
                    for j in range(L):
                        b = (Lv.sh(y, mu, j), mu)
                        k1 = (i, Lv.li[b]); M[k1] = M.get(k1, F(0)) + c
        O[('Qstr', l)] = {k: v for k, v in M.items() if v != 0}
        # h: level-l 1-forms -> level-(l+1) functions, average over y in B(X) of the axial integral c_X -> y
        M = {}
        c = F(1, L ** d)
        for X in Up.sites:
            i = Up.si[X]
            base = [L * X[a] for a in range(d)]
            cX = [base[a] + off for a in range(d)]
            for a in itertools.product(range(L), repeat=d):
                y = [base[t] + a[t] for t in range(d)]
                p = list(cX)
                for mu in range(d):            # axial order 0 then 1
                    if y[mu] > p[mu]:
                        for t in range(p[mu], y[mu]):
                            q = list(p); q[mu] = t
                            b = (tuple(r % Lv.n for r in q), mu)
                            k1 = (i, Lv.li[b]); M[k1] = M.get(k1, F(0)) + c
                    elif y[mu] < p[mu]:
                        for t in range(y[mu], p[mu]):
                            q = list(p); q[mu] = t
                            b = (tuple(r % Lv.n for r in q), mu)
                            k1 = (i, Lv.li[b]); M[k1] = M.get(k1, F(0)) - c
                    p[mu] = y[mu]
        O[('h', l)] = {k: v for k, v in M.items() if v != 0}
        # Q = Q_str - dfun_{l+1} . h
        O[('Q', l)] = msub(O[('Qstr', l)], mmul(O[('dfun', l + 1)], O[('h', l)]))
    return lev, O


def solve_div(Lv, u):
    """exact j with d*j = u, for u a list over sites with total 0 (torus)."""
    n = Lv.n
    assert sum(u) == 0
    j = [F(0)] * len(Lv.links)
    # row totals
    U = [sum(u[Lv.si[(x0, x1)]] for x0 in range(n)) for x1 in range(n)]
    # direction 0: a(z-e0) - a(z) = u(z) - U(z1)/n
    for x1 in range(n):
        acc = F(0)
        vals = []
        for x0 in range(n):
            r = u[Lv.si[(x0, x1)]] - F(U[x1], n)
            acc -= r                      # a(x0) = -sum_{t<=x0} r(t)
            vals.append(acc)
        for x0 in range(n):
            j[Lv.li[((x0, x1), 0)]] = vals[x0]
    # direction 1: b(z1-1) - b(z1) = U(z1)/n
    acc = F(0)
    for x1 in range(n):
        acc -= F(U[x1], n)
        for x0 in range(n):
            j[Lv.li[((x0, x1), 1)]] = acc
    return j


def rnd(seed, m, lo=-3, hi=3):
    """deterministic small-integer pseudo-random vector (no RNG library needed)"""
    out = []
    s = seed
    for _ in range(m):
        s = (1103515245 * s + 12345) % 2147483648
        out.append(F(lo + (s >> 7) % (hi - lo + 1)))
    return out

def gauss(Am, bs):
    """exact Gaussian elimination, Am square, bs a list of right-hand sides"""
    n = len(Am)
    M = [row[:] + [b[i] for b in bs] for i, row in enumerate(Am)]
    nb = len(bs)
    piv = []
    r = 0
    for c in range(n):
        p = None
        for rr in range(r, n):
            if M[rr][c] != 0:
                p = rr; break
        if p is None:
            return None
        M[r], M[p] = M[p], M[r]
        inv = F(1) / M[r][c]
        M[r] = [v * inv for v in M[r]]
        for rr in range(n):
            if rr != r and M[rr][c] != 0:
                f = M[rr][c]
                Mr = M[r]
                M[rr] = [a - f * b for a, b in zip(M[rr], Mr)]
        piv.append(c); r += 1
        if r == n:
            break
    if r < n:
        return None
    return [[M[i][n + k] for i in range(n)] for k in range(nb)]



# ======================================================================
#   bb10 TESTS  (new in session 10)
# ======================================================================
res = {}
PI = lambda l, v: (L ** ((d - 1) * (K - l))) * mx(v)   # model coarse convention, amendment (iii)

def ops(T):
    lev, O = build(T)
    return lev, O

def mkC(O, lev, j0, j1):
    """C(j) = j_0 + (Q^{(0->1)})^T j_1  (k = 2)"""
    n0L = len(lev[0].links)
    return [a + b for a, b in zip(j0, mapply(mt(O[('Q', 0)]), j1, n0L))]

def DofS(O, lev, j0, j1):
    """D(S) = d*j_0 + ev^{(0->1)T} d*_1 j_1, a level-0 function"""
    nF0 = len(lev[0].sites)
    a = mapply(O[('dstar', 0)], j0, nF0)
    b = mapply(mt(O[('ev', 0)]), mapply(O[('dstar', 1)], j1, len(lev[1].sites)), nF0)
    return [p + q for p, q in zip(a, b)]

def rootrestrict(O, lev, Dfun, lvl):
    """R_lvl(D): the level-'lvl' function whose ev^{(0->lvl)T} placement is Dfun.
    Returns (R, ok) with ok False if Dfun is not supported on the level-'lvl' roots."""
    off = (L - 1) // 2
    n0 = lev[0].n
    R = [F(0)] * len(lev[lvl].sites)
    for X in lev[lvl].sites:
        z = tuple((L ** lvl * X[a] + sum(L ** t * off for t in range(lvl))) % n0 for a in range(d))
        R[lev[lvl].si[X]] = Dfun[lev[0].si[z]]
    back = Dfun[:]
    for X in lev[lvl].sites:
        z = tuple((L ** lvl * X[a] + sum(L ** t * off for t in range(lvl))) % n0 for a in range(d))
        back[lev[0].si[z]] = F(0)
    return R, (not nz(back))

def build_source(O, lev, seed, rootq=None):
    """plain collection (j_0, j_1) with D(S) = placement(rootq) (default 0).
    j_1 random; j_0 solves d*j_0 = D_target - ev^T d*_1 j_1."""
    nF0 = len(lev[0].sites)
    j1 = rnd(seed, len(lev[1].links))
    evTdsj1 = mapply(mt(O[('ev', 0)]), mapply(O[('dstar', 1)], j1, len(lev[1].sites)), nF0)
    Dtar = [F(0)] * nF0
    if rootq is not None:
        off = (L - 1) // 2
        n0 = lev[0].n
        for X in lev[K].sites:
            z = tuple((L ** K * X[a] + sum(L ** t * off for t in range(K))) % n0 for a in range(d))
            Dtar[lev[0].si[z]] = rootq[lev[K].si[X]]
    u = [a - b for a, b in zip(Dtar, evTdsj1)]
    j0 = solve_div(lev[0], u)
    return j0, j1

# ======================= PART A (T = 2) =======================
T = 2
levA, OA = ops(T)
nA0L, nA1L, nAF0 = len(levA[0].links), len(levA[1].links), len(levA[0].sites)
print("[bb10] PART A, T = %d: level sides %s (d = %d, L = %d, k = %d)"
      % (T, [levA[l].n for l in range(K + 1)], d, L, K))
print("[bb10] push-down exponent used: L^{-(d-1)} = L^{-%d} (criteria amendment (i))" % (d - 1))

# ---- A1: DF (ii) telescoping, 10 random chains x 10 random currents (level 1) ----
ok = True
for s in range(10):
    Y0 = rnd(1000 + s, nA0L); Y1 = rnd(2000 + s, nA1L)
    j1 = rnd(3000 + s, nA1L)
    r0 = [a - b for a, b in zip(mapply(OA[('Q', 0)], Y0, nA1L), Y1)]
    lhs = sum(a * b for a, b in zip(j1, Y1))
    rhs = (sum(a * b for a, b in zip(mapply(mt(OA[('Q', 0)]), j1, nA0L), Y0))
           - sum(a * b for a, b in zip(j1, r0)))
    if lhs != rhs:
        ok = False
res['A1'] = ok
print("A1 DF(ii) telescoping at level 1 (trivial at k = 2; exactness check) : %s"
      % ("PASS" if ok else "FAIL"))

# ---- A2: d* C(j) = D(S) on 10 random collections (no co-closedness imposed) ----
ok = True
for s in range(10):
    j0 = rnd(4000 + s, nA0L); j1 = rnd(5000 + s, nA1L)
    C = mkC(OA, levA, j0, j1)
    if nz([a - b for a, b in zip(mapply(OA[('dstar', 0)], C, nAF0), DofS(OA, levA, j0, j1))]):
        ok = False
res['A2'] = ok
print("A2 d* C(j) = D(S) on random collections                              : %s"
      % ("PASS" if ok else "FAIL"))

# ---- constructed families ----
CC0 = [build_source(OA, levA, 7000 + 11 * s) for s in range(4)]          # D(S) = 0 strictly
rootfams = []
for s in range(3):                                                        # D(S) on level-2 roots, total 0
    q = rnd(8000 + 13 * s, len(levA[K].sites))
    tot = sum(q)
    q = [a for a in q]; q[0] -= tot
    if all(a == 0 for a in q):
        q[0] = F(1); q[1] = F(-1)
    rootfams.append((build_source(OA, levA, 8500 + 17 * s, rootq=q), q))

def psis(O, lev, j0, j1):
    """psi_0, psi_1 from the cascade (RT-cc (a)): ev^{(0->l+1)T} psi_l = Psi_l."""
    nF0 = len(lev[0].sites)
    Psi0 = mapply(O[('dstar', 0)], j0, nF0)
    ev0T = mt(O[('ev', 0)])
    Psi1 = [a + b for a, b in zip(Psi0,
            mapply(ev0T, mapply(O[('dstar', 1)], j1, len(lev[1].sites)), nF0))]
    p0, ok0 = rootrestrict(O, lev, Psi0, 1)
    p1, ok1 = rootrestrict(O, lev, Psi1, 2)
    return p0, p1, ok0, ok1

# ---- A3: xi_0 + psi_0 = R_1(D(S)) ----
ok = True; nonvac = False
for (j0, j1) in CC0 + [f[0] for f in rootfams]:
    p0, p1, ok0, ok1 = psis(OA, levA, j0, j1)
    if not (ok0 and ok1):
        ok = False; continue
    xi0 = mapply(OA[('dstar', 1)], j1, len(levA[1].sites))        # xi_0 = sum_{l>0} ev^T d*j_l = d*_1 j_1
    R1, okR = rootrestrict(OA, levA, DofS(OA, levA, j0, j1), 1)
    if (not okR) or nz([a + b - c for a, b, c in zip(xi0, p0, R1)]):
        ok = False
    if nz(p0) and nz(xi0):
        nonvac = True
res['A3'] = ok and nonvac
print("A3 xi_0 = R_1(D(S)) - psi_0 (exact), non-vacuous (psi_0, xi_0 != 0) %s : %s"
      % (nonvac, "PASS" if res['A3'] else "FAIL"))

# ---- A4: regrouping under (CC-0): C(j) = jhat_0 + Qstr_0^T jhat_1 ----
ok = True; nonvac = False
for (j0, j1) in CC0:
    assert not nz(DofS(OA, levA, j0, j1))
    p0, p1, ok0, ok1 = psis(OA, levA, j0, j1)
    f0 = mapply(mt(OA[('h', 0)]), p0, nA0L)
    f1 = mapply(mt(OA[('h', 1)]), p1, nA1L)
    jh0 = [a + b for a, b in zip(j0, f0)]
    jh1 = [a + b for a, b in zip(j1, f1)]
    rhs = [a + b for a, b in zip(jh0, mapply(mt(OA[('Qstr', 0)]), jh1, nA0L))]
    if nz([a - b for a, b in zip(mkC(OA, levA, j0, j1), rhs)]):
        ok = False
    if nz(f0):
        nonvac = True
    if nz(p1):
        ok = False      # under (CC-0) psi_{k-1} must vanish
res['A4'] = ok and nonvac
print("A4 Lemma DF-cc (ii) under (CC-0): C = jhat_0 + Qstr_0^T jhat_1, h_0^Tpsi_0 != 0 %s : %s"
      % (nonvac, "PASS" if res['A4'] else "FAIL"))

# ---- A5: control -- the root-charge defect (uniform identity) ----
ok = True; defect_nonzero = False
for ((j0, j1), q) in rootfams:
    Dfun = DofS(OA, levA, j0, j1)
    if not nz(Dfun):
        ok = False; continue
    p0, p1, ok0, ok1 = psis(OA, levA, j0, j1)
    f0 = mapply(mt(OA[('h', 0)]), p0, nA0L)
    f1 = mapply(mt(OA[('h', 1)]), p1, nA1L)
    jh0 = [a + b for a, b in zip(j0, f0)]
    jh1 = [a + b for a, b in zip(j1, f1)]
    straight = [a + b for a, b in zip(jh0, mapply(mt(OA[('Qstr', 0)]), jh1, nA0L))]
    C = mkC(OA, levA, j0, j1)
    lhs = [a - b for a, b in zip(C, straight)]
    R1, okR1 = rootrestrict(OA, levA, Dfun, 1)
    R2, okR2 = rootrestrict(OA, levA, Dfun, 2)
    pred = [-(a + b) for a, b in zip(mapply(mt(OA[('h', 0)]), R1, nA0L),
             mapply(mt(OA[('Qstr', 0)]), mapply(mt(OA[('h', 1)]), R2, nA1L), nA0L))]
    if (not (okR1 and okR2)) or nz([a - b for a, b in zip(lhs, pred)]):
        ok = False
    if nz(lhs):
        defect_nonzero = True
res['A5'] = ok and defect_nonzero
print("A5 control: root-charge defect = -sum_i Qstr^T h_i^T R_{i+1}(D(S)) exactly, defect != 0 %s : %s"
      % (defect_nonzero, "PASS" if res['A5'] else "FAIL"))

# ---- A6: coarse-size claims ----
ok = True
for s in range(10):
    v = rnd(9000 + s, nA1L)
    if not (mx(mapply(mt(OA[('Qstr', 0)]), v, nA0L)) <= F(1, L ** (d - 1)) * mx(v)):
        ok = False
for (j0, j1) in CC0 + [f[0] for f in rootfams]:
    p0, p1, _, _ = psis(OA, levA, j0, j1)
    f0 = mapply(mt(OA[('h', 0)]), p0, nA0L)
    if not (mx(f0) <= mx(p0)):
        ok = False
    bound = mx(mapply(OA[('dstar', 0)], j0, nAF0))
    if not (mx(p0) <= bound):
        ok = False
res['A6'] = ok
print("A6 |Qstr^T v| <= L^{-(d-1)}|v| ; |h_0^T psi_0| <= |psi_0| <= |d*j_0|  : %s"
      % ("PASS" if ok else "FAIL"))

# ---- A7: naive vs regrouped (second half vacuous at k = 2 under (CC-0)) ----
found = False; second_ok = True; vacuous = True
for (j0, j1) in CC0:
    p0, p1, _, _ = psis(OA, levA, j0, j1)
    xi0 = mapply(OA[('dstar', 1)], j1, len(levA[1].sites))
    naive = mapply(mt(OA[('h', 0)]), xi0, nA0L)
    jh1 = [a + b for a, b in zip(j1, mapply(mt(OA[('h', 1)]), p1, nA1L))]
    thr = F(1, L ** (d - 1)) * mx(jh1)
    regrouped = mapply(mt(OA[('Qstr', 0)]), mapply(mt(OA[('h', 1)]), p1, nA1L), nA0L)
    if mx(naive) > thr:
        found = True
    if mx(regrouped) > thr:
        second_ok = False
    if nz(regrouped):
        vacuous = False
res['A7'] = found and second_ok
print("A7 naive funnel exceeds L^{-(d-1)}|jhat_1| %s ; regrouped does not %s (vacuous at k=2: %s) : %s"
      % (found, second_ok, vacuous, "PASS" if res['A7'] else "FAIL"))

# ---- A8 (amendment (iii)): the size claim in both groupings ----
ok = True
for n, (j0, j1) in enumerate(CC0):
    p0, p1, _, _ = psis(OA, levA, j0, j1)
    f0 = mapply(mt(OA[('h', 0)]), p0, nA0L)
    xi0 = mapply(OA[('dstar', 1)], j1, len(levA[1].sites))
    naive = mapply(mt(OA[('h', 0)]), xi0, nA0L)
    a = PI(0, f0); b = PI(0, naive); pj0 = PI(0, j0); pj1 = PI(1, j1)
    c1 = a <= 2 * d * pj0
    c2 = b <= 2 * d * (L ** (d - 1)) * pj1
    if not (c1 and c2):
        ok = False
    print("   A8[%d] pi_0(h_0^Tpsi_0) = %s  pi_0(h_0^Txi_0) = %s  pi_0(j_0) = %s  pi_1(j_1) = %s  ratio = %s  (%s,%s)"
          % (n, a, b, pj0, pj1, (F(b, 1) / a) if a != 0 else "n/a", c1, c2))
res['A8'] = ok
print("A8 pi_0(h_0^Tpsi_0) <= 2d pi_0(j_0) and pi_0(h_0^Txi_0) <= 2d L^{d-1} pi_1(j_1) : %s"
      % ("PASS" if ok else "FAIL"))
print("[bb10] Part A done, t = %.1f s" % (time.time() - t0))

# ======================= PART B (T = 1, exact solve) =======================
T = 1
levB, OB = ops(T)
B0_, B1_, B2_ = levB[0], levB[1], levB[2]
n0L, n1L = len(B0_.links), len(B1_.links)
nF0 = len(B0_.sites)
N = n0L + n1L
print("[bb10] PART B, T = %d: level sides %s, unknowns %d"
      % (T, [levB[l].n for l in range(K + 1)], N))

Q0, Q1 = OB[('Q', 0)], OB[('Q', 1)]
Qs0, Qs1 = OB[('Qstr', 0)], OB[('Qstr', 1)]
D0 = OB[('dform', 0)]
dfun0, dfun1 = OB[('dfun', 0)], OB[('dfun', 1)]
ev0 = OB[('ev', 0)]

def Hop(x):
    x0, x1 = x[:n0L], x[n0L:]
    r0 = [a - b for a, b in zip(mapply(Q0, x0, n1L), x1)]
    r1 = mapply(Q1, x1, len(B2_.links))
    g0 = [a + KAP[0] * b for a, b in zip(mapply(mt(D0), mapply(D0, x0, len(B0_.sites)), n0L),
                                         mapply(mt(Q0), r0, n0L))]
    g1 = [-KAP[0] * a + KAP[1] * b for a, b in zip(r0, mapply(mt(Q1), r1, n1L))]
    return g0 + g1

def Xi(lam):
    a = mapply(dfun0, lam, n0L)
    b = mapply(dfun1, mapply(ev0, lam, len(B1_.sites)), n1L)
    return a + b
def XiT(x):
    x0, x1 = x[:n0L], x[n0L:]
    a = mapply(mt(dfun0), x0, nF0)
    b = mapply(mt(ev0), mapply(mt(dfun1), x1, len(B1_.sites)), nF0)
    return [p + q for p, q in zip(a, b)]
def Aop(x):
    h = Hop(x); g = Xi(XiT(x))
    return [p + q for p, q in zip(h, g)]
def dense(op, n):
    cols = []
    for j in range(n):
        e = [F(0)] * n; e[j] = F(1)
        cols.append(op(e))
    return [[cols[j][i] for j in range(n)] for i in range(n)]

Amat = dense(Aop, N)
print("[bb10] A built, t = %.1f s" % (time.time() - t0))

j0B, j1B = build_source(OB, levB, 31)
S = j0B + j1B
strict = not nz(XiT(S))
print("B: D(S) = 0 strictly : %s ; d*j_0 != 0 : %s"
      % (strict, nz(mapply(OB[('dstar', 0)], j0B, nF0))))

sols = gauss(Amat, [S])
print("[bb10] solve done, t = %.1f s" % (time.time() - t0))
if sols is None:
    print("B: ABORTED (A singular)"); sys.exit(1)
x = sols[0]

Hx = Hop(x)
res['B0'] = (not nz([a - b for a, b in zip(Hx, S)])) and (not nz(XiT(x))) and strict
print("B0 criticality Hx = S, Xi^T x = 0, source strictly (CC-0)             : %s"
      % ("PASS" if res['B0'] else "FAIL"))

x0, x1 = x[:n0L], x[n0L:]
r0 = [a - b for a, b in zip(mapply(Q0, x0, n1L), x1)]
r1 = mapply(Q1, x1, len(B2_.links))
rho0 = [KAP[0] * v for v in r0]
rho1 = [KAP[1] * v for v in r1]
CB = mkC(OB, levB, j0B, j1B)
chk1 = not nz(mapply(OB[('dstar', 0)], CB, nF0))
J0 = [a - b for a, b in zip(j0B, mapply(mt(Q0), rho0, n0L))]
push = mapply(mt(Qs0), mapply(mt(Qs1), rho1, n1L), n0L)
chk2 = not nz([a - b + c for a, b, c in zip(J0, CB, push)])
res['B1'] = chk1 and chk2
print("B1 d*C(j) = 0 %s ; J_0 = C(j) - (Qstr^{(0->k)})^T rho_{k-1} %s        : %s"
      % (chk1, chk2, "PASS" if res['B1'] else "FAIL"))
print("B2 scope (pre-registered): at T = 1 the level-%d lattice has %d site(s), so a root-supported"
      % (K, len(B2_.sites)))
print("   function with total 0 vanishes: the root-charge branch is NOT exercised in Part B (A5 carries it at T = 2).")

ids = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'B0', 'B1']
bad = [i for i in ids if not res.get(i)]
print("[bb10] t = %.1f s" % (time.time() - t0))
print("VERDICT bb10 (%s): %s%s" % (", ".join(ids),
      "ALL PASS" if not bad else "NOT ALL PASS", "" if not bad else " -- FAILED: " + ", ".join(bad)))
