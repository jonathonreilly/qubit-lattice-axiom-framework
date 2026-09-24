#!/usr/bin/env python3
"""The persistent-record threshold in 3D: checks for ATTEMPT.md (attempt 2 of 2), worker w-macbookpro9927a-j59b0 (claude-opus-5-5).

Object (block 96 T2, PR #8866): M(k) = E(k) T, E = diag(exp(-i k.d)) over d = +-e_j, T = p I + q (J - I), q = (1-p)/5, a = p - q.
Exact parts: sympy identities and exact sign facts. Parts marked "floating point" are numerical evidence only (numpy eigenvalues on grids).
"""
from __future__ import annotations

import json
import subprocess
import sys

import numpy as np
import sympy as sp

OUT: list[str] = []
FAILS: list[str] = []


def check(tag: str, ok: bool, msg: str) -> None:
    OUT.append(f"{'ok  ' if ok else 'FAIL'} {tag}: {msg}")
    if not ok:
        FAILS.append(tag)


R = sp.Rational
NOTES = [
    ("b96", "111143f765", "docs/ADMISSIBILITY_RULE_WAVES_AMONG_MOVING_RECORDS_NEED_A_COUPLING_THAT_TIME_REVERSAL_FLIPS_CLOCKED_RECORD_MOTION_"
     "NEVER_OSCILLATES_BOUNDED_THEOREM_NOTE_2026-09-23.md",
     ["Its mode matrix `M(k) = E(k) T` satisfies `conj(M(k)) = Π M(k) Π`",
      "On a line this is exact: the modes are non-real if and only if `|sin k| > (1 − p)/p`.",
      "non-real from `|k| = 0.45`"]),
    ("a1", "d48987ea1f", "probes/work/derive/the-persistent-record-threshold-in-3d/w-jonathonsmac4f50-j0e93/ATTEMPT.md",
     ["1. **General directions.** Along the face diagonal, a floating-point scan finds the density branch real for all `κ`, at "
      "`p = 0.5, 0.9, 0.99`.",
      "2. **Is the body diagonal extremal?**"]),
]
TASK_Q = ["(a) Along the axes and the body diagonal, the exact boundary (in k and p) where the leading multiplier leaves the real line",
          "(b) its small-(1 - p) scaling (the memory length). HIT: (a) exact."]


def family_q() -> None:
    miss = []
    for tag, sha, path, qs in NOTES:
        txt = subprocess.run(["git", "show", f"{sha}:{path}"], capture_output=True, text=True).stdout
        miss += [f"{tag}[{i}]" for i, q in enumerate(qs) if q not in txt]
    d = json.load(open("probes/TASKS.json"))
    ts = d if isinstance(d, list) else d.get("tasks", d)
    ts = ts if isinstance(ts, list) else list(ts.values())
    what = next((t["what"] for t in ts if isinstance(t, dict) and t.get("id") == "J:derive:the-persistent-record-threshold-in-3d:a2"), "")
    miss += [f"task[{i}]" for i, q in enumerate(TASK_Q) if q not in what]
    check("Q", not miss, f"block 96 T2 (head 111143f7), attempt 1's open items (ai/probes d48987ea) and the task quoted verbatim (7 lines)"
          f"{'; missing ' + str(miss) if miss else ''}")


lam, p, r = sp.symbols("lambda p r")
q_ = (1 - p) / 5
a_ = p - q_


