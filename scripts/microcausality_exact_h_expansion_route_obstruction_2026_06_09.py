"""Exact-H bridge: canonical one-step expansion route vs the canonical budget.

Companion to
`docs/MICROCAUSALITY_EXACT_H_EXPANSION_ROUTE_QUANTIFIED_OBSTRUCTION_NOTE_2026-06-09.md`.

The parent microcausality note's exact-H bridge step asks for a quasilocal
reconstructed Hamiltonian `H = -log(T)/a_tau`. The action-support bridge note
(`MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md`)
supplies the local action budget `J_max = |m| + 78` on the canonical surface
and records the exact-log step as its BCH frontier. This runner quantifies why
that step is not
supplied by the canonical one-step norm-convergent expansion route
(BCH / Magnus / small-step effective-Hamiltonian constructions using
the landed one-step layer budget), while exhibiting that the OBJECT
(the exact spectral log) can remain quasilocal where the method fails.
The separation leaves the spectral/analyticity route live (already
instantiated on the free surface by `RECONSTRUCTED_H_QUASILOCAL_FROM_
ANALYTIC_DISPERSION_MICROCAUSALITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md`).

Checks:

  Minimal-pair convergence radius (derived, not imported): for the
      minimal non-commuting Euclidean pair X = s*sx, Y = s*sz the BCH
      object Z(s) = log(e^X e^Y) has the closed form
      tr(e^{s sx} e^{s sz})/2 = cosh^2 s (proved in exact arithmetic),
      so the nearest singularity of Z(s) sits at cosh^2 s* = -1, i.e.
      |s*| = sqrt(ln(1+sqrt 2)^2 + (pi/2)^2) ~= 1.8012. The Taylor /
      BCH series radius is verified against this value by a
      root test on coefficients computed from the closed form.

  Canonical-scale series behavior: partial sums of
      the series converge to the exact spectral log at s = 0.3 (inside)
      and diverge at s = 2.3 (the matter-only per-site budget
      |m| + d/2 at m = 0.3, d = 4) and s = 78 (the landed full
      canonical budget above |m|) — coefficient growth |c_n s^n| -> oo.

  Method-vs-object separation on a 1D layered chain (one-particle
      free hopping, checkerboard layers at the canonical hop
      coefficient 1/2): inside the convergent regime (lam = 1) the
      order-4 BCH partial sum beats order-1 by ~80x; beyond it
      (lam = 12) order-4 is WORSE than order-1 (adding orders hurts).
      Meanwhile the exact spectral log remains well-defined and
      quasilocal at both couplings: its 2x2 Bloch symbol is strictly
      positive definite for all real momenta (analytic strip => the
      exponential-tail mechanism of the analytic-dispersion note), and
      the measured tails decay exponentially.

  Budget-vs-threshold arithmetic (exact): the landed canonical
      budget 78 exceeds the standard BCH sufficient ball ln 2 by
      >= 112x and the exhibited minimal-pair radius by >= 43x; even
      the matter-only floor 2.3 exceeds both. The expansion route's
      hypotheses are violated on the canonical surface by 1.3-112x
      depending on the reading. At fixed xi = 1 (kinetic-isotropy
      primitive surface), per-layer norms scale ~ a_tau / a_s, so the
      route's hypotheses are recovered only at anisotropy xi >= 43-113,
      i.e. off the approved canonical kinetic-form surface.

External thresholds (BCH ln 2 ball; Magnus pi criterion; small-step
Floquet/effective-Hamiltonian thresholds) are CITED as comparators in
the note; every number this runner asserts is derived here from the
closed form, exact arithmetic, or explicit matrices.

Reproducibility: deterministic; no random input.
"""
from __future__ import annotations

import math

import mpmath as mp
import numpy as np
import sympy as sp
from scipy.linalg import expm

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    print(f"  [{status}] {name}")
    if detail:
        print(f"         {detail}")


# ---- Minimal-pair radius, derived from the closed form ----------------------

def closed_form_log(sv):
    """Z(s) = log(e^{s sx} e^{s sz}) via exact 2x2 spectral log (mpmath)."""
    Es = mp.matrix([[mp.cosh(sv), mp.sinh(sv)], [mp.sinh(sv), mp.cosh(sv)]])
    Ez = mp.matrix([[mp.exp(sv), 0], [0, mp.exp(-sv)]])
    M = Es * Ez
    tr = M[0, 0] + M[1, 1]
    det = M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0]
    disc = mp.sqrt(tr * tr - 4 * det)
    lam1, lam2 = (tr + disc) / 2, (tr - disc) / 2
    v1 = mp.matrix([M[0, 1], lam1 - M[0, 0]])
    v2 = mp.matrix([M[0, 1], lam2 - M[0, 0]])
    P = mp.matrix([[v1[0], v2[0]], [v1[1], v2[1]]])
    return P * mp.matrix([[mp.log(lam1), 0], [0, mp.log(lam2)]]) * P ** -1


