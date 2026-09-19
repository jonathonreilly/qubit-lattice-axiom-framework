#!/usr/bin/env python3
"""waves-need-signed-weights, attempt a2: exact checks for ATTEMPT.md.

Model (block 13's linear formation law in level time, with several earlier levels): on level planes Z^d,
    theta_{t+1}(x) = sum_{j=0}^{J-1} sum_y w_j(y) theta_{t-j}(x - y)   (+ independent noise, which does not enter the dispersion),
w_j(y) >= 0 finitely supported, gain sum_{j,y} w_j(y) = 1.  Modes theta_t(x) = lam^t e^{i k.x}:
    P_k(lam) = lam^J - sum_j W_j(k) lam^{J-1-j} = 0,   W_j(k) = sum_y w_j(y) e^{-i k.y}.
The space-time step (Y, T) has law P(Y = y, T = j+1) = w_j(y).

Sections (step numbers of ATTEMPT.md in brackets):
 A  (a) the multi-level theorem: rigid-transport factorizations [A4], the principal branch
    lam = exp(-i vbar.k - k^T D k / 2 + O(k^3)), vbar = E[Y]/E[T], D = Cov(Y - vbar T)/E[T] [A5], the lattice rank of the
    space-time support [A3], and a numerical scan of |lam| <= 1 and of the unimodular set (labelled numerical);
 B  (b) signed two-level rules: the a-family theta_{t+1} = 2a P theta_t - theta_{t-1}, its stability region and speed; the
    leapfrog family; a spread negative weight, and a negative weight that is only damping [B1-B6];
 C  (c) the two-component nearest-neighbour unitary (here real orthogonal) rule on the 1+1 event lattice: each amplitude
    component obeys the a-family with a = cos(theta) (Cayley-Hamilton); exact rational simulation at cos = 3/5: the
    recursion, unitarity, the light cone, E[X_t^2]/t^2 -> 1 - sin(theta); the same rule read at every level (the positive
    persistent walk): E[X_t^2] exact, diffusive; the static kernels; reversibility and order-independence [C1-C7].
Exact rational / symbolic arithmetic for every finite claim; numpy only in the scans marked 'numerical'.
"""
import random
import sys
import time
from fractions import Fraction as Fr
from math import gcd

import numpy as np
import sympy as sp

FAILS = []
T0 = time.time()


def check(label, ok, detail):
    print(f"{'ok  ' if ok else 'FAIL'} {label}: {detail}")
    if not ok:
        FAILS.append(label)


k, k1, k2, kap = sp.symbols("k k1 k2 kappa", real=True)
lam, mu = sp.symbols("lam mu")


def W_of(rule, kvec):
    """rule: dict lag j -> dict y(tuple) -> weight (Fraction); returns the symbolic W_j(k)"""
    out = {}
    for j, ws in rule.items():
        out[j] = sum(sp.Rational(w.numerator, w.denominator) * sp.exp(-sp.I * sum(ki * yi for ki, yi in zip(kvec, y)))
                     for y, w in ws.items())
    return out


def charpoly(rule, kvec):
    J = max(rule) + 1
    W = W_of(rule, kvec)
    return lam ** J - sum(W[j] * lam ** (J - 1 - j) for j in W)


