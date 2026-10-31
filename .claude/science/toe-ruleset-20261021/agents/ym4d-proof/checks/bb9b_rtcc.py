#!/usr/bin/env python3
"""bb9b_rtcc.py -- rerun of bb9_rtcc.py with ONE bug fixed in the Hessian assembly (Q_1^T was applied
twice in the level-1 gradient: `mapply(mt(Q1), mapply(mt(Q1), r1, n1L), n1L)` -> `mapply(mt(Q1), r1, n1L)`).
The pre-registered criteria of checks/bb9_criteria.md are UNCHANGED; checks/bb9.out is kept as the record of the
first run, in which B3 and B4 FAILED because of this bug. Nothing else in the script is changed.

Original header follows.
"""
"""bb9_rtcc.py -- exact rational check of Lemma RT-cc and Lemma FT (BFT_B.md session 9, Sec 27.2 / 29).

Criteria: checks/bb9_criteria.md (written before this script; amendment A7 also written before this script).
Exact arithmetic only (fractions.Fraction and Python ints). No numpy, no BLAS, single thread.
Model: d = 2, L = 3, k = 2, kappa_0 = 1, kappa_1 = 2, roots = block centres, axial order 0 then 1.
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

# ======================= PART A (T = 2) =======================
res = {}
T = 2
levA, OA = build(T)
print("[bb9b] PART A, T = %d: level sides %s" % (T, [levA[l].n for l in range(K + 1)]))

ok = True
for l in range(K):
    lhs = mmul(OA[('Q', l)], OA[('dfun', l)])
    rhs = mmul(OA[('dfun', l + 1)], OA[('ev', l)])
    ok = ok and eq(lhs, rhs)
res['A1'] = ok
print("A1 root covariance Q_l d = d ev : %s" % ("PASS" if ok else "FAIL"))

ok = True
for l in range(K):
    lhs = mmul(OA[('dstar', l)], mt(OA[('Q', l)]))
    rhs = mmul(mt(OA[('ev', l)]), OA[('dstar', l + 1)])
    ok = ok and eq(lhs, rhs)
res['A2'] = ok
print("A2 d* Q_l^T = ev^T d*        : %s" % ("PASS" if ok else "FAIL"))

ok = True
for l in range(K):
    lhs = mt(OA[('Q', l)])
    rhs = msub(mt(OA[('Qstr', l)]), mmul(mt(OA[('h', l)]), OA[('dstar', l + 1)]))
    ok = ok and eq(lhs, rhs)
res['A3'] = ok
print("A3 Q_l^T = Qstr_l^T - h^T d* : %s" % ("PASS" if ok else "FAIL"))

# A4: Lemma FT (i)
okA, okB, okC, worst = True, True, True, F(0)
for l in range(K):
    H = OA[('h', l)]
    percol = {}
    for (i, j), v in H.items():
        percol.setdefault(j, []).append((i, v))
        if abs(v) > worst:
            worst = abs(v)
        if abs(v) > 1:
            okB = False
    for j, lst in percol.items():
        if len(lst) > 1:
            okA = False
    # crossing links: both endpoints must be in one block
    Lv = levA[l]
    for j, lst in percol.items():
        (z, mu) = Lv.links[j]
        z2 = Lv.sh(z, mu)
        if (z[0] // L, z[1] // L) != (z2[0] // L, z2[1] // L):
            okC = False
res['A4'] = okA and okB and okC
print("A4 FT(i): one block/link %s, |c| <= 1 %s (max |c| = %s), no crossing link %s : %s"
      % (okA, okB, worst, okC, "PASS" if res['A4'] else "FAIL"))

# A5 / A6: the cascade support claim and its control
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

L0, L1, L2 = levA[0], levA[1], levA[2]
rootsL1 = set(L0.si[tuple((L * X[a] + (L - 1) // 2) % L0.n for a in range(d))] for X in L1.sites)
rootsL2site1 = set(L1.si[tuple((L * X[a] + (L - 1) // 2) % L1.n for a in range(d))] for X in L2.sites)
rootsL2 = set(L0.si[L1.sites[i] and tuple((L * L1.sites[i][a] + (L - 1) // 2) % L0.n for a in range(d))]
              for i in rootsL2site1)

okA5 = True
for seed in (11, 23, 47, 101, 211, 307):
    j1 = rnd(seed, len(L1.links))
    dsj1 = mapply(OA[('dstar', 1)], j1, len(L1.sites))
    # Psi_1 : supported on the level-2 roots (inside level 0), total 0
    psi1site = rnd(seed + 5, len(L2.sites))
    tot = sum(psi1site)
    psi1site[0] -= tot
    Psi1 = [F(0)] * len(L0.sites)
    for idx, X in enumerate(L2.sites):
        z = tuple((L * L * X[a] + (L * (L - 1) // 2) + (L - 1) // 2) % L0.n for a in range(d))
        Psi1[L0.si[z]] += psi1site[idx]
    # u := Psi_1 - ev^T d* j_1  (level-0 function), then solve d* j_0 = u
    evT = mt(OA[('ev', 0)])
    evTd = mapply(evT, dsj1, len(L0.sites))
    u = [Psi1[i] - evTd[i] for i in range(len(L0.sites))]
    j0 = solve_div(L0, u)
    dsj0 = mapply(OA[('dstar', 0)], j0, len(L0.sites))
    XiTS = [dsj0[i] + evTd[i] for i in range(len(L0.sites))]
    sup0 = all(dsj0[i] == 0 for i in range(len(L0.sites)) if i not in rootsL1)
    sup1 = all(XiTS[i] == 0 for i in range(len(L0.sites)) if i not in rootsL2)
    okA5 = okA5 and sup0 and sup1 and nz(dsj0)
res['A5'] = okA5
print("A5 cascade support (Psi_0 on level-1 roots, Psi_1 on level-2 roots, d*j_0 != 0) : %s"
      % ("PASS" if okA5 else "FAIL"))

# A6: control -- a source whose d*j_0 is not root-supported is not composite-co-closed
j0c = rnd(777, len(L0.links))
j1c = rnd(888, len(L1.links))
dsj0c = mapply(OA[('dstar', 0)], j0c, len(L0.sites))
evTdc = mapply(mt(OA[('ev', 0)]), mapply(OA[('dstar', 1)], j1c, len(L1.sites)), len(L0.sites))
XiTSc = [dsj0c[i] + evTdc[i] for i in range(len(L0.sites))]
notroot = any(dsj0c[i] != 0 for i in range(len(L0.sites)) if i not in rootsL1)
notcc = any(XiTSc[i] != 0 for i in range(len(L0.sites)) if i not in rootsL2)
res['A6'] = notroot and notcc
print("A6 control: random d*j_0 not root-supported %s and Xi^T S != 0 off level-2 roots %s : %s"
      % (notroot, notcc, "PASS" if res['A6'] else "FAIL"))

# A7 (amendment): non-vacuity of the funnel
okA7, ratios = True, []
for l in range(K):
    rho = rnd(1234 + l, len(levA[l + 1].links))
    dsr = mapply(OA[('dstar', l + 1)], rho, len(levA[l + 1].sites))
    fun = mapply(mt(OA[('h', l)]), dsr, len(levA[l].links))
    if not nz(dsr) or not nz(fun):
        okA7 = False
    r = mx(fun) / mx(dsr) if mx(dsr) != 0 else F(0)
    ratios.append(r)
    if r > 1:
        okA7 = False
res['A7'] = okA7
print("A7 funnel non-vacuity, max|h^T d*rho|/max|d*rho| = %s : %s"
      % ([str(r) for r in ratios], "PASS" if okA7 else "FAIL"))
print("[bb9b] Part A done, t = %.1f s" % (time.time() - t0))

# ======================= PART B (T = 1, exact solve) =======================
T = 1
levB, OB = build(T)
B0_, B1_, B2_ = levB[0], levB[1], levB[2]
n0L, n1L = len(B0_.links), len(B1_.links)
N = n0L + n1L
print("[bb9b] PART B, T = %d: level sides %s, unknowns %d"
      % (T, [levB[l].n for l in range(K + 1)], N))

Q0, Q1 = OB[('Q', 0)], OB[('Q', 1)]
Qs1 = OB[('Qstr', 1)]
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

# Xi tilde : level-0 functions -> chain
nF0 = len(B0_.sites)
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
    h = Hop(x)
    g = Xi(XiT(x))
    return [p + q for p, q in zip(h, g)]

def dense(op, n):
    cols = []
    for j in range(n):
        e = [F(0)] * n; e[j] = F(1)
        cols.append(op(e))
    return [[cols[j][i] for j in range(n)] for i in range(n)]

Amat = dense(Aop, N)
print("[bb9b] A built, t = %.1f s" % (time.time() - t0))

# --- source: composite-co-closed, plain only, d*j_0 != 0 ---
j1 = rnd(31, n1L)
dsj1 = mapply(OB[('dstar', 1)], j1, len(B1_.sites))
evTdsj1 = mapply(mt(ev0), dsj1, nF0)
u = [-v for v in evTdsj1]
j0 = solve_div(B0_, u)
S = j0 + j1
XiTS = XiT(S)
print("B: Xi^T S == 0 : %s ; d*j_0 != 0 : %s" % (not nz(XiTS), nz(mapply(OB[('dstar', 0)], j0, nF0))))

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

Sbad = rnd(999, n0L) + rnd(1001, n1L)
sols = gauss(Amat, [S, Sbad])
print("[bb9b] solve done, t = %.1f s" % (time.time() - t0))
if sols is None:
    print("B: ABORTED (A singular)"); sys.exit(1)
x, xbad = sols

# B0
Hx = Hop(x)
res['B0'] = (not nz([a - b for a, b in zip(Hx, S)])) and (not nz(XiT(x)))
print("B0 criticality Hx = S and Xi^T x = 0 : %s" % ("PASS" if res['B0'] else "FAIL"))

x0, x1 = x[:n0L], x[n0L:]
r0 = [a - b for a, b in zip(mapply(Q0, x0, n1L), x1)]
r1 = mapply(Q1, x1, len(B2_.links))
rho0 = [KAP[0] * v for v in r0]
rho1 = [KAP[1] * v for v in r1]
psi0 = mapply(OB[('dstar', 1)], rho0, len(B1_.sites))
psi1 = mapply(OB[('dstar', 2)], rho1, len(B2_.sites))
dsj0 = mapply(OB[('dstar', 0)], j0, nF0)

res['B1'] = nz(dsj0) and nz(psi0)
print("B1 non-vacuity: d*j_0 != 0 %s, psi_0 = d*rho_0 != 0 %s : %s"
      % (nz(dsj0), nz(psi0), "PASS" if res['B1'] else "FAIL"))

# B2: psi_0(Z) = (d*j_0)(z_Z) and ev^T psi_0 = d*j_0
off = (L - 1) // 2
pred = [F(0)] * len(B1_.sites)
for X in B1_.sites:
    z = tuple((L * X[a] + off) % B0_.n for a in range(d))
    pred[B1_.si[X]] = dsj0[B0_.si[z]]
chk1 = not nz([a - b for a, b in zip(psi0, pred)])
chk2 = not nz([a - b for a, b in zip(mapply(mt(ev0), psi0, nF0), dsj0)])
res['B2'] = chk1 and chk2
print("B2 RT-cc(a): psi_0 = root restriction of d*j_0 %s ; ev^T psi_0 = d*j_0 %s : %s"
      % (chk1, chk2, "PASS" if res['B2'] else "FAIL"))

# B3 / B4
fun1 = mapply(mt(OB[('h', 1)]), psi1, n1L)
jhat1 = [a + b for a, b in zip(j1, fun1)]
lhs = rho0
rhs = [a - b for a, b in zip(mapply(mt(Qs1), rho1, n1L), jhat1)]
res['B3'] = not nz([a - b for a, b in zip(lhs, rhs)])
print("B3 RT-cc(b,c): rho_0 = Qstr_1^T rho_1 - jhat_1 : %s" % ("PASS" if res['B3'] else "FAIL"))
rhs_nofun = [a - b for a, b in zip(mapply(mt(Qs1), rho1, n1L), j1)]
holds_nofun = not nz([a - b for a, b in zip(lhs, rhs_nofun)])
branch = "psi_1 = 0" if not nz(psi1) else "psi_1 != 0"
res['B4'] = (not nz(psi1) and holds_nofun) or (nz(psi1) and not holds_nofun)
print("B4 control branch %s ; identity without the funnel holds = %s : %s"
      % (branch, holds_nofun, "PASS" if res['B4'] else "FAIL"))

# B5
J0 = [a - b for a, b in zip(j0, mapply(mt(Q0), rho0, n0L))]
chk1 = not nz(mapply(OB[('dstar', 0)], J0, nF0))
chk2 = not nz([a - b for a, b in zip(mapply(mt(D0), mapply(D0, x0, len(B0_.sites)), n0L), J0)])
res['B5'] = chk1 and chk2
print("B5 RT-cc(d): d*J_0 = 0 %s ; d*d x_0 = J_0 %s : %s" % (chk1, chk2, "PASS" if res['B5'] else "FAIL"))

# B6
fun0 = mapply(mt(OB[('h', 0)]), psi0, n0L)
chk1 = mx(fun0) <= mx(psi0)
chk2 = True
for i, (z, mu) in enumerate(B0_.links):
    if fun0[i] != 0:
        z2 = B0_.sh(z, mu)
        if (z[0] // L, z[1] // L) != (z2[0] // L, z2[1] // L):
            chk2 = False
res['B6'] = chk1 and chk2
print("B6 FT(i) at the solution: max|h_0^T psi_0| = %s <= max|psi_0| = %s is %s ; no crossing link %s : %s"
      % (mx(fun0), mx(psi0), chk1, chk2, "PASS" if res['B6'] else "FAIL"))

# B7
res['B7'] = nz([a - b for a, b in zip(Hop(xbad), Sbad)])
print("B7 control: Xi^T S' != 0 gives H x' != S' : %s" % ("PASS" if res['B7'] else "FAIL"))

fails = [k for k, v in sorted(res.items()) if not v]
print("[bb9b] t = %.1f s" % (time.time() - t0))
print("VERDICT bb9b (A1,A2,A3,A4,A5,A6,A7,B0,B1,B2,B3,B4,B5,B6,B7): %s%s"
      % ("ALL PASS" if not fails else "NOT ALL PASS", "" if not fails else "  FAILING: " + ",".join(fails)))
