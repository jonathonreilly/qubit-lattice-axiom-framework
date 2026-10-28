#!/usr/bin/env python3
"""r55n_q1 -- independent exact enumeration of Setting SC's Q = Q_root (S4' linearised) at L=3, d=4.
REVIEW55_NORMS reviewer (claude-opus-5-5). Criteria: checks/r55n_q1_criteria.md (written before this file).
Built only from the definitions in PROOF.md S4' and LINEAR_PACKAGE.md 1.1-1.2. Imports nothing from other checks.
Exact integer/Fraction arithmetic; plain python; no numpy."""
import sys, itertools
from fractions import Fraction as Fr

D, L = 4, 3
O = (L - 1) // 2
ORDERS = list(itertools.permutations(range(D)))       # d! coordinate orders
NS = len(ORDERS) * L ** D                              # number of (sigma, y) contours = 1944
out = []
def say(s):
    out.append(s); print(s, flush=True)

def add(v, w):
    return tuple(a + b for a, b in zip(v, w))
def e(mu, k=1):
    return tuple(k if i == mu else 0 for i in range(D))
def root(X):            # level-(i+1) site X -> its level-i root c_X = L X + O(1,..,1)
    return tuple(L * x + O for x in X)
def block(X):           # B(X) = L X + {0..L-1}^d
    return [tuple(L * x + t for x, t in zip(X, off)) for off in itertools.product(range(L), repeat=D)]

def axial_path(a, b, sigma, acc, sgn):
    """complete-axial path a -> b moving coordinate sigma[0] first; adds sgn*(line-integral coefficients) to acc."""
    s = list(a)
    for c in sigma:
        while s[c] != b[c]:
            if b[c] > s[c]:
                lk = (tuple(s), c); acc[lk] = acc.get(lk, 0) + sgn; s[c] += 1
            else:
                s[c] -= 1; lk = (tuple(s), c); acc[lk] = acc.get(lk, 0) - sgn
    assert tuple(s) == tuple(b)

def clean(acc):
    return {k: v for k, v in acc.items() if v != 0}

def qroot_row(X, mu):
    """integer row over denominator NS: sum over contours of line-integral coefficients"""
    cX, cY = root(X), add(root(X), e(mu, L))
    acc = {}
    for sigma in ORDERS:
        for y in block(X):
            axial_path(cX, y, sigma, acc, +1)                       # near funnel c_X -> y
            for j in range(L):                                       # straight leg S_y
                lk = (add(y, e(mu, j)), mu); acc[lk] = acc.get(lk, 0) + 1
            axial_path(cY, add(y, e(mu, L)), sigma, acc, -1)        # far funnel, reversed
    return clean(acc)

def h_row(X):
    """integer row (denominator NS) of the slice functional h at coarse site X: avg_{sigma,y} int_{P^sigma(c_X->y)}"""
    cX = root(X); acc = {}
    for sigma in ORDERS:
        for y in block(X):
            axial_path(cX, y, sigma, acc, +1)
    return clean(acc)

def qstr_lp_row(X, mu):
    """integer row over denominator L^d (LINEAR_PACKAGE l.71)"""
    acc = {}
    for y in block(X):
        for j in range(L):
            lk = (add(y, e(mu, j)), mu); acc[lk] = acc.get(lk, 0) + 1
    return clean(acc)

def qstr_norms_row(X, mu, start):
    """integer row over denominator L^(d-1) (NORMS l.103-104): L^(d-1) straight paths of L links, transverse offsets
    over the block; start='a': from c_X + t ; start='b': from block low face + t"""
    acc = {}; cX = root(X)
    trans = [nu for nu in range(D) if nu != mu]
    for offs in itertools.product(range(-O, O + 1), repeat=D - 1):
        t = [0] * D
        for nu, o in zip(trans, offs):
            t[nu] = o
        base = add(cX, tuple(t))
        if start == 'b':
            base = tuple(L * X[mu] if i == mu else base[i] for i in range(D))
        for j in range(L):
            lk = (add(base, e(mu, j)), mu); acc[lk] = acc.get(lk, 0) + 1
    return clean(acc)

