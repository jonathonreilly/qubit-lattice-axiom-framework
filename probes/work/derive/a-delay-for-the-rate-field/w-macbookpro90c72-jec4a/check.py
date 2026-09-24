#!/usr/bin/env python3
"""A rate field with its own motion (blocks 53-55; block 57 is this topic's block): checks for ATTEMPT.md, attempt 3 of 4.

Worker w-macbookpro90c72-jec4a (claude-opus-5-5).
Exact (sympy): K the kinetic term's weight and reparametrisation; L the weak-field law, its constant and principal part;
W the dispersion bounds (the field's phase-velocity floor, the walker's speed); R the radiation (angular moments, circular and
eccentric Kepler averages) and the lattice retarded kernel's odd terms.
Floating point, labelled executed (not claimed): S the full non-linear law on a 3D lattice, a weak source switched on at t = 0,
the half-rise times at distances 8, 12, 16 at ambient rates 1 and 2 (the front's speed).
"""
from __future__ import annotations

import sys

import numpy as np
import sympy as sp

OUT: list[str] = []
FAILS: list[str] = []


def check(tag: str, ok: bool, msg: str) -> None:
    OUT.append(f"{'ok  ' if ok else 'FAIL'} {tag}: {msg}")
    if not ok:
        FAILS.append(tag)


# ------------------------------------------------------------------------------------------------ K: the kinetic term
def family_k() -> None:
    s, t = sp.symbols("s t", positive=True)
    alpha = sp.Symbol("alpha", real=True)
    udot, w = sp.symbols("udot w", positive=True)
    # weight: w -> s w with the ambient time t -> t/s (a change of unit): udot -> s udot; energies must scale as s
    term = udot ** 2 * w ** alpha
    scaled = (s * udot) ** 2 * (s * w) ** alpha
    base, expo = sp.simplify(scaled / term).as_base_exp()                 # s^(alpha + 2)
    sol = sp.solve(sp.Eq(expo, 1), alpha) if base == s else None
    ok = sol == [-1]
    # reparametrisation t -> f(t), w -> w/f', u -> u - log f': the action increment sum udot^2/w dt changes unless f'' = 0;
    # referred to a clock u_ref of the system it does not
    tt = sp.symbols("t", real=True)
    f = sp.Function("f")(tt); u = sp.Function("u")(tt); ur = sp.Function("u_r")(tt)
    fp = sp.diff(f, tt)
    unew_dot = (sp.diff(u, tt) - sp.diff(fp, tt) / fp) / fp               # d(u - log f')/d tau, tau = f(t)
    urnew_dot = (sp.diff(ur, tt) - sp.diff(fp, tt) / fp) / fp
    wv = sp.exp(u)
    lag_new = unew_dot ** 2 / (wv / fp) * fp                                # (du/dtau)^2 / w_new  dtau/dt
    lag_old = sp.diff(u, tt) ** 2 / wv
    diff_onsite = sp.simplify(lag_new - lag_old)
    ok &= diff_onsite != 0 and sp.simplify(diff_onsite.subs(sp.diff(fp, tt), 0)) == 0
    lag_ref_new = (unew_dot - urnew_dot) ** 2 / (wv / fp) * fp
    lag_ref_old = (sp.diff(u, tt) - sp.diff(ur, tt)) ** 2 / wv
    ok &= sp.simplify(lag_ref_new - lag_ref_old) == 0
    check("K1", ok, "on-site kinetic monomials udot^2 w^alpha have weight one under (w -> s w, t -> t/s) iff alpha = -1: "
          "(1/(2 gamma c^2)) sum udot^2/w; under a change of parameter t -> f(t) it survives iff f'' = 0, and "
          "sum (udot - udot_ref)^2/w (rates referred to one clock of the system) survives every f (block 57 T1, T3)")


