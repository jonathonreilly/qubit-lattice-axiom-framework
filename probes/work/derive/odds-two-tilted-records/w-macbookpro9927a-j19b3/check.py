#!/usr/bin/env python3
"""Two tilted records: checks for ATTEMPT.md (attempt 1 of 2), worker w-macbookpro9927a-j19b3 (claude-opus-5-5).

Objects (blocks 42, 103): sphere menu, K1 f(s) = int e^{beta s.b} f dsigma/Z; the ordered sea F = (K1F)^6/<(K1F)^6>, g = K1 F;
unformed odds pi_x ~ prod_y (K1 pi_y); the site normalizer Z_x = <prod_y g_y> (block 42 T4(b)); a tilted record held as a
boundary value of the turn field (block 103 T4). Exact: the integration-by-parts identity, the direct coefficient, the lattice
identity for the neighbourhood variance (4^3 torus, Fractions). Floating point, labelled: the response R(k) and the nonlinear solver.
"""
from __future__ import annotations

import itertools
import json
import math
import subprocess
import sys
from fractions import Fraction as Fr

import numpy as np
import sympy as sp

OUT: list[str] = []
FAILS: list[str] = []


def check(tag: str, ok: bool, msg: str) -> None:
    OUT.append(f"{'ok  ' if ok else 'FAIL'} {tag}: {msg}")
    if not ok:
        FAILS.append(tag)


B103 = ("ff6da653b1", "docs/ADMISSIBILITY_RULE_POSSIBILITYS_ODDS_CARRY_CONTENT_NOT_RECORD_COUNT_AT_LONG_RANGE_A_MASSLESS_TURN_CHANNEL_IN_THE_"
        "ORDERED_SEA_BOUNDED_THEOREM_NOTE_2026-09-23.md")
B103_Q = ["In the linearized turn channel, hold the records of a body `S` at a common tilt `u₀`, as a boundary value (block 42 T6).",
          "So `u = u₀h_S`, where `h_S(x)` is the probability that a simple walk from `x` reaches `S`",
          "Its linearization is `η_x = Σ_y(Aη_y − ⟨Aη_y⟩_F)`, with `Aη = K₁(Fη)/g` and `g = K₁F`."]
TASK_Q = ["(a) Exactly at second order in the turn field: the normalizer of an unformed site at distance r from ONE tilted record, its law in "
          "r on Z^3 and its sign (is formation favoured or disfavoured near a tilted record?).",
          "against block 41 T4's quadratic model -kappa ab G(r)/(G(0)^2 - G(r)^2) (like attract)"]


def family_q() -> None:
    txt = subprocess.run(["git", "show", f"{B103[0]}:{B103[1]}"], capture_output=True, text=True).stdout
    d = json.load(open("probes/TASKS.json"))
    ts = d if isinstance(d, list) else d.get("tasks", d)
    ts = ts if isinstance(ts, list) else list(ts.values())
    what = next((t["what"] for t in ts if isinstance(t, dict) and t.get("id") == "J:derive:odds-two-tilted-records:a1"), "")
    miss = [f"b103[{i}]" for i, q in enumerate(B103_Q) if q not in txt] + [f"task[{i}]" for i, q in enumerate(TASK_Q) if q not in what]
    check("Q", not miss, f"block 103 (head ff6da653, PR #8919) and the task quoted verbatim ({len(B103_Q) + len(TASK_Q)} lines)"
          f"{'; missing ' + str(miss) if miss else ''}")


