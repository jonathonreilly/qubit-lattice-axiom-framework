#!/usr/bin/env python3
"""bb10c_cof3.py -- exact rational check of Lemma DF-cc at k = 3 (BFT_B.md session 10, Sec 35.3 / 37.4).

Criteria: checks/bb10c_criteria.md, written BEFORE this script and after bb10 ran.  bb10 is NOT altered and
no bb10 criterion is retuned; bb10c is a new check at k = 3.

The model and the whole operator construction (Lev, the sparse helpers, build(), solve_div, rnd) are COPIED
from checks/bb9b_rtcc.py with EXACTLY ONE change: K = 3 in place of K = 2.  So d = 2, L = 3, k = 3,
roots = block centres, axial order 0 then 1, top side T = 1 (level sides 27, 9, 3, 1).  Part A only: no solve.

Exact arithmetic only (fractions.Fraction and Python ints). No numpy, no BLAS, single thread.
"""
from fractions import Fraction as F
import itertools, time, sys

d = 2
L = 3
K = 3            # <-- the ONLY change to the copied core (bb9b has K = 2)
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

# ======================================================================
#   bb10c TESTS (k = 3, Part A only)
# ======================================================================
T = 1
lev, O = build(T)
nL = {l: len(lev[l].links) for l in range(K + 1)}
nS = {l: len(lev[l].sites) for l in range(K + 1)}
print("[bb10c] d = %d, L = %d, k = %d, T = %d: level sides %s" % (d, L, K, T, [lev[l].n for l in range(K + 1)]))
res = {}
PI = lambda l, v: (L ** ((d - 1) * (K - l))) * mx(v)
off = (L - 1) // 2

def c0(X, l):
    """level-0 site of the level-l root X"""
    return tuple((L ** l * X[a] + sum(L ** t * off for t in range(l))) % lev[0].n for a in range(d))

def place(v, l):
    """ev^{(0->l)T} v : level-l function -> level-0 function"""
    out = [F(0)] * nS[0]
    for X in lev[l].sites:
        out[lev[0].si[c0(X, l)]] = v[lev[l].si[X]]
    return out

def restrict(u, l):
    """R_l(u): level-l function with ev^{(0->l)T} R = u; returns (R, ok)"""
    R = [F(0)] * nS[l]
    for X in lev[l].sites:
        R[lev[l].si[X]] = u[lev[0].si[c0(X, l)]]
    return R, (not nz([a - b for a, b in zip(place(R, l), u)]))

def Dof(j):
    out = mapply(O[('dstar', 0)], j[0], nS[0])
    for l in range(1, K):
        out = [a + b for a, b in zip(out, place(mapply(O[('dstar', l)], j[l], nS[l]), l))]
    return out

def Qcomp(a, b, straight):
    """Q^{(a->b)} as a sparse matrix (identity if a == b)"""
    key = 'Qstr' if straight else 'Q'
    M = None
    for i in range(a, b):
        M = O[(key, i)] if M is None else mmul(O[(key, i)], M)
    return M

def Qstr_push(v, i):
    """(Q_str^{(0->i)})^T v  : level-i 1-form -> level-0 1-form"""
    if i == 0:
        return v
    return mapply(mt(Qcomp(0, i, True)), v, nL[0])

def cascade(j):
    """psi_i (i = 0..K-1) and xi_i, plus the root-support flags"""
    D = Dof(j)
    Psi = []
    acc = mapply(O[('dstar', 0)], j[0], nS[0])
    Psi.append(acc[:])
    for l in range(1, K):
        acc = [a + b for a, b in zip(acc, place(mapply(O[('dstar', l)], j[l], nS[l]), l))]
        Psi.append(acc[:])
    psi, okf = [], []
    for i in range(K):
        R, ok = restrict(Psi[i], i + 1)
        psi.append(R); okf.append(ok)
    xi = []
    for i in range(K):
        x = [F(0)] * nS[i + 1]
        for l in range(i + 1, K):
            dsl = mapply(O[('dstar', l)], j[l], nS[l])
            if l == i + 1:
                add = dsl
            else:
                add = [F(0)] * nS[i + 1]
                for X in lev[l].sites:          # ev^{(i+1->l)T}
                    Y = tuple((L ** (l - i - 1) * X[a] + sum(L ** t * off for t in range(l - i - 1)))
                              % lev[i + 1].n for a in range(d))
                    add[lev[i + 1].si[Y]] = dsl[lev[l].si[X]]
            x = [a + b for a, b in zip(x, add)]
        xi.append(x)
    return D, psi, xi, okf

def build_cc0(seed):
    """plain collection with D(S) = 0: j_1, j_2 random, j_0 solves d*j_0 = -(placements)"""
    j1 = rnd(seed, nL[1]); j2 = rnd(seed + 1, nL[2])
    tgt = place(mapply(O[('dstar', 1)], j1, nS[1]), 1)
    tgt = [a + b for a, b in zip(tgt, place(mapply(O[('dstar', 2)], j2, nS[2]), 2))]
    j0 = solve_div(lev[0], [-v for v in tgt])
    return [j0, j1, j2]