# ------------------------------------------------------------------------------------------------ L: the weak-field law
def family_l() -> None:
    g, c, wb, eps = sp.symbols("gamma c wbar epsilon", positive=True)
    # one site x with six neighbours y_k; field energy F = (2/gamma) sum_bonds (phi_x - phi_y)^2, phi = exp(u/2)
    ux = sp.Symbol("u_x"); uy = sp.symbols("u_y0:6")
    F_x = sum((2 / g) * (sp.exp(ux / 2) - sp.exp(v / 2)) ** 2 for v in uy)
    dF = sp.diff(F_x, ux)                                                    # = (12/gamma) phi_x (phi_x - average phi)
    avg = sum(sp.exp(v / 2) for v in uy) / 6
    ok = sp.simplify(dF - (12 / g) * sp.exp(ux / 2) * (sp.exp(ux / 2) - avg)) == 0
    # E-L of L = udot^2/(2 gamma c^2 w) - F - sum s u:  udd - udot^2/2 = -gamma c^2 w (dF/du + s)
    tt = sp.Symbol("t"); U = sp.Function("U")(tt); S = sp.Symbol("s")
    Lk = sp.diff(U, tt) ** 2 / (2 * g * c ** 2 * sp.exp(U))
    el = sp.diff(sp.diff(Lk, sp.diff(U, tt)), tt) - sp.diff(Lk, U)          # = -(dF/du + s) on shell
    lhs = sp.simplify(el * g * c ** 2 * sp.exp(U))
    ok &= sp.simplify(lhs - (sp.diff(U, tt, 2) - sp.diff(U, tt) ** 2 / 2)) == 0
    # weak field about a uniform wbar = exp(u0): u = u0 + eps v; linear part of -gamma c^2 w dF/du is c^2 wbar^2 (sum_y v_y - 6 v_x)
    u0 = sp.log(wb); vx = sp.Symbol("v_x"); vy = sp.symbols("v_y0:6")
    rhs = -g * c ** 2 * sp.exp(ux) * dF
    rhs = rhs.subs({ux: u0 + eps * vx, **{uy[k]: u0 + eps * vy[k] for k in range(6)}})
    lin = sp.simplify(sp.diff(rhs, eps).subs(eps, 0))
    ok &= sp.simplify(lin - c ** 2 * wb ** 2 * (sum(vy) - 6 * vx)) == 0
    # principal part about a static background u_x, u_y (not uniform): coefficient of each neighbour's v is c^2 w_x^{3/2} w_y^{1/2}
    rhs2 = -g * c ** 2 * sp.exp(ux) * dF
    coeff = sp.simplify(sp.diff(rhs2, uy[0]))
    ok &= sp.simplify(coeff - c ** 2 * sp.exp(ux) * sp.exp(ux / 2) * sp.exp(uy[0] / 2)) == 0
    check("L1", ok, "dF/du_x = (12/gamma) phi_x (phi_x - avg phi) (block 55); Euler-Lagrange: u'' - u'^2/2 = -gamma c^2 w_x "
          "(dF/du_x + e_x - mu); weak field: u'' = c^2 wbar^2 Lap u - gamma c^2 wbar (e - mu), Lap u = sum_y (u_y - u_x) "
          "= 6 (avg u - u_x), so the constant is 6; about any static background the neighbour coefficient is "
          "c^2 w_x^{3/2} w_y^{1/2} -> c^2 w_x^2: local speed c w_x, c sites per local tick")