# ------------------------------------------------------------------------------------------------ A: the local second-order algebra
def family_a() -> None:
    t = sp.Symbol("t", real=True)
    ok = True
    for gexpr in (1 + t + t ** 2 / 3, sp.exp(2 * t) * (1 + t ** 2)):
        g = gexpr
        gp, gpp = sp.diff(g, t), sp.diff(g, t, 2)
        avg = lambda f: sp.integrate(f, (t, -1, 1)) / 2
        A1 = avg(g ** 5 * gp * t); A2 = avg(g ** 5 * gpp * (1 - t ** 2)); A3 = avg(g ** 4 * gp ** 2 * (1 - t ** 2)); Z0 = avg(g ** 6)
        ok &= sp.simplify(A2 - (2 * A1 - 5 * A3)) == 0 or abs(float(A2 - 2 * A1 + 5 * A3)) < 1e-12
        c = -(gp / g) * t / 2 + sp.diff(sp.log(g), t, 2) * (1 - t ** 2) / 4
        Fc = avg(g ** 6 * c) / Z0
        ok &= abs(float(Fc + sp.Rational(3, 2) * A3 / Z0)) < 1e-12
    # the product over six neighbours at second order: numerically for one concrete g and random small tilts
    rng = np.random.default_rng(3)
    tq, wq = np.polynomial.legendre.leggauss(80); ph = np.linspace(0, 2 * np.pi, 96, endpoint=False)
    T, P = np.meshgrid(tq, ph, indexing="ij"); Wt = np.repeat(wq / 2, 96).reshape(80, 96) / 96
    s = np.stack([np.sqrt(1 - T ** 2) * np.cos(P), np.sqrt(1 - T ** 2) * np.sin(P), T], -1)
    gf = lambda u: np.exp(2 * u) * (1 + u ** 2)
    g1 = lambda u: np.exp(2 * u) * (2 * (1 + u ** 2) + 2 * u)
    Z0n = np.sum(Wt * gf(T) ** 6)
    A3n = np.sum(Wt * gf(T) ** 4 * g1(T) ** 2 * (1 - T ** 2))
    th = rng.normal(size=(6, 2)) * 1e-3
    ns = [np.array([a, b, 1.0]) / math.sqrt(1 + a * a + b * b) for a, b in th]
    Zn = np.sum(Wt * np.prod([gf(s @ n) for n in ns], axis=0))
    V = np.sum((th - th.mean(0)) ** 2)
    ok &= abs((Zn / Z0n - 1) / (-1.5 * A3n / Z0n * V) - 1) < 2e-3
    check("A", ok, "local algebra: A2 = 2A1 - 5A3 by parts (A1 = <g^5 g' t>, A2 = <g^5 g'' (1-t^2)>, A3 = <g^4 g'^2 (1-t^2)>; two g, exact), "
          "so rotation invariance leaves Z_x/Z0 = 1 - (3A3/(2Z0)) V_x, V_x = sum_y |theta_y - thetabar_x|^2 (checked numerically for six random "
          "tilts); the site's m = 0 source is c(t) V_x with c = -(g'/g)t/2 + (log g)''(1-t^2)/4 and <Fc> = -3A3/(2Z0) exactly")


# ------------------------------------------------------------------------------------------------ B: the lattice identity
def torus4_G():
    cs = [1, 0, -1, 0]
    sites = list(itertools.product(range(4), repeat=3))
    G = {}
    for k in sites:
        tot = Fr(0)
        for qv in sites:
            if qv != (0, 0, 0):
                tot += Fr(cs[(qv[0] * k[0] + qv[1] * k[1] + qv[2] * k[2]) % 4], sum(2 - 2 * cs[c] for c in qv))
        G[k] = tot / 64
    return G, sites


def family_b() -> None:
    G, sites = torus4_G()
    E6 = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    sh = lambda a, b: tuple((x + y) % 4 for x, y in zip(a, b))
    ok = True
    for S1, S2, q1, q2 in (((0, 0, 0), (2, 1, 0), Fr(3), Fr(-3)), ((0, 0, 0), (1, 0, 0), Fr(2), Fr(-2)), ((0, 0, 0), (2, 2, 2), Fr(5, 7), Fr(-5, 7))):
        th = {x: q1 * G[sh(x, tuple(-c for c in S1))] + q2 * G[sh(x, tuple(-c for c in S2))] for x in sites}
        V = Fr(0)
        for x in sites:
            vals = [th[sh(x, e)] for e in E6]; mean = sum(vals) / 6
            V += sum((v - mean) ** 2 for v in vals)
        rhs = sum(q * (2 * th[S] - q / 6) for S, q in ((S1, q1), (S2, q2)))
        ok &= V == rhs
    check("B", ok, "lattice identity (exact, 4^3 torus, charges of zero sum): for theta = sum_i q_i G(. - S_i), sum_x sum_y |theta_y - thetabar_x|^2 = "
          "sum_i q_i (2 theta(S_i) - q_i/6), since 6(1 - P^2) = (-Lap)(1 + P) and thetabar = theta - q/6 at a charge")