# ------------------------------------------------------------------------------------------------ L: rank one plus diagonal; the Poisson form
def family_l() -> None:
    e = sp.symbols("e0:6")
    a, q = sp.symbols("a q")
    E = sp.diag(*e)
    T = a * sp.eye(6) + q * sp.ones(6, 6)
    lhs = (lam * sp.eye(6) - E * T).det(method="berkowitz")
    prod = sp.prod([lam - a * ei for ei in e])
    rhs = prod - q * sum(e[i] * sp.prod([lam - a * e[j] for j in range(6) if j != i]) for i in range(6))
    ok = sp.expand(lhs - rhs) == 0
    # one pair e, conj(e) with e = c - i s, c^2 + s^2 = 1: its secular term equals (P(r, kappa) - 1)/a, r = a/lambda
    c, s = sp.symbols("c s", real=True)
    ep, em = c - sp.I * s, c + sp.I * s
    pair = ep / (lam - a * ep) + em / (lam - a * em)
    P = (1 - r ** 2) / (1 - 2 * r * c + r ** 2)
    num, den = sp.fraction(sp.together(pair))
    num = sp.expand(num).subs(s ** 2, 1 - c ** 2)
    den = sp.expand(den).subs(s ** 2, 1 - c ** 2)
    ok &= not (num.has(s) or den.has(s)) and sp.simplify(num / den - (P.subs(r, a / lam) - 1) / a) == 0
    # T = pI + q(J - I) = a I + q J with a = p - q, a + 6q = 1; the level 3 + a/q = (2 + 3p)/(1 - p)
    ok &= sp.simplify(a_ + 6 * q_ - 1) == 0 and sp.simplify(3 + a_ / q_ - (2 + 3 * p) / (1 - p)) == 0
    check("L", ok, "det(lam - E(aI + qJ)) = prod(lam - a e_d) (1 - q sum_d e_d/(lam - a e_d)) for six free e_d (exact); a pair e, conj e "
          "contributes (P(r, kappa) - 1)/a with r = a/lam and P = (1 - r^2)/(1 - 2 r cos kappa + r^2) the Poisson kernel: a real "
          "lam > a is a multiplier iff sum_j P(r, kappa_j) = (2 + 3p)/(1 - p)")


# ------------------------------------------------------------------------------------------------ I: every coordinate plane
def family_i() -> None:
    c = sp.Symbol("c")
    A, B = 1 - r ** 2, 1 + r ** 2
    P = (1 - r ** 2) / (1 - 2 * r * c + r ** 2)
    dP = sp.diff(P, r)
    ok = sp.simplify(dP - P * (P * A - B) / (r * A)) == 0                      # dP/dr is a function of P and r only
    P0 = (1 + r) / (1 - r)
    psi = lambda x: A * x ** 2 - B * x
    ok &= sp.simplify(psi(P0) - 2 * r * P0) == 0
    S = sp.Symbol("S")
    Qs = 2 * r * P0 + A * S ** 2 / 2 - B * S                                  # psi(P0) + 2 psi(S/2)
    X = (2 - 4 * r) / (1 - r)                                                  # S >= X when F >= 3
    ok &= sp.simplify(Qs.subs(S, X) - 12 * r ** 3 / (1 - r)) == 0
    omega = r ** 4 - 4 * r ** 3 - 6 * r ** 2 - 4 * r + 1
    ok &= sp.simplify(B ** 2 - 4 * (A / 2) * 2 * r * P0 - omega) == 0         # the S-discriminant of Q is omega(r)
    ok &= omega.subs(r, R(1, 4)) == R(-111, 256)
    dom = sp.diff(omega, r)
    ok &= not any(0 <= rt <= 1 for rt in sp.Poly(dom, r).real_roots()) and dom.subs(r, 0) < 0   # omega decreasing on [0, 1]
    vert = sp.simplify((X - B / A) * (1 - r ** 2))                             # X - vertex = (1 - 2r - 5r^2)/(1 - r^2)
    ok &= sp.expand(vert - (1 - 2 * r - 5 * r ** 2)) == 0 and (1 - 2 * r - 5 * r ** 2).subs(r, R(1, 4)) == R(3, 16)
    # floating point evidence: F >= 3 => F' > 0 on a grid; one real multiplier above a at every in-plane grid point
    rs = np.linspace(1e-4, 0.9999, 1500)
    worst = np.inf
    Pn = lambda rr, cc: (1 - rr * rr) / (1 - 2 * rr * cc + rr * rr)
    for c1 in np.linspace(-1, 1, 41):
        for c2 in np.linspace(-1, 1, 41):
            F = Pn(rs, 1.0) + Pn(rs, c1) + Pn(rs, c2)
            dF = np.gradient(F, rs)
            worst = min(worst, float(np.min(np.where(F >= 3, dF, np.inf))))
    ok &= worst > 0
    check("I", ok, "dP/dr = P(P(1 - r^2) - (1 + r^2))/(r(1 - r^2)); with kappa_3 = 0, psi(P0) = 2r P0, the convex bound "
          "psi(P0) + 2 psi(S/2) at S = X = 3 - P0 equals 12 r^3/(1 - r) > 0, its S-discriminant is omega = r^4 - 4r^3 - 6r^2 - 4r + 1, "
          "omega(1/4) = -111/256 and omega decreases on [0, 1], and X exceeds the vertex for r <= 1/4 (3/16 > 0): F >= 3 forces F' > 0 on "
          f"(0, 1) [floating point: min F' where F >= 3 on a grid = {worst:.2e}]")