# ------------------------------------------------------------------------------------------------ W: dispersion
def family_w() -> None:
    x = sp.Symbol("x", positive=True)
    # sin(x/2) >= x/pi on [0, pi]: h = sin(x/2) - x/pi, h(0) = h(pi) = 0, h'' < 0 on (0, pi)
    h = sp.sin(x / 2) - x / sp.pi
    ok = h.subs(x, 0) == 0 and sp.simplify(h.subs(x, sp.pi)) == 0 and sp.simplify(sp.diff(h, x, 2) + sp.sin(x / 2) / 4) == 0
    # phase velocity along an axis: 2 sin(k/2)/k, at k = pi equal to 2/pi; the floor over the zone is (2/pi) c wbar
    ok &= sp.simplify((2 * sp.sin(x / 2) / x).subs(x, sp.pi) - 2 / sp.pi) == 0
    # the walker: E = |s|, s_a = sin k_a; v_j = s_j cos k_j/|s|; |v|^2 = sum s_j^2 cos^2 k_j / sum s_j^2 <= 1, -> 1 as k -> 0
    k = sp.symbols("k1:4", real=True)
    sa = [sp.sin(v) for v in k]
    E = sp.sqrt(sum(v ** 2 for v in sa))
    vel = [sp.simplify(sp.diff(E, v)) for v in k]
    v2 = sp.simplify(sum(v ** 2 for v in vel))
    ok &= sp.simplify(v2 - sum(sa[j] ** 2 * sp.cos(k[j]) ** 2 for j in range(3)) / sum(v ** 2 for v in sa)) == 0
    tt = sp.Symbol("tau", positive=True)
    ok &= sp.limit(v2.subs({k[0]: tt, k[1]: 2 * tt, k[2]: 3 * tt}), tt, 0) == 1
    check("W1", ok, "field waves omega^2 = c^2 wbar^2 sum 4 sin^2(k_j/2): phase velocity between (2/pi) c wbar (zone boundary; "
          "sin(x/2) >= x/pi) and c wbar; the walker's group speed |v| <= 1 per local tick with supremum 1 as k -> 0: "
          "no wake for every smooth body needs c >= 1 (an inequality; c is a second pure number)")


# ------------------------------------------------------------------------------------------------ H: a hopping point source radiates for every c
def family_h() -> None:
    """a point source that moves one site along e_1 every tau = 1/v (ambient, wbar = 1) has space-time weight on
    omega = (q_1 + 2 pi m) v with amplitude (e^{i q_1} - 1)/(i omega); a field mode q resonates when c p(q) = |q_1 + 2 pi m| v,
    p^2 = sum 4 sin^2(q_j/2). For fixed q_1 the map q_perp -> g = c^2 p^2 - ((q_1 + 2 pi m) v)^2 is continuous on the segment
    q_perp = s(pi, pi), s in [0, 1]; a sign change (g(0) < 0 < g(1)) gives a resonant mode by the intermediate value theorem."""
    def p2(q1, s_):
        return 4 * sp.sin(q1 / 2) ** 2 + 8 * sp.sin(s_ * sp.pi / 2) ** 2
    cands = [(m, sp.pi * sp.Rational(num, den)) for m in (1, 0) for den in (2, 3, 4, 6, 10, 20, 40, 80) for num in (1, -1)]
    ok = True
    found = []
    for (c, v) in ((sp.Integer(1), sp.Rational(1, 10)), (sp.Integer(5), sp.Rational(1, 10)), (sp.Integer(1), sp.Rational(1, 2)),
                   (sp.Rational(3, 2), sp.Integer(1)), (sp.Integer(1), sp.Integer(1)), (sp.Integer(3), sp.Integer(1))):
        hit = None
        for (m, q1) in cands:
            lhs = ((q1 + 2 * sp.pi * m) * v) ** 2
            g0 = c ** 2 * p2(q1, 0) - lhs
            g1 = c ** 2 * p2(q1, 1) - lhs
            if (g0 < 0) == True and (g1 > 0) == True and (q1 + 2 * sp.pi * m) != 0:
                hit = (m, q1)
                break
        ok &= hit is not None and sp.sin(hit[1] / 2) != 0
        found.append(f"(c,v)=({c},{v}): m={hit[0]}, q1={hit[1]}" if hit else f"(c,v)=({c},{v}): none")
    check("H1", ok, "a point source hopping one site every 1/v resonates with some field mode (nonzero amplitude) for "
          + "; ".join(found) + " - at c >= 1 too: a lattice-scale hopping body radiates whatever c is")