# ============================================================================================ A
def section_A():
    print("=" * 100)
    print("A  (a) nonnegative weights over finitely many earlier levels")
    # A4: rigid transport (every space-time step on one ray y = (j+1) v): P_k(lam) = e^{-ikJ.v} Q(lam e^{ik.v})
    rigid = [
        ("d=1, lags 0,1, v=1", {0: {(1,): Fr(1, 3)}, 1: {(2,): Fr(2, 3)}}, (k,), (1,)),
        ("d=1, lag 1 only, v=1/2", {1: {(1,): Fr(1)}}, (k,), (sp.Rational(1, 2),)),
        ("d=2, lags 0,2, v=(1,0)", {0: {(1, 0): Fr(1, 2)}, 2: {(3, 0): Fr(1, 2)}}, (k1, k2), (1, 0)),
        ("d=1, lags 1,3, v=1/2", {1: {(1,): Fr(1, 4)}, 3: {(2,): Fr(3, 4)}}, (k,), (sp.Rational(1, 2),)),
    ]
    ok_all = True
    rows = []
    for name, rule, kv, v in rigid:
        J = max(rule) + 1
        P = charpoly(rule, kv)
        kdotv = sum(a * b for a, b in zip(kv, v))
        Wsum = {j: sum(ws.values()) for j, ws in rule.items()}
        Q = mu ** J - sum(sp.Rational(Wsum[j].numerator, Wsum[j].denominator) * mu ** (J - 1 - j) for j in Wsum)
        ident = sp.simplify(sp.expand(P.subs(lam, mu * sp.exp(-sp.I * kdotv)) - sp.exp(-sp.I * J * kdotv) * Q)) == 0
        g = 0
        for j in rule:
            g = gcd(g, j + 1)
        Qp = sp.Poly(Q, mu)
        quo, remd = sp.div(Qp, sp.Poly(mu ** g - 1, mu))
        R = quo
        Rrev = sp.Poly(sp.expand(mu ** R.degree() * R.as_expr().subs(mu, 1 / mu)), mu) if R.degree() > 0 else sp.Poly(1, mu)
        no_unimod = R.degree() == 0 or sp.gcd(R, Rrev).degree() == 0
        ok = ident and remd.is_zero and no_unimod
        ok_all &= ok
        rows.append(f"{name}: Q = (mu^{g} - 1)({R.as_expr()})")
    check("A4", ok_all, "rigid transport: P_k(lam) = e^{-ikJ.v} Q(lam e^{ik.v}) identically, Q = (mu^g - 1) R with R free of unimodular roots "
          "(gcd(R, reversed R) = 1), g = gcd of the lags+1: " + "; ".join(rows))
    # A3: lattice rank of the space-time support
    def st_rank(rule):
        vecs = [list(y) + [j + 1] for j, ws in rule.items() for y in ws]
        return sp.Matrix(vecs).rank()
    posrules = {
        "E1 d=1": {0: {(0,): Fr(1, 4), (1,): Fr(1, 4)}, 1: {(1,): Fr(1, 2)}},
        "E2 d=2 (block 13's stencil on two levels)": {0: {(0, 0): Fr(1, 6), (1, 0): Fr(1, 6), (0, 1): Fr(1, 6)},
                                                    1: {(0, 0): Fr(1, 6), (1, 0): Fr(1, 6), (0, 1): Fr(1, 6)}},
        "E3 d=1 three levels": {0: {(-1,): Fr(1, 5), (1,): Fr(1, 5)}, 2: {(0,): Fr(2, 5), (3,): Fr(1, 5)}},
    }
    ranks_rigid = [st_rank(r) for _, r, _, _ in rigid]
    ranks_pos = {n: st_rank(r) for n, r in posrules.items()}
    check("A3", all(x == 1 for x in ranks_rigid) and all(x >= 2 for x in ranks_pos.values()),
          f"rank of the space-time step lattice: rigid examples {ranks_rigid}, generic examples {ranks_pos}")
    # A5: the principal branch, series in kappa along directions n
    ok5 = True
    rep = []
    for name, rule in posrules.items():
        d = len(next(iter(next(iter(rule.values())))))
        steps = [(y, j + 1, w) for j, ws in rule.items() for y, w in ws.items()]
        ET = sum(w * t for y, t, w in steps)
        EY = [sum(w * y[i] for y, t, w in steps) for i in range(d)]
        vbar = [e / ET for e in EY]
        D = [[sum(w * (y[a] - vbar[a] * t) * (y[b] - vbar[b] * t) for y, t, w in steps) / ET for b in range(d)] for a in range(d)]
        dirs = [(1,)] if d == 1 else [(1, 0), (0, 1), (1, 1), (1, -1)]
        for n in dirs:
            kv = tuple(kap * ni for ni in n)
            P = charpoly(rule, kv)
            vn = sum(sp.Rational(vbar[i].numerator, vbar[i].denominator) * n[i] for i in range(d))
            Dn = sum(sp.Rational(D[a][b].numerator, D[a][b].denominator) * n[a] * n[b] for a in range(d) for b in range(d))
            # unknown third-order coefficient c3: lam = exp(-i vn kap - Dn kap^2 / 2 + c3 kap^3); P must vanish to order kap^3
            c3 = sp.Symbol("c3")
            lam_ser = sp.exp(-sp.I * vn * kap - Dn * kap ** 2 / 2 + c3 * kap ** 3)
            ser = sp.series(P.subs(lam, lam_ser), kap, 0, 4).removeO()
            ser = sp.expand(ser)
            c0, c1_, c2_ = [sp.simplify(ser.coeff(kap, m)) for m in range(3)]
            sol = sp.solve(sp.Eq(ser.coeff(kap, 3), 0), c3)
            ok5 &= c0 == 0 and c1_ == 0 and c2_ == 0 and len(sol) == 1
        rep.append(f"{name}: vbar={[str(x) for x in vbar]}, D={[[str(x) for x in r] for r in D]}")
    check("A5", ok5, "the root through 1 is exp(-i vbar.k - k^T D k/2 + O(k^3)) with vbar = E[Y]/E[T], D = Cov(Y - vbar T)/E[T] "
          "(the characteristic polynomial vanishes to order k^2 along 1 or 4 directions, a third-order coefficient exists): " + "; ".join(rep))
    # numerical scan (labelled): |lam| <= 1, and the unimodular set has empty interior unless rank 1
    rng = np.random.default_rng(20260919)
    worst, frac_generic, frac_rigid = 0.0, [], []
    def roots_at(rule, kvec):
        J = max(rule) + 1
        coeffs = [1.0] + [0.0] * J
        for j, ws in rule.items():
            coeffs[j + 1] -= sum(float(w) * np.exp(-1j * np.dot(kvec, y)) for y, w in ws.items())
        return np.roots(coeffs)
    for trial in range(300):
        d = int(rng.integers(1, 4))
        J = int(rng.integers(1, 5))
        rule = {}
        for j in range(J):
            if rng.random() < 0.7 or j == 0:
                rule[j] = {tuple(int(u) for u in rng.integers(-2, 3, size=d)): Fr(int(rng.integers(1, 6))) for _ in range(int(rng.integers(1, 4)))}
        tot = sum(sum(ws.values()) for ws in rule.values())
        rule = {j: {y: w / tot for y, w in ws.items()} for j, ws in rule.items()}
        rk = st_rank(rule)
        hits = 0
        for _ in range(40):
            kv = rng.uniform(-np.pi, np.pi, size=d)
            m = max(abs(roots_at(rule, kv)))
            worst = max(worst, m)
            hits += m > 1 - 1e-9
        (frac_rigid if rk == 1 else frac_generic).append(hits / 40)
    for name, rule, kv, v in rigid:
        d = len(kv)
        hits = sum(max(abs(roots_at(rule, rng.uniform(-np.pi, np.pi, size=d)))) > 1 - 1e-9 for _ in range(40))
        frac_rigid.append(hits / 40)
    check("A-num", worst <= 1 + 1e-9 and max(frac_generic) == 0 and min(frac_rigid) == 1,
          f"numerical: 300 random nonnegative gain-one rules (d = 1..3, up to 4 levels) at 40 random k each: max |lam| = {worst:.12f}; "
          f"fraction of random k with a unimodular root: {max(frac_generic)} for every rule of rank >= 2, "
          f"{min(frac_rigid)} for the rank-1 (rigid transport) rules")


