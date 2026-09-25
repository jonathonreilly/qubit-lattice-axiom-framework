#!/usr/bin/env python3
"""check.py for J:derive:the-completions-that-bend-like-the-comparator:a1 (worker w-macbookpro9927a-j8782, claude-opus-5-5).

Setting (blocks 55, 60, 110 as landed on main). Rates w = e^u (weight one), lengths l = e^lam (weight zero), chi = sqrt(l),
N = w chi; rays see the index n = l/w = chi^3/N (block 110). A local static completion: a field energy of weight one,
covariant, nearest-neighbour, vanishing on uniform fields; at long wavelength (two derivatives) every such energy is
  F = -K int e^u [A(lam) grad u.grad lam + C(lam) |grad lam|^2 + D(lam) |grad u|^2],
with block 60 T3's second-order jet fixed: A(0) = 1 (normalisation), C(0) = 1/(2 beta), D(0) = 0 (beta = 1 for the
curvature member, block 110's A = e^lam, C = e^lam/2, D = 0). The third-order jet is (A1, C1, D1) = (A', C', D')(0), the
fourth-order (A2, C2, D2) = (A'', C'', D'')(0). A point body's exterior has charges u ~ U1/r, lam ~ L1/r; sigma = -U1/L1
(sigma = 1/beta for a body at rest at weak field). M is defined by nu1 = 2M (first-order turn 4M/b).

Families
  Q  pinned sources (blocks 55, 60, 110 on main; the task)
  S  the exterior to third order (sympy, order by order from the Euler-Lagrange equations); the curvature member's exact
     exterior chi = 1 + a/r, N = 1 - p/r reproduced term by term; index coefficients nu1, nu2, nu3; the turn from
     Bouguer's invariant: alpha = 2 nu1/b + pi(nu2 + nu1^2/2)/b^2 + (4 nu1^3/3 + 8 nu1 nu2 + 4 nu3)/b^3; the comparator's
     4M, 15 pi/4, 128/3 with nu = (2M, 7M^2/4, M^3)
  B  classification: nu2/M^2 = -2(2A1 - C1 + D1 s^2 - 4 D1 s - 2 s^2 - s - 2)/(1+s)^2; at sigma = 1 the comparator's
     7M^2/4 iff 4A1 - 2C1 - 6D1 = 3 (a plane); 128/3 iff nu3 = M^3, one linear condition on (A2, C2, D2); the curvature
     member satisfies both; the wall term (block 60 T1) sees only the second-order jet
  W  bilinear members F = -c sum (X_y - X_x)(Y_y - Y_x): the jet forces X = w f(l), Y = g(l), f(1) = 1, f'(1) = 1/2;
     outside the body X and Y are exactly harmonic; the index is l f(l)/X; with g(1) = g'(1) = 1 it is the comparator's at
     every order (all turn terms, capture at 3 sqrt3 M) iff l f(l) = ((1 + g(l))/2)^3: one member for every g, the
     curvature member being g = 2 sqrt(l) - 1; among power laws Y = l^gamma only gamma = 1/2 (nu2 = (17 - 6 gamma)/8 M^2)
  N  [float] the third-order series against direct integration of the nonlinear radial equations for a generic jet at
     sigma = 1 and 0.6; capture thresholds min r n(r) for power-law members
"""
import hashlib
import json
import os
import subprocess
import sys
import time

import numpy as np
import sympy as sp

T0 = time.time()
REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), *([os.pardir] * 5)))
FAILS = []
ONLY = set(sys.argv[1:])


def rep(fam, ok, msg):
    if not ok:
        FAILS.append(fam)
    print(f"[{fam}] {'PASS' if ok else 'FAIL'} {msg}")
    sys.stdout.flush()


# ------------------------------------------------------------------ Q
MAIN = "60c5f194d940a7bbaf1cdd545296e31d74a02f1a"
N110 = ("docs/ADMISSIBILITY_RULE_AROUND_A_BODY_THE_WALKS_RAYS_MATCH_THE_COMPARATORS_AT_EVERY_ORDER_EXACTLY_WHEN_ITS_TWO"
        "_CHARGES_AGREE_AND_THEY_AGREE_ONLY_WHEN_HOP_ENERGY_BALANCES_THE_SLOWED_CLOCKS_BOUNDED_THEOREM_NOTE_2026-09-24.md")