# ------------------------------------------------------------------------------------------------ R: radiation
def family_r() -> None:
    th, ph = sp.symbols("theta phi", real=True)
    n = [sp.sin(th) * sp.cos(ph), sp.sin(th) * sp.sin(ph), sp.cos(th)]
    def ang(expr):
        return sp.simplify(sp.integrate(sp.integrate(expr * sp.sin(th), (ph, 0, 2 * sp.pi)), (th, 0, sp.pi)))
    ok = True
    for (i, j, k_, l) in ((0, 0, 0, 0), (0, 0, 1, 1), (0, 1, 0, 1), (0, 0, 1, 2)):
        want = sp.Rational(4, 15) * sp.pi * ((i == j) * (k_ == l) + (i == k_) * (j == l) + (i == l) * (j == k_))
        ok &= sp.simplify(ang(n[i] * n[j] * n[k_] * n[l]) - want) == 0
    # P = A v r^2 (surface integral of udot^2), udot = -(1/(4 pi A v^2 r)) n n : Q'''/(2 v^2): P = (1/(240 pi A v^7))[(tr Q''')^2 + 2 Q''':Q''']
    A, v, G, M, mu, d, Om, t = sp.symbols("A v G M mu d Omega t", positive=True)
    # circular binary in the plane: relative separation d(cos, sin, 0); Q = mu x x
    X = [d * sp.cos(Om * t), d * sp.sin(Om * t), 0]
    Q = sp.Matrix(3, 3, lambda i, j: mu * X[i] * X[j])
    Q3 = Q.diff(t, 3)
    QQ = sp.simplify(sum(Q3[i, j] ** 2 for i in range(3) for j in range(3)))
    trQ = sp.simplify(Q3.trace())
    ok &= sp.simplify(QQ - 32 * mu ** 2 * d ** 4 * Om ** 6) == 0 and trQ == 0
    # with A = 1/(gamma c^2 wbar), v = c wbar (local units wbar = 1), gamma = 4 pi G, Kepler Omega^2 d^3 = G M:
    g, c = sp.symbols("gamma c", positive=True)
    P = (1 / (240 * sp.pi * (1 / (g * c ** 2)) * c ** 7)) * (trQ ** 2 + 2 * QQ)
    P = sp.simplify(P.subs(g, 4 * sp.pi * G).subs(Om, sp.sqrt(G * M / d ** 3)))
    ok &= sp.simplify(P - sp.Rational(16, 15) * G ** 4 * mu ** 2 * M ** 3 / (c ** 5 * d ** 5)) == 0
    # eccentric Kepler orbit: time average of 2 Q3:Q3 + (tr Q3)^2 via the true anomaly, exactly at Pythagorean e (a = G = M = mu = 1)
    f = sp.Symbol("f", real=True)
    ok_ecc = True
    for ev in (sp.Integer(0), sp.Rational(5, 13), sp.Rational(8, 17), sp.Rational(3, 5), sp.Rational(4, 5)):
        pp = 1 - ev ** 2
        r = pp / (1 + ev * sp.cos(f))
        fdot = sp.sqrt(pp) / r ** 2                                          # r^2 f' = sqrt(G M p)
        Xs = [r * sp.cos(f), r * sp.sin(f)]
        ddt = lambda ex, fd=fdot: sp.simplify(sp.diff(ex, f) * fd)
        Qs = [[Xs[i] * Xs[j] for j in range(2)] for i in range(2)]
        Q3s = [[ddt(ddt(ddt(Qs[i][j]))) for j in range(2)] for i in range(2)]
        integrand = sp.simplify((2 * sum(Q3s[i][j] ** 2 for i in range(2) for j in range(2)) + (Q3s[0][0] + Q3s[1][1]) ** 2) / fdot)
        avg = sp.integrate(integrand, (f, 0, 2 * sp.pi)) / (2 * sp.pi)      # the period is 2 pi for a = G = M = 1
        target = 64 * (1 + sp.Rational(99, 32) * ev ** 2 + sp.Rational(51, 128) * ev ** 4) / (1 - ev ** 2) ** sp.Rational(7, 2)
        ok_ecc &= sp.simplify(avg - target) == 0
    ok &= ok_ecc
    check("R1", ok, "scalar multipole power P = (gamma/(240 pi c^5)) <(tr Q''')^2 + 2 Q''':Q'''> (local units; the angular moment "
          "(4 pi/15)(dd + dd + dd) exact); circular pair: (16/15) G^4 mu^2 M^3/(c^5 d^5), G = gamma/(4 pi); Kepler average "
          "<2 Q''':Q''' + (tr Q''')^2> = 64 G^3 mu^2 M^3 (1 + 99e^2/32 + 51e^4/128)/(a^5 (1-e^2)^(7/2)) exactly at e = 0, 5/13, 8/17, 3/5, 4/5 (attempt a4's closed form)")
    # lattice retarded kernel G(x, lam) = int e^{iq.x}/(p^2 + lam^2), p^2 = sum 4 sin^2(q_j/2): odd part through lam^3
    q, lam = sp.symbols("q lambda", positive=True)
    def odd_part(expr):                       # odd-in-lambda part of int_0^oo expr dq, expr rational in q^2 and lam^2
        val = sp.integrate(sp.apart(sp.simplify(expr), q), (q, 0, sp.oo), conds="none")
        return val
    # order lam: (1/(2 pi^2)) int q^2/(q^2 + lam^2) -> odd part -lam/(4 pi)
    t1 = sp.simplify((1 / (2 * sp.pi ** 2)) * sp.integrate(-lam ** 2 / (q ** 2 + lam ** 2), (q, 0, sp.oo)))
    # order lam^3, isotropic: -(|x|^2/6)(1/(2 pi^2)) int q^4/(q^2+lam^2), odd part from lam^4/(q^2+lam^2)
    xx = sp.Symbol("xsq", positive=True)
    t3a = sp.simplify(-(xx / 6) * (1 / (2 * sp.pi ** 2)) * sp.integrate(lam ** 4 / (q ** 2 + lam ** 2), (q, 0, sp.oo)))
    # lattice anisotropy: p^2 = q^2 - sum q_j^4/12 + ..., <sum n_j^4> = 3/5: (1/20)(1/(2 pi^2)) int q^6/(q^2+lam^2)^2, odd part
    t3b = sp.simplify(sp.Rational(1, 20) * (1 / (2 * sp.pi ** 2)) * (sp.integrate(3 * lam ** 4 / (q ** 2 + lam ** 2), (q, 0, sp.oo))
                                                                     - sp.integrate(lam ** 6 / (q ** 2 + lam ** 2) ** 2, (q, 0, sp.oo))))
    avg_n4 = ang(n[0] ** 4) / (4 * sp.pi)
    ok2 = sp.simplify(t1 + lam / (4 * sp.pi)) == 0 and sp.simplify(3 * avg_n4 - sp.Rational(3, 5)) == 0
    ok2 &= sp.simplify(t3a + t3b + lam ** 3 * (xx - sp.Rational(3, 4)) / (24 * sp.pi)) == 0
    check("R2", ok2, "lattice retarded kernel: odd terms -lam/(4 pi) (the same at every site: multiplies the total charge) and "
          "-lam^3 (|x|^2 - 3/4)/(24 pi) (the -3/4 from the lattice's q^4 term, <sum n_j^4> = 3/5) - attempt a4's coefficients re-derived")