# ------------------------------------------------------------------------------------------------ C: the response R(k), executed
def response(beta, Nq=300):
    from numpy.polynomial import legendre as Lg
    from scipy.special import ive
    t, w = Lg.leggauss(Nq); r = np.sqrt(1 - t ** 2); wn = w / 2
    T, Tp = np.meshgrid(t, t, indexing="ij"); R, Rp = np.meshgrid(r, r, indexing="ij")
    k0 = np.exp(beta * (T * Tp + R * Rp - 1)) * beta / (1 - math.exp(-2 * beta)) * ive(0, beta * R * Rp)
    F = np.exp(3 * beta * t); F /= np.sum(wn * F)
    for _ in range(20000):
        g = k0 @ (w * F); Fn = g ** 6; Fn /= np.sum(wn * Fn)
        if np.max(np.abs(Fn - F)) < 1e-14 * np.max(F):
            F = Fn; break
        F = Fn
    g = k0 @ (w * F)
    B = np.array([Lg.legval(t, np.eye(80)[l]) for l in range(80)]).T
    cg = np.linalg.lstsq(B, np.log(g), rcond=None)[0]
    c = -Lg.legval(t, Lg.legder(cg)) * t / 2 + Lg.legval(t, Lg.legder(cg, 2)) * (1 - t ** 2) / 4
    A = (k0 * (w * F)[None, :]) / g[:, None]
    Fc = np.sum(wn * F * c)
    PA = A - np.outer(np.ones(Nq), wn * F) @ A
    Pc = c - np.sum(wn * F * c)
    Rk = lambda gam: Fc + 6 * gam * np.sum(wn * F * (A @ np.linalg.solve(np.eye(Nq) - 6 * gam * PA, Pc)))
    return Fc, Rk, np.sum(wn * t * F)


def family_c() -> dict:
    rows, ok, keep = [], True, {}
    for beta in (0.6, 1.0, 2.0, 4.0):
        Fc, Rk, M = response(beta)
        R0 = Rk(1.0)
        ok &= Fc < 0 and R0 < Fc
        rows.append(f"b={beta:g}: <Fc> {Fc:.4f}, R(0) {R0:.4f} ({R0/Fc:.3f}x)")
        keep[beta] = (Fc, R0, M)
    OUT.append("     [executed, float] " + "; ".join(rows))
    check("C", ok, "second order in full: the neighbours' induced m = 0 odds eta = (1 - P sum_y A)^-1 P c V (block 103's linearization, massive) "
          "feed back, so d log Z = R * V with R(k) = <Fc> + 6 gamma(k) <F A (1 - 6 gamma PA)^-1 P c>; R(0) < <Fc> < 0 at beta = 0.6, 1, 2, 4")
    return keep