N60 = ("docs/ADMISSIBILITY_RULE_A_LEDGER_LINEAR_IN_THE_RATES_EVERY_CLOCK_A_MULTIPLIER_THE_LEDGER_A_WALL_TERM_AND_THE"
       "_CURVATURE_MEMBER_DOUBLES_THE_BENDING_BOUNDED_THEOREM_NOTE_2026-09-21.md")
N55 = ("docs/ADMISSIBILITY_RULE_ACTION_AND_REACTION_THE_RATE_FIELDS_SOURCE_IS_THE_AMPLITUDES_ENERGY_DENSITY_MATCHED_PULLS"
       "_AND_A_KEPT_LEDGER_FIX_THE_CLOCK_LAWS_SECOND_ORDER_BOUNDED_THEOREM_NOTE_2026-09-21.md")
SRC = [("block110", MAIN, N110, "42cd07855b280414956cd50099eeed374035a6e8c0d446d5a3696d4bfd7a966b",
        ["- **The curvature member** (block 60 T4, landed): the field energy `F = −8K Σ_bonds (N_y − N_x)(χ_y − χ_x)`",
         "turns a ray by `2ν₁/b + π(ν₂ + ν₁²/2)/b² + …`",
         "`n = χ³/N = (r + a)³/(r²(r − p))`"]),
       ("block60", MAIN, N60, "3a54bebf805d1722b225c1af9326fd610580ec2cbdcf9dad409aefad952b3f80",
        ["- **Rates and lengths.** `w_x = e^{u_x} > 0` (weight one). One length per site, `ℓ_x = e^{λ_x} > 0` (weight zero)",
         "*Statement.* (a) For `G = K ℓ^p (aΔλ + bq)` the part of `F` of second order in `(u − ū, λ)` is "
         "`K w̄ [a u·Δλ + (ap − b) λ·Δλ]`; there is no term in `u` alone."]),
       ("block55", MAIN, N55, "39d93ccb81349ae535401587958e86b3401fe8947830ebbd0ad07f955ee430da",
        ["A variational field equation keeps that ledger; conservation alone does not uniquely force this equation.",
         "An onsite term c w_x is also homogeneous and local, but spoils that normalized uniform-vacuum condition"])]
TASKQ = ("92631f30519815c72f4703011c12669d49a71e1e", "J:derive:the-completions-that-bend-like-the-comparator:a1",
         ["(a) For a general local static completion - a field energy of weight one in the rates, covariant, "
          "nearest-neighbour, with block 60 T3's second-order jet fixed - compute the exterior of a point body to second "
          "order and nu2 in terms of the third-order jet;",
          "(c) the same at third order (128/3).",
          "HIT: an exact classification, or a clause that forces the comparator's second order."])


def git_show(spec, branch=None):
    r = subprocess.run(["git", "show", spec], cwd=REPO, capture_output=True)
    if r.returncode != 0:
        subprocess.run(["git", "fetch", "--quiet", "origin", branch or "main"], cwd=REPO, capture_output=True)
        r = subprocess.run(["git", "show", spec], cwd=REPO, capture_output=True)
    return r.stdout if r.returncode == 0 else None


def fam_Q():
    ok, msg = True, []
    for tag, c, p, h, quotes in SRC:
        b = git_show(f"{c}:{p}", "main")
        if b is None:
            rep("Q", False, f"{tag} unreadable")
            return
        good = hashlib.sha256(b).hexdigest() == h
        n = sum(q in b.decode() for q in quotes)
        ok &= good and n == len(quotes)
        msg.append(f"{tag}@{c[:8]} {'sha ok' if good else 'SHA MISMATCH'} {n}/{len(quotes)}")
    b = git_show(f"{TASKQ[0]}:probes/TASKS.json", "ai/probes")
    what = next((t["what"] for t in json.loads(b.decode()) if t["id"] == TASKQ[1]), "") if b else ""
    n = sum(q in what for q in TASKQ[2])
    ok &= n == len(TASKQ[2])
    msg.append(f"task@{TASKQ[0][:8]} {n}/{len(TASKQ[2])}")
    rep("Q", ok, "; ".join(msg))


