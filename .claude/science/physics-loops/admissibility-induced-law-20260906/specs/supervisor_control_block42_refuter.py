#!/usr/bin/env python3
"""Block 42 refuting pass: machinery disjoint from the runner's (brute-force enumeration, symbolic differentiation, hill-climbing).

W1  the summed form's gap weights by enumeration of the unformed sites' contents on a path (no matrix powers)
W2  the 2 x 3 window: every arrangement's content-summed weight equals Z; contents across unformed sites are correlated
W3  the derivative of the six-outcome map at the uniform field by symbolic differentiation, for symbolic (p, q, r)
W4  the seven-outcome map: fixed point and the two eigenvalues as identities in symbolic (rho, g, p, q, r)
W5  the mode sum solves the linear field equation at all 216 sites of the 6^3 torus (vector and quadrupole strengths), and at all 27 sites of the 3^3 torus
W6  hill-climbing against the one-factor contraction bound; two trajectories of the full map on a window contract as bounded
W7  the second-order coefficient of the content-blind weight by symbolic expansion
W8  all integer triples up to 40 with 6 l1 = 1 are exactly those with 5p = 7q + 4r; the two massless surfaces meet on q = r, 5p = 11q
Exact arithmetic (Fractions, sympy rationals).
"""
import random
import sys
from fractions import Fraction as F
from itertools import combinations, product

import sympy as sp

AX = [(0, 0, 1), (0, 0, -1), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0)]
fails = 0


def report(tag, ok, msg):
    global fails
    fails += 0 if ok else 1
    print(("PASS" if ok else "FAIL") + f": {tag} {msg}")


def om(p, q, r):
    return [[p if a == b else q if tuple(-t for t in AX[a]) == AX[b] else r for b in range(6)] for a in range(6)]


def w1():
    ok = True
    for (p, q, r) in ((12, 1, 2), (3, 1, 2)):
        w = om(p, q, r)
        t = p + q + 4 * r
        l1, l2 = F(p - q, t), F(p + q - 2 * r, t)
        for n in (1, 2, 3, 4):
            vals = {}
            for b in (0, 1, 2):
                tot = 0
                for mid in product(range(6), repeat=n - 1):
                    chain = (0,) + mid + (b,)
                    pr = 1
                    for i in range(n):
                        pr *= w[chain[i]][chain[i + 1]]
                    tot += pr
                vals[b] = F(6 * tot, t ** n)
            ok = ok and vals[0] == 1 + 3 * l1 ** n + 2 * l2 ** n and vals[1] == 1 - 3 * l1 ** n + 2 * l2 ** n and vals[2] == 1 - l2 ** n
            ok = ok and vals[0] + vals[1] + 4 * vals[2] == 6
    report("W1", ok, "gap weights at n = 1..4 by enumeration of the unformed contents on a path, (12,1,2) and (3,1,2): the three formulas and the content average 1")


def w2():
    cols, rows = 3, 2
    idx = {(i, j): i * cols + j for i in range(rows) for j in range(cols)}
    bonds = [(idx[i, j], idx[i, j + 1]) for i in range(rows) for j in range(cols - 1)] + [(idx[0, j], idx[1, j]) for j in range(cols)]
    w = om(3, 1, 2)
    weights = {}
    for cfg in product(range(6), repeat=6):
        pr = 1
        for (i, j) in bonds:
            pr *= w[cfg[i]][cfg[j]]
        weights[cfg] = pr
    z_all = sum(weights.values())
    ok = True
    for k in range(7):
        for eta in combinations(range(6), k):
            # summing the weight over the contents of eta and of the rest is the same total for every eta: check via marginals
            marg = {}
            for cfg, pr in weights.items():
                key = tuple(cfg[i] for i in eta)
                marg[key] = marg.get(key, 0) + pr
            ok = ok and sum(marg.values()) == z_all
    marg = {}
    for cfg, pr in weights.items():
        key = (cfg[idx[0, 0]], cfg[idx[0, 2]])
        marg[key] = marg.get(key, 0) + pr
    corr = F(marg[0, 0], z_all) - F(1, 36)
    report("W2", ok and corr > 0, f"the 2 x 3 window at (3,1,2): all 64 arrangements weigh Z once contents are summed; two records at the ends of a row, every other site unformed, agree more often than chance (excess {corr})")


