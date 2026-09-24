#!/usr/bin/env python3
"""Bending over fall at strong field: checks for ATTEMPT.md (attempt 1 of 2), worker w-macbookpro9927a-j7735 (claude-opus-5-5).

Objects: block 60's exact one-body field (PR #8590) chi = 1 + Qg, N = 1 - Pg, P = Q w0, w0 = 1/(1 + 2Qg0), l = chi^2, w = N/chi;
the walk coupled to isotropic lengths either by block 60's bond crossing sqrt(w_x w_y)/(chi_x chi_y) ("frame") or by block 69's
reach-three strain term sum_a sigma_a (1/2){C_a[b], P_a} with 1 + b = 1/l ("reach three", PR #8601), rates by phi H phi, and block 77's
staggered rest term m w eps (PR #8612). Families S, A, B, C are exact (sympy); E is floating point and labelled.
"""
from __future__ import annotations

import json
import subprocess
import time

import numpy as np
import sympy as sp

OUT: list[str] = []
FAILS: list[str] = []


def check(tag: str, ok: bool, msg: str) -> None:
    OUT.append(f"{'ok  ' if ok else 'FAIL'} {tag}: {msg}")
    if not ok:
        FAILS.append(tag)


R_ = sp.Rational
NOTES = [
    ("b59", "7ff9b1540a", "docs/ADMISSIBILITY_RULE_BOND_RATES_AND_LENGTHS_A_BODY_AT_REST_SOURCES_NO_LENGTH_AND_THE_BENDING_OF_RAYS_CARRIES_"
     "ONE_MORE_FREE_NUMBER_BOUNDED_THEOREM_NOTE_2026-09-21.md",
     ["for `m = 0` and a wave vector along an axis across the gradient, the transverse acceleration is `−c² ∇log c`, exactly on the "
      "lattice. The ratio of the two is `d log c/d log a`."]),
    ("b60", "ec3a6abdf0", "docs/ADMISSIBILITY_RULE_A_LEDGER_LINEAR_IN_THE_RATES_EVERY_CLOCK_A_MULTIPLIER_THE_LEDGER_A_WALL_TERM_AND_THE_"
     "CURVATURE_MEMBER_DOUBLES_THE_BENDING_BOUNDED_THEOREM_NOTE_2026-09-21.md",
     ["chi = sqrt(l), N = w chi, bonds crossed at sqrt(w_x w_y)/(chi_x chi_y)",
      "N = 1 - sum P_i g_i with P_i = Q_i w_i",
      "one body: w_0 = 1/(1 + 2 Q g_0)",
      "Far field: the lengths carry 2Q and the rates P + Q, equal only to first order: bending over fall = 1 + (1 + 2Qg_0)/(1 + Qg_0), "
      "between 2 and 3."]),
    ("b69", "40fa4423f2", "docs/ADMISSIBILITY_RULE_REACH_THREE_A_MOMENTUM_THAT_IS_THE_SAME_FOR_ALL_EIGHT_SPECIES_GIVES_A_COUPLING_WITH_THE_"
     "EXACT_CURRENT_AND_ONE_GEOMETRY_FOR_ALL_BOUNDED_THEOREM_NOTE_2026-09-21.md",
     ["i[H, G] = sum_a sum_j sigma_a (1/2){C_a[d_a xi_j], P_j}, a deformation on the bonds along a with REACH THREE",
      "(T4) A uniform strain coupled this way gives H(k) = sum_a sigma_a [sin k_a + cos k_a sum_j B_a^j sin k_j cos k_j]",
      "With `ℓ = (w̄/w)^β`, `1 + b = 1/ℓ`"]),
    ("b71", "e7ef26762e", "docs/ADMISSIBILITY_RULE_AMPLITUDES_OF_NEGATIVE_ENERGY_FALL_LIKE_THE_OTHERS_AND_SOURCE_THE_OPPOSITE_FIELD_A_"
     "NEGATIVE_BODY_AT_REST_HAS_A_LARGEST_SIZE_BOUNDED_THEOREM_NOTE_2026-09-21.md",
     ["one body at rest of either sign, mu = m/(8K): r = (1 + 4 g_0 mu)^(1/2), Q = (r - 1)/(2 g_0), P = Q/r, chi_0 = (1 + r)/2, w_0 = 1/r.",
      "bending over fall, 1 + 2r/(1 + r), falls from 2 to 1"]),
    ("b77", "a2c138c297", "docs/ADMISSIBILITY_RULE_THE_AXIOMS_OWN_GENERATOR_THE_SCALAR_HOP_SPLITS_THE_EIGHT_SPECIES_INTO_FOUR_LEVELS_OF_"
     "ONE_SENSE_AND_A_STAGGERED_TERM_GIVES_THEM_MASS_BOUNDED_THEOREM_NOTE_2026-09-22.md",
     ["(the walk, the a-hops, block 62's varying frame, block 65's twist hop, the reach-three strain term)",
      "phi (H + m eps) phi = phi H phi + m w eps: a rest energy m timed by the local clock"]),
    ("a2", "e1d7063194", "probes/work/derive/bending-over-fall-at-strong-field/w-jonathonsmac4f50-j3a05/ATTEMPT.md",
     ["`(2 + 3Qg₀ − Qg)/(1 + Qg₀) = 1 + 2/(1 + w₀/w(x))`",
      "Everything is in the ray limit. Nothing is claimed at finite wavelength.",
      "The finite-wavelength corrections to both laws, from the lattice dispersion."]),
]
TASK_Q = ["(with the frame/strain coupling of reach three for lengths, isotropic)",
          "HIT if the ratio exceeds 3 or falls below 1 at any strength."]