# ------------------------------------------------------------------ S: the exterior, order by order
r, eps = sp.symbols("r epsilon", positive=True)
A1, A2, C1, C2, D1, D2, beta = sp.symbols("A1 A2 C1 C2 D1 D2 beta")
L1, U1, l2, u2, l3, u3, M, sig = sp.symbols("L1 U1 l2 u2 l3 u3 M sigma")
RES = {}


def exterior():
    Af = lambda x: 1 + A1 * x + A2 * x ** 2 / 2
    Cf = lambda x: 1 / (2 * beta) + C1 * x + C2 * x ** 2 / 2
    Df = lambda x: D1 * x + D2 * x ** 2 / 2
    u = sp.Function("u")(r)
    lam = sp.Function("lam")(r)
    Lag = r ** 2 * sp.exp(u) * (Af(lam) * u.diff(r) * lam.diff(r) + Cf(lam) * lam.diff(r) ** 2 + Df(lam) * u.diff(r) ** 2)
    EL = [sp.diff(Lag, f) - sp.diff(sp.diff(Lag, f.diff(r)), r) for f in (u, lam)]
    ua = eps * U1 / r + eps ** 2 * u2 / r ** 2 + eps ** 3 * u3 / r ** 3
    la = eps * L1 / r + eps ** 2 * l2 / r ** 2 + eps ** 3 * l3 / r ** 3
    res = []
    for e in EL:
        ex = e.subs({u.diff(r, 2): ua.diff(r, 2), lam.diff(r, 2): la.diff(r, 2)})
        ex = ex.subs({u.diff(r): ua.diff(r), lam.diff(r): la.diff(r)}).subs({u: ua, lam: la})
        res.append(sp.expand(sp.series(sp.expand(ex), eps, 0, 4).removeO()))
    o1 = [sp.simplify(e.coeff(eps, 1)) for e in res]
    s2 = sp.solve([sp.expand(e.coeff(eps, 2) * r ** 4) for e in res], [u2, l2], dict=True)[0]
    s3 = sp.solve([sp.expand((e.coeff(eps, 3) * r ** 5).subs(s2)) for e in res], [u3, l3], dict=True)[0]
    n = sp.series(sp.exp(la - ua), eps, 0, 4).removeO()
    nu1 = sp.expand(n.coeff(eps, 1) * r)
    nu2 = sp.expand((n.coeff(eps, 2) * r ** 2).subs(s2))
    nu3 = sp.expand((n.coeff(eps, 3) * r ** 3).subs(s2).subs(s3))
    return o1, s2, s3, nu1, nu2, nu3


def turn_coeffs():
    n1, n2, n3, z, a1, a2, a3 = sp.symbols("nu1 nu2 nu3 z a1 a2 a3")
    rr = (1 + a1 * z + a2 * z ** 2 + a3 * z ** 3) / z                     # r as a function of rho = r n(r), z = 1/rho
    eq = sp.expand(sp.series(rr * (1 + n1 / rr + n2 / rr ** 2 + n3 / rr ** 3) * z - 1, z, 0, 4).removeO())
    sol = sp.solve([eq.coeff(z, k) for k in (1, 2, 3)], [a1, a2, a3], dict=True)[0]
    rr = rr.subs(sol)
    lnn = sp.expand(sp.series(sp.log(1 + n1 / rr + n2 / rr ** 2 + n3 / rr ** 3), z, 0, 4).removeO())
    t = sp.symbols("t", positive=True)
    Ik = [sp.integrate(1 / (t ** (k + 1) * sp.sqrt(t ** 2 - 1)), (t, 1, sp.oo)) for k in (1, 2, 3)]
    alpha = [sp.simplify(2 * k * lnn.coeff(z, k) * Ik[k - 1]) for k in (1, 2, 3)]
    return (n1, n2, n3), alpha