def test_O1_minimal_pair_radius() -> bool:
    print("=" * 72)
    print("TEST: minimal-pair BCH series radius (closed form, derived)")
    print("=" * 72)
    print()

    # (a) closed form for the trace, exact arithmetic
    s = sp.symbols('s')
    sx = sp.Matrix([[0, 1], [1, 0]])
    sz = sp.Matrix([[1, 0], [0, -1]])
    Es = sp.cosh(s) * sp.eye(2) + sp.sinh(s) * sx
    Ez = sp.cosh(s) * sp.eye(2) + sp.sinh(s) * sz
    resid = sp.simplify(sp.trace(Es * Ez) / 2 - sp.cosh(s) ** 2)
    ok_trace = resid == 0
    print(f"  (a) tr(e^(s sx) e^(s sz))/2 - cosh^2 s = {resid}")
    check("minimal-pair trace — closed form tr M/2 = cosh^2 s (exact)", ok_trace)

    # (b) nearest singularity: cosh^2 s* = -1  =>  s* = ln(1+sqrt2) + i pi/2
    mp.mp.dps = 40
    r_pred = mp.sqrt(mp.log(1 + mp.sqrt(2)) ** 2 + (mp.pi / 2) ** 2)
    # verify the singularity equation at the predicted point
    s_star = mp.log(1 + mp.sqrt(2)) + mp.mpc(0, 1) * mp.pi / 2
    sing_resid = abs(mp.cosh(s_star) ** 2 + 1)
    print(f"  (b) |s*| = {mp.nstr(r_pred, 12)};  |cosh^2(s*) + 1| = {mp.nstr(sing_resid, 3)}")
    check("minimal-pair singularity — cosh^2 s* = -1 at |s*| = 1.8012 (40-digit)", sing_resid < mp.mpf(10) ** -30,
          f"|s*| = {mp.nstr(r_pred, 12)}")

    # (c) root test on Taylor coefficients of Z(s) entry (0,1)
    N = 60
    coeffs = mp.taylor(lambda sv: closed_form_log(sv)[0, 1], 0, N,
                       method='quad', radius=0.5)
    ests = [abs(coeffs[n]) ** (mp.mpf(-1) / n)
            for n in range(N - 12, N + 1) if abs(coeffs[n]) > 0]
    r_est = sum(ests) / len(ests)
    ratio = r_est / r_pred
    print(f"  (c) root-test radius estimate = {mp.nstr(r_est, 8)}  (ratio to |s*|: {mp.nstr(ratio, 6)})")
    ok_root = mp.mpf('0.95') < ratio < mp.mpf('1.10')
    check("minimal-pair root test — Taylor coefficients reproduce the radius",
          ok_root, f"estimate/predicted = {mp.nstr(ratio, 6)}")
    return ok_trace and sing_resid < mp.mpf(10) ** -30 and ok_root


# ---- Inside/outside the radius at the canonical scales ----------------------

def test_O2_inside_outside() -> bool:
    print()
    print("=" * 72)
    print("TEST: series behavior at s = 0.3 (inside) vs 2.3 and 78 (canonical scales)")
    print("=" * 72)
    print()

    mp.mp.dps = 40
    N = 60
    coeffs01 = mp.taylor(lambda sv: closed_form_log(sv)[0, 1], 0, N,
                         method='quad', radius=0.5)

    # inside: partial sums converge to the exact spectral log entry
    s_in = mp.mpf('0.3')
    exact_in = closed_form_log(s_in)[0, 1]
    partial = mp.mpf(0)
    errs_in = []
    for n in range(N + 1):
        partial += coeffs01[n] * s_in ** n
        if n in (10, 25, 50):
            errs_in.append(abs(partial - exact_in))
    print(f"  inside  s=0.3: |partial - exact| at N=10,25,50: "
          f"{[mp.nstr(e, 3) for e in errs_in]}")
    ok_in = errs_in[-1] < mp.mpf(10) ** -25 and errs_in[0] > errs_in[-1]
    check("inside-radius series — partial sums converge to the exact log at s = 0.3", ok_in)

    # outside: coefficient terms |c_n s^n| blow up at the canonical scales
    blowups = {}
    for s_out in (mp.mpf('2.3'), mp.mpf(78)):
        terms = [abs(coeffs01[n]) * s_out ** n for n in range(20, N + 1)]
        grow = terms[-1] / terms[0]
        blowups[float(s_out)] = grow
        print(f"  outside s={mp.nstr(s_out, 4)}: |c_n s^n| growth n=20->60: factor {mp.nstr(grow, 4)}")
    ok_out = blowups[2.3] > mp.mpf(10) ** 2 and blowups[78.0] > mp.mpf(10) ** 60
    check("canonical-scale series — terms diverge at the matter floor (2.3) and full budget (78)",
          ok_out,
          "the BCH series does not represent the (existing) exact log at canonical norms")
    return ok_in and ok_out


