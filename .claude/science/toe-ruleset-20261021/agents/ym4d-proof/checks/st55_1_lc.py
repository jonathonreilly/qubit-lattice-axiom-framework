# st55_1 -- exact checks of STEP55 section 2 (Lemmas ST, Q2, CC, DS, CERT; Theorem LC), d = 4, L = 3.
# Criteria: st55_1_criteria.md (sha256 70d412bb..., written 2026-10-29T05:38:47Z before this script).
# Plain python, fractions/integers only. No floats in any verdict.
from fractions import Fraction as F
from itertools import permutations, product
import random, sys, time

T0 = time.time()
def log(*a):
    print(*a, flush=True)

d = 4
L = 3
ORDERS = list(permutations(range(d)))          # 24 coordinate orders
NCONT = len(ORDERS) * L ** d                   # 1944 contours per coarse link
OFF = tuple([(L - 1) // 2] * d)                # root offset o
PL = [(m, n) for m in range(d) for n in range(m + 1, d)]   # 6 plaquette orientations
RESULTS = {}

def unit(k):
    return tuple(1 if i == k else 0 for i in range(d))
def add(a, b):
    return tuple(x + y for x, y in zip(a, b))
def scal(c, a):
    return tuple(c * x for x in a)

def axial_path(start, end, sigma):
    """complete-axial path start -> end, coordinates in the order sigma.
    returns [(base_site, direction, sign)]: sign +1 = traversed from base to base+e_k, -1 = from base+e_k to base."""
    cur = list(start); steps = []
    for k in sigma:
        while cur[k] < end[k]:
            steps.append((tuple(cur), k, 1)); cur[k] += 1
        while cur[k] > end[k]:
            cur[k] -= 1; steps.append((tuple(cur), k, -1))
    return steps

def build_maps():
    """integer count maps for the coarse link (0, mu); offsets relative to L*X (block B(0) = {0..L-1}^d, root OFF).
    Qroot = count/NCONT, Qstr = count/NCONT (straight legs only), h = count/NCONT (first legs, a 0-form at X)."""
    qroot = {}; qstr = {}; hmap = {}
    cX = OFF
    for mu in range(d):
        cY = add(cX, scal(L, unit(mu)))
        cr = {}; cs = {}
        for sigma in ORDERS:
            for y in product(range(L), repeat=d):
                p1 = axial_path(cX, y, sigma)
                p2 = [(add(y, scal(j, unit(mu))), mu, 1) for j in range(L)]
                p3f = axial_path(cY, add(y, scal(L, unit(mu))), sigma)
                p3 = [(s, k, -sg) for (s, k, sg) in reversed(p3f)]
                for (s, k, sg) in p1 + p2 + p3:
                    cr[(s, k)] = cr.get((s, k), 0) + sg
                for (s, k, sg) in p2:
                    cs[(s, k)] = cs.get((s, k), 0) + sg
                if mu == 0:
                    for (s, k, sg) in p1:
                        hmap[(s, k)] = hmap.get((s, k), 0) + sg
        qroot[mu] = {key: v for key, v in cr.items() if v != 0}
        qstr[mu] = {key: v for key, v in cs.items() if v != 0}
    hmap = {key: v for key, v in hmap.items() if v != 0}
    return qroot, qstr, hmap

QROOT, QSTR, HMAP = build_maps()
log("maps built: |Qroot_mu| =", [len(QROOT[m]) for m in range(d)], " |h| =", len(HMAP), " t=%.1fs" % (time.time() - T0))

class Lat:
    def __init__(self, n):
        self.n = n
        self.N = n ** d
        self.sites = list(product(range(n), repeat=d))
    def si(self, x):
        n = self.n
        i = 0
        for c in x:
            i = i * n + (c % n)
        return i
    def li(self, x, mu):
        return self.si(x) * d + mu
    def pi(self, x, o):
        return self.si(x) * 6 + o

def d0(lat, lam):
    out = [0] * (lat.N * d)
    for x in lat.sites:
        i = lat.si(x); lx = lam[i]
        for mu in range(d):
            out[i * d + mu] = lam[lat.si(add(x, unit(mu)))] - lx
    return out
def d0T(lat, s):
    out = [0] * lat.N
    for x in lat.sites:
        i = lat.si(x); acc = 0
        for mu in range(d):
            acc += s[lat.li(add(x, scal(-1, unit(mu))), mu)] - s[i * d + mu]
        out[i] = acc
    return out
def d1(lat, A):
    out = [0] * (lat.N * 6)
    for x in lat.sites:
        i = lat.si(x)
        for o, (m, n_) in enumerate(PL):
            out[i * 6 + o] = (A[i * d + m] + A[lat.li(add(x, unit(m)), n_)]
                              - A[lat.li(add(x, unit(n_)), m)] - A[i * d + n_])
    return out
def d1T(lat, Fm):
    out = [0] * (lat.N * d)
    for x in lat.sites:
        i = lat.si(x)
        for o, (m, n_) in enumerate(PL):
            v = Fm[i * 6 + o]
            if v == 0:
                continue
            out[i * d + m] += v
            out[lat.li(add(x, unit(m)), n_)] += v
            out[lat.li(add(x, unit(n_)), m)] -= v
            out[i * d + n_] -= v
    return out

def apply_map(fine, coarse, mp, A, mu):
    """sum over coarse sites X of the (count) map of the link (X,mu) applied to the fine 1-form A; returns list over X"""
    out = []
    for X in coarse.sites:
        base = scal(L, X); acc = 0
        for (s, k), c in mp.items():
            acc += c * A[fine.li(add(base, s), k)]
        out.append(acc)
    return out
def Q_scaled(fine, coarse, A, which):
    """NCONT * Q(A) (which = QROOT or QSTR) as a coarse 1-form of integers (if A is integer)"""
    out = [0] * (coarse.N * d)
    for mu in range(d):
        vals = apply_map(fine, coarse, which[mu], A, mu)
        for j, X in enumerate(coarse.sites):
            out[coarse.si(X) * d + mu] = vals[j]
    return out
def QT_scaled(fine, coarse, s, which):
    out = [0] * (fine.N * d)
    for X in coarse.sites:
        base = scal(L, X); ci = coarse.si(X)
        for mu in range(d):
            v = s[ci * d + mu]
            if v == 0:
                continue
            for (sx, k), c in which[mu].items():
                out[fine.li(add(base, sx), k)] += c * v
    return out
def h_scaled(fine, coarse, A):
    out = [0] * coarse.N
    for X in coarse.sites:
        base = scal(L, X); acc = 0
        for (s, k), c in HMAP.items():
            acc += c * A[fine.li(add(base, s), k)]
        out[coarse.si(X)] = acc
    return out
def evT(fine, coarse, lam_c):
    out = [0] * fine.N
    for X in coarse.sites:
        out[fine.si(add(scal(L, X), OFF))] = lam_c[coarse.si(X)]
    return out
Q2OFF = {}
def q2off(o, side):
    key = (o, side)
    if key not in Q2OFF:
        m, n_ = PL[o]; cnt = {}
        for y in product(range(L), repeat=d):
            for a in range(side):
                for b in range(side):
                    off = add(y, add(scal(a, unit(m)), scal(b, unit(n_))))
                    cnt[off] = cnt.get(off, 0) + 1
        Q2OFF[key] = list(cnt.items())
    return Q2OFF[key]
def Q2_scaled(fine, coarse, Fm, side=L):
    """L^4 * Q_2(F) with squares of side `side` (side = L is Q_2; side = L-1 is the control)"""
    out = [0] * (coarse.N * 6)
    for X in coarse.sites:
        base = scal(L, X); ci = coarse.si(X)
        for o in range(6):
            acc = 0
            for off, c in q2off(o, side):
                acc += c * Fm[fine.pi(add(base, off), o)]
            out[ci * 6 + o] = acc
    return out
def Q2T_scaled(fine, coarse, Fc):
    out = [0] * (fine.N * 6)
    for X in coarse.sites:
        base = scal(L, X); ci = coarse.si(X)
        for o in range(6):
            v = Fc[ci * 6 + o]
            if v == 0:
                continue
            for off, c in q2off(o, L):
                out[fine.pi(add(base, off), o)] += c * v
    return out
def dot(a, b):
    return sum(x * y for x, y in zip(a, b))
def rnd(rng, n, lo=-5, hi=5):
    return [rng.randint(lo, hi) for _ in range(n)]

# ---------------------------------------------------------------- Part A
log("\n== Part A: exact identities")
fine6 = Lat(6); coarse2 = Lat(2)
okA = {}
for seed in (1, 2):
    rng = random.Random(1000 + seed)
    A = rnd(rng, fine6.N * d)
    QA = Q_scaled(fine6, coarse2, A, QROOT)                       # 1944 * Qroot A
    QsA = Q_scaled(fine6, coarse2, A, QSTR)                       # 1944 * Qstr A
    hA = h_scaled(fine6, coarse2, A)                              # 1944 * h A
    a1 = (QA == [u - v for u, v in zip(QsA, d0(coarse2, hA))])
    a2 = (d1(coarse2, QA) == [24 * v for v in Q2_scaled(fine6, coarse2, d1(fine6, A))])
    s = rnd(rng, coarse2.N * d)
    a3 = (d0T(fine6, QT_scaled(fine6, coarse2, s, QROOT)) == [NCONT * v for v in evT(fine6, coarse2, d0T(coarse2, s))])
    Xi = rnd(rng, coarse2.N * 6)
    a4 = (QT_scaled(fine6, coarse2, d1T(coarse2, Xi), QROOT) == [24 * v for v in d1T(fine6, Q2T_scaled(fine6, coarse2, Xi))])
    # A5, k = 1
    B0 = rnd(rng, fine6.N * d); B1 = rnd(rng, coarse2.N * d); Xi = rnd(rng, coarse2.N * 6)
    lhs = dot(d1(coarse2, B1), Xi)
    r0s = [u - NCONT * v for u, v in zip(Q_scaled(fine6, coarse2, B0, QROOT), B1)]   # 1944 r_0
    rhs = F(dot(d1(fine6, B0), Q2T_scaled(fine6, coarse2, Xi)), L ** 4) - F(dot(r0s, d1T(coarse2, Xi)), NCONT)
    a5 = (F(lhs) == rhs)
    okA[seed] = (a1, a2, a3, a4, a5)
    log("seed", seed, ": A1", a1, " A2", a2, " A3", a3, " A4", a4, " A5(k=1)", a5, " (lhs = %d)" % lhs)
# A5, k = 2 (sides 18 -> 6 -> 2)
log("A5 k=2: building side-18 lattice ... t=%.1fs" % (time.time() - T0))
fine18 = Lat(18); mid6 = Lat(6)
a5k2 = []
for seed in (3, 4):
    rng = random.Random(2000 + seed)
    B0 = rnd(rng, fine18.N * d, -3, 3); B1 = rnd(rng, mid6.N * d); B2 = rnd(rng, coarse2.N * d); Xi = rnd(rng, coarse2.N * 6)
    lhs = F(dot(d1(coarse2, B2), Xi))
    Xi0s = Q2T_scaled(mid6, coarse2, Xi)              # 81 Xi_0
    Xim1s = Q2T_scaled(fine18, mid6, Xi0s)           # 81^2 Xi_{-1}
    r0s = [u - NCONT * v for u, v in zip(Q_scaled(fine18, mid6, B0, QROOT), B1)]   # 1944 r_0
    r1s = [u - NCONT * v for u, v in zip(Q_scaled(mid6, coarse2, B1, QROOT), B2)]  # 1944 r_1
    rhs = (F(dot(d1(fine18, B0), Xim1s), L ** 8)
           - F(dot(r0s, d1T(mid6, Xi0s)), NCONT * L ** 4)
           - F(dot(r1s, d1T(coarse2, Xi)), NCONT))
    a5k2.append(lhs == rhs)
    log("seed", seed, ": A5(k=2)", lhs == rhs, " lhs =", lhs, " t=%.1fs" % (time.time() - T0))
# control: (L-1)-squares in place of Q_2
rng = random.Random(77)
A = rnd(rng, fine6.N * d)
QA = Q_scaled(fine6, coarse2, A, QROOT)
wrong = Q2_scaled(fine6, coarse2, d1(fine6, A), side=L - 1)
ctlA = not (d1(coarse2, QA) == [24 * v for v in wrong]) and not (d1(coarse2, QA) == [F(24 * L * L, (L - 1) ** 2) * v for v in wrong])
log("A-ctl ((L-1)-squares) identity fails as designed:", ctlA)
RESULTS['A'] = all(all(t) for t in okA.values()) and all(a5k2)
RESULTS['A-ctl fired'] = ctlA

# ---------------------------------------------------------------- Part B
log("\n== Part B: norm lemmas")
b1 = True
for seed in range(4):
    rng = random.Random(3000 + seed)
    Fm = rnd(rng, fine6.N * 6)
    q = Q2_scaled(fine6, coarse2, Fm)
    lhs = F(dot(q, q), L ** 8); rhs = F(dot(Fm, Fm))
    b1 = b1 and (lhs <= rhs)
    log("B1 random: |Q2F|^2/|F|^2 =", lhs / rhs)
Fm = [0] * (fine6.N * 6)
for x in fine6.sites:
    Fm[fine6.pi(x, 0)] = 1
q = Q2_scaled(fine6, coarse2, Fm)
eq1 = (F(dot(q, q), L ** 8) == F(dot(Fm, Fm)))
log("B1 constant (01)-form: equality", eq1)
RESULTS['B1'] = b1 and eq1

b2 = True
for seed in range(4):
    rng = random.Random(4000 + seed)
    Xi = rnd(rng, mid6.N * 6)
    s = d1T(mid6, Xi)                                   # co-closed level-1 form
    qr = QT_scaled(fine18, mid6, s, QROOT)              # 1944 Qroot^T s
    qs = QT_scaled(fine18, mid6, s, QSTR)               # 1944 Qstr^T s
    same = (qr == qs)
    cc = all(v == 0 for v in d0T(fine18, qr))
    ratio = F(dot(qr, qr), NCONT ** 2) / F(dot(s, s))
    b2 = b2 and same and cc and ratio <= F(1, L * L)
    log("B2 co-closed: Qroot^T s == Qstr^T s:", same, " d*(Q^T s)=0:", cc, " ratio =", ratio, "<= 1/9:", ratio <= F(1, 9),
        " t=%.1fs" % (time.time() - T0))
s = [0] * (mid6.N * d)
for x in mid6.sites:
    s[mid6.li(x, 0)] = 1
qr = QT_scaled(fine18, mid6, s, QROOT)
eq2 = (F(dot(qr, qr), NCONT ** 2) == F(dot(s, s), L * L))
log("B2 constant co-closed form: equality |Q^T s|^2 = |s|^2/9:", eq2)
RESULTS['B2'] = b2 and eq2
s = [0] * (coarse2.N * d); s[coarse2.li((0, 0, 0, 0), 0)] = 1
qr = QT_scaled(fine6, coarse2, s, QROOT)
ctlB = F(dot(qr, qr), NCONT ** 2)
log("B2-ctl: |Qroot^T delta_c|^2 =", ctlB, "=", "%.6f" % (ctlB.numerator / ctlB.denominator), " > 1/9:", ctlB > F(1, 9))
RESULTS['B2-ctl fired'] = ctlB > F(1, 9)

b3 = True
for seed in range(4):
    rng = random.Random(5000 + seed)
    Xi = rnd(rng, fine6.N * 6)
    t = d1T(fine6, Xi)
    b3 = b3 and (dot(t, t) <= 16 * dot(Xi, Xi))
B = [0] * (fine6.N * d)
for x in fine6.sites:
    sg = (-1) ** sum(x)
    B[fine6.li(x, 0)] = sg; B[fine6.li(x, 1)] = -sg
Xi = d1(fine6, B); t = d1T(fine6, Xi)
eq3 = (dot(t, t) == 16 * dot(Xi, Xi))
log("B3 random <= 16:", b3, "; staggered transverse mode equality:", eq3)
RESULTS['B3'] = b3 and eq3

# ---------------------------------------------------------------- Part C
log("\n== Part C: complete k=1 check on the side-2 coarse torus (fine side 6), kappa_0 = 1")
KAPPA = F(1)
FD = list(product(range(L), repeat=d))                     # fundamental domain sites
VAR = {(z, a): j for j, (z, a) in enumerate((z, a) for z in FD for a in range(d))}
def is_tree(z, a):
    if a == 0: return z[0] in (0, 1)
    if a == 1: return z[0] == 0 and z[1] in (0, 1)
    if a == 2: return z[0] == 0 and z[1] == 0 and z[2] in (0, 1)
    return z[0] == 0 and z[1] == 0 and z[2] == 0 and z[3] in (0, 1)
TREE = [VAR[(z, a)] for z in FD for a in range(d) if is_tree(z, a)]
assert len(TREE) == (L ** d - 1)
FREE = [j for j in range(len(VAR)) if j not in set(TREE)]
POS = {j: i for i, j in enumerate(FREE)}

def twist(chi, x):
    """B0(x) = coeff * b(z) for a fine site x in Z (not reduced): returns (coeff, z)"""
    c = 1; z = []
    for bta in range(d):
        q, r = divmod(x[bta], L)
        if chi[bta] == -1 and q % 2 == 1:
            c = -c
        z.append(r)
    return c, tuple(z)

def sector(chi):
    nv = len(FREE)
    A = [[F(0)] * nv for _ in range(nv)]
    # curl-curl part: plaquettes based in the fundamental domain
    for z in FD:
        for o, (m, n_) in enumerate(PL):
            terms = {}
            for (pt, k, sg) in ((z, m, 1), (add(z, unit(m)), n_, 1), (add(z, unit(n_)), m, -1), (z, n_, -1)):
                c, zz = twist(chi, pt)
                j = VAR[(zz, k)]
                if j in POS:
                    terms[POS[j]] = terms.get(POS[j], 0) + c * sg
            items = [(i, v) for i, v in terms.items() if v != 0]
            for i, vi in items:
                for j, vj in items:
                    A[i][j] += F(vi * vj)   # (1/2)|db|^2 has Hessian sum_p c_p c_p^T
    # the energy is (1/2) b^T K b + (kappa/2) sum_mu (q_mu - bhat_mu)^2 ; A := K + kappa sum_mu w_mu w_mu^T
    W = []
    for mu in range(d):
        w = [F(0)] * nv
        for (s, k), c in QROOT[mu].items():
            cc, zz = twist(chi, s)
            j = VAR[(zz, k)]
            if j in POS:
                w[POS[j]] += F(cc * c, NCONT)
        W.append(w)
    for mu in range(d):
        w = W[mu]
        nz = [(i, v) for i, v in enumerate(w) if v != 0]
        for i, vi in nz:
            for j, vj in nz:
                A[i][j] += KAPPA * vi * vj
    return A, W

def ldl_solve(A, rhs_list):
    n = len(A)
    Lm = [[F(0)] * n for _ in range(n)]
    D = [F(0)] * n
    for j in range(n):
        s = A[j][j]
        Lj = Lm[j]
        for k in range(j):
            if Lj[k] != 0:
                s -= Lj[k] * Lj[k] * D[k]
        if s <= 0:
            raise ValueError("matrix not positive definite at %d" % j)
        D[j] = s
        for i in range(j + 1, n):
            t = A[i][j]
            Li = Lm[i]
            for k in range(j):
                if Li[k] != 0 and Lj[k] != 0:
                    t -= Li[k] * Lj[k] * D[k]
            Li[j] = t / s
    sols = []
    for b in rhs_list:
        y = list(b)
        for i in range(n):
            Li = Lm[i]; acc = y[i]
            for k in range(i):
                if Li[k] != 0:
                    acc -= Li[k] * y[k]
            y[i] = acc
        z = [y[i] / D[i] for i in range(n)]
        x = [F(0)] * n
        for i in reversed(range(n)):
            acc = z[i]
            for k in range(i + 1, n):
                if Lm[k][i] != 0:
                    acc -= Lm[k][i] * x[k]
            x[i] = acc
        sols.append(x)
    return sols

def AF_matrix(chi):
    M = [[F(0)] * d for _ in range(d)]
    for (m, n_) in PL:
        # coefficient vector of bhat in  bhat_m (1 - chi_n) - bhat_n (1 - chi_m)
        v = [0] * d
        v[m] += 1 - chi[n_]; v[n_] -= 1 - chi[m]
        for i in range(d):
            for j in range(d):
                M[i][j] += v[i] * v[j]
    return M

def principal_minors_nonneg(M):
    n = len(M)
    from itertools import combinations
    def det(S):
        sub = [[M[i][j] for j in S] for i in S]
        # exact fraction Gaussian elimination
        m = len(sub); detv = F(1)
        sub = [row[:] for row in sub]
        for c in range(m):
            p = None
            for r in range(c, m):
                if sub[r][c] != 0:
                    p = r; break
            if p is None:
                return F(0)
            if p != c:
                sub[c], sub[p] = sub[p], sub[c]; detv = -detv
            detv *= sub[c][c]
            for r in range(c + 1, m):
                f = sub[r][c] / sub[c][c]
                if f != 0:
                    for cc in range(c, m):
                        sub[r][cc] -= f * sub[c][cc]
        return detv
    for size in range(1, n + 1):
        for S in combinations(range(n), size):
            if det(S) < 0:
                return False
    return True

def AE_matrix(chi):
    A, W = sector(chi)
    sols = ldl_solve(A, W)                      # A^{-1} w_mu
    M = [[F(0)] * d for _ in range(d)]
    for mu in range(d):
        for nu in range(d):
            val = -KAPPA * KAPPA * dot(W[mu], sols[nu]) / 2
            if mu == nu:
                val += KAPPA / 2
            M[mu][nu] = val
    # symmetrise exactly (the two orders agree in exact arithmetic; report if not)
    asym = max(abs(M[i][j] - M[j][i]) for i in range(d) for j in range(d))
    return M, asym

# C0: chi = +1 -- direct zero-energy configuration B0 = bhat/L
chi0 = (1, 1, 1, 1)
c0 = True
for mu in range(d):
    q = [F(0)] * d
    for nu in range(d):
        for (s, k), c in QROOT[nu].items():
            if k == mu:
                q[nu] += F(c, NCONT) * F(1, L)
    bhat = [F(1) if i == mu else F(0) for i in range(d)]
    c0 = c0 and (q == bhat)
AF0 = AF_matrix(chi0)
c0 = c0 and all(v == 0 for row in AF0 for v in row)
log("C0 (flat sector): B0 = bhat/L reproduces bhat exactly and A_F = 0:", c0)
RESULTS['C0'] = c0

reps = [(-1, 1, 1, 1), (-1, -1, 1, 1), (-1, -1, -1, 1), (-1, -1, -1, -1)]
c1 = True
AEs = {}
for chi in reps:
    t1 = time.time()
    AE, asym = AE_matrix(chi)
    AF = AF_matrix(chi)
    AEs[chi] = AE
    M = [[AE[i][j] - F(1, 34) * AF[i][j] for j in range(d)] for i in range(d)]
    ok = principal_minors_nonneg(M) and asym == 0
    c1 = c1 and ok
    log("C1 chi =", chi, ": A_E - A_F/34 PSD:", ok, " (asym =", asym, ") t_sector=%.1fs" % (time.time() - t1))
RESULTS['C1'] = c1
chi = (-1, -1, -1, -1)
AE = AEs[chi]; AF = AF_matrix(chi)
M30 = [[AE[i][j] - F(1, 30) * AF[i][j] for j in range(d)] for i in range(d)]
c2fired = not principal_minors_nonneg(M30)
log("C2 (designed FAIL): A_E - A_F/30 PSD at chi = -1:", not c2fired, " -> control fired:", c2fired)
RESULTS['C2-ctl fired'] = c2fired
bh = [F(1), F(-1), F(0), F(0)]
num = sum(bh[i] * AE[i][j] * bh[j] for i in range(d) for j in range(d))
den = sum(bh[i] * AF[i][j] * bh[j] for i in range(d) for j in range(d))
R = num / den
log("report: exact Rayleigh quotient at chi = -1, bhat = (1,-1,0,0): R =", R, "= %.7f" % (R.numerator / R.denominator),
    "; 1/34 = %.7f ; c31 E float record 0.0310" % (1 / 34))
RESULTS['R(pi^4)'] = R
# C3 covariance control
AEa, _ = AE_matrix((1, -1, 1, 1))
P = [1, 0, 2, 3]
c3 = all(AEa[i][j] == AEs[(-1, 1, 1, 1)][P[i]][P[j]] for i in range(d) for j in range(d))
log("C3 covariance (0<->1):", c3)
RESULTS['C3'] = c3

# ---------------------------------------------------------------- Part D
log("\n== Part D: constants")
def cco(k, kap=F(1)):
    return 1 / (2 + 32 * sum(F(1, L ** (2 * m)) / kap for m in range(k)))
cinf = 1 / (2 + F(32 * L * L, L * L - 1))
log("c_co(1) =", cco(1), " c_co(2) =", cco(2), " c_co(3) =", cco(3), " c_co(inf) =", cinf)
pl, pu = F(333, 106), F(355, 113)
Rbar = 1 + F(1, L * L - 1) + F(1, 9)
def cE(p):
    return 2 / (p * p * (1 + 4 * p * p * Rbar))
cE_lo, cE_hi = cE(pu), cE(pl)            # c_E decreasing in pi
rat_lo, rat_hi = cinf / cE_hi, cinf / cE_lo
log("Rbar =", Rbar, "; c_E in [%.6f, %.6f]; c_co/c_E in [%.4f, %.4f]" % (cE_lo.numerator / cE_lo.denominator,
    cE_hi.numerator / cE_hi.denominator, rat_lo.numerator / rat_lo.denominator, rat_hi.numerator / rat_hi.denominator))
c1PG = F(1, 3500000)
g_old_lo = 2 * c1PG * cE_lo / (L * L); g_new = 2 * c1PG * cinf / (L * L)
log("gamma^sharp_i (i>=1): old >= %.4e (c_E lower end), new = %.4e" % (g_old_lo.numerator / g_old_lo.denominator,
    g_new.numerator / g_new.denominator))
log("cross-check vs measured float record c31 E (k=1,2,3): 0.0310, 0.0297, 0.0296 > c_co(k):",
    all(F(x) > cco(k) for x, k in ((F(310, 10000), 1), (F(297, 10000), 2), (F(296, 10000), 3))))

overall = (RESULTS['A'] and RESULTS['B1'] and RESULTS['B2'] and RESULTS['B3'] and RESULTS['C0'] and RESULTS['C1']
           and RESULTS['C3'] and RESULTS['A-ctl fired'] and RESULTS['B2-ctl fired'] and RESULTS['C2-ctl fired'])
log("\nRESULTS:", {k: (v if not isinstance(v, F) else str(v)) for k, v in RESULTS.items()})
log("OVERALL:", "PASS" if overall else "FAIL", " total time %.1fs" % (time.time() - T0))