def fam_S():
    t0 = time.time()
    o1, s2, s3, nu1, nu2, nu3 = exterior()
    RES.update(s2=s2, s3=s3, nu1=nu1, nu2=nu2, nu3=nu3)
    # the curvature member: A = e^lam, C = e^lam/2, D = 0, beta = 1; exact exterior chi = 1 + a/r, N = 1 - p/r
    a, p = sp.symbols("a p", positive=True)
    cm = {beta: 1, A1: 1, A2: 1, C1: sp.Rational(1, 2), C2: sp.Rational(1, 2), D1: 0, D2: 0}
    lam_ex = sp.series(2 * sp.log(1 + eps * a / r), eps, 0, 4).removeO()
    u_ex = sp.series(sp.log(1 - eps * p / r) - sp.log(1 + eps * a / r), eps, 0, 4).removeO()
    chg = {L1: 2 * a, U1: -(a + p)}
    ok_cm = all(sp.simplify(e) == 0 for e in (
        (s2[l2].subs(cm).subs(chg)) - sp.expand(lam_ex).coeff(eps, 2) * r ** 2,
        (s2[u2].subs(cm).subs(chg)) - sp.expand(u_ex).coeff(eps, 2) * r ** 2,
        (s3[l3].subs(cm).subs(chg)) - sp.expand(lam_ex).coeff(eps, 3) * r ** 3,
        (s3[u3].subs(cm).subs(chg)) - sp.expand(u_ex).coeff(eps, 3) * r ** 3,
        nu2.subs(cm).subs(chg) - (3 * a ** 2 + 3 * a * p + p ** 2)))
    (n1, n2, n3), alpha = turn_coeffs()
    ok_turn = (alpha[0] == 2 * n1 and sp.simplify(alpha[1] - sp.pi * (n2 + n1 ** 2 / 2)) == 0
               and sp.simplify(alpha[2] - (sp.Rational(4, 3) * n1 ** 3 + 8 * n1 * n2 + 4 * n3)) == 0)
    sch = {n1: 2 * M, n2: sp.Rational(7, 4) * M ** 2, n3: M ** 3}
    comp = [sp.simplify(x.subs(sch)) for x in alpha]
    idx = sp.series(((1 + M / (2 * r)) ** 3 / (1 - M / (2 * r))).subs(r, 1 / eps), eps, 0, 4).removeO()
    ok_idx = [sp.expand(idx).coeff(eps, k) for k in (1, 2, 3)] == [2 * M, sp.Rational(7, 4) * M ** 2, M ** 3]
    ok = all(v == 0 for v in o1) and ok_cm and ok_turn and ok_idx and comp == [4 * M, sp.Rational(15, 4) * sp.pi * M ** 2,
                                                                                 sp.Rational(128, 3) * M ** 3]
    rep("S", ok, "Euler-Lagrange equations of the general completion solved to third order (first order: both fields "
        "harmonic, charges L1, U1); the curvature member's exact exterior (block 110 T1) reproduced at orders 2 and 3, and "
        "nu2 = 3a^2 + 3ap + p^2; Bouguer's invariant gives alpha = 2nu1/b + pi(nu2 + nu1^2/2)/b^2 + (4nu1^3/3 + 8nu1 nu2 + "
        f"4nu3)/b^3; the comparator's index (1+M/2r)^3/(1-M/2r) has nu = (2M, 7M^2/4, M^3) and turn (4M, 15pi/4, 128/3)  "
        f"({time.time() - t0:.0f}s)")