def l1(row, den):
    return Fr(sum(abs(v) for v in row.values()), den)

def lam(s):   # cubic in every coordinate
    return sum((i + 2) * s[i] ** 3 for i in range(D)) + s[0] * s[1] * s[2] * s[3] + 3 * s[1] * s[2] ** 2
def dlam(lk):
    s, nu = lk
    return lam(add(s, e(nu))) - lam(s)
def apply_row(row, den, f):
    return Fr(sum(v * f(k) for k, v in row.items()), den)

results = {}
X0 = (0, 0, 0, 0)
# ---------------- h
hX = h_row(X0)
h_l1 = l1(hX, NS)
avg_dist = Fr(sum(sum(abs(a - b) for a, b in zip(y, root(X0))) for y in block(X0)), L ** D)
closed = Fr(D * (L * L - 1), 4 * L)
say("q1-G  ||h|| row l1 = %s ; avg_y |y-c_X|_1 = %s ; d(L^2-1)/(4L) = %s ; support = %d" % (h_l1, avg_dist, closed, len(hX)))
results['q1-G'] = (h_l1 == avg_dist == closed)

okA = okB = okC = okD = okH = True
ctrlC_fired = {}; ctrlD_fired = {}
for mu in range(D):
    q = qroot_row(X0, mu)
    v = l1(q, NS)
    say("q1-A  mu=%d : sum_b |Q_root(c,b)| = %s (= %.6f), support = %d" % (mu, v, float(v), len(q)))
    okA &= (v == Fr(205, 27) and len(q) == 459)
    okB &= (v > L)
    # slice identity: Q_root == Q_str^LP - (h(Y) - h(X)), all over common denominator NS
    s_lp = qstr_lp_row(X0, mu)
    hY = h_row(add(X0, e(mu)))
    scale_lp = NS // (L ** D)
    rhs = {}
    for k_, v_ in s_lp.items(): rhs[k_] = rhs.get(k_, 0) + v_ * scale_lp
    for k_, v_ in hY.items(): rhs[k_] = rhs.get(k_, 0) - v_
    for k_, v_ in hX.items(): rhs[k_] = rhs.get(k_, 0) + v_
    rhs = clean(rhs)
    keys = set(q) | set(rhs)
    ndiff = sum(1 for k_ in keys if q.get(k_, 0) != rhs.get(k_, 0))
    say("q1-C  mu=%d : Q_root vs Q_str^LP - d.h : differing entries = %d" % (mu, ndiff))
    okC &= (ndiff == 0)
    for start in ('a', 'b'):
        s_n = qstr_norms_row(X0, mu, start)
        scale_n = NS // (L ** (D - 1))
        rhs2 = {}
        for k_, v_ in s_n.items(): rhs2[k_] = rhs2.get(k_, 0) + v_ * scale_n
        for k_, v_ in hY.items(): rhs2[k_] = rhs2.get(k_, 0) - v_
        for k_, v_ in hX.items(): rhs2[k_] = rhs2.get(k_, 0) + v_
        rhs2 = clean(rhs2)
        keys2 = set(q) | set(rhs2)
        nd2 = sum(1 for k_ in keys2 if q.get(k_, 0) != rhs2.get(k_, 0))
        ctrlC_fired[(mu, start)] = (nd2 != 0)
        say("q1-C' mu=%d : NORMS Q_str (%s) in the slice identity: differing entries = %d (control fires: %s)"
            % (mu, start, nd2, nd2 != 0))
        if mu == 0:
            say("q1-H  NORMS Q_str (%s): support = %d, row sum = %s" % (start, len(s_n), l1(s_n, L ** (D - 1))))
            okH &= (len(s_n) == 81)
    if mu == 0:
        prof = {}
        for (s, nu), c in s_lp.items():
            prof.setdefault(s[mu], set()).add(c)
        say("q1-H  Q_str^LP: support = %d, row sum = %s, multiplicity by longitudinal coordinate = %s"
            % (len(s_lp), l1(s_lp, L ** D), {k_: sorted(v_) for k_, v_ in sorted(prof.items())}))
        okH &= (len(s_lp) == 135 and [sorted(prof[k_]) for k_ in sorted(prof)] == [[1], [2], [3], [2], [1]])
    # root covariance
    cX, cY = root(X0), add(root(X0), e(mu, L))
    target = lam(cY) - lam(cX)
    got = apply_row(q, NS, dlam)
    got_s = apply_row(s_lp, L ** D, dlam)
    say("q1-D  mu=%d : Q_root(d lam) = %s ; lam(c_Y)-lam(c_X) = %s ; Q_str^LP(d lam) = %s" % (mu, got, target, got_s))
    okD &= (got == target)
    ctrlD_fired[mu] = (got_s != target)