# ------------------------------------------------------------------------------------------------ B: the body diagonal from the Poisson kernel
def family_b() -> None:
    c = sp.Symbol("c", positive=True)
    s = sp.sqrt(1 - c ** 2)
    P = (1 - r ** 2) / (1 - 2 * r * c + r ** 2)
    rstar = (1 - s) / c
    ok = sp.simplify(sp.diff(P, r).subs(r, rstar)) == 0 and sp.simplify(P.subs(r, rstar) - 1 / s) == 0
    ok &= sp.simplify(R(3, 1) / ((2 + 3 * p) / (1 - p)) - 3 * (1 - p) / (3 * p + 2)) == 0
    check("B", ok, "on the body diagonal F = 3P(r, kappa); for cos kappa > 0 its maximum over r is 1/|sin kappa| at r* = (1 - |sin kappa|)/"
          "cos kappa, so the density branch is real iff 3/|sin kappa| >= (2 + 3p)/(1 - p), i.e. |sin kappa| <= 3(1 - p)/(3p + 2) "
          "(attempt 1's B2, here from the Poisson form); for cos kappa <= 0, P <= 1 and it is non-real")


# ------------------------------------------------------------------------------------------------ S: the long-memory limit, all directions
def family_s() -> None:
    eps, K, n, Lam = sp.symbols("epsilon K n Lambda", positive=True)
    sv = sp.Rational(6, 5) - Lam
    lam_e = 1 - eps * Lam
    a_e, q_e = 1 - R(6, 5) * eps, eps / 5
    ep, em = sp.exp(-sp.I * eps * K * n), sp.exp(sp.I * eps * K * n)
    pair = q_e * (ep / (lam_e - a_e * ep) + em / (lam_e - a_e * em))
    lim = sp.simplify(sp.limit(pair, eps, 0))
    ok = sp.simplify(lim - R(1, 5) * 2 * sv / (sv ** 2 + K ** 2 * n ** 2)) == 0
    sig, t, v = sp.symbols("sigma t v", positive=True)
    # in a coordinate plane: each non-zero term's slope is at most 1/(2 sigma^2), the zero term's is -2/sigma^2
    slope = sp.diff(2 * sig / (sig ** 2 + t), sig)
    gap = 1 / (2 * sig ** 2) - slope
    ok &= sp.simplify(gap - ((t - sig ** 2) ** 2 + 4 * sig ** 4) / (2 * sig ** 2 * (sig ** 2 + t) ** 2)) == 0
    # off the planes: f(t) = (t - v)/(v + t)^2 is concave on t < 5v, so for v >= 1/3 Jensen gives sum_j f(t_j) <= 3 f(1/3) <= 0
    f = (t - v) / (v + t) ** 2
    ok &= sp.simplify(sp.diff(f, t, 2) + (10 * v - 2 * t) / (v + t) ** 4) == 0
    # t -> 2 sigma/(sigma^2 + t) is convex, so g_n >= g_diag pointwise; g_diag peaks at sigma = 1/sqrt3 with 3 sqrt3
    ok &= sp.simplify(sp.diff(2 * sig / (sig ** 2 + t), t, 2) - 4 * sig / (sig ** 2 + t) ** 3) == 0
    gd = 6 * sig / (sig ** 2 + R(1, 3))
    ok &= sp.simplify(sp.diff(gd, sig).subs(sig, 1 / sp.sqrt(3))) == 0 and sp.simplify(gd.subs(sig, 1 / sp.sqrt(3)) - 3 * sp.sqrt(3)) == 0
    # floating point evidence: the limiting threshold over random off-plane directions is never below 3 sqrt3/5
    rng = np.random.default_rng(5)
    mins = []
    ss = np.logspace(-4, 2, 40000)
    for _ in range(400):
        nn = np.abs(rng.normal(size=3)); nn /= np.linalg.norm(nn)
        g = sum(2 * ss / (ss ** 2 + nj ** 2) for nj in nn)
        dg = np.diff(g)
        crit = np.where((dg[:-1] > 0) & (dg[1:] <= 0))[0]
        mo = g[crit[-1] + 1] if len(crit) else np.inf
        mins.append(mo / 5)
    kmin = float(np.min(mins))
    ok &= kmin >= 3 * np.sqrt(3) / 5 - 1e-6
    check("S", ok, "long memory (eps = 1 - p -> 0, k = eps K n): each pair tends exactly to (1/5) 2s/(s^2 + K^2 n_j^2), s = 6/5 - Lambda, "
          "so 5K = g_n(sigma) = sum_j 2 sigma/(sigma^2 + n_j^2); in a plane g_n' <= -1/sigma^2 (numerator (t - sigma^2)^2 + 4 sigma^4): "
          "never non-real; off the planes all critical points have sigma^2 <= 1/3 (concavity) and g_n >= g_diag (convexity), so "
          f"K*(n) >= 3 sqrt3/5, equality only on the body diagonals [floating point: min over 400 random directions {kmin:.4f}]")