def fam_B():
    if not RES:
        o1, s2, s3, nu1, nu2, nu3 = exterior()
        RES.update(s2=s2, s3=s3, nu1=nu1, nu2=nu2, nu3=nu3)
    nu1, nu2, nu3 = RES["nu1"], RES["nu2"], RES["nu3"]
    sub = {beta: 1, U1: -sig * L1}
    Ls = sp.solve(sp.Eq(nu1.subs(sub), 2 * M), L1)[0]
    n2 = sp.simplify(nu2.subs(sub).subs(L1, Ls) / M ** 2)
    n3 = sp.simplify(nu3.subs(sub).subs(L1, Ls) / M ** 3)
    claim2 = -2 * (2 * A1 - C1 + D1 * sig ** 2 - 4 * D1 * sig - 2 * sig ** 2 - sig - 2) / (1 + sig) ** 2
    ok2 = sp.simplify(n2 - claim2) == 0
    plane = sp.simplify(n2.subs(sig, 1) - sp.Rational(7, 4) - (-(4 * A1 - 2 * C1 - 6 * D1 - 3) / 4)) == 0
    third = sp.expand(n3.subs(sig, 1))
    lin4 = [sp.diff(third, v) for v in (A2, C2, D2)]
    ok3 = lin4 == [-sp.Rational(1, 3), sp.Rational(1, 6), sp.Rational(1, 2)]
    cm = {A1: 1, A2: 1, C1: sp.Rational(1, 2), C2: sp.Rational(1, 2), D1: 0, D2: 0}
    ok_cm = sp.simplify(n2.subs(sig, 1).subs(cm)) == sp.Rational(7, 4) and sp.simplify(third.subs(cm)) == 1
    quad = {A1: 0, A2: 0, C1: 0, C2: 0, D1: 0, D2: 0}                         # constant coefficients (e^u times a quadratic form)
    q2 = sp.simplify(n2.subs(sig, 1).subs(quad))
    # body at rest at weak field for general beta: sigma = 1/beta
    n2b = sp.factor(sp.simplify(nu2.subs(U1, -L1 / beta).subs(L1, sp.solve(sp.Eq(nu1.subs(U1, -L1 / beta), 2 * M), L1)[0]) / M ** 2))
    # the wall term: the far-field radial flux of dL/du' is 4 pi K A(0) L1 whatever the third-order jet
    u = sp.Function("u")(r)
    lam = sp.Function("lam")(r)
    Lag = sp.exp(u) * ((1 + A1 * lam) * u.diff(r) * lam.diff(r) + (sp.Rational(1, 2) + C1 * lam) * lam.diff(r) ** 2
                       + D1 * lam * u.diff(r) ** 2)
    flux = sp.diff(Lag, u.diff(r))
    fl = flux.subs({u.diff(r): -U1 / r ** 2, lam.diff(r): -L1 / r ** 2}).subs({u: U1 / r, lam: L1 / r})
    wall = sp.limit(-r ** 2 * fl, r, sp.oo)
    ok_wall = sp.simplify(wall - L1) == 0
    rep("B", ok2 and plane and ok3 and ok_cm and ok_wall,
        f"nu2/M^2 = -2(2A1 - C1 + D1 s^2 - 4D1 s - 2s^2 - s - 2)/(1+s)^2 (s = sigma, beta = 1); at sigma = 1 it is 7/4 iff "
        f"4A1 - 2C1 - 6D1 = 3; nu3/M^3 at sigma = 1 has d/d(A2, C2, D2) = (-1/3, 1/6, 1/2), so 128/3 is one linear "
        f"condition on the fourth-order jet; the curvature member gives 7/4 and 1; constant coefficients give {q2}; a body "
        f"at rest, general beta: nu2/M^2 = {n2b}; the wall term (flux of dL/du') is A(0) L1: blind to the third-order jet")
    RES.update(n2=n2, n3=third)