def w3():
    p, q, r = sp.symbols("p q r", positive=True)
    w = sp.Matrix(om(p, q, r))
    t = p + q + 4 * r
    pis = [[sp.Symbol(f"pi_{y}_{b}") for b in range(6)] for y in range(6)]
    n = [sp.prod([sum(w[s, b] * pis[y][b] for b in range(6)) for y in range(6)]) for s in range(6)]
    tot = sum(n)
    uniform = {pis[y][b]: sp.Rational(1, 6) for y in range(6) for b in range(6)}
    ok = True
    for s in range(6):
        for b in range(6):
            d = sp.simplify(sp.diff(n[s] / tot, pis[0][b]).subs(uniform) - (w[s, b] / t - sp.Rational(1, 6)))
            ok = ok and d == 0
    report("W3", ok, "symbolic differentiation of the six-outcome map at the uniform field, symbolic (p, q, r): the derivative is K_1(s,b) - 1/6 in all 36 entries")


def w4():
    p, q, r, rho, g = sp.symbols("p q r rho g", positive=True)
    w = sp.Matrix(om(p, q, r))
    t = p + q + 4 * r
    c = g * 6 / t
    z = rho / (6 * (1 - rho) * (1 + rho * (g - 1)) ** 6)
    pis = [[sp.Symbol(f"pi_{y}_{b}") for b in range(7)] for y in range(6)]
    n = [z * sp.prod([pis[y][6] + c * sum(w[s, b] * pis[y][b] for b in range(6)) for y in range(6)]) for s in range(6)]
    n.append(sp.prod([sum(pis[y]) for y in range(6)]))
    tot = sum(n)
    uni = {pis[y][b]: (rho / 6 if b < 6 else 1 - rho) for y in range(6) for b in range(7)}
    fixed = all(sp.simplify((n[s] / tot).subs(uni) - (rho / 6 if s < 6 else 1 - rho)) == 0 for s in range(7))
    jac = sp.Matrix(7, 7, lambda s, b: sp.diff(n[s] / tot, pis[0][b]).subs(uni))
    u_s = sp.Matrix([sp.Rational(1, 6)] * 6 + [-1])
    u_v = sp.Matrix([sp.Rational(AX[a][2], 2) for a in range(6)] + [0])
    lam_s = rho * (1 - rho) * (g - 1) / (1 + rho * (g - 1))
    lam_v = rho * g * ((p - q) / t) / (1 + rho * (g - 1))
    ok_s = all(sp.simplify(v) == 0 for v in (jac * u_s - lam_s * u_s))
    ok_v = all(sp.simplify(v) == 0 for v in (jac * u_v - lam_v * u_v))
    report("W4", fixed and ok_s and ok_v, "the seven-outcome map, symbolic in (rho, g, p, q, r): the uniform field is a fixed point at the stated z, and the scalar and vector eigenvalues are rho(1-rho)(g-1)/(1+rho(g-1)) and rho g l1/(1+rho(g-1)) identically; the scalar one vanishes identically at g = 1: " + str(sp.simplify(lam_s.subs(g, 1)) == 0))


def w5():
    ok = True
    for (L, cosv) in ((6, (F(1), F(1, 2), F(-1, 2), F(-1), F(-1, 2), F(1, 2))), (3, (F(1), F(-1, 2), F(-1, 2)))):
        sites = list(product(range(L), repeat=3))
        for lam in (F(3, 23), F(1, 12), F(-1, 9)):
            denom = {k: 1 - lam * 2 * sum(cosv[c] for c in k) for k in sites}
            val = {x: sum(cosv[sum(k[i] * x[i] for i in range(3)) % L] / denom[k] for k in sites) / L ** 3 for x in sites}
            for x in sites:
                nb = sum(val[tuple((x[j] + (d if j == i else 0)) % L for j in range(3))] for i in range(3) for d in (1, -1))
                ok = ok and val[x] - lam * nb == (1 if x == (0, 0, 0) else 0)
    report("W5", ok, "the mode sum of 1/(1 - l (6 - E(k))) solves v_x - l (sum of the six neighbours) = point source at all 216 sites of the 6^3 torus and all 27 of the 3^3 torus, for l = 3/23, 1/12 and -1/9")


def ratio(x, y):
    g = [a / b for a, b in zip(x, y)]
    return max(g) / min(g)


def kappa(w):
    vals = []
    for s in range(6):
        for t in range(6):
            if s != t:
                g = [F(w[s][b], w[t][b]) for b in range(6)]
                vals.append(min(g) / max(g))
    return min(vals)


