#!/usr/bin/env python3
"""b4w55_1 -- CEN1 exact centring cancellation, its position-convention dependence, the exact commutator
representation, and three counting constants.  Criteria: checks/b4w55_1_criteria.md (written first).
Exact rational arithmetic only (fractions.Fraction); no floats in any verdict."""
from fractions import Fraction as Fr
import itertools, random

L = 3
TC = 4
HALF = (L - 1) // 2


def build(d, shift_axis=None):
    """Linearised root map Q (one step, level l -> l+1) on the periodic level-l lattice of side L*TC.
    Returns W[c][a] (exact weights) and DEL[c][a] = m_a - m_c (centred convention, unwrapped)."""
    n = L * TC
    orders = list(itertools.permutations(range(d)))
    ys = list(itertools.product(range(-HALF, HALF + 1), repeat=d))
    if shift_axis is not None:  # control K1: non-centred contour family
        ys = [tuple(v[i] + (1 if i == shift_axis else 0) for i in range(d)) for v in ys]
    nrm = Fr(1, len(orders) * len(ys))
    W, DEL = {}, {}
    for X in itertools.product(range(TC), repeat=d):
        cX = tuple(L * X[i] + HALF for i in range(d))
        for mu in range(d):
            c = (X, mu)
            mc = tuple(Fr(cX[i]) + (Fr(L, 2) if i == mu else 0) for i in range(d))
            w, disp = {}, {}
            for sig in orders:
                for v in ys:
                    steps, p = [], list(cX)
                    for ax in sig:
                        k = v[ax]
                        for _ in range(abs(k)):
                            if k > 0:
                                steps.append((tuple(p), ax, 1)); p[ax] += 1
                            else:
                                p[ax] -= 1; steps.append((tuple(p), ax, -1))
                    contour = list(steps)
                    q = list(p)
                    for _ in range(L):
                        contour.append((tuple(q), mu, 1)); q[mu] += 1
                    for (s0, ax, sg) in steps:  # go path translated by L e_mu, traversed backwards
                        contour.append((tuple(s0[i] + (L if i == mu else 0) for i in range(d)), ax, -sg))
                    for (s0, ax, sg) in contour:
                        a = (tuple(s0[i] % n for i in range(d)), ax)
                        ma = tuple(Fr(s0[i]) + (Fr(1, 2) if i == ax else 0) for i in range(d))
                        dl = tuple(ma[i] - mc[i] for i in range(d))
                        if a in disp:
                            assert disp[a] == dl, "torus wrapping ambiguity"
                        disp[a] = dl
                        w[a] = w.get(a, Fr(0)) + sg * nrm
            w = {a: x for a, x in w.items() if x != 0}
            W[c] = w
            DEL[c] = {a: disp[a] for a in w}
    return W, DEL


def p1_failures(d, W, DEL, offset=None):
    """P1: sum_{a: dir(a)=mu'} w_{c,a} (delta_{c,a})_nu = 0 for all c, nu, mu'.  offset: added to every delta (K2)."""
    bad = 0
    for c in W:
        for nu in range(d):
            for mp in range(d):
                s = Fr(0)
                for a, x in W[c].items():
                    if a[1] != mp:
                        continue
                    dl = DEL[c][a][nu] + (offset[nu] if offset else 0)
                    s += x * dl
                if s != 0:
                    bad += 1
    return bad


def l1(v):
    return sum(abs(t) for t in v)