def family_q() -> None:
    miss = []
    for tag, sha, path, qs in NOTES:
        txt = subprocess.run(["git", "show", f"{sha}:{path}"], capture_output=True, text=True).stdout
        miss += [f"{tag}[{i}]" for i, q in enumerate(qs) if q not in txt]
    d = json.load(open("probes/TASKS.json"))
    ts = d if isinstance(d, list) else d.get("tasks", d)
    ts = ts if isinstance(ts, list) else list(ts.values())
    what = next((t["what"] for t in ts if isinstance(t, dict)
                 and t.get("id") == "J:derive:bending-over-fall-at-strong-field:a1"), "")
    miss += [f"task[{i}]" for i, q in enumerate(TASK_Q) if q not in what]
    check("Q", not miss, "blocks 59, 60, 69, 71, 77 (PR heads), attempt 2 (ai/probes e1d70631) and the task quoted verbatim (17 lines)"
          f"{'; missing ' + str(miss) if miss else ''}")


# ---------------------------------------------------------------- S: symbols of the two couplings
z = sp.Symbol("z", nonzero=True)          # z = exp(i k)
b, ell = sp.symbols("b ell", positive=True)
SIN = (z - 1 / z) / (2 * sp.I)
COS = (z + 1 / z) / 2


def family_s() -> None:
    P2 = (z ** 2 - z ** -2) / (4 * sp.I)                     # two-step momentum P = S C
    Cb = b * COS                                            # C[b] for a uniform bond field b
    s_r3 = SIN + Cb * P2                                    # S + (1/2){C[b], P}, the two commute for uniform b
    ok1 = sp.simplify(s_r3 - SIN * (1 + b * COS ** 2)) == 0
    sig = SIN * (COS ** 2 + ell * SIN ** 2)
    ok2 = sp.simplify(ell * (SIN * (1 + (1 / ell - 1) * COS ** 2)) - sig) == 0
    ok3 = sp.simplify(s_r3.subs(z, -z) + s_r3) == 0 and sp.simplify(P2.subs(z, -z) - P2) == 0
    check("S1", ok1 and ok2 and ok3, "reach three: symbol of S_a + (1/2){C_a[b], P_a} is s_a = sin k_a (1 + b cos^2 k_a); with 1 + b = 1/l, "
          "l s_a = sin k_a (cos^2 k_a + l sin^2 k_a); both couplings' symbols change sign under k -> k + pi (odd reach)")
    # operator level on a 6 x 6 torus: uniform rational fields, plane wave at k = (2 pi/6)(1, 2)
    L = 6
    w, chi, m = R_(67, 101), R_(3, 2), R_(2)
    lb = chi * chi
    bb = 1 / lb - 1
    sx = sp.Matrix([[0, 1], [1, 0]])
    sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    kv = (2 * sp.pi / L, 4 * sp.pi / L)
    ok_all = True
    for cp in ("frame", "reach3"):
        def Hpsi(psi):                                      # psi[(i, j)] -> 2-vector
            out = {}
            for (i, j), v in psi.items():
                acc = sp.zeros(2, 1)
                for a, sg in ((0, sx), (1, sy)):
                    def at(dd):
                        ii, jj = ((i + dd, j) if a == 0 else (i, j + dd))
                        return psi[(ii % L, jj % L)]
                    if cp == "frame":
                        hop = (w / lb) * (at(1) - at(-1)) / (2 * sp.I)
                    else:
                        S1v = (at(1) - at(-1)) / (2 * sp.I)
                        # (1/2){C[b], P}: C[b] P + P C[b] with P = (T^2 - T^-2)/(4i), C[b] = b (T + T^-1)/2 (uniform)
                        D = bb * ((at(3) - at(-1)) + (at(1) - at(-3))) / (8 * sp.I)
                        hop = w * (S1v + D)
                    acc += sg * hop
                out[(i, j)] = acc + m * w * (-1) ** (i + j) * v
            return out
        for u in (sp.Matrix([1, 0]), sp.Matrix([0, 1])):
            psi = {(i, j): sp.exp(sp.I * (kv[0] * i + kv[1] * j)) * u for i in range(L) for j in range(L)}
            hp = Hpsi(psi)
            s1 = [sp.sin(k) / lb if cp == "frame" else sp.sin(k) * (1 + bb * sp.cos(k) ** 2) for k in kv]
            for (i, j) in [(0, 0), (1, 3), (5, 2)]:
                expect = w * (sx * s1[0] + sy * s1[1]) * psi[(i, j)] + m * w * (-1) ** (i + j) * psi[(i, j)]
                ok_all &= all(sp.simplify(sp.expand_complex(e)) == 0 for e in (hp[(i, j)] - expect))
    # anticommutation of eps with every hop: all hop entries join opposite parities (both couplings reach 1 or 3)
    check("S2", ok_all, "operator level, 6x6 torus, w = 67/101, l = 9/4, m = 2, k = (2pi/6)(1,2): H psi = w[sigma.s(k) + m eps] psi "
          "for both couplings; every hop moves 1 or 3 steps, so eps anticommutes with it and E^2 = w^2 (m^2 + |s|^2) (block 77 T3)")