def w6():
    rng = random.Random(2)
    ok = True
    best_all = F(0)
    for (p, q, r) in ((3, 1, 2), (5, 2, 4), (21, 20, 20)):
        w = om(p, q, r)
        kp = kappa(w)

        def score(x, y):
            r_in = ratio(x, y)
            if r_in < 2:
                return F(0)                                # the trivial equality at x proportional to y is excluded
            r_out = ratio([sum(w[s][b] * x[b] for b in range(6)) for s in range(6)], [sum(w[s][b] * y[b] for b in range(6)) for s in range(6)])
            return r_out / (r_in / ((1 - kp) + kp * r_in))

        for start in range(6):
            x = [F(rng.randint(1, 50)) for _ in range(6)]
            y = [F(rng.randint(1, 50)) for _ in range(6)]
            cur = score(x, y)
            for _ in range(400):
                xx, yy = list(x), list(y)
                tgt = xx if rng.random() < 0.5 else yy
                i = rng.randrange(6)
                tgt[i] = tgt[i] * F(rng.choice((1, 2, 3, 5, 10, 100)), rng.choice((1, 2, 3, 5, 10, 100)))
                sc = score(xx, yy)
                if sc >= cur:
                    x, y, cur = xx, yy, sc
            ok = ok and cur <= 1
            best_all = max(best_all, cur)
    # two trajectories of the full map on the 2 x 2 x 2 window (8 sites, degree 3) with one record: the sup ratio obeys the product bound at every step
    w = om(21, 20, 20)
    kp = kappa(w)
    nbrs = {v: [v ^ 1, v ^ 2, v ^ 4] for v in range(8)}
    rec = {0: 2}
    def step(field):
        new = {}
        for x in range(1, 8):
            n = []
            for s in range(6):
                t = F(1)
                for yv in nbrs[x]:
                    t *= F(w[s][rec[yv]]) if yv in rec else sum(w[s][b] * field[yv][b] for b in range(6))
                n.append(t)
            tot = sum(n)
            new[x] = [v / tot for v in n]
        return new
    def rnd():
        v = [F(rng.randint(1, 40)) for _ in range(6)]
        return [a / sum(v) for a in v]
    fa = {x: rnd() for x in range(1, 8)}
    fb = {x: rnd() for x in range(1, 8)}
    for _ in range(3):
        na, nb_ = step(fa), step(fb)
        for x in range(1, 8):
            bound = F(1)
            for yv in nbrs[x]:
                if yv not in rec:
                    r_in = ratio(fa[yv], fb[yv])
                    bound *= r_in / ((1 - kp) + kp * r_in)
            ok = ok and ratio(na[x], nb_[x]) <= bound
        fa, fb = na, nb_
    report("W6", ok, f"hill-climbing from 18 starts against the one-factor bound, pairs with ratio at least 2, never exceeds it (best {best_all.numerator * 10 ** 6 // best_all.denominator}/10^6 of the bound); two trajectories of the full map on the cube window with a record obey the product bound at every site for three steps")


def w7():
    t_, p, q, r = sp.symbols("t p q r", positive=True)
    ms = [[sp.Symbol(f"m_{y}_{i}") for i in range(3)] for y in range(6)]
    l1 = (p - q) / (p + q + 4 * r)
    expr = sp.Rational(1, 6) * sum(sp.prod([1 + 3 * l1 * t_ * sum(ms[y][i] * AX[s][i] for i in range(3)) for y in range(6)]) for s in range(6))
    poly = sp.Poly(sp.expand(expr), t_)
    c0, c1, c2 = poly.coeff_monomial(1), poly.coeff_monomial(t_), poly.coeff_monomial(t_ ** 2)
    want = 3 * l1 ** 2 * sum(sum(ms[i][d] * ms[j][d] for d in range(3)) for i in range(6) for j in range(i + 1, 6))
    report("W7", c0 == 1 and c1 == 0 and sp.simplify(c2 - want) == 0, "symbolic expansion of the content-averaged weight in the leans: constant 1, no first-order term, second-order term 3 l1^2 sum_{y<y'} m_y.m_y'")


def w8():
    hits = [(p, q, r) for p in range(1, 41) for q in range(1, 41) for r in range(1, 41) if 6 * F(p - q, p + q + 4 * r) == 1]
    ok = all(5 * p == 7 * q + 4 * r for (p, q, r) in hits) and len(hits) == sum(1 for p in range(1, 41) for q in range(1, 41) for r in range(1, 41) if 5 * p == 7 * q + 4 * r)
    both = [(p, q, r) for (p, q, r) in hits if 6 * F(p + q - 2 * r, p + q + 4 * r) == 1]
    ok = ok and all(q == r and 5 * p == 11 * q for (p, q, r) in both) and (11, 5, 5) in both and (3, 1, 2) in hits
    report("W8", ok, f"integer triples up to 40: 6 l1 = 1 exactly on 5p = 7q + 4r ({len(hits)} triples, (3,1,2) the smallest); both channels lose their mass term together exactly on q = r, 5p = 11q ({len(both)} triples, (11,5,5) the smallest)")


if __name__ == "__main__":
    for fn in (w1, w2, w5, w6, w8, w7, w3, w4):
        fn()
    print(f"REFUTER TOTAL: FAIL={fails}")
    sys.exit(1 if fails else 0)