# ---- Method-vs-object separation on the layered chain -----------------------

def chain_layers(L: int):
    def layer(start):
        Mx = np.zeros((L, L))
        for i in range(start, L - 1, 2):
            Mx[i, i + 1] = Mx[i + 1, i] = 0.5  # canonical hop coefficient
        return Mx
    return layer(0), layer(1)


def chain_exact_log(A, B, lam):
    S = expm(-lam * A / 2.0)
    Si = expm(+lam * A / 2.0)
    Tsym = S @ expm(-lam * B) @ S
    w, V = np.linalg.eigh(Tsym)
    if w.min() <= 0:
        raise ValueError("transfer symbol lost positivity (conditioning)")
    logT = V @ np.diag(np.log(w)) @ V.T
    return S @ logT @ Si, w


def chain_bch_partial(A, B, lam, order):
    X, Y = -lam * A, -lam * B
    c = lambda P, Q: P @ Q - Q @ P
    Z = X + Y
    if order >= 2:
        Z = Z + 0.5 * c(X, Y)
    if order >= 3:
        Z = Z + (c(X, c(X, Y)) + c(Y, c(Y, X))) / 12.0
    if order >= 4:
        Z = Z - c(Y, c(X, c(X, Y))) / 24.0
    return Z


def bloch_min_eig(lam: float, n: int = 4001) -> float:
    """Min eigenvalue of the 2x2 Bloch symbol of T_sym over the BZ."""
    a = b = 0.5
    mins = []
    for p in np.linspace(-np.pi, np.pi, n):
        Ap = np.array([[0, a], [a, 0]], dtype=complex)
        Bp = np.array([[0, b * np.exp(-1j * p)], [b * np.exp(1j * p), 0]], dtype=complex)
        S = expm(-lam * Ap / 2)
        T = S @ expm(-lam * Bp) @ S
        mins.append(np.linalg.eigvalsh(T).min())
    return float(min(mins))


def test_O3_method_vs_object() -> bool:
    print()
    print("=" * 72)
    print("TEST: method fails, object survives (1D layered chain, hop = 1/2)")
    print("=" * 72)
    print()

    L = 96
    A, B = chain_layers(L)
    results_ok = []

    for lam, label in ((1.0, "inside"), (12.0, "beyond")):
        Zx, w = chain_exact_log(A, B, lam)
        errs = [float(np.linalg.norm(chain_bch_partial(A, B, lam, k) - Zx, 2))
                for k in (1, 2, 3, 4)]
        ratio41 = errs[3] / errs[0]
        print(f"  lam={lam:>4} ({label}): BCH errors order 1..4 = "
              f"{['%.3e' % e for e in errs]}  err4/err1 = {ratio41:.3f}")
        if label == "inside":
            ok = ratio41 < 0.05  # adding orders helps (~80x here)
            check("inside chain expansion — order-4 partial sum beats order-1 by > 20x",
                  ok, f"err4/err1 = {ratio41:.4f}")
        else:
            ok = ratio41 > 1.0  # adding orders HURTS
            check("beyond-radius chain expansion — order-4 partial sum is WORSE than order-1",
                  ok, f"err4/err1 = {ratio41:.4f}; the expansion method has no foothold")
        results_ok.append(ok)

    # object side: Bloch-symbol positivity (analytic strip) at both couplings
    for lam in (1.0, 12.0):
        bmin = bloch_min_eig(lam)
        ok = bmin > 0
        results_ok.append(ok)
        check(f"exact-log object — Bloch symbol strictly positive at lam={lam}",
              ok, f"min eig over 4001 BZ points = {bmin:.6e}")

    # illustration: measured exponential tails inside and at moderate beyond-radius coupling
    for lam, kwin in ((1.0, (4, 16)), (4.0, (10, 38))):
        Zx, _ = chain_exact_log(A, B, lam)
        Hx = -Zx
        ks = list(range(2, 44))
        vals = [max(abs(Hx[i, i + k]) for i in range(L - k)) for k in ks]
        lo, hi = kwin
        kk = np.array([k for k in ks if lo <= k <= hi], dtype=float)
        vv = np.log(np.array([vals[ks.index(int(k))] for k in kk]))
        slope, icpt = np.polyfit(kk, vv, 1)
        resid = float(np.abs(vv - (slope * kk + icpt)).max())
        rate = -slope
        ok = rate > 0.05 and resid < 0.7
        results_ok.append(ok)
        check(f"exact-log tails — exponential decay at lam={lam}",
              ok, f"fit rate = {rate:.4f} over k in [{lo},{hi}], max fit residual = {resid:.3f}")

    return all(results_ok)