# ------------------------------------------------------------------------------------------------ C: the zone corner of the face diagonal
def family_c() -> None:
    a, q = sp.symbols("a q", positive=True)
    c = sp.Symbol("c")
    D = lam ** 2 - 2 * a * lam * c + a ** 2
    Pfd = (lam - a) * D - 2 * q * ((2 * lam * c - 2 * a) * (lam - a) + D)
    at_corner = sp.factor(sp.expand(Pfd.subs(c, -1)))
    ok = sp.expand(at_corner - (lam + a) * (lam ** 2 + 2 * q * lam - a ** 2 - 6 * q * a)) == 0
    root = sp.sqrt(q ** 2 + a ** 2 + 6 * q * a)
    lp, lm = -q + root, -q - root
    ok &= sp.simplify(lp + lm + 2 * q) == 0            # |lm| - lp = 2q > 0: the corner is led by the negative root
    # floating point evidence: along the face diagonal near the corner the leading multiplier can be non-real while the density
    # branch stays real (p = 9/10)
    pn = 0.9
    qn = (1 - pn) / 5
    ds = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    Tn = pn * np.eye(6) + qn * (np.ones((6, 6)) - np.eye(6))
    found = False
    for kk in np.linspace(2.9, np.pi, 400):
        k = np.array([kk, kk, 0.0])
        ev = np.linalg.eigvals(np.diag([np.exp(-1j * k.dot(d)) for d in ds]) @ Tn)
        lead = max(ev, key=abs)
        dens = [e.real for e in ev if abs(e.imag) < 1e-10 and e.real > (6 * pn - 1) / 5]
        if abs(lead.imag) > 1e-8 and len(dens) == 1:
            found = True
            break
    ok &= found
    check("C", ok, "face diagonal at the zone corner k = (pi, pi, 0): its cubic is (lam + a)(lam^2 + 2q lam - a^2 - 6qa), roots -a and "
          "-q +- sqrt(q^2 + a^2 + 6qa); the negative one exceeds the density root in modulus by exactly 2q, so the leading multiplier "
          "there is not the density branch [floating point, p = 9/10: nearby the leading multiplier is a non-real pair while the density "
          "branch is real]")


def main() -> int:
    family_q()
    family_l()
    family_i()
    family_b()
    family_s()
    family_c()
    print("The persistent-record threshold in 3D - checks; worker w-macbookpro9927a-j59b0 (claude-opus-5-5)")
    for line in OUT:
        print(line)
    print(f"checks: {len(OUT) - len(FAILS)} ok, {len(FAILS)} fail")
    if FAILS:
        print(f"SUMMARY: ROUTE FAILS AT {FAILS[0]}")
        return 1
    print("SUMMARY: PARTIAL exact: with r = a/lam a real lam > a is a multiplier iff sum_j P(r, kappa_j) = (2 + 3p)/(1 - p), P the Poisson "
          "kernel; (1) on every coordinate plane (one kappa_j = 0: the axes, the face diagonals and every direction between) F >= 3 "
          "forces F' > 0, so for every p in (1/6, 1) the density branch is the unique real multiplier above a, simple, at every wave "
          "vector; (2) the body diagonal's threshold |sin kappa| = 3(1 - p)/(3p + 2) is 3/max_r P; (3) in the long-memory limit the "
          "threshold is K*(n) = (outer peak of sum_j 2 sigma/(sigma^2 + n_j^2))/5 >= 3 sqrt3/5, equality only on the body diagonals, "
          "infinite on the planes; (4) at k = (pi, pi, 0) the leading multiplier is the negative root, 2q above the density root")
    print("HIT: the density branch of the direction-memory record is real and simple on all three coordinate planes for every p in "
          "(1/6, 1) (Poisson form: sum_j P(r, kappa_j) = (2 + 3p)/(1 - p), and F >= 3 forces F' > 0 there); in the long-memory limit "
          "it first leaves the real line on the body diagonals: K*(n) >= 3 sqrt3/5 with equality only there")
    return 0


if __name__ == "__main__":
    sys.exit(main())