# ---------------------------------------------------------------- A: the acceleration law at every wave number
x, y, k1, k2 = sp.symbols("x y k1 k2", real=True)
gw, gl, wc, lc, m_ = sp.symbols("g_w g_l w_c l_c m", positive=True)


def s_of(k, lv, cp):
    return sp.sin(k) / lv if cp == "frame" else sp.sin(k) * (1 + (1 / lv - 1) * sp.cos(k) ** 2)


def pb(f, E):
    return sum(sp.diff(f, q) * sp.diff(E, p) - sp.diff(f, p) * sp.diff(E, q) for q, p in ((x, k1), (y, k2)))


def accel(cp, nh, carrier, mass, lval):
    X = nh[0] * x + nh[1] * y
    wv = wc * sp.exp(gw * X)
    lv = lval * sp.exp(gl * X)
    s1, s2 = s_of(k1, lv, cp), s_of(k2, lv, cp)
    E = wv * sp.sqrt(mass ** 2 + s1 ** 2 + s2 ** 2)
    Xn = nh[0] * x + nh[1] * y
    a = pb(pb(Xn, E), E)
    a = a.subs({x: 0, y: 0})
    return a, carrier


def A_rho(cp, k, lv, trig=None):
    s = s_of(k, ell, cp)
    A = ell ** 2 * (sp.diff(s, k) ** 2 + s * sp.diff(s, k, 2))
    rho = -ell * sp.diff(sp.log(s), ell)
    if trig is not None:                                     # exact values at rational sin, cos
        return sp.nsimplify(sp.simplify(A.subs(trig).subs(ell, lv))), sp.nsimplify(sp.simplify(rho.subs(trig).subs(ell, lv)))
    return sp.simplify(A.subs(ell, lv)), sp.simplify(rho.subs(ell, lv))