results['q1-A'] = okA; results['q1-B'] = okB; results['q1-C'] = okC; results['q1-D'] = okD; results['q1-H'] = okH
say("q1-C' control fired in %d of %d (mu, realisation) cases" % (sum(ctrlC_fired.values()), len(ctrlC_fired)))
say("q1-D' control fired in %d of 4 directions: %s" % (sum(ctrlD_fired.values()), ctrlD_fired))

# ---------------- composite j = 2
def composite2(mu, rowfun, den):
    lvl1 = rowfun(X0, mu)                      # entries over level-1 links (same pattern in level-1 units)
    pats = {nu: rowfun(X0, nu) for nu in range(D)}
    acc = {}
    for (s1, nu), c1 in lvl1.items():
        # level-1 link (s1, nu) has level-0 row = pattern_nu translated by L*s1
        sh = tuple(L * x for x in s1)
        for (s0, nu0), c0 in pats[nu].items():
            lk = (add(s0, sh), nu0); acc[lk] = acc.get(lk, 0) + c1 * c0
    acc = clean(acc)
    return acc, den * den

okE = True
for mu in (0, 3):
    c2, den2 = composite2(mu, qroot_row, NS)
    v2 = l1(c2, den2)
    say("q1-E  mu=%d : sum_b |Q^(2)(c,b)| = %s (= %.6f), support = %d" % (mu, v2, float(v2), len(c2)))
    okE &= (v2 == Fr(2021, 81) and len(c2) == 47385)
    s2, dens2 = composite2(mu, qstr_lp_row, L ** D)
    v2s = l1(s2, dens2)
    nonneg = all(v_ > 0 for v_ in s2.values())
    say("q1-E  mu=%d : Q_str^(2) row sum = %s, all entries > 0: %s, support = %d" % (mu, v2s, nonneg, len(s2)))
    okE &= (v2s == 9 and nonneg)
    if mu == 0:
        V2 = v2
results['q1-E'] = okE

# ---------------- NQ-1 domination
V1 = Fr(205, 27)
b1 = L + Fr(D * (L * L - 1), 2 * L) * Fr(L - 1, L - 1)
b2 = L ** 2 + Fr(D * (L * L - 1), 2 * L) * Fr(L ** 2 - 1, L - 1)
q0 = 1 + Fr(D * (L + 1), 2 * L)
say("q1-F  NQ-1 sharp bounds j=1,2: %s, %s ; q0 = %s ; q0*L^j = %s, %s" % (b1, b2, q0, q0 * L, q0 * L * L))
say("q1-F  computed/L^j: j=1 %s (= %.6f), j=2 %s (= %.6f)" % (V1 / L, float(V1 / L), V2 / 9, float(V2 / 9)))
results['q1-F'] = (V1 <= b1 <= q0 * L) and (V2 <= b2 <= q0 * 9) and (V1 / L >= Fr(205, 81))
say("SUMMARY " + " ".join("%s=%s" % (k_, "PASS" if v_ else "FAIL") for k_, v_ in sorted(results.items())))