def run_dim(d, log):
    log.append(f"=== d = {d}, L = {L}, TC = {TC} ===")
    W, DEL = build(d)
    ncl = len(W)
    # ---- P1
    f1 = p1_failures(d, W, DEL)
    P1 = (f1 == 0)
    log.append(f"P1 (CEN1 exact, centred): nonzero entries {f1} of {ncl * d * d} -> {'PASS' if P1 else 'FAIL'}")
    # ---- P5 constants
    rowmax = max(sum(abs(x) for x in W[c].values()) for c in W)
    col = {}
    for c in W:
        for a, x in W[c].items():
            col[a] = col.get(a, Fr(0)) + abs(x)
    colmax = max(col.values())
    dmax = max(l1(DEL[c][a]) for c in W for a in W[c])
    rb, cb, db = Fr(L + d * (L - 1)), Fr(2 * d) + Fr(1, L ** (d - 1)), Fr(d * (L - 1), 2) + Fr(L, 2)
    P5 = rowmax <= rb and colmax <= cb and dmax <= db
    log.append(f"P5 row max {rowmax} (<= {rb}), column max {colmax} (<= {cb}), max |delta|_1 {dmax} (<= {db}) -> "
               f"{'PASS' if P5 else 'FAIL'}")
    # ---- P2 (three seeds)
    n = L * TC
    links = [(z, ax) for z in itertools.product(range(n), repeat=d) for ax in range(d)]
    P2 = True
    worst = Fr(0)
    for seed in (11, 23, 37):
        rng = random.Random(seed * 100 + d)
        rr = lambda: Fr(rng.randint(-40, 40), rng.randint(1, 13))
        b = [rr() for _ in range(d)]
        C = [[Fr(0)] * d for _ in range(d)]
        for i in range(d):
            for j in range(i, d):
                C[i][j] = C[j][i] = rr()
        x = {a: rr() for a in links}
        g = Fr(0)
        for (z, ax) in links:
            for nu in range(d):
                z2 = tuple((z[i] + (1 if i == nu else 0)) % n for i in range(d))
                g = max(g, abs(x[(z2, ax)] - x[(z, ax)]))
        xinf = max(abs(t) for t in x.values())
        cmax = max(abs(C[i][j]) for i in range(d) for j in range(d))
        for (X, mu) in W:
            cX = tuple(L * X[i] + HALF for i in range(d))
            mc = tuple(Fr(cX[i]) + (Fr(L, 2) if i == mu else 0) for i in range(d))
            grad = [b[i] + 2 * sum(C[i][j] * mc[j] for j in range(d)) for i in range(d)]
            ginf = max(abs(t) for t in grad)
            comm = Fr(0)
            for a, wt in W[(X, mu)].items():
                dl = DEL[(X, mu)][a]
                dpsi = sum(grad[i] * dl[i] for i in range(d)) + sum(C[i][j] * dl[i] * dl[j] for i in range(d) for j in range(d))
                comm += wt * dpsi * x[a]
            same = {}
            for a in W[(X, mu)]:
                same.setdefault(a[1], []).append(DEL[(X, mu)][a])
            DN = max(l1(tuple(p[i] - q[i] for i in range(d))) for lst in same.values() for p in lst for q in lst)
            bound = sum(abs(wt) * (ginf * l1(DEL[(X, mu)][a]) * DN * g + cmax * l1(DEL[(X, mu)][a]) ** 2 * xinf)
                        for a, wt in W[(X, mu)].items())
            if abs(comm) > bound:
                P2 = False
            if bound != 0:
                worst = max(worst, abs(comm) / bound)
    log.append(f"P2 (Taylor bound, 3 seeds): {'PASS' if P2 else 'FAIL'} (largest |comm|/bound = {float(worst):.4f}, informational)")
    # ---- P4 (corner convention: uncancelled term)
    rng = random.Random(500 + d)
    bvec = [Fr(rng.randint(1, 9), rng.randint(1, 5)) for _ in range(d)]  # b.1 > 0
    xbar = [Fr(rng.randint(1, 9), rng.randint(1, 5)) for _ in range(d)]  # all nonzero
    P4 = True
    for (X, mu) in W:
        val = Fr(0)
        for a, wt in W[(X, mu)].items():
            dlK = tuple(DEL[(X, mu)][a][i] + HALF for i in range(d))  # m_a - m_c^K
            val += wt * sum(bvec[i] * dlK[i] for i in range(d)) * xbar[a[1]]
        pred = sum(bvec) * HALF * L * xbar[mu]
        if val != pred or val == 0:
            P4 = False
    log.append(f"P4 (corner convention leaves (b.((L-1)/2)1) L xbar_mu, nonzero): {'PASS' if P4 else 'FAIL'}")
    # ---- P3 (exact commutator representation, any convention) with control K3
    plaq = [(z, m1, m2) for z in itertools.product(range(n), repeat=d) for m1 in range(d) for m2 in range(m1 + 1, d)]

    def bnd(pl):
        z, m1, m2 = pl
        e = lambda zz, ax: tuple((zz[i] + (1 if i == ax else 0)) % n for i in range(d))
        return [((z, m1), 1), ((e(z, m1), m2), 1), ((e(z, m2), m1), -1), ((z, m2), -1)]

    B = {pl: bnd(pl) for pl in plaq}
    inc = {}
    for pl in plaq:
        for (a, s) in B[pl]:
            inc.setdefault(a, []).append((pl, s))
    cls = list(W.keys())
    P3, K3 = True, True
    for seed in (11, 23, 37):
        rng = random.Random(seed * 7 + d)
        rr = lambda: Fr(rng.randint(-30, 30), rng.randint(1, 11))
        kap = Fr(rng.randint(1, 9), rng.randint(1, 4))
        ul = {a: rr() for a in links}; uh = {c: rr() for c in cls}
        xl = {a: rr() for a in links}; xh = {c: rr() for c in cls}
        pa = {a: rr() for a in links}; pc = {c: rr() for c in cls}; pp = {pl: rr() for pl in plaq}

        def dform(v, pl):
            return sum(s * v[a] for (a, s) in B[pl])

        def resid(vl, vh, c):
            return sum(wt * vl[a] for a, wt in W[c].items()) - vh[c]

        def energy(vl, vh, yl, yh):
            e1 = sum(dform(vl, pl) * dform(yl, pl) for pl in plaq)
            e2 = kap * sum(resid(vl, vh, c) * resid(yl, yh, c) for c in cls)
            return e1 + e2

        psu_l = {a: pa[a] * ul[a] for a in links}; psu_h = {c: pc[c] * uh[c] for c in cls}
        psx_l = {a: pa[a] * xl[a] for a in links}; psx_h = {c: pc[c] * xh[c] for c in cls}
        lhs = energy(psu_l, psu_h, xl, xh) - energy(ul, uh, psx_l, psx_h)
        G = {pl: sum(s * (pa[a] - pp[pl]) * ul[a] for (a, s) in B[pl]) for pl in plaq}
        du = {pl: dform(ul, pl) for pl in plaq}
        jW = {a: -sum(s * (pa[a] - pp[pl]) * du[pl] for (pl, s) in inc.get(a, [])) for a in links}
        ru = {c: resid(ul, uh, c) for c in cls}
        rx = {c: resid(xl, xh, c) for c in cls}
        sS = {c: kap * sum(wt * (pa[a] - pc[c]) * ul[a] for a, wt in W[c].items()) for c in cls}
        jS = {a: Fr(0) for a in links}
        for c in cls:
            for a, wt in W[c].items():
                jS[a] -= kap * wt * (pa[a] - pc[c]) * ru[c]
        part = (sum(G[pl] * dform(xl, pl) for pl in plaq) + sum(jW[a] * xl[a] for a in links)
                + sum(sS[c] * rx[c] for c in cls))
        rhs = part + sum(jS[a] * xl[a] for a in links)
        if lhs != rhs:
            P3 = False
        if lhs == part:  # control K3 must make the identity fail
            K3 = False
    log.append(f"P3 (exact commutator representation, 3 seeds): {'PASS' if P3 else 'FAIL'}")
    # ---- controls
    Wk, Dk = build(d, shift_axis=0)
    K1 = p1_failures(d, Wk, Dk) > 0
    K2 = p1_failures(d, W, DEL, offset=[Fr(HALF)] * d) > 0
    c0 = next(iter(W)); a0 = next(iter(W[c0]))
    Wp = {c: dict(W[c]) for c in W}
    Wp[c0][a0] += Fr(1, 997)
    K4 = p1_failures(d, Wp, DEL) > 0
    log.append(f"K1 (no centring) fires: {K1}; K2 (corner positions in P1) fires: {K2}; "
               f"K3 (drop j_S) fires: {K3}; K4 (one weight +1/997) fires: {K4}")
    ok = P1 and P2 and P3 and P4 and P5 and K1 and K2 and K3 and K4
    log.append(f"d = {d}: {'PASS' if ok else 'FAIL'}")
    return ok


if __name__ == "__main__":
    log = []
    res = [run_dim(d, log) for d in (2, 3)]
    log.append("OVERALL: " + ("PASS" if all(res) else "FAIL"))
    print("\n".join(log))