def family_a() -> None:
    kk = sp.Symbol("k", positive=True)
    t = R_(1, 10)
    S, C = 2 * t / (1 + t ** 2), (1 - t ** 2) / (1 + t ** 2)          # kappa = 2 arctan(1/10)
    trig = {sp.sin(k1): S, sp.cos(k1): C, sp.sin(k2): S, sp.cos(k2): C}
    rs = []
    ok = True
    for cp in ("frame", "reach3"):
        # slow body at rest: n.a = -(w/l)^2 d_n log w
        a, _ = accel(cp, (0, 1), None, m_, lc)
        a = sp.simplify(a.subs({k1: 0, k2: 0}))
        ok &= sp.simplify(a + (wc / lc) ** 2 * gw) == 0
        # axis ray, carrier (kappa, 0), gradient along y: A = 1, rho = rho_a (symbolic l)
        a, _ = accel(cp, (0, 1), None, 0, lc)
        a = sp.simplify(a.subs({k2: 0}).subs({sp.sin(k1): S, sp.cos(k1): C}))
        _, rho = A_rho(cp, kk, lc, {sp.sin(kk): S, sp.cos(kk): C})
        pred = -(wc / lc) ** 2 * (gw - rho * gl)                # A = 1: the transverse axis carries no wave number
        ok &= sp.simplify(a - pred) == 0
        # diagonal ray, carrier (kappa, kappa), gradient along (1, -1)/sqrt2, at l = 9/4
        nh = (1 / sp.sqrt(2), -1 / sp.sqrt(2))
        a, _ = accel(cp, nh, None, 0, R_(9, 4))
        a = sp.simplify(a.subs(trig))
        A9, r9 = A_rho(cp, kk, R_(9, 4), {sp.sin(kk): S, sp.cos(kk): C})
        pred = -(wc / R_(9, 4)) ** 2 * A9 * (gw - r9 * gl)
        ok &= sp.simplify(a - pred) == 0
        rs.append((A9, r9))
    check("A1", ok, "Hamilton's equations for E = w sqrt(m^2 + |s(k; l)|^2) with log-linear w, l: slow body -(w/l)^2 d log w (both); "
          "a ray crossing the gradient -(w/l)^2 A [d log w - rho d log l]: axis carrier A = 1 for both, rho = 1 (frame), rho_a "
          "(reach three, symbolic l); diagonal carrier at l = 9/4, tan(kappa/2) = 1/10, exact")
    Af, _ = A_rho("frame", kk, ell)
    A3, r3 = A_rho("reach3", kk, ell)
    okf = sp.simplify(Af - sp.cos(2 * kk)) == 0
    okr = sp.simplify(r3 - sp.cos(kk) ** 2 / (sp.cos(kk) ** 2 + ell * sp.sin(kk) ** 2)) == 0
    ser = sp.expand(sp.series(A3, kk, 0, 6).removeO())
    oks = sp.simplify(ser - (1 + (12 * ell - 14) * kk ** 2 + (15 * ell ** 2 - 50 * ell + R_(107, 3)) * kk ** 4)) == 0
    # group speed along an axis in units of the long-wave speed w/l: l s' = cos k (1 + 3(l - 1) sin^2 k)
    s3 = s_of(kk, ell, "reach3")
    spd = sp.simplify(ell * sp.diff(s3, kk) - sp.cos(kk) * (1 + 3 * (ell - 1) * sp.sin(kk) ** 2)) == 0
    sser = sp.expand(sp.series(ell * sp.diff(s3, kk), kk, 0, 4).removeO())
    oksp = sp.simplify(sser - (1 + (3 * ell - R_(7, 2)) * kk ** 2)) == 0
    cc = sp.Symbol("c", positive=True)
    f94 = cc * (1 + 3 * (R_(9, 4) - 1) * (1 - cc ** 2))
    crit = sp.solve(sp.diff(f94, cc), cc)
    vmax = sp.nsimplify(f94.subs(cc, crit[0]))
    okv = crit[0] ** 2 == R_(19, 45) and sp.simplify(vmax - R_(19, 6) * sp.sqrt(R_(19, 45))) == 0
    # the O(k^4) anisotropy of |s|^2 = sum s_a^2 vanishes iff l = 7/6
    q4 = sp.expand(sp.series(s3 ** 2, kk, 0, 6).removeO()).coeff(kk, 4)
    ok76 = sp.solve(sp.Eq(q4, 0), ell) == [R_(7, 6)]
    # small-kappa diagonal ratio at R = 3: A_a (1 + 2 rho_a) = 3 + (34 l - 42) kappa^2 + O(kappa^4)
    rser = sp.expand(sp.series(A3 * (1 + 2 * r3), kk, 0, 4).removeO())
    ok2117 = sp.simplify(rser - (3 + (34 * ell - 42) * kk ** 2)) == 0
    check("A2", okf and okr and oks and spd and oksp and okv and ok76 and ok2117,
          "frame: l^2(s'^2 + s s'') = cos 2k, so A = sum n_a^2 cos 2k_a <= 1; reach three: rho_a = cos^2 k/(cos^2 k + l sin^2 k), "
          "A_a = 1 + (12l - 14)k^2 + (15l^2 - 50l + 107/3)k^4 + ...; l s' = cos k (1 + 3(l-1) sin^2 k) = 1 + (3l - 7/2)k^2 + ...; "
          "max at l = 9/4 is (19/6)sqrt(19/45) at cos^2 k = 19/45; quartic anisotropy of |s|^2 vanishes only at l = 7/6; "
          "diagonal at R = 3: 3 + (34l - 42)kappa^2")
    return rs