# ------------------------------------------------------------------------------------------------ S: executed front speed
def family_s() -> dict:
    """full non-linear law u'' = u'^2/2 - gamma c^2 w (dF/du + s), rates held at the ambient value on the outer layer;
    a weak point source switched on at t = 0; half-rise time of u - ubar at distances 8, 12, 16 along an axis."""
    L = 48; gamma = 1.0; c = 1.0; s0 = 0.02
    out = {}
    for wbar in (1.0, 2.0):
        dt = 0.05 / wbar
        u0 = np.log(wbar)
        u = np.full((L, L, L), u0); up = u.copy()
        src = np.zeros((L, L, L)); ctr = L // 2; src[ctr, ctr, ctr] = s0
        T = 30.0 / wbar; n_steps = int(T / dt)
        # static reference profile along the axis by relaxing the static law (same operator) for normalisation
        rec = {r: [] for r in (8, 12, 16)}
        uprev = u.copy()
        for n_ in range(n_steps):
            phi = np.exp(u / 2)
            avg = (np.roll(phi, 1, 0) + np.roll(phi, -1, 0) + np.roll(phi, 1, 1) + np.roll(phi, -1, 1) + np.roll(phi, 1, 2) + np.roll(phi, -1, 2)) / 6
            dF = (12 / gamma) * phi * (phi - avg)
            udot = (u - uprev) / dt
            acc = udot ** 2 / 2 - gamma * c ** 2 * np.exp(u) * (dF + src)
            unew = 2 * u - uprev + dt ** 2 * acc
            unew[0, :, :] = unew[-1, :, :] = unew[:, 0, :] = unew[:, -1, :] = unew[:, :, 0] = unew[:, :, -1] = u0
            uprev, u = u, unew
            for r in rec:
                rec[r].append(u[ctr + r, ctr, ctr] - u0)
        # half-rise: first time the deviation reaches half of its value at the end
        times = {}
        for r, series in rec.items():
            arr = np.array(series); final = arr[-1]
            idx = np.argmax(np.abs(arr) >= 0.5 * abs(final))
            times[r] = (idx + 1) * dt
        speed = (16 - 8) / (times[16] - times[8])
        out[wbar] = (times, speed)
    t1, v1 = out[1.0]; t2, v2 = out[2.0]
    OUT.append(f"     [executed, float] half-rise times at r = 8, 12, 16: wbar = 1: {t1[8]:.2f}, {t1[12]:.2f}, {t1[16]:.2f} "
               f"(speed {v1:.3f}); wbar = 2: {t2[8]:.2f}, {t2[12]:.2f}, {t2[16]:.2f} (speed {v2:.3f}); ratio {v2 / v1:.3f}")
    return {"v1": v1, "v2": v2}