# ---- Budget-vs-threshold arithmetic (exact) --------------------------------

def test_O4_budget_arithmetic() -> bool:
    print()
    print("=" * 72)
    print("TEST: canonical budgets vs expansion thresholds (exact arithmetic)")
    print("=" * 72)
    print()

    mp.mp.dps = 50
    ln2 = mp.log(2)
    r_pair = mp.sqrt(mp.log(1 + mp.sqrt(2)) ** 2 + (mp.pi / 2) ** 2)

    # canonical budgets (above |m|), from the landed bridge note:
    #   matter-only per-site floor: d/2 = 2 at d=4, plus |m| = 0.3 test mass
    #   full canonical budget: 78 (J_max = |m| + 78 on main)
    m = mp.mpf('0.3')
    matter_floor = mp.mpf(4) / 2 + m       # 2.3
    full_budget = mp.mpf(78)

    rows = [
        ("matter floor 2.3 vs BCH ball ln 2", matter_floor / ln2, mp.mpf(3)),
        ("matter floor 2.3 vs pair radius 1.8012", matter_floor / r_pair, mp.mpf('1.2')),
        ("full budget 78 vs BCH ball ln 2", full_budget / ln2, mp.mpf(112)),
        ("full budget 78 vs pair radius 1.8012", full_budget / r_pair, mp.mpf(43)),
    ]
    ok_all = True
    for label, val, floor_ in rows:
        ok = val > floor_
        ok_all = ok_all and ok
        print(f"  {label}: gap factor = {mp.nstr(val, 6)}  (> {mp.nstr(floor_, 4)})")
    check("budget arithmetic — every expansion threshold is exceeded on the canonical surface",
          ok_all, "gaps 1.28x (floor/pair) to 112.5x (full/ball)")

    # xi-line: per-layer norms scale ~ a_tau/a_s at fixed spatial couplings, so the
    # route's hypotheses are recovered only at anisotropy xi >= budget/threshold —
    # i.e. 43x-113x off the canonical xi = 1 kinetic-form primitive surface.
    xi_ball = full_budget / ln2
    xi_pair = full_budget / r_pair
    print(f"  xi needed for expansion guarantees: >= {mp.nstr(xi_pair, 5)} (pair radius) "
          f"to >= {mp.nstr(xi_ball, 6)} (BCH ball); canonical surface has xi = 1")
    ok_xi = xi_pair > 43 and xi_ball > 112
    check("xi line — expansion route requires xi >= 43-113, off the canonical xi = 1 surface",
          ok_xi, "the route lives off the canonical xi = 1 surface")
    return ok_all and ok_xi


# ---- Main --------------------------------------------------------------------

def main() -> None:
    print()
    print("=" * 72)
    print("EXACT-H BRIDGE: EXPANSION-ROUTE QUANTIFIED OBSTRUCTION RUNNER")
    print("=" * 72)
    print()
    print("Companion: docs/MICROCAUSALITY_EXACT_H_EXPANSION_ROUTE_QUANTIFIED_OBSTRUCTION_NOTE_2026-06-09.md")
    print("Scopes the exact-H step of AXIOM_FIRST_MICROCAUSALITY_LIEB_ROBINSON:")
    print("canonical one-step norm-convergent expansion constructions of -log(T)/a_tau")
    print("do not reach the canonical-surface budget; the spectral/analyticity route")
    print("(free-surface step already landed 2026-06-06) remains live.")
    print()

    o1 = test_O1_minimal_pair_radius()
    o2 = test_O2_inside_outside()
    o3 = test_O3_method_vs_object()
    o4 = test_O4_budget_arithmetic()

    print()
    print("=" * 72)
    print("SUMMARY")
    print("=" * 72)
    print(f"  Minimal-pair radius derived (1.8012, closed form):      {'PASS' if o1 else 'FAIL'}")
    print(f"  Series converges inside / diverges at 2.3 and 78:       {'PASS' if o2 else 'FAIL'}")
    print(f"  Method fails while object stays quasilocal (chain):     {'PASS' if o3 else 'FAIL'}")
    print(f"  Budget-vs-threshold gaps 1.28x-112.5x + xi-line:        {'PASS' if o4 else 'FAIL'}")
    print()
    all_ok = o1 and o2 and o3 and o4
    print(f"  PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    print(f"  OVERALL: {'PASS' if all_ok else 'FAIL'}")
    print()
    print("The runner derives every asserted number (radius, gaps, tails) from closed")
    print("forms, exact arithmetic, or explicit matrices. Literature thresholds (BCH")
    print("ln 2 ball, Magnus pi criterion, small-step effective-Hamiltonian bounds)")
    print("are comparator citations in the note, not derivation inputs here.")
    print()

    if not all_ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