# ------------------------------------------------------------------ W: bilinear members
def fam_W():
    lam, ellv, x = sp.symbols("lam ell x", positive=True)
    s_ = sp.symbols("s")
    # (i) weight one and no |grad u|^2 at second order: X = w^s f(l), Y = w^(1-s) g(l) gives s(1-s) |grad u|^2 -> s in {0, 1}
    ok_s = sp.solve(s_ * (1 - s_), s_) == [0, 1]
    # (ii) second-order jet with X = w f(l), Y = g(l): A = f g' l, C = g' l^2 f' (in lam = log l); C(0)/A(0) = 1/2 iff f'(1) = 1/2
    f, g = sp.Function("f"), sp.Function("g")
    Aexpr = f(x) * sp.diff(g(x), x) * x
    Cexpr = sp.diff(g(x), x) * x ** 2 * sp.diff(f(x), x)
    ratio = sp.simplify((Cexpr / Aexpr).subs(x, 1).subs(f(1), 1))
    ok_jet = sp.simplify(ratio - sp.Subs(sp.diff(f(x), x), x, 1).doit()) == 0
    # (iii) exterior: for F = int grad X . grad Y, EL in u gives X Lap Y = 0, EL in lam gives X_lam Lap Y + Y_lam Lap X = 0
    uu, ll = sp.symbols("uu ll")
    Xf = sp.exp(uu) * f(sp.exp(ll))
    Yf = g(sp.exp(ll))
    ok_el = sp.simplify(sp.diff(Xf, uu) - Xf) == 0 and sp.diff(Yf, uu) == 0
    # (iv) matched members: g(1) = g'(1) = 1 and l f(l) = ((1+g)/2)^3; exterior X = 1 - p/r, Y = 1 + q/r, sigma = 1 gives
    #      p = q/2 = M/2 and n = l f(l)/X = ((1 + Y)/2)^3/X = (1 + M/2r)^3/(1 - M/2r): the comparator's index identically
    rr, Mm = sp.symbols("r M", positive=True)
    Y = 1 + Mm / rr
    X = 1 - Mm / (2 * rr)
    n_matched = ((1 + Y) / 2) ** 3 / X
    ok_match = sp.simplify(n_matched - (1 + Mm / (2 * rr)) ** 3 / (1 - Mm / (2 * rr))) == 0
    # first-order charge relation of a matched member: lam ~ q/r (g'(1) = 1), u = log X - log f(l) ~ -p/r - (q/2)/r;
    # sigma = -U1/L1 = (p + q/2)/q = 1 iff p = q/2
    qq, pp = sp.symbols("q p", positive=True)
    ok_sigma = sp.solve(sp.Eq((pp + qq / 2) / qq, 1), pp) == [qq / 2]
    # several g, each with its own f: the second-order jet and nu2 = 7/4, nu3 = 1 at sigma = 1 (general formulas of family B)
    if "n2" not in RES:
        fam_B()
    n2, n3 = RES["n2"], RES["n3"]
    okg = True
    gs = [2 * sp.sqrt(x) - 1, x, 1 + sp.log(x), 1 + (x ** 3 - 1) / 3, (3 - 1 / x ** 2) / 2]
    for gx in gs:
        gx = sp.simplify(gx)
        okg &= gx.subs(x, 1) == 1 and sp.simplify(sp.diff(gx, x).subs(x, 1)) == 1
        fx = ((1 + gx) / 2) ** 3 / x
        Ae = sp.series((fx * sp.diff(gx, x) * x).subs(x, sp.exp(lam)), lam, 0, 3).removeO()
        Ce = sp.series((sp.diff(gx, x) * x ** 2 * sp.diff(fx, x)).subs(x, sp.exp(lam)), lam, 0, 3).removeO()
        jets = {A1: Ae.coeff(lam, 1) / Ae.coeff(lam, 0), A2: 2 * Ae.coeff(lam, 2) / Ae.coeff(lam, 0),
                C1: Ce.coeff(lam, 1) / Ae.coeff(lam, 0), C2: 2 * Ce.coeff(lam, 2) / Ae.coeff(lam, 0), D1: 0, D2: 0}
        okg &= sp.simplify(Ae.coeff(lam, 0)) == 1 and sp.simplify(Ce.coeff(lam, 0)) == sp.Rational(1, 2)
        okg &= sp.simplify(n2.subs(sig, 1).subs(jets)) == sp.Rational(7, 4) and sp.simplify(n3.subs(jets)) == 1
    # power laws X = N = w l^(1/2), Y = l^gamma: at sigma = 1, n = (1 + gamma M/r)^(3/(2 gamma))/(1 - M/(2r))
    gam = sp.symbols("gamma", positive=True)
    npow = (1 + gam * Mm / rr) ** (3 / (2 * gam)) / (1 - Mm / (2 * rr))
    ser = sp.series(npow.subs(rr, 1 / eps), eps, 0, 3).removeO()
    ok_pow = sp.simplify(sp.expand(ser).coeff(eps, 1) - 2 * Mm) == 0 and \
        sp.simplify(sp.expand(ser).coeff(eps, 2) - (17 - 6 * gam) / 8 * Mm ** 2) == 0
    only_half = sp.solve(sp.Eq((17 - 6 * gam) / 8, sp.Rational(7, 4)), gam) == [sp.Rational(1, 2)]
    # capture at 3 sqrt3 M for the comparator index: min of r n(r) at r = (1 + sqrt... ) exactly
    rn = rr * (1 + Mm / (2 * rr)) ** 3 / (1 - Mm / (2 * rr))
    crit = [c for c in sp.solve(sp.diff(rn.subs(Mm, 1), rr), rr) if c.is_real and c > sp.Rational(1, 2)]
    ok_cap = len(crit) == 1 and sp.simplify(rn.subs(Mm, 1).subs(rr, crit[0]) - 3 * sp.sqrt(3)) == 0
    rep("W", ok_s and ok_jet and ok_el and ok_match and ok_sigma and okg and ok_pow and only_half and ok_cap,
        "bilinear members: weight one and D(0) = 0 force X = w f(l), Y = g(l); the jet forces f'(1) = 1/2; outside the body "
        "X and Y are harmonic (EL: X Lap Y = 0, X_lam Lap Y + Y_lam Lap X = 0); with g(1) = g'(1) = 1 and sigma = 1 (p = q/2) "
        "the index l f/X is the comparator's identically iff l f = ((1+g)/2)^3; five choices of g (incl. the curvature "
        "member 2 sqrt(l) - 1, and g = l, 1 + log l) give nu2 = 7/4, nu3 = 1 by family B's formulas; power laws Y = "
        "l^gamma: nu2 = (17 - 6 gamma)/8 M^2, 7/4 only at gamma = 1/2; capture of the comparator index at r n = 3 sqrt3 M")