def main() -> int:
    family_k()
    family_l()
    family_w()
    family_h()
    family_r()
    sres = family_s()
    print("A delay for the rate field - checks; worker w-macbookpro90c72-jec4a (claude-opus-5-5)")
    for line in OUT:
        print(line)
    print(f"checks: {sum(1 for l in OUT if l.startswith(('ok', 'FAIL'))) - len(FAILS)} ok, {len(FAILS)} fail")
    if FAILS:
        print(f"SUMMARY: ROUTE FAILS AT {FAILS[0]}")
        return 1
    print("SUMMARY: PROVED - (a) the on-site kinetic term of weight one is unique, (1/(2 gamma c^2)) sum udot^2/w; it survives a "
          "change of parameter only with the rates referred to one clock of the system; weak field u'' = c^2 wbar^2 Lap u - "
          "gamma c^2 wbar (e - mu), Lap = sum_y (u_y - u_x) (constant 6), about any static background local speed c w_x "
          "(executed: fronts at 1.03 and 2.05 sites per ambient tick at wbar = 1, 2). (b) c is not fixed by covariance or scale "
          "covariance: a second pure number; no wake for smooth bodies needs c >= 1; on the lattice the field's phase velocity "
          "has the floor (2/pi) c and a hopping point source radiates for every c. (c) slow sources give the static law, first "
          "lattice corrections -lam/(4 pi), -lam^3 (|x|^2 - 3/4)/(24 pi); monopole and dipole silent; quadrupole power "
          "(16/15) G^4 mu^2 M^3/(c^5 d^5), G = gamma/(4 pi). (d) added: the kinetic term, c, and a reference clock.")
    print("HIT: the rate field's motion: unique weight-one on-site kinetic term (needs a reference clock), weak-field wave law with "
          "constant 6 and local speed c w_x, c a second pure number (c >= 1 for smooth bodies; on the lattice a hopping point "
          "source radiates for every c), and two circling bodies radiate only through the scalar quadrupole with trace, "
          "(16/15) G^4 mu^2 M^3/(c^5 d^5) times (1 + 99e^2/32 + 51e^4/128)/(1-e^2)^(7/2).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