# ---------------------------------------------------------------- B: block 60's one-body field
def family_b(rs) -> None:
    Q, g, g0, G = sp.symbols("Q g g_0 G", positive=True)
    w0 = 1 / (1 + 2 * Q * g0)
    chi, N = 1 + Q * g, 1 - Q * w0 * g
    lw, ll = sp.log(N / chi), sp.log(chi ** 2)
    Rloc = sp.simplify(1 - sp.diff(ll, g) / sp.diff(lw, g))
    wv = N / chi
    ok1 = sp.simplify(Rloc - (2 + 3 * Q * g0 - Q * g) / (1 + Q * g0)) == 0 and sp.simplify(Rloc - (1 + 2 * wv / (wv + w0))) == 0
    W = sp.Symbol("W", real=True)
    Rfar = (3 + W) / (1 + W)
    okm = sp.simplify(Rfar - 1 - 2 / (1 + W)) == 0 and sp.simplify(3 - Rfar - 2 * W / (1 + W)) == 0
    mu = sp.Symbol("mu", real=True)
    r = sp.sqrt(1 + 4 * g0 * mu)
    roots = [(-1 + r) / (2 * g0), (-1 - r) / (2 * g0)]
    okr = all(sp.simplify(q_ * (1 + q_ * g0) - mu) == 0 for q_ in roots) and \
        sp.simplify(1 / (1 + 2 * roots[0] * g0) - 1 / r) == 0 and sp.simplify(1 / (1 + 2 * roots[1] * g0) + 1 / r) == 0 and \
        sp.simplify(Rfar.subs(W, 1 / r) - (1 + 2 * r / (1 + r))) == 0
    check("B1", ok1 and okm and okr, "long waves: R = 1 - dlog l/dlog w = (2 + 3Qg0 - Qg)/(1 + Qg0) = 1 + 2w/(w + w0) (attempt 2's "
          "formula); far R = (3 + w0)/(1 + w0) = 1 + 2/(1 + w0), 3 - R = 2w0/(1 + w0): R in (1, 3) iff w0 > 0; roots of "
          "Q(1 + Qg0) = mu have w0 = +-1/r, the + root is block 71's 1 + 2r/(1 + r)")
    # the witness: the point Qg = 1/2 (l = 9/4), diagonal carrier tan(kappa/2) = 1/10, reach three
    A9, r9 = rs[1]
    Af9, _ = rs[0]
    w0G = 1 / (1 + 2 * G)
    wpt = (1 - w0G / 2) / R_(3, 2)
    Rpt = sp.simplify(1 + 2 * wpt / (wpt + w0G))
    okR = sp.simplify(Rpt - 3 / (1 + w0G)) == 0 and sp.simplify(Rpt - 3 * (2 * G + 1) / (2 * (G + 1))) == 0
    ratio = sp.factor(A9 * (1 + r9 * (Rpt - 1)))
    Gs = sp.solve(sp.Eq(ratio, 3), G)
    r50, rinf = ratio.subs(G, 50), sp.limit(ratio, G, sp.oo)
    ok_nums = A9 == R_(1606444785801, 1061520150601) and r9 == R_(1089, 1189) and len(Gs) == 1 and Gs[0] == \
        R_(667780227338489, 1081638144398800) and r50 == R_(182153167817189589, 42913013608196026) and \
        rinf == R_(5408899593791967, 1262147459064589) and sp.simplify(sp.diff(ratio, G)) > 0
    t = R_(1, 10)
    S, C = 2 * t / (1 + t ** 2), (1 - t ** 2) / (1 + t ** 2)
    bb = 1 / R_(9, 4) - 1
    spd = R_(9, 4) * C * (1 + bb * (3 * C ** 2 - 2))            # diagonal group speed / (w/l) = l s'(kappa)
    ang50, anginf = r50 / spd ** 2, rinf / spd ** 2
    okang = spd == R_(1158399, 1030301) and ang50 > 3 and anginf > 3
    frame9 = sp.simplify(Af9 * Rpt.subs(G, 50))
    g1000 = ratio.subs(G, 1000)
    okR = okR and g1000 == R_(1606444785801 * 6737467, 2524294918129178 * 1001)
    check("B2", okR and ok_nums and okang,
          f"witness (reach three, l = 9/4 at Qg = 1/2 where R = 3/(1 + w0), carrier (kappa, kappa, 0), tan(kappa/2) = 1/10, gradient "
          f"along (1,-1,0)): A = {A9} = {float(A9):.4f}, rho = {r9}; ratio(G = Qg0) increasing, above 3 for G > "
          f"{float(Gs[0]):.4f}; G = 50: {float(r50):.4f}; G = 1000: {float(g1000):.4f}; G -> oo: {float(rinf):.4f}; speed l s' = {spd} = {float(spd):.4f} of w/l, "
          f"deflection per length over fall at w/l {float(ang50):.3f} (G = 50), {float(anginf):.3f} (G -> oo); frame there "
          f"{float(frame9):.4f}")


def family_b3() -> None:
    t = R_(3, 10)
    S, C = 2 * t / (1 + t ** 2), (1 - t ** 2) / (1 + t ** 2)
    A = C ** 2 - S ** 2                                        # frame, diagonal carrier: A = cos 2 kappa
    W = sp.Symbol("W", positive=True)
    Rfar = (3 + W) / (1 + W)
    wstar = sp.solve(sp.Eq(A * Rfar, 1), W)
    G = sp.Symbol("G", positive=True)
    Gstar = sp.solve(sp.Eq(1 / (1 + 2 * G), wstar[0]), G)
    ok = A == R_(4681, 11881) and len(wstar) == 1 and sp.simplify((A * Rfar).subs(W, 1) - 2 * A) == 0 and 2 * A < 1
    check("B3", ok, f"frame, diagonal carrier tan(kappa/2) = 3/10: A = cos 2kappa = {A} = {float(A):.4f}; far from a body the ratio "
          f"A(3 + w0)/(1 + w0) is below 1 iff w0 > {wstar[0]} = {float(wstar[0]):.4f}, i.e. Qg0 < {float(Gstar[0]):.4f}, and 2A < 1 at "
          "first order: below 1 at weak field")