# ------------------------------------------------------------------ N [float]
def fam_N():
    from scipy.integrate import solve_ivp
    t0 = time.time()
    if "s3" not in RES:
        o1, s2, s3, nu1, nu2, nu3 = exterior()
        RES.update(s2=s2, s3=s3, nu1=nu1, nu2=nu2, nu3=nu3)
    jet = {beta: 1, A1: 0.3, A2: 0.1, C1: -0.2, C2: 0.4, D1: 0.5, D2: -0.3}
    Af = lambda x: 1 + jet[A1] * x + jet[A2] * x * x / 2
    Ap = lambda x: jet[A1] + jet[A2] * x
    Cf = lambda x: 0.5 + jet[C1] * x + jet[C2] * x * x / 2
    Cp = lambda x: jet[C1] + jet[C2] * x
    Df = lambda x: jet[D1] * x + jet[D2] * x * x / 2
    Dp = lambda x: jet[D1] + jet[D2] * x

    def rhs(rv, y):
        uu, ll, up, lp = y
        # Lagrangian r^2 e^u [A u'l' + C l'^2 + D u'^2]; EL: d/dr(dL/du') = dL/du, d/dr(dL/dl') = dL/dl
        E = np.exp(uu) * rv * rv
        pu = E * (Af(ll) * lp + 2 * Df(ll) * up)
        pl = E * (Af(ll) * up + 2 * Cf(ll) * lp)
        dLdu = E * (Af(ll) * up * lp + Cf(ll) * lp ** 2 + Df(ll) * up ** 2)
        dLdl = E * (Ap(ll) * up * lp + Cp(ll) * lp ** 2 + Dp(ll) * up ** 2)
        # d pu/dr = dLdu ; pu = E (A lp + 2 D up): expand d/dr and solve the 2x2 system for (upp, lpp)
        dE = E * (up + 2 / rv)
        gu = dLdu - dE * (Af(ll) * lp + 2 * Df(ll) * up) - E * (Ap(ll) * lp * lp + 2 * Dp(ll) * lp * up)
        gl = dLdl - dE * (Af(ll) * up + 2 * Cf(ll) * lp) - E * (Ap(ll) * lp * up + 2 * Cp(ll) * lp * lp)
        Mx = E * np.array([[2 * Df(ll), Af(ll)], [Af(ll), 2 * Cf(ll)]])
        upp, lpp = np.linalg.solve(Mx, [gu, gl])
        return [up, lp, upp, lpp]

    errs = []
    for sv in (1.0, 0.6):
        Lv = 0.02
        vals = {L1: Lv, U1: -sv * Lv, **jet}
        c2 = [float(RES["s2"][u2].subs(vals)), float(RES["s2"][l2].subs(vals))]
        c3 = [float(RES["s3"][u3].subs(vals)), float(RES["s3"][l3].subs(vals))]
        ch = [vals[U1], Lv]
        S = lambda rv, k, order: ch[k] / rv + c2[k] / rv ** 2 + (c3[k] / rv ** 3 if order == 3 else 0.0)
        dS = lambda rv, k: -ch[k] / rv ** 2 - 2 * c2[k] / rv ** 3 - 3 * c3[k] / rv ** 4
        r0 = 400.0
        sol = solve_ivp(rhs, (r0, 2.0), [S(r0, 0, 3), S(r0, 1, 3), dS(r0, 0), dS(r0, 1)], rtol=1e-13, atol=1e-16,
                        method="DOP853", dense_output=True)
        for k in (0, 1):
            d = {rv: (sol.sol(rv)[k] - S(rv, k, 2)) * rv ** 3 for rv in (4.0, 8.0)}
            est = 2 * d[8.0] - d[4.0]                          # c3 + c4/r: linear extrapolation in 1/r
            dev3 = abs(sol.sol(2.0)[k] - S(2.0, k, 3))
            errs.append((sv, k, c3[k], est, dev3))
    ok_ode = all((abs(e[3] - e[2]) < 0.05 * abs(e[2]) if abs(e[2]) > 1e-7 else abs(e[3] - e[2]) < 2e-8) and e[4] < 1e-8
                 for e in errs)
    # capture thresholds of power-law bilinear members at sigma = 1 (M = 1): min over r of r n(r)
    caps = {}
    for gm in (0.25, 0.5, 1.0, 1.5):
        rs = np.linspace(0.51, 20, 400001)
        rn = rs * (1 + gm / rs) ** (3 / (2 * gm)) / (1 - 0.5 / rs)
        caps[gm] = rn.min()
    ok_cap = abs(caps[0.5] - 3 * np.sqrt(3)) < 1e-6 and all(abs(caps[g] - 3 * np.sqrt(3)) > 1e-3 for g in (0.25, 1.0, 1.5))
    rep("N", ok_ode and ok_cap, f"[float] generic jet (A1, A2, C1, C2, D1, D2) = (0.3, 0.1, -0.2, 0.4, 0.5, -0.3), charges "
        f"0.02: direct integration of the nonlinear radial equations from r = 400: the 1/r^3 coefficients of (numerical - "
        f"second-order series), extrapolated from r = 4, 8, equal the third-order series' (u, lam) at sigma = 1: "
        f"({errs[0][3]:.3e} vs {errs[0][2]:.3e}, {errs[1][3]:.4e} vs {errs[1][2]:.4e}), sigma = 0.6: ({errs[2][3]:.4e} vs "
        f"{errs[2][2]:.4e}, {errs[3][3]:.4e} vs {errs[3][2]:.4e}); at r = 2 the third-order series is within "
        f"{max(e[4] for e in errs):.1e}; capture min r n(r) of power-law members at sigma = 1: "
        + ", ".join(f"gamma {g}: {v:.5f}" for g, v in caps.items()) + f" (3 sqrt3 = {3 * np.sqrt(3):.5f})  "
        f"({time.time() - t0:.0f}s)")