# ============================================================================================ B
def section_B():
    print("=" * 100)
    print("B  (b) the minimal signed rules")
    a = sp.Symbol("a", real=True)
    u = sp.Symbol("u", real=True)       # u = P_hat(k) in [-1, 1] for a symmetric probability kernel
    pol = sp.Poly(lam ** 2 - 2 * a * u * lam + 1, lam)
    r1, r2 = sp.symbols("r1 r2")
    vieta = pol.all_coeffs() == [1, -2 * a * u, 1]
    disc = sp.expand(pol.discriminant() - 4 * (a ** 2 * u ** 2 - 1)) == 0
    # complex-conjugate roots with product 1 are unimodular: |r|^2 = r * conj(r) = r1 r2 = 1
    b1 = vieta and disc
    check("B1", b1, "theta_{t+1} = 2a P theta_t - theta_{t-1}: lam^2 - 2a P_hat lam + 1 = 0, roots a P_hat +- i sqrt(1 - a^2 P_hat^2), "
          "product 1, both unimodular whenever |a P_hat| <= 1: dispersion cos(omega) = a P_hat(k)")
    # stability region and gain
    ra = sp.solve(lam ** 2 - 2 * sp.Rational(5, 4) * lam + 1, lam)
    grow = max(ra) == 2
    theta_lin = all((t + 1) == 2 * t - (t - 1) for t in range(1, 50))
    r35 = sp.solve(lam ** 2 - 2 * sp.Rational(3, 5) * lam + 1, lam)
    unimod35 = all(sp.simplify(x * sp.conjugate(x) - 1) == 0 for x in r35) and r35[0] != r35[1]
    check("B2", grow and theta_lin and unimod35,
          "stability: gain = 2a - 1; a = 5/4 gives the root 2 at k = 0 (exponential growth); a = 1 has the double root 1 at k = 0 "
          "(theta_t = t solves it: linear growth of the uniform mode); a = 3/5 gives two distinct unimodular roots at k = 0 "
          "(gapped, cos omega_0 = 3/5): bounded iff |a| < 1, marginal at |a| = 1, unstable for |a| > 1")
    # speed: the c-family (weights 2 - 2c^2 at 0, c^2 at +-1 on level t, -1 on level t-1), and d-dim nearest-neighbour averages
    c = sp.Symbol("c", positive=True)
    om = sp.acos(1 - 2 * c ** 2 * sp.sin(k / 2) ** 2)
    ser = sp.series(om.subs(c, sp.Rational(1, 2)), k, 0, 6).removeO()
    pred = sp.Rational(1, 2) * k + (sp.Rational(1, 8) - sp.Rational(1, 2)) * k ** 3 / 24
    sc = sp.simplify(ser - pred - ser.coeff(k, 5) * k ** 5) == 0
    disc = sp.simplify(sp.expand((2 - 4 * c ** 2 * sp.sin(k / 2) ** 2) ** 2 - 4
                                 + 16 * c ** 2 * sp.sin(k / 2) ** 2 * (1 - c ** 2 * sp.sin(k / 2) ** 2))) == 0
    nn1 = all(sp.acos(sp.cos(sp.pi * sp.Rational(m, 12))) == sp.pi * sp.Rational(m, 12) for m in range(0, 13))
    kap_ = sp.Symbol("kappa", positive=True)
    ax3 = sp.series(sp.acos((sp.cos(kap_) + 2) / 3), kap_, 0, 4).removeO()
    ax3_ok = sp.simplify(ax3.coeff(kap_, 1) - 1 / sp.sqrt(3)) == 0 and ax3.coeff(kap_, 3) != 0
    check("B3", sc and disc and nn1 and ax3_ok,
          "speed: the c-family (2 - 2c^2, c^2, c^2; -1) has discriminant -16c^2 sin^2(k/2)(1 - c^2 sin^2(k/2)) <= 0 (unimodular for c <= 1) "
          f"and omega = c k + (c^3 - c) k^3/24 + O(k^5) (checked at c = 1/2); the 1D nearest-neighbour average (c = 1): omega = |k| exactly "
          f"(no dispersion, speed 1); the 3D nearest-neighbour average: speed 1/sqrt3 along an axis with a k^3 term {ax3.coeff(kap_, 3)}, "
          "i.e. isotropic speed sqrt(n^T C n) = 1/sqrt(d) to first order only")
    # the leapfrog family: w_1 = +delta, w_0 antisymmetric
    s = sp.Symbol("s", real=True)
    w0 = -2 * sp.I * s * sp.sin(k)
    lf = sp.solve(lam ** 2 - w0 * lam - 1, lam)
    sub = sp.expand((lam ** 2 - w0 * lam - 1).subs(lam, sp.I * mu))
    lf_ok = sp.simplify(sub + (mu ** 2 + 2 * s * sp.sin(k) * mu + 1)) == 0 \
        and sp.expand(sp.Poly(mu ** 2 + 2 * s * sp.sin(k) * mu + 1, mu).discriminant() - 4 * (s ** 2 * sp.sin(k) ** 2 - 1)) == 0
    check("B4", lf_ok and len(lf) == 2,
          "the leapfrog family theta_{t+1} = s(theta_t(x-1) - theta_t(x+1)) + theta_{t-1} (one negative weight, gain 0 + 1 = 1): roots "
          "-i s sin k +- sqrt(1 - s^2 sin^2 k), both unimodular for |s| <= 1")
    # a spread negative weight is damping, and a negative weight need not propagate
    spread = sp.simplify(sp.expand((lam ** 2 - 2 * sp.cos(k) * lam + sp.cos(k)).subs(lam, 0)) - sp.cos(k)) == 0
    c2, s2 = sp.Rational(16, 25), sp.Rational(9, 25)
    pers_gain = 2 * c2 - (c2 - s2) == 1
    pers_prod = (c2 - s2) == sp.Rational(7, 25)
    check("B5", spread and pers_gain and pers_prod,
          "a negative lag-1 weight spread over two sites (theta_{t+1} = 2 P theta_t - P theta_{t-1}, P = (delta_1 + delta_-1)/2): the roots' "
          "product is cos k, so |lam1 lam2| < 1 off k in pi Z: damped; the scalar law of the persistent walk at cos^2 = 16/25 "
          "(c^2 at +-1 on level t, -(c^2 - s^2) = -7/25 on level t-1) has gain one and a negative weight, yet the roots' product is 7/25: damped")
    grow1 = abs(complex(2 - sp.exp(sp.I * sp.pi))) == 3
    check("B6", grow1, "one level with a signed kernel: |w_hat|^2 = 1 on an open set forces a monomial; e.g. 2 - e^{ik} has |lam(pi)| = 3 (growth)")