# ---------------------------------------------------------------- C: long-wave straight-line bending and fall, closed forms
def family_c() -> None:
    tt = sp.Symbol("t", real=True)
    a_ = sp.Symbol("a", real=True)
    bq = sp.Symbol("b", positive=True)
    F = 2 / sp.sqrt(bq ** 2 - a_ ** 2) * sp.atan(sp.sqrt((bq - a_) / (bq + a_)) * sp.tanh(tt / 2))
    d = sp.diff(F, tt) - 1 / (bq * sp.cosh(tt) + a_)
    pts = [(R_(3), R_(1), R_(1, 2)), (R_(7, 2), R_(-2), R_(-3)), (R_(5), R_(9, 2), R_(2)), (R_(2), R_(-1, 3), R_(7))]
    ok1 = all(abs(sp.N(d.subs({bq: B, a_: A, tt: T}), 60)) < sp.Float("1e-50") for B, A, T in pts)
    J = lambda A, B: -sp.pi + 2 * B / sp.sqrt(B ** 2 - A ** 2) * sp.acos(A / B)
    # direct quadrature of J at a rational point, 40 digits
    A0, B0 = R_(1, 3), R_(2)
    quad = sp.N(sp.Integral(-A0 * B0 / ((sp.sqrt(B0 ** 2 + tt ** 2)) ** 2 * (sp.sqrt(B0 ** 2 + tt ** 2) + A0)),
                            (tt, -sp.oo, sp.oo)), 40)
    ok2 = abs(quad - sp.N(J(A0, B0), 40)) < 1e-30
    q, p, u = sp.symbols("q p u", positive=True)
    Bb = -3 * J(q, 1 / u) + J(-p, 1 / u)                       # straight-line bending of the long-wave ray, b = 1/u
    Fb = J(-p, 1 / u) - J(q, 1 / u)                            # straight-line fall
    lim = sp.simplify(sp.limit(Bb / Fb, u, 0))
    ok3 = sp.simplify(lim - (3 * q + p) / (q + p)) == 0
    check("C1", ok1 and ok2 and ok3, "long waves in the continuum far field chi = 1 + q/r, N = 1 - p/r (q = Q/4pi, p = w0 q): "
          "int dt/(b cosh t + a) antiderivative verified; J(a, b) = -pi + (2b/sqrt(b^2 - a^2)) arccos(a/b) = int d_b log(1 + a/r) ds "
          "(40-digit quadrature); bending(b) = -3J(q,b) + J(-p,b), fall(b) = J(-p,b) - J(q,b), ratio -> (3q + p)/(q + p) as b -> oo")