fams = [build_cc0(100 + 7 * s) for s in range(6)]

# ---- C1 ----
ok = True; twolev = False
for j in fams:
    D, psi, xi, okf = cascade(j)
    if nz(D):
        ok = False
    if not all(okf):
        ok = False
    for i in range(K):
        if nz([a + b for a, b in zip(xi[i], psi[i])]):
            ok = False
    if nz(psi[0]) and nz(psi[1]):
        twolev = True
res['C1'] = ok and twolev
print("C1 xi_i = -psi_i for i = 0,1,2 (exact), two nonzero cascade levels %s : %s"
      % (twolev, "PASS" if res['C1'] else "FAIL"))

# ---- C2 / C3 ----
ok2 = True; ok3 = True; upper = False
for j in fams:
    D, psi, xi, okf = cascade(j)
    jh = []
    for l in range(K):
        f = mapply(mt(O[('h', l)]), psi[l], nL[l])
        jh.append([a + b for a, b in zip(j[l], f)])
        if l >= 1 and nz(f):
            upper = True
    C = [F(0)] * nL[0]
    for l in range(K):
        C = [a + b for a, b in zip(C, mapply(mt(Qcomp(0, l, False)), j[l], nL[0]) if l else j[l])]
    rhs = [F(0)] * nL[0]
    for l in range(K):
        rhs = [a + b for a, b in zip(rhs, Qstr_push(jh[l], l))]
    if nz([a - b for a, b in zip(C, rhs)]):
        ok2 = False
    if nz(mapply(O[('dstar', 0)], C, nS[0])):
        ok3 = False
res['C2'] = ok2 and upper
res['C3'] = ok3
print("C2 Lemma DF-cc (ii) at k = 3: C(j) = sum_l (Qstr^{(0->l)})^T jhat_l ; h_l^Tpsi_l != 0 for some l >= 1 %s : %s"
      % (upper, "PASS" if res['C2'] else "FAIL"))
print("C3 d*C(j) = D(S) = 0 (exact)                                          : %s"
      % ("PASS" if res['C3'] else "FAIL"))

# ---- C4: the two bounds ----
okA = True; okB = False
for n, j in enumerate(fams):
    D, psi, xi, okf = cascade(j)
    pj = [PI(l, j[l]) for l in range(K)]
    row = []
    for i in range(K):
        f = mapply(mt(O[('h', i)]), psi[i], nL[i])
        V = PI(0, Qstr_push(f, i))
        Bpsi = 2 * d * sum(F(1, L ** ((d - 1) * (i - lp))) * pj[lp] for lp in range(i + 1))
        Bxi = 2 * d * sum((L ** ((d - 1) * (l - i))) * pj[l] for l in range(i + 1, K))
        if not (V <= Bpsi):
            okA = False
        if i == 0 and Bxi > Bpsi:
            okB = True
        row.append((i, V, Bpsi, Bxi))
    print("   C4[%d] pi_l(j_l) = %s" % (n, pj))
    for (i, V, Bp, Bx) in row:
        print("        i = %d : V = %s   B^psi = %s   B^xi = %s   (V<=B^psi %s, B^xi>B^psi %s)"
              % (i, V, Bp, Bx, V <= Bp, Bx > Bp))
res['C4'] = okA and okB
print("C4 V_i <= B^psi_i always %s ; B^xi_0 > B^psi_0 somewhere %s            : %s"
      % (okA, okB, "PASS" if res['C4'] else "FAIL"))

# ---- C5: control (random collections) ----
badsupport = False; identity_fails = False
for s in range(4):
    j = [rnd(500 + 11 * s, nL[0]), rnd(600 + 11 * s, nL[1]), rnd(700 + 11 * s, nL[2])]
    D, psi, xi, okf = cascade(j)
    if not all(okf):
        badsupport = True
        jh = []
        for l in range(K):
            f = mapply(mt(O[('h', l)]), psi[l], nL[l])
            jh.append([a + b for a, b in zip(j[l], f)])
        C = [F(0)] * nL[0]
        for l in range(K):
            C = [a + b for a, b in zip(C, mapply(mt(Qcomp(0, l, False)), j[l], nL[0]) if l else j[l])]
        rhs = [F(0)] * nL[0]
        for l in range(K):
            rhs = [a + b for a, b in zip(rhs, Qstr_push(jh[l], l))]
        if nz([a - b for a, b in zip(C, rhs)]):
            identity_fails = True
res['C5'] = badsupport and identity_fails
print("C5 control: random collection fails root support %s and fails C2's identity %s : %s"
      % (badsupport, identity_fails, "PASS" if res['C5'] else "FAIL"))

ids = ['C1', 'C2', 'C3', 'C4', 'C5']
bad = [i for i in ids if not res.get(i)]
print("[bb10c] t = %.1f s" % (time.time() - t0))
print("VERDICT bb10c (%s): %s%s" % (", ".join(ids), "ALL PASS" if not bad else "NOT ALL PASS",
      "" if not bad else " -- FAILED: " + ", ".join(bad)))