def family_n(keep) -> None:
    sys.path.insert(0, "probes/lib")
    from odds_sphere_lattice import solve
    beta, L = 1.0, 17
    c0 = L // 2
    runs = {}
    for name, al in (("0", 0.0), ("+", 0.08), ("-", -0.08)):
        runs[name] = solve(beta, L, {(c0, c0, c0): (math.sin(al), 0.0, math.cos(al))}, omega=1.6, tol=1e-12, verbose=False)
    M = keep[1.0][2]; ratio_pred = keep[1.0][1] / keep[1.0][0]
    th = runs["+"]["T"] / M
    d2 = (runs["+"]["logN"] + runs["-"]["logN"]) / 2 - runs["0"]["logN"]
    E6 = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    rows, ok = [], True
    for rr in range(2, 7):
        x = (c0 + rr, c0, c0)
        vals = np.array([th[tuple(np.add(x, e))] for e in E6]); Vx = np.sum((vals - vals.mean()) ** 2)
        direct = keep[1.0][0] * Vx
        rows.append(f"r={rr}: {d2[x]:+.2e} = {d2[x]/direct:.3f} x direct")
        ok &= d2[x] < 0
    last = d2[(c0 + 6, c0, c0)] / (keep[1.0][0] * np.sum((np.array([th[tuple(np.add((c0 + 6, c0, c0), e))] for e in E6]) - np.mean([th[tuple(np.add((c0 + 6, c0, c0), e))] for e in E6])) ** 2))
    ok &= abs(last - ratio_pred) < 0.1 * ratio_pred
    # two records, like against unlike tilts at d = 4: the configuration's summed log-normalizer
    recs = lambda sa, sb: {(c0 - 2, c0, c0): (math.sin(sa), 0.0, math.cos(sa)), (c0 + 2, c0, c0): (math.sin(sb), 0.0, math.cos(sb))}
    tot = {}
    for name, (sa, sb) in (("like", (0.08, 0.08)), ("unlike", (0.08, -0.08))):
        out = solve(beta, L, recs(sa, sb), omega=1.6, tol=1e-12, verbose=False)
        mask = np.ones((L, L, L), bool); mask[0, :, :] = mask[-1, :, :] = mask[:, 0, :] = mask[:, -1, :] = mask[:, :, 0] = mask[:, :, -1] = False
        mask[c0 - 2, c0, c0] = mask[c0 + 2, c0, c0] = False
        tot[name] = np.sum(out["logN"][mask])
    ok &= tot["like"] > tot["unlike"]
    OUT.append(f"     [executed, nonlinear solver, beta = 1, 17^3, tilt 0.08] one record: {'; '.join(rows)} (R(0)/<Fc> = {ratio_pred:.3f}); "
               f"two records 4 apart: sum log N like - unlike = {tot['like'] - tot['unlike']:+.3e}")
    check("N", ok, "the full nonlinear odds agree: the even-in-tilt change of log N is negative at every distance, tends to R(0)/<Fc> times the direct "
          "term far out, and two like-tilted records carry a larger summed log-normalizer than unlike ones")


def main() -> int:
    family_q(); family_a(); family_b()
    keep = family_c()
    family_n(keep)
    print("Two tilted records - checks; worker w-macbookpro9927a-j19b3 (claude-opus-5-5)")
    for line in OUT:
        print(line)
    print(f"checks: {sum(1 for l in OUT if l.startswith(('ok', 'FAIL'))) - len(FAILS)} ok, {len(FAILS)} fail")
    if FAILS:
        print(f"SUMMARY: ROUTE FAILS AT {FAILS[0]}")
        return 1
    print("SUMMARY: PARTIAL exact at second order in the turn field (uniform-sea region): d log Z_x = (R * V)(x), V_x = sum_y |theta_y - thetabar_x|^2, "
          "R(k) = <Fc> + 6 gamma <F A (1 - 6 gamma P A)^-1 P c>, <Fc> = -3A3/(2Z0); R(0) < 0 at every beta tried, so (a) formation is disfavoured near "
          "a tilted record, as R(0) u0^2/(8 pi^2 G(0)^2 r^4) far out; (b) sum_x V_x = sum_i q_i(2 theta_i - q_i/6) exactly, so two records carry "
          "-4 R(0)(1 - 1/(6G(0)))(a.b) G(d)/G(0)^2 at order 1/d: like tilts attract, by the capacity law times 1 - 1/(6G(0)); the solver agrees")
    print("HIT: at second order in the turn field a site's content-blind normalizer drops by (R * V), V the neighbourhood variance of the turn and "
          "R(0) < 0: formation is disfavoured near a tilted record as r^-4, and two tilted records attract when alike, "
          "log W = -4 R(0)(1 - 1/(6G(0)))(a.b) G(d)/G(0)^2 + O(d^-2)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