# ---------------------------------------------------------------- E: floating-point controls (labelled)
def build(N, logw, logl, coupling, m=0.0):
    import scipy.sparse as sps
    n = N * N
    w = np.exp(logw).ravel(order="F")
    chi = np.sqrt(np.exp(logl)).ravel(order="F")
    idx = np.arange(n).reshape((N, N), order="F")
    s1 = np.array([[0, 1], [1, 0]], complex)
    s2 = np.array([[0, -1j], [1j, 0]])
    H = sps.csr_matrix((2 * n, 2 * n), dtype=complex)
    phi = np.sqrt(w)
    for a, sg in ((0, s1), (1, s2)):
        if a == 0:
            src, dst, src2, dst2 = idx[:-1, :].ravel(), idx[1:, :].ravel(), idx[:-2, :].ravel(), idx[2:, :].ravel()
        else:
            src, dst, src2, dst2 = idx[:, :-1].ravel(), idx[:, 1:].ravel(), idx[:, :-2].ravel(), idx[:, 2:].ravel()
        if coupling == "frame":
            tb = np.sqrt(w[src] * w[dst]) / (chi[src] * chi[dst])
            Sa = sps.csr_matrix((tb / (2j), (src, dst)), shape=(n, n))
            Sa = Sa + Sa.conj().T
        else:
            T1 = sps.csr_matrix((np.ones(len(src)), (src, dst)), shape=(n, n))
            T2 = sps.csr_matrix((np.ones(len(src2)), (src2, dst2)), shape=(n, n))
            Cb = sps.csr_matrix(((1.0 / (chi[src] * chi[dst]) - 1.0) / 2, (src, dst)), shape=(n, n))
            Cb = Cb + Cb.T
            P = (T2 - T2.T) / (4j)
            Ph = sps.diags(phi)
            Sa = Ph @ ((T1 - T1.T) / (2j) + 0.5 * (Cb @ P + P @ Cb)) @ Ph
        H = H + sps.kron(Sa, sg, format="csr")
    if m:
        eps = (1 - 2 * (((idx % N) + (idx // N)) % 2)).ravel(order="F").astype(float)
        H = H + sps.kron(sps.diags(m * w * eps), np.eye(2), format="csr")
    return H.tocsr()


def packet(N, xc, k0, sig, lc_, coupling, massive):
    X, Y = np.meshgrid(np.arange(N), np.arange(N), indexing="ij")
    env = np.exp(-((X - xc[0]) ** 2 + (Y - xc[1]) ** 2) / (4 * sig ** 2)) * np.exp(1j * (k0[0] * X + k0[1] * Y))
    if massive:
        p0, p1 = env * ((X + Y) % 2 == 0), np.zeros_like(env)
    else:
        Fk = np.fft.fft2(env)
        kx = 2 * np.pi * np.fft.fftfreq(N)[:, None] * np.ones((1, N))
        ky = 2 * np.pi * np.fft.fftfreq(N)[None, :] * np.ones((N, 1))
        sym = (lambda k: np.sin(k) / lc_) if coupling == "frame" else (lambda k: np.sin(k) * (1 + (1 / lc_ - 1) * np.cos(k) ** 2))
        th = np.angle(sym(kx) + 1j * sym(ky))
        p0, p1 = np.fft.ifft2(Fk / np.sqrt(2)), np.fft.ifft2(Fk * np.exp(1j * th) / np.sqrt(2))
    psi = np.empty(2 * N * N, complex)
    psi[0::2], psi[1::2] = p0.ravel(order="F"), p1.ravel(order="F")
    return psi / np.linalg.norm(psi)


def measure(N, logw, logl, cp, nh, k0, sig, massive, wcen, T=120.0, nt=41):
    from scipy.sparse.linalg import expm_multiply
    X, Y = np.meshgrid(np.arange(N), np.arange(N), indexing="ij")
    xc = ((N - 1) / 2, (N - 1) / 2)
    H = build(N, logw, logl, cp, 1.0 if massive else 0.0)
    psi = packet(N, xc, k0, sig, 9 / 4, cp, massive)
    if massive:                                            # first-order projection on positive energy, E ~ w m
        psi = psi + (H @ psi) / wcen
        psi /= np.linalg.norm(psi)
    dn = np.repeat((nh[0] * (X - xc[0]) + nh[1] * (Y - xc[1])).ravel(order="F"), 2)
    out = expm_multiply(-1j * H, psi, start=0, stop=T, num=nt, endpoint=True)
    nn = np.array([np.real(np.vdot(pv, dn * pv)) for pv in out])
    return 2 * np.polyfit(np.linspace(0, T, nt), nn, 3)[1]


def family_e() -> None:
    t0 = time.time()
    kap = 2 * np.arctan(0.1)
    r2 = np.sqrt(0.5)
    A9, r9 = 1606444785801 / 1061520150601, 1089 / 1189
    # E1: straight-line deflection over fall at w/l for the witness ray, G = 1000, continuum far field (b in units of q)
    from scipy.integrate import quad
    S, C = np.sin(kap), np.cos(kap)
    G = 1000.0
    w0 = 1 / (1 + 2 * G)

    def loc(yv):
        lv = (1 + yv) ** 2
        wv = (1 - w0 * yv) / (1 + yv)
        Rv = 1 + 2 * wv / (wv + w0)
        bb = 1 / lv - 1
        s = S * (1 + bb * C ** 2)
        sp1 = C * (1 + bb * (3 * C ** 2 - 2))
        spp = -S * (1 + bb) - 3 * bb * (2 * S * C ** 2 - S ** 3)
        A = lv ** 2 * (sp1 ** 2 + s * spp)
        rho = C ** 2 / (C ** 2 + lv * S ** 2)
        return A * (1 + rho * (Rv - 1)) / (lv * sp1) ** 2

    def line(bq):
        wt = lambda u: (w0 / (1 - w0 / np.hypot(bq, u)) + 1 / (1 + 1 / np.hypot(bq, u))) * bq / np.hypot(bq, u) ** 3
        num = quad(lambda u: wt(u) * loc(1 / np.hypot(bq, u)), -np.inf, np.inf, limit=400)[0]
        return num / quad(wt, -np.inf, np.inf, limit=400)[0]
    vals = [(bq, line(bq)) for bq in (1, 2, 4, 5, 20)]
    check("E1", vals[2][1] > 3 > vals[3][1] and vals[4][1] < 3,
          "FLOATING, straight line in the plane of the carrier, G = 1000, witness ray (deflection per length over fall at w/l): "
          + ", ".join(f"b = {bq}q {v:.3f}" for bq, v in vals) + "; long waves stay below 3 (C1); b < 6.75q is inside the long-wave "
          "capture radius (attempt 2), so there the straight line is formal")
    # E2: packets in a patch with uniform log-gradients at the witness point's values (G = 50), extrapolated in 1/sigma^2
    Rw, wcen, lc_ = 101 / 34, 67 / 101, 9 / 4
    gwv = 2.5e-4
    pred = {("reach3", "dg"): A9 * (1 + r9 * (Rw - 1)), ("reach3", "ax"): 1 + r9 * (Rw - 1),
            ("frame", "dg"): np.cos(2 * kap) * Rw, ("frame", "ax"): Rw}
    res = {}
    for N, sig in ((261, 24), (321, 32)):
        Xg, Yg = np.meshgrid(np.arange(N), np.arange(N), indexing="ij")
        c0 = (N - 1) / 2
        for cp in ("reach3", "frame"):
            for nm, nh, k0 in (("dg", (r2, -r2), (kap, kap)), ("ax", (0, 1), (kap, 0))):
                dn = nh[0] * (Xg - c0) + nh[1] * (Yg - c0)
                lw_, ll_ = np.log(wcen) + gwv * dn, np.log(lc_) - (Rw - 1) * gwv * dn
                af = measure(N, lw_, ll_, cp, nh, (0, 0), sig, True, wcen)
                ar = measure(N, lw_, ll_, cp, nh, k0, sig, False, wcen)
                res[(cp, nm, sig)] = ar / af
    ext = {key: res[key + (32,)] - (res[key + (32,)] - res[key + (24,)]) / (1 / 32 ** 2 - 1 / 24 ** 2) / 32 ** 2 for key in pred}
    ok2 = all(abs(ext[kk_] / pred[kk_] - 1) < 0.01 for kk_ in pred)
    check("E2", ok2, "FLOATING, lattice packets (sigma 24, 32 -> infinity) in a patch with the witness point's l, w and log-gradients "
          "(G = 50): " + ", ".join(f"{a} {bq} {ext[(a, bq)]:.3f} (ray {pred[(a, bq)]:.3f})" for a, bq in pred))
    # E3: packets in a window of the exact strong field (G = 1000, continuum g = 1/(4 pi r)), body outside the window
    q, G3 = 315.0, 1000.0
    w03 = 1 / (1 + 2 * G3)
    R3 = 3 / (1 + w03)
    pred3 = {("reach3", "dg"): A9 * (1 + r9 * (R3 - 1)), ("reach3", "ax"): 1 + r9 * (R3 - 1),
             ("frame", "dg"): np.cos(2 * kap) * R3, ("frame", "ax"): R3}
    res3 = {}
    for N, sig in ((261, 24), (321, 32)):
        Xg, Yg = np.meshgrid(np.arange(N), np.arange(N), indexing="ij")
        c0 = (N - 1) / 2
        for cp in ("reach3", "frame"):
            for nm, nh, k0 in (("dg", (r2, -r2), (kap, kap)), ("ax", (0, 1), (kap, 0))):
                yv = q / np.hypot(Xg - (c0 - 2 * q * nh[0]), Yg - (c0 - 2 * q * nh[1]))
                lw_, ll_ = np.log1p(-w03 * yv) - np.log1p(yv), 2 * np.log1p(yv)
                af = measure(N, lw_, ll_, cp, nh, (0, 0), sig, True, (1 - w03 / 2) / 1.5)
                ar = measure(N, lw_, ll_, cp, nh, k0, sig, False, (1 - w03 / 2) / 1.5)
                res3[(cp, nm, sig)] = ar / af
    ext3 = {key: res3[key + (32,)] - (res3[key + (32,)] - res3[key + (24,)]) / (1 / 32 ** 2 - 1 / 24 ** 2) / 32 ** 2 for key in pred3}
    ok3 = all(abs(ext3[kk_] / pred3[kk_] - 1) < 0.01 for kk_ in pred3)
    check("E3", ok3, "FLOATING, packets on a slice window of the exact one-body field, Qg0 = 1000, at r = 2q (Qg = 1/2): "
          + ", ".join(f"{a} {bq} {ext3[(a, bq)]:.3f} ({pred3[(a, bq)]:.3f})" for a, bq in pred3) + f"; {time.time() - t0:.0f} s")


def main() -> None:
    t0 = time.time()
    family_q()
    family_s()
    rs = family_a()
    family_b(rs)
    family_b3()
    family_c()
    family_e()
    print("\n".join(OUT))
    print(f"families Q S A B C (exact) and E (floating): {len(OUT) - len(FAILS)}/{len(OUT)} ok, {time.time() - t0:.0f} s")
    if FAILS:
        print(f"SUMMARY: ROUTE FAILS AT {FAILS[0]}")
        return
    print("SUMMARY: PARTIAL exact finite-wave-number law of bending over fall in block 60's one-body field: a ray of carrier k "
          "crossing the gradient bends A[1 + rho(R - 1)] times the fall, R = 1 + 2w/(w + w0) the long-wave ratio; block 60's bond "
          "crossing has rho = 1, A = sum n_a^2 cos 2k_a <= 1 (never above R, below 1 for short off-axis waves); block 69's reach-three "
          "coupling has A = 1 + (12l - 14) sum n_a^2 k_a^2 + ..., so off-axis rays where l > 21/17 near a strong body exceed 3")
    print("HIT: under block 69's reach-three coupling of block 60's lengths (1 + b = 1/l) the ray law is E = w|sigma|/l, sigma_a = "
          "sin k_a (cos^2 k_a + l sin^2 k_a), and a ray crossing the gradient bends A[1 + rho(R - 1)] times a slow body's fall, "
          "A = l^2 sum n_a^2 (s_a'^2 + s_a s_a'') = 1 + (12l - 14) sum n_a^2 k_a^2 + O(k^4), rho = sum (s_a^2/|s|^2) cos^2 k_a/"
          "(cos^2 k_a + l sin^2 k_a); at the point Qg = 1/2 (r = Q/2pi) of a body with Qg0 = 1000 a ray of carrier (kappa, kappa, 0), "
          "tan(kappa/2) = 1/10, crossing the gradient in its plane has bending over fall 4.283 (4.2855 as Qg0 grows; packets on a "
          "slice window of that field 4.295), above 3; block 60's bond crossing gives A = sum n_a^2 cos 2k_a <= 1: never above "
          "the long-wave value, below 1 for short off-axis waves")


if __name__ == "__main__":
    main()