if __name__ == "__main__":
    for tag, fn in (("Q", fam_Q), ("S", fam_S), ("B", fam_B), ("W", fam_W), ("N", fam_N)):
        if not ONLY or tag in ONLY:
            fn()
    print(f"total {time.time() - T0:.0f}s; failing families: {sorted(set(FAILS)) or 'none'}")
    if FAILS:
        print("SUMMARY: ROUTE FAILS AT " + ",".join(sorted(set(FAILS))))
    else:
        print("SUMMARY: PARTIAL (long-wave reduction assumed), exact: nu2/M^2 = -2(2A1 - C1 + D1 s^2 - 4D1 s - 2s^2 - s - 2)/(1+s)^2; "
              "the comparator's second order iff 4A1 - 2C1 - 6D1 = 3 at sigma = 1, its third order one more linear condition "
              "on (A2, C2, D2); bilinear members give the comparator's index at every order iff l f = ((1+g)/2)^3, one for "
              "each g; weight one, kept books and coin-rotation blindness leave the jet free")
        print("HIT: exact classification of weight-one static completions with block 60 T3's second-order jet: a point "
              "body's second-order bending coefficient is nu2 = -2(2A1 - C1 + D1 s^2 - 4D1 s - 2s^2 - s - 2)/(1+s)^2 M^2 "
              "(third-order jet A1, C1, D1; charge ratio s); the comparator's 7M^2/4 at s = 1 iff 4A1 - 2C1 - 6D1 = 3, and "
              "128/3 is one further linear condition on the fourth-order jet; the curvature member is not singled out: every "
              "bilinear member X = w f(l), Y = g(l) with l f = ((1+g)/2)^3 has the comparator's index at every order "
              "(capture at 3 sqrt3 M), and no listed clause fixes the jet")