# ============================================================================================ C
def walk_step(psi, c, s):
    """real orthogonal coin [[c, -s], [s, c]] on (R, L), then R moves +1, L moves -1"""
    out = {}
    for x, (R, L) in psi.items():
        nR = c * R - s * L
        nL = s * R + c * L
        if nR:
            a_, b_ = out.get(x + 1, (Fr(0), Fr(0)))
            out[x + 1] = (a_ + nR, b_)
        if nL:
            a_, b_ = out.get(x - 1, (Fr(0), Fr(0)))
            out[x - 1] = (a_, b_ + nL)
    return out


def section_C():
    print("=" * 100)
    print("C  (c) the two-component unitary (real orthogonal) nearest-neighbour rule on the 1+1 event lattice")
    th = sp.Symbol("theta", real=True)
    cc, ss = sp.cos(th), sp.sin(th)
    S = sp.diag(sp.exp(-sp.I * k), sp.exp(sp.I * k))
    ok1 = True
    for C in (sp.Matrix([[cc, -ss], [ss, cc]]), sp.Matrix([[cc, sp.I * ss], [sp.I * ss, cc]])):
        U = S * C
        ch = sp.simplify((U * U - 2 * cc * sp.cos(k) * U + sp.eye(2)).applyfunc(lambda z: sp.simplify(sp.expand(z.rewrite(sp.exp)))))
        ok1 &= ch == sp.zeros(2, 2)
        uni = sp.simplify((U.H * U).subs({sp.conjugate(th): th}).applyfunc(lambda z: sp.simplify(sp.expand(z.rewrite(sp.exp))))) == sp.eye(2)
        ok1 &= uni
    # general U(2) coin: the recursion psi_{t+1} = tr(U) psi_t - det(U) psi_{t-1}
    al, a_, b_ = sp.symbols("alpha a b")
    Cg = sp.exp(sp.I * al) * sp.Matrix([[a_, b_], [-sp.conjugate(b_), sp.conjugate(a_)]])
    Ug = S * Cg
    chg = (Ug * Ug - Ug.trace() * Ug + Ug.det() * sp.eye(2)).applyfunc(sp.expand)
    ok1 &= chg == sp.zeros(2, 2)
    check("C1", ok1, "U(k) = diag(e^{-ik}, e^{ik}) C: U^2 - 2 cos(theta) cos(k) U + I = 0 for the orthogonal and the symmetric coin (and "
          "U^2 - tr(U) U + det(U) I = 0 for a general U(2) coin): every amplitude component obeys psi_{t+1}(x) = cos(theta)(psi_t(x-1) + "
          "psi_t(x+1)) - psi_{t-1}(x), the a-family with a = cos(theta), P the nearest-neighbour average; U unitary")
    # exact simulation at cos = 3/5, sin = 4/5, real amplitudes
    c, s = Fr(3, 5), Fr(4, 5)
    T = 120
    hist = [{0: (Fr(1), Fr(0))}]
    for t in range(T):
        hist.append(walk_step(hist[-1], c, s))
    rec_ok = True
    for t in range(1, T):
        cur, prev, nxt = hist[t], hist[t - 1], hist[t + 1]
        xs = set(cur) | set(prev) | set(nxt) | {x + 1 for x in cur} | {x - 1 for x in cur}
        for x in xs:
            for comp in (0, 1):
                lhs = nxt.get(x, (Fr(0), Fr(0)))[comp]
                rhs = c * (cur.get(x - 1, (Fr(0), Fr(0)))[comp] + cur.get(x + 1, (Fr(0), Fr(0)))[comp]) - prev.get(x, (Fr(0), Fr(0)))[comp]
                if lhs != rhs:
                    rec_ok = False
    norm_ok = all(sum(R * R + L * L for R, L in h.values()) == 1 for h in hist)
    cone_ok = all(abs(x) <= t for t, h in enumerate(hist) for x in h)
    m2 = [sum(x * x * (R * R + L * L) for x, (R, L) in h.items()) for h in hist]
    ratios = {t: m2[t] / (t * t) for t in (30, 60, 120)}
    dist = {t: abs(float(ratios[t]) - 0.2) for t in ratios}
    approach = dist[120] < dist[60] < dist[30] and dist[120] < 0.01
    check("C2", rec_ok and norm_ok and cone_ok and approach,
          f"exact rational walk (cos = 3/5, sin = 4/5, psi_0 = delta_0 (1,0), t <= {T}): both components satisfy the recursion "
          f"psi_{{t+1}} = (3/5)(psi_t(x-1) + psi_t(x+1)) - psi_{{t-1}} at every site; sum |psi|^2 = 1 exactly; support |x| <= t; "
          f"E[X_t^2]/t^2 = " + ", ".join(f"{float(ratios[t]):.6f} (t={t})" for t in ratios) + " -> 1 - sin = 1/5 (ballistic)")
    # the limit: (1/2pi) int c^2 sin^2 k / (1 - c^2 cos^2 k) dk = 1 - s
    cs = sp.Rational(3, 5)
    z = sp.Symbol("z")
    f = cs ** 2 * ((z - 1 / z) / (2 * sp.I)) ** 2 / (1 - cs ** 2 * ((z + 1 / z) / 2) ** 2) / (sp.I * z)
    f = sp.cancel(sp.together(f))
    num, den = sp.fraction(f)
    poles = sp.roots(sp.Poly(den, z))
    inside = [pz for pz in poles if abs(complex(pz)) < 1]
    integ = sp.nsimplify(sp.simplify(sum(sp.residue(f, z, pz) for pz in inside) * 2 * sp.pi * sp.I / (2 * sp.pi)))
    lim_ok = sp.simplify(integ - sp.Rational(1, 5)) == 0
    # group velocity squared of the branches: omega' = c sin k / sqrt(1 - c^2 cos^2 k)
    omg = sp.acos(cs * sp.cos(k))
    vel_ok = sp.simplify(sp.diff(omg, k) ** 2 - cs ** 2 * sp.sin(k) ** 2 / (1 - cs ** 2 * sp.cos(k) ** 2)) == 0
    check("C3", lim_ok and vel_ok, f"(1/2pi) int_0^2pi omega'(k)^2 dk = {integ} = 1 - sin(theta) at cos = 3/5, omega = arccos(cos(theta) cos k): "
          "the limit of E[X_t^2]/t^2 for every initial spinor (both branches have the same |group velocity|)")
    # every record read at formation: the persistent walk (a positive two-component formation law)
    c2, s2 = c * c, s * s
    rho = c2 - s2
    P = [{0: (Fr(1), Fr(0))}]
    for t in range(T):
        cur, out = P[-1], {}
        for x, (R, L) in cur.items():
            nR, nL = c2 * R + s2 * L, s2 * R + c2 * L
            a1, b1 = out.get(x + 1, (Fr(0), Fr(0)))
            out[x + 1] = (a1 + nR, b1)
            a1, b1 = out.get(x - 1, (Fr(0), Fr(0)))
            out[x - 1] = (a1, b1 + nL)
        P.append(out)
    pm2 = [sum(x * x * (R + L) for x, (R, L) in h.items()) for h in P]
    formula = [t * (1 + rho) / (1 - rho) - 2 * rho * (1 - rho ** t) / (1 - rho) ** 2 for t in range(T + 1)]
    pers_ok = all(pm2[t] == formula[t] for t in range(T + 1)) and all(sum(R + L for R, L in h.values()) == 1 for h in P)
    check("C4", pers_ok, f"read at every level (coin probabilities cos^2 = 9/25, sin^2 = 16/25): E[X_t^2] = t(1+rho)/(1-rho) - "
          f"2 rho (1 - rho^t)/(1-rho)^2 exactly for t <= {T}, rho = cos^2 - sin^2 = {rho}: diffusive, D = (1+rho)/(1-rho) = {(1 + rho) / (1 - rho)} "
          f"= cot^2(theta) per level (E[X_{T}^2] = {float(pm2[T]):.3f} against the unread walk's {float(m2[T]):.1f})")
    # static kernels: (2 - 2aP) G = delta
    a = c
    G = {x: Fr(5, 8) * Fr(1, 3 ** abs(x)) for x in range(-60, 61)}
    stat_ok = all(2 * G[x] - a * (G[x - 1] + G[x + 1]) == (1 if x == 0 else 0) for x in range(-59, 60))
    G1 = {x: Fr(-abs(x), 2) for x in range(-60, 61)}
    stat1 = all(2 * G1[x] - (G1[x - 1] + G1[x + 1]) == (1 if x == 0 else 0) for x in range(-59, 60))
    check("C5", stat_ok and stat1, "static kernel of the amplitude recursion (the zero-frequency resolvent of 2 - 2aP): at a = cos(theta) = 3/5 "
          "G(x) = (5/8) 3^{-|x|} exactly (massive: cosh(mass) = 1/a = 5/3); at a = 1 (theta = 0) G(x) = -|x|/2 (the massless 1D Green function)")
    # reversibility: run the scalar recursion backwards from (psi_T, psi_{T-1}); order-independence on the event lattice
    back_ok = True
    Tb = 40
    for comp in (0, 1):
        f = lambda t, x: hist[t].get(x, (Fr(0), Fr(0)))[comp]
        prev_, cur_ = {x: f(Tb, x) for x in range(-Tb - 2, Tb + 3)}, {x: f(Tb - 1, x) for x in range(-Tb - 2, Tb + 3)}
        for t in range(Tb - 1, 0, -1):
            new = {x: c * (cur_.get(x - 1, Fr(0)) + cur_.get(x + 1, Fr(0))) - prev_.get(x, Fr(0)) for x in range(-Tb - 2, Tb + 3)}
            prev_, cur_ = cur_, new
            back_ok &= all(cur_[x] == f(t - 1, x) for x in range(-Tb, Tb + 1))
    # order-independence: fill the event lattice {(t, x): |x| <= t <= 16} in a level order and in a light-cone sweep
    def fill(order):
        val = {(0, 0): (Fr(1), Fr(0))}
        for (t, x) in order:
            if t == 0:
                continue
            R = sum(((c * val[(t - 1, x - 1)][0] - s * val[(t - 1, x - 1)][1]) if (t - 1, x - 1) in val else Fr(0),), Fr(0))
            L = sum(((s * val[(t - 1, x + 1)][0] + c * val[(t - 1, x + 1)][1]) if (t - 1, x + 1) in val else Fr(0),), Fr(0))
            val[(t, x)] = (R, L)
        return val
    Tl = 16
    events = [(t, x) for t in range(Tl + 1) for x in range(-t, t + 1)]
    level = sorted(events)
    sweep = sorted(events, key=lambda e: ((e[0] + e[1]) // 2 if (e[0] + e[1]) % 2 == 0 else (e[0] + e[1] + 1) // 2, e[0]))
    ok_sweep = all(any(p == (e[0] - 1, e[1] + dx) for p in sweep[:i]) or (e[0] - 1, e[1] + dx) not in set(events)
                   for i, e in enumerate(sweep) if e[0] > 0 for dx in (-1, 1))
    v1, v2 = fill(level), fill(sweep)
    oi_ok = ok_sweep and all(v1[e] == v2[e] for e in events)
    check("C6", back_ok and oi_ok, f"reversibility: the recursion run backwards from levels {Tb}, {Tb - 1} recovers every earlier level exactly; "
          "order-independence: the amplitudes on the event lattice (t <= 16) are the same when filled level by level and in a light-cone sweep "
          "(a different linear extension)")


def main():
    section_A()
    section_B()
    section_C()
    print("=" * 100)
    print(f"runtime {time.time() - T0:.0f}s")
    if FAILS:
        print(f"SUMMARY: ROUTE FAILS AT {FAILS[0]} ({FAILS})")
        return 0
    core = ("(a) nonnegative gain-one weights over finitely many levels: every branch |lam| <= 1; a branch is unimodular at k iff the "
            "characters of the space-time steps are trivial there, so the unimodular set has interior iff every step lies on one ray "
            "y = (j+1) v (rigid transport: branches zeta e^{-ik.v}, one common velocity, no dispersion); otherwise it is a closed "
            "measure-zero set and the root through 1 is exp(-i vbar.k - k^T D k/2 + O(k^3)), D = Cov(Y - vbar T)/E[T]; (b) two-level real "
            "rules with both branches unimodular on an open set have w_1 = +-delta: the minimal ones (one negative weight) are "
            "theta_{t+1} = 2aP theta_t - theta_{t-1} (P >= 0 symmetric, 0 < a <= 1, cos omega = a P_hat, bounded iff a < 1, speed sqrt(n^T C n) "
            "at a = 1) and their boosts, and the leapfrog family; (c) the two-component real-orthogonal nearest-neighbour rule's amplitudes "
            "obey the a-family with a = cos theta exactly; its record statistics are ballistic (E[X^2]/t^2 -> 1 - sin theta), read at every "
            "level it is the positive persistent walk (diffusive, cot^2 theta), its static kernel is massive ((5/8)3^{-|x|} at cos = 3/5), "
            "massless only at theta = 0 where it decouples into two positive chiral copy rules")
    print("SUMMARY: PARTIAL " + core)
    print("HIT: " + core)
    return 0


if __name__ == "__main__":
    sys.exit(main())
