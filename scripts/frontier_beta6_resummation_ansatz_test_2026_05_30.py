#!/usr/bin/env python3
"""
beta=6 SU(3) Wilson single-plaquette resummation-ansatz TEST HARNESS
====================================================================

What this is
------------
A test harness for the two remaining unproven analytic continuation
ansaetze named in the beta=6 closure research map
(`docs/BETA6_PLAQUETTE_CLOSURE_NOTE_2026-05-29.md`,
Route 1 + the tadpole/boosted-PT comparator):

  (a) d-log-Pade resummation of the connected-shell series of
        Delta(beta) = P_full(beta) - P_1plaq(beta),
  (b) tadpole-improved / boosted perturbation theory
        (u_0 = <P>^{1/4} self-consistency).

It does BOTH of the two tests the campaign needs:

  FORWARD TEST       : compute the implied <P>(6) = P_1plaq(6) + Delta(6)
                       under each ansatz, as a function of how many connected
                       coefficients are supplied; report convergence toward
                       the Monte-Carlo comparator 0.594 and the sensitivity to
                       the (currently unknown) next coefficient.

  PREDICTIVE TEST    : given lower-order connected series, compute what each
                       ansatz PREDICTS for the next connected coefficient, then
                       run exact-vs-predicted leave-one-out tests on the current
                       d_5..d_11 coefficient frontier.

What this is NOT (honesty, non-negotiable)
------------------------------------------
This harness does NOT close beta=6 and must not be read as doing so.

  * 0.594 is a Monte-Carlo COMPARATOR (P_inf = 0.59400 +/- 0.00037, from
    `plaquette_4d_mc_fss_numerical_theorem_note_2026-05-05`), NOT a derivation
    input. Nothing here is fitted to 0.594. The harness TESTS whether an
    ansatz fixed by the LOW-order exact coefficients independently reaches it.

  * The exact connected coefficients currently exposed by the beta=6 frontier
    packets are d_5..d_11. The old 2026-05-30 single-coefficient waiting state
    is stale. This runner now consumes the live d_5..d_11 frontier and reports
    the ansatz verdicts against those exact coefficients.

  * A genuine resummation needs many exact connected coefficients; producing
    them collides with the treewidth-29 infeasibility wall
    (`su3_wigner_l3_treewidth_infeasible_2026-05-04`, audited_conditional).
    This harness is the METHODOLOGY that will evaluate the route; not the route.

Type: bounded_theorem (methodology). Status authority: independent audit lane
only. No new tags, no new vocabulary, no promotion language.

Load-bearing inputs (all retained / recomputed here for self-consistency)
-------------------------------------------------------------------------
  * J(beta) = int_{SU(3)} exp((beta/3) Re Tr U) dU via the exact order-3
    dominant-weight recurrence
      6(N+1)(N+4)(N+5) a_{N+1} = N(N+1) a_N + 2(2N+3) a_{N-1} + a_{N-2},
      a_0 = 1, a_1 = 0, a_2 = 1/36
    (`gauge_vacuum_plaquette_transfer_operator_character_recurrence_note`,
     `plaquette_v1_picard_fuchs_ode_note_2026-05-05`).
  * P_1plaq(beta) = J'(beta)/J(beta); P_1plaq(6) = 0.4225317396 (retained).
  * d_5 = 1/472392 (retained order-beta^5 connected coefficient).
  * d_6..d_11 from the exact beta=6 coefficient packets landed by 2026-06-04.

Run:
  python3 scripts/frontier_beta6_resummation_ansatz_test_2026_05_30.py
"""

from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction
from typing import Callable, Optional

import mpmath as mp

mp.mp.dps = 60

# ---------------------------------------------------------------------------
# scorecard
# ---------------------------------------------------------------------------
PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS += 1
    else:
        FAIL += 1
    print(f"  [{status}] {name}")
    if detail:
        print(f"         {detail}")


def section(title: str) -> None:
    print()
    print("=" * 78)
    print(title)
    print("=" * 78)


# ===========================================================================
# 1. Retained single-plaquette baseline P_1plaq(beta) = J'(beta)/J(beta)
# ===========================================================================
def build_J_taylor(order: int) -> list[Fraction]:
    """Exact Taylor coefficients a_n of J(beta) via the retained recurrence."""
    a = [Fraction(1), Fraction(0), Fraction(1, 36)]
    for N in range(2, order + 1):
        rhs = N * (N + 1) * a[N] + 2 * (2 * N + 3) * a[N - 1] + a[N - 2]
        a.append(rhs / (6 * (N + 1) * (N + 4) * (N + 5)))
    return a[: order + 1]


_A = build_J_taylor(80)


def _Jval(beta: mp.mpf) -> mp.mpf:
    s = mp.mpf(0)
    bp = mp.mpf(1)
    for an in _A:
        s += mp.mpf(an.numerator) / mp.mpf(an.denominator) * bp
        bp *= beta
    return s


def _Jpval(beta: mp.mpf) -> mp.mpf:
    s = mp.mpf(0)
    bp = mp.mpf(1)
    for n in range(1, len(_A)):
        an = _A[n]
        s += n * mp.mpf(an.numerator) / mp.mpf(an.denominator) * bp
        bp *= beta
    return s


def P_1plaq(beta: mp.mpf) -> mp.mpf:
    """Single-plaquette-in-isolation Wilson expectation."""
    return _Jpval(beta) / _Jval(beta)


def P_1plaq_taylor(order: int) -> list[Fraction]:
    """Exact Taylor coefficients c_n of P_1plaq(beta) (rational series division)."""
    N = order + 1
    num = [(n + 1) * _A[n + 1] for n in range(N)]
    den = list(_A[:N])
    c = [Fraction(0)] * N
    for n in range(N):
        s = num[n] - sum(den[k] * c[n - k] for k in range(1, n + 1))
        c[n] = s / den[0]
    return c


# Constants from the research map (recomputed independently for self-consistency).
BETA = mp.mpf(6)
P1_AT_6 = P_1plaq(BETA)
MC_COMPARATOR = mp.mpf("0.594")          # Monte-Carlo comparator (P_inf=0.59400), NOT a derivation input
MC_SIGMA = mp.mpf("0.00037")
MC_COMPARATOR_4DP = mp.mpf("0.5934")     # the 4-dp canonical comparator quoted in the research map
DELTA_TARGET = MC_COMPARATOR - P1_AT_6   # ~0.1715 (comparator-derived, not fitted)
D5 = Fraction(1, 472392)                 # retained exact order-beta^5 connected coefficient

EXACT_CONNECTED = {
    5: Fraction(1, 472392),
    6: Fraction(7, 5668704),
    7: Fraction(5, 17006112),
    8: Fraction(5, 272097792),
    9: Fraction(-2035, 264479053824),
    10: Fraction(-10483, 5289581076480),
    11: Fraction(-13, 3967185807360),
}


def mp_fraction(value: Fraction) -> mp.mpf:
    return mp.mpf(value.numerator) / mp.mpf(value.denominator)


# ===========================================================================
# 2. Generic power-series helpers (exact mpmath)
# ===========================================================================
def series_log(c: list[mp.mpf]) -> list[mp.mpf]:
    """Taylor series of log(sum c_k x^k), requires c[0] != 0."""
    n = len(c)
    out = [mp.log(c[0])] + [mp.mpf(0)] * (n - 1)
    for k in range(1, n):
        out[k] = c[k] / c[0] - sum(
            (mp.mpf(j) / k) * out[j] * (c[k - j] / c[0]) for j in range(1, k)
        )
    return out


def series_exp(c: list[mp.mpf]) -> list[mp.mpf]:
    """Taylor series of exp(sum c_k x^k)."""
    n = len(c)
    out = [mp.e ** c[0]] + [mp.mpf(0)] * (n - 1)
    for k in range(1, n):
        out[k] = sum((mp.mpf(j) / k) * c[j] * out[k - j] for j in range(1, k + 1))
    return out


def series_deriv(c: list[mp.mpf]) -> list[mp.mpf]:
    """Taylor series of d/dx (sum c_k x^k)."""
    return [(k + 1) * c[k + 1] for k in range(len(c) - 1)]


def ratio_series(P: list[mp.mpf], Q: list[mp.mpf], N: int) -> list[mp.mpf]:
    """Taylor coefficients (0..N) of the rational function P(x)/Q(x)."""
    c = [mp.mpf(0)] * (N + 1)
    for k in range(N + 1):
        num = P[k] if k < len(P) else mp.mpf(0)
        num -= sum((Q[j] if j < len(Q) else mp.mpf(0)) * c[k - j] for j in range(1, k + 1))
        c[k] = num / Q[0]
    return c


# ===========================================================================
# 3. The connected series object Delta(beta)
# ===========================================================================
@dataclass
class ConnectedSeries:
    """
    Delta(beta) = P_full(beta) - P_1plaq(beta) = sum_{n>=5} d_n beta^n.

    The lowest connected order is 5 (Theorem 2 of the mixed-cumulant audit:
    no nonlocal correction through order beta^4). `coeffs` maps order n -> d_n.
    d_5 is retained; d_6, d_7, ... are parameters supplied by the parallel cycle.
    """
    coeffs: dict[int, mp.mpf] = field(default_factory=dict)
    lowest_order: int = 5

    def set_coeff(self, n: int, value) -> None:
        self.coeffs[n] = mp.mpf(value) if not isinstance(value, mp.mpf) else value

    def contiguous(self) -> list[tuple[int, mp.mpf]]:
        """Contiguous (n, d_n) starting at lowest_order, stopping at first gap."""
        out = []
        n = self.lowest_order
        while n in self.coeffs:
            out.append((n, self.coeffs[n]))
            n += 1
        return out

    def shifted_h(self) -> list[mp.mpf]:
        """h_j such that Delta = beta^lowest * sum_j h_j beta^j (h_0 = d_lowest)."""
        return [v for _, v in self.contiguous()]

    def eval_truncated(self, beta: mp.mpf) -> mp.mpf:
        s = mp.mpf(0)
        for n, d in self.contiguous():
            s += d * beta ** n
        return s


# ===========================================================================
# 4. ANSATZ (a): d-log-Pade resummation
# ===========================================================================
@dataclass
class DlogPadeResult:
    order: int
    delta6: Optional[mp.mpf]
    sing_abs: Optional[mp.mpf]
    sing_arg: Optional[mp.mpf]
    note: str = ""


def _dlog_H_series(h: list[mp.mpf]) -> list[mp.mpf]:
    """H = d/dbeta log h  (the d-log series of the shifted analytic part h)."""
    return series_deriv(series_log(h))


def dlog_pade_singularity(h: list[mp.mpf], order: int) -> tuple[Optional[mp.mpf], Optional[mp.mpf]]:
    """
    Form the [order/order] Pade approximant of the d-log series H and return
    (|beta_c|, arg beta_c) of the nearest singularity (root of the Pade
    denominator). Returns (None, None) if too few coefficients.
    """
    H = _dlog_H_series(h)
    need = 2 * order + 1
    if len(H) < need:
        return None, None
    P, Q = mp.pade(H[:need], order, order)
    # roots of Q(x): coefficients low->high; polyroots wants high->low
    coeffs_hi_lo = [Q[i] for i in range(len(Q) - 1, -1, -1)]
    try:
        roots = mp.polyroots(coeffs_hi_lo, maxsteps=400, extraprec=300)
    except Exception:
        return None, None
    roots = [r for r in roots if abs(r) > mp.mpf("1e-9")]
    if not roots:
        return None, None
    near = min(roots, key=lambda r: abs(r))
    return abs(near), mp.arg(near)


def dlog_pade_forward(series: ConnectedSeries, order: int, beta: mp.mpf = BETA) -> DlogPadeResult:
    """
    d-log-Pade FORWARD evaluation of Delta(beta).

      Delta = beta^m * h(beta), h analytic, h(0) = d_m.
      H(beta) = (log h)'(beta).
      [order/order] Pade of H, integrate 0->beta to recover log h(beta) - log h(0),
      exponentiate, multiply by beta^m.

    Returns the resummed Delta(beta) and the nearest-singularity diagnostics.
    """
    h = series.shifted_h()
    m = series.lowest_order
    need = 2 * order + 1
    if len(h) < need + 1:
        return DlogPadeResult(order, None, None, None,
                              note=f"need >= {need + 1} contiguous coeffs, have {len(h)}")
    H = _dlog_H_series(h)
    P, Q = mp.pade(H[:need], order, order)

    def H_pade(b):
        num = sum(P[i] * b ** i for i in range(len(P)))
        den = sum(Q[i] * b ** i for i in range(len(Q)))
        return num / den

    integral = mp.quad(H_pade, [0, beta])
    h_beta = h[0] * mp.e ** integral
    delta6 = beta ** m * h_beta
    sabs, sarg = dlog_pade_singularity(h, order)
    return DlogPadeResult(order, delta6, sabs, sarg)


def dlog_pade_predict_next(series: ConnectedSeries) -> tuple[Optional[mp.mpf], str]:
    """
    PREDICTIVE TEST (d-log-Pade): from the contiguous connected coefficients
    d_m .. d_K, predict the next coefficient d_{K+1}.

    Mechanism: build the d-log series H of h, form the highest balanced Pade
    [a/b] that the known coefficients support, re-expand it ONE order further,
    integrate back through log/exp to recover the predicted next h-coefficient,
    which equals d_{K+1}.

    One contiguous coefficient cannot fix a non-trivial continuation, so this
    honestly returns None until >= 2 contiguous coefficients are supplied.
    On the current frontier this is used for exact leave-one-out tests.
    """
    h = series.shifted_h()
    if len(h) < 4:
        return None, ("under-determined: a non-trivial [>=1/>=1] d-log Pade re-expansion needs "
                      ">= 4 contiguous connected coeffs (d_m..d_{m+3}); fewer fix only a constant "
                      "or empty d-log. The d-log-Pade predictive test activates once "
                      "d_5..d_8 are all supplied (then it predicts d_9).")
    logh = series_log(h)
    H = series_deriv(logh)                       # H[k] = (k+1)*logh[k+1]; len(H) = len(h)-1
    nH = len(H)
    a_deg = (nH - 1) // 2
    b_deg = nH - 1 - a_deg
    if a_deg < 1:
        return None, "under-determined: too few d-log coefficients for a [>=1/>=1] Pade"
    P, Q = mp.pade(H, a_deg, b_deg)
    Hext = ratio_series(P, Q, nH)                # indices 0..nH (one term beyond known H)
    # next log coeff: logh[len(h)] = H[len(h)-1] / len(h) = Hext[nH] / (nH+1)
    logh_pred = list(logh) + [Hext[nH] / mp.mpf(nH + 1)]
    h_ext = series_exp(logh_pred)
    return h_ext[len(h)], f"d-log-Pade [{a_deg}/{b_deg}] re-expansion"


# ===========================================================================
# 5. ANSATZ (b): tadpole-improved / boosted PT
# ===========================================================================
@dataclass
class TadpoleResult:
    label: str
    P: Optional[mp.mpf]
    beta_eff: Optional[mp.mpf]
    converged: bool
    note: str = ""


def tadpole_fixed_point(boost_map: Callable[[mp.mpf], mp.mpf],
                        label: str,
                        seed: mp.mpf = mp.mpf("0.5")) -> TadpoleResult:
    """
    Self-consistent boosted-PT fixed point P = P_1plaq(beta_eff(P)), where the
    boosted coupling beta_eff is a function of the current <P> (= u_0^4).
    Damped iteration. Reports the fixed point and whether it converged.
    """
    P = seed
    for _ in range(2000):
        try:
            Pn = P_1plaq(boost_map(P))
        except Exception:
            return TadpoleResult(label, None, None, False, "evaluation failed")
        if abs(Pn - P) < mp.mpf("1e-30"):
            return TadpoleResult(label, Pn, boost_map(Pn), True)
        P = mp.mpf("0.5") * P + mp.mpf("0.5") * Pn
    return TadpoleResult(label, P, boost_map(P), False, "did not reach fixed-point tolerance")


def boosted_coupling_for_value(target: mp.mpf) -> mp.mpf:
    """beta_eff^can = P_1plaq^{-1}(target). The IMPLICIT boosted coupling that
    would reproduce `target` through the single-plaquette function. This is a
    read-off, NOT a derivation of `target` (research map Section 7)."""
    return mp.findroot(lambda b: P_1plaq(b) - target, mp.mpf("9.0"))


def tadpole_geometric_predict_next(series: ConnectedSeries) -> tuple[Optional[mp.mpf], str]:
    """
    PREDICTIVE TEST (tadpole / boosted PT). A boosted-coupling continuation with
    a single nearest real boosting singularity beta* maps the connected series
    onto a leading geometric tail: d_{n+1}/d_n -> 1/beta* asymptotically. From
    the last two contiguous coefficients (d_{K-1}, d_K) it estimates the ratio
    rho = d_K / d_{K-1} and predicts d_{K+1} = rho * d_K.

    One contiguous coefficient gives no ratio -> returns None (honest null).
    On the current frontier this is used for exact leave-one-out tests.
    """
    cc = series.contiguous()
    if len(cc) < 2:
        return None, "under-determined: a geometric ratio needs >= 2 contiguous connected coeffs"
    (_, c_prev), (_, c_last) = cc[-2], cc[-1]
    if c_prev == 0:
        return None, "previous coefficient is zero; ratio undefined"
    rho = c_last / c_prev
    return rho * c_last, f"boosted single-pole ratio rho = d_K/d_(K-1) = {mp.nstr(rho, 8)} (beta* = {mp.nstr(1/rho, 8)})"


# ===========================================================================
# 6. EXACT-VS-PREDICTED comparison
# ===========================================================================
def compare_against_exact(predicted: Optional[mp.mpf],
                          exact,
                          ansatz: str,
                          coeff_label: str,
                          rel_tol: mp.mpf = mp.mpf("0.05")) -> Optional[bool]:
    """
    Compare an ansatz's PREDICTED next connected coefficient against the EXACT
    one supplied by the parallel cycle. Returns True (SUPPORT), False (FALSIFY),
    or None (no prediction available yet). Prints the comparison line.

    rel_tol is the support window (default 5% relative). A genuine continuation
    of the right analytic class should land well inside it; a miss by more than
    rel_tol falsifies the ansatz at this order.
    """
    if exact is None:
        print(f"  [NO-PREDICTION] {ansatz}: exact {coeff_label} not supplied "
              f"(predicted = {mp.nstr(predicted, 8) if predicted is not None else 'n/a'})")
        return None
    exact = mp.mpf(exact) if not isinstance(exact, mp.mpf) else exact
    if predicted is None:
        print(f"  [NO-PREDICTION] {ansatz}: no prediction for {coeff_label} from the supplied series "
              f"(exact = {mp.nstr(exact, 8)})")
        return None
    rel = abs((predicted - exact) / exact) if exact != 0 else abs(predicted - exact)
    ok = rel <= rel_tol
    tag = "SUPPORT" if ok else "FALSIFY"
    print(f"  [{tag}] {ansatz}: {coeff_label} predicted = {mp.nstr(predicted, 8)}, "
          f"exact = {mp.nstr(exact, 8)}, rel = {mp.nstr(rel, 4)} (window {mp.nstr(rel_tol, 3)})")
    return ok


# ===========================================================================
# 7. Controlled complex-pair PROXY (validates that the method is sound when the
#    singularity structure cooperates -- the research-map claim, reproduced)
# ===========================================================================
def proxy_series(order: int, R: mp.mpf, theta: mp.mpf, power: mp.mpf,
                 target_at_6: mp.mpf) -> tuple[ConnectedSeries, mp.mpf]:
    """
    A function with a complex-conjugate-pair branch point at beta = R e^{+-i theta},
    amplitude tuned so f(6) = target_at_6. Models the conjectured analytic
    structure of the PHYSICAL Delta (dominant singularity a complex pair off the
    real axis, with beta = 6 sitting just BEYOND the singular radius |beta_c| ~ 5.7,
    so the bare Taylor sum diverges and analytic continuation is mandatory --
    exactly the regime the resummation must handle).

    f(beta) = A * [ (1 - 2 (beta/R) cos theta + (beta/R)^2)^(-power) - 1 ].

    The closed form is the Gegenbauer (ultraspherical) generating function, so the
    Taylor coefficients are A * C_n^(power)(cos theta) / R^n -- computed in closed
    form (NOT by numerical differentiation, which fails across the branch cut).
    The value at beta = 6 is taken from the closed form (the analytic continuation),
    NOT from the divergent series. Lowest order is 1.
    """
    x = mp.cos(theta)

    def f_unit(beta):                              # closed-form analytic continuation
        z = beta / R
        return (1 - 2 * z * x + z * z) ** (-power) - 1

    A = target_at_6 / f_unit(mp.mpf(6))
    s = ConnectedSeries(lowest_order=1)
    for k in range(1, order + 1):
        s.set_coeff(k, A * mp.gegenbauer(k, power, x) / R ** k)   # exact Taylor coeff
    true6 = A * f_unit(mp.mpf(6))
    return s, true6


# ===========================================================================
# MAIN
# ===========================================================================
def main() -> int:
    section("0. Baseline (retained primitives, recomputed for self-consistency)")
    check("P_1plaq(6) = 0.4225317396 (retained single-plaquette value)",
          abs(P1_AT_6 - mp.mpf("0.4225317396")) < mp.mpf("1e-9"),
          f"P_1plaq(6) = {mp.nstr(P1_AT_6, 12)}")
    cpt = P_1plaq_taylor(7)
    check("P_1plaq Taylor c_1 = 1/18 (recurrence self-check)",
          cpt[1] == Fraction(1, 18), f"c_1 = {cpt[1]}")
    check("d_5 = 1/472392 (retained exact connected coefficient)",
          D5 == Fraction(1, 472392), f"d_5 = {mp.nstr(mp.mpf(1)/472392, 8)}")
    check("Delta(6) target from comparator = 0.594 - P_1plaq(6) ~ 0.1715 (comparator, NOT fitted)",
          abs(DELTA_TARGET - mp.mpf("0.17146826")) < mp.mpf("1e-6"),
          f"Delta_target = {mp.nstr(DELTA_TARGET, 8)} = 0.594(MC comparator) - {mp.nstr(P1_AT_6, 8)}")
    check("beta_eff^can = P_1plaq^{-1}(0.5934) = 9.32617 (research map Section 7; read-off, not derivation)",
          abs(boosted_coupling_for_value(MC_COMPARATOR_4DP) - mp.mpf("9.32617")) < mp.mpf("1e-3"),
          f"beta_eff^can = {mp.nstr(boosted_coupling_for_value(MC_COMPARATOR_4DP), 8)} "
          f"(reproduces the research map's recomputed constant; NOT a derivation of the value)")

    # -----------------------------------------------------------------------
    section("1. PROXY validation: the method is sound when the structure cooperates")
    print("  Controlled complex-pair branch point at |beta_c| ~ 5.7, amplitude tuned")
    print("  so the proxy's Delta(6) = 0.171 (matches the physical Delta(6) ~ 0.1715).")
    print("  This reproduces the research-map claim that d-log-Pade converges to ~1e-3")
    print("  by ~[10/10] -- and proves the predictive next-coefficient call works.\n")
    proxy, proxy_true6 = proxy_series(order=24, R=mp.mpf("5.7"), theta=mp.mpf("0.55"),
                                      power=mp.mpf("0.5"), target_at_6=mp.mpf("0.171"))

    # 1a. singularity localization improves with order
    sing = {}
    for order in (4, 6, 8, 10):
        sa, sg = dlog_pade_singularity(proxy.shifted_h(), order)
        sing[order] = (sa, sg)
        print(f"    [{order:2d}/{order:2d}] nearest singularity |beta_c| = {mp.nstr(sa, 8)}, "
              f"arg = {mp.nstr(sg, 5)}")
    check("proxy d-log-Pade localizes the complex-pair singularity near |beta_c| = 5.70",
          abs(sing[10][0] - mp.mpf("5.7")) < mp.mpf("0.05"),
          f"[10/10] |beta_c| = {mp.nstr(sing[10][0], 8)} (true 5.7)")
    check("proxy singularity is OFF the real axis (arg != 0), i.e. a genuine complex pair",
          abs(sing[10][1]) > mp.mpf("0.4"),
          f"[10/10] arg = {mp.nstr(sing[10][1], 5)} (true 0.55)")

    # 1b. forward reconstruction converges to ~1e-3 by [10/10]
    #     ([n/n] needs 2n+1 d-log coeffs; the order-24 proxy supports up to [11/11]).
    proxy_errs = {}
    for order in (4, 6, 8, 10, 11):
        r = dlog_pade_forward(proxy, order)
        if r.delta6 is None:
            continue
        err = abs(r.delta6 - proxy_true6)
        proxy_errs[order] = err
        print(f"    [{order:2d}/{order:2d}] recon Delta(6) = {mp.nstr(r.delta6, 10)}  "
              f"abs err = {mp.nstr(err, 4)}")
    check("proxy d-log-Pade FORWARD converges to <= 1e-3 by [10/10] (research-map claim)",
          proxy_errs[10] <= mp.mpf("1e-3"),
          f"[10/10] abs err = {mp.nstr(proxy_errs[10], 4)} (true Delta(6) = {mp.nstr(proxy_true6, 8)})")
    check("proxy d-log-Pade FORWARD is monotone-improving 6->8->10",
          proxy_errs[8] < proxy_errs[6] and proxy_errs[10] < proxy_errs[8],
          f"err[6]={mp.nstr(proxy_errs[6],3)} err[8]={mp.nstr(proxy_errs[8],3)} err[10]={mp.nstr(proxy_errs[10],3)}")

    # 1c. PREDICTIVE next-coefficient mechanism recovers a held-out proxy coefficient.
    #     This IS the exact-vs-predicted scaffold, validated on a known function: feed the
    #     predictor the contiguous coefficients d_1..d_K and check it reproduces d_{K+1}.
    cc_proxy = proxy.contiguous()
    rel_by_K = {}
    for K in (6, 8, 11):
        pk = ConnectedSeries(lowest_order=1)
        for n, v in cc_proxy[:K]:
            pk.set_coeff(n, v)
        pred_k, _ = dlog_pade_predict_next(pk)
        true_k = cc_proxy[K][1]
        rel_by_K[K] = abs((pred_k - true_k) / true_k)
        print(f"    given d_1..d_{K}: predicted d_{K + 1} = {mp.nstr(pred_k, 10)}, "
              f"true = {mp.nstr(true_k, 10)}, rel = {mp.nstr(rel_by_K[K], 4)}")
    check("proxy PREDICTIVE d-log-Pade recovers held-out next coefficient and SHARPENS with order",
          rel_by_K[11] < mp.mpf("1e-5") and rel_by_K[8] < rel_by_K[6],
          f"rel at K=6,8,11 = {mp.nstr(rel_by_K[6],3)}, {mp.nstr(rel_by_K[8],3)}, {mp.nstr(rel_by_K[11],3)} "
          f"(the more contiguous coeffs, the sharper the next-coeff prediction)")

    # -----------------------------------------------------------------------
    section("2. PHYSICAL series -- current exact coefficient frontier d_5..d_11")
    phys = ConnectedSeries(lowest_order=5)
    for n in sorted(EXACT_CONNECTED):
        phys.set_coeff(n, mp_fraction(EXACT_CONNECTED[n]))

    print("  Connected series Delta(beta) = P_full(beta) - P_1plaq(beta)")
    print("                         = sum_{n>=5} d_n beta^n")
    print("  Current contiguous exact frontier: d_5..d_11 (7 coefficients).\n")
    for n in sorted(EXACT_CONNECTED):
        value = EXACT_CONNECTED[n]
        print(f"    d_{n:<2d} = {value} = {float(value):+.8e}")

    ratios = {
        n: mp_fraction(EXACT_CONNECTED[n + 1]) / mp_fraction(EXACT_CONNECTED[n])
        for n in range(5, 11)
    }
    print("\n  Consecutive ratios:")
    for n, ratio in ratios.items():
        print(f"    d_{n + 1}/d_{n} = {mp.nstr(ratio, 12)}")

    delta6_trunc = phys.eval_truncated(BETA)
    P6_trunc = P1_AT_6 + delta6_trunc
    print("\n  Forward strong-coupling partial sum through d_11:")
    print(f"    Delta_{{5..11}}(6) = {mp.nstr(delta6_trunc, 12)}")
    print(f"    P_1plaq(6) + Delta_{{5..11}}(6) = {mp.nstr(P6_trunc, 12)}")
    print(f"    comparator 0.594; gap = {mp.nstr(MC_COMPARATOR - P6_trunc, 8)}")

    check("current coefficient frontier is contiguous d_5..d_11",
          [n for n, _ in phys.contiguous()] == list(range(5, 12)),
          "all exact coefficients d_5 through d_11 are loaded; old waiting-on-d_6 state retired")
    check("d_6/d_5 and d_7/d_6 already break a single-ratio geometric tail",
          ratios[5] != ratios[6],
          f"d_6/d_5 = {mp.nstr(ratios[5], 8)} while d_7/d_6 = {mp.nstr(ratios[6], 8)}")
    check("d_9 is the first sign flip of the connected coefficient sequence",
          all(EXACT_CONNECTED[n] > 0 for n in range(5, 9)) and EXACT_CONNECTED[9] < 0,
          "d_5..d_8 > 0 but d_9 < 0")
    check("d_11 is a near-cancellation diagnostic, not a convergence closure",
          abs(ratios[10]) < mp.mpf("0.01"),
          f"d_11/d_10 = {mp.nstr(ratios[10], 8)}")
    check("the d_5..d_11 truncated strong-coupling partial sum does not close beta=6",
          abs(P6_trunc - MC_COMPARATOR) > mp.mpf("0.05"),
          f"P_trunc(6) = {mp.nstr(P6_trunc, 8)} is a divergent/diagnostic partial sum, not 0.594")

    # -----------------------------------------------------------------------
    section("3. TADPOLE / boosted-PT self-consistency fixed points (forward test)")
    print("  u_0 = <P>^{1/4} self-consistency. Several boosting conventions; report each.\n")
    tp_collapse = tadpole_fixed_point(lambda P: BETA * P, "beta_eff = beta * u_0^4 = beta*<P>")
    tp_overboost = tadpole_fixed_point(lambda P: BETA / P, "beta_eff = beta / <P> (over-boost)", seed=mp.mpf("0.8"))
    print(f"    {tp_collapse.label}: P = {mp.nstr(tp_collapse.P, 8)}, "
          f"beta_eff = {mp.nstr(tp_collapse.beta_eff, 6)}  (converged={tp_collapse.converged})")
    print(f"    {tp_overboost.label}: P = {mp.nstr(tp_overboost.P, 8)}, "
          f"beta_eff = {mp.nstr(tp_overboost.beta_eff, 6)}  (converged={tp_overboost.converged})")
    print(f"    P_1plaq(31.5) = {mp.nstr(P_1plaq(mp.mpf('31.5')), 8)}  "
          f"(reproduces blocked Drouffe-Itzykson M4 value 0.8740)\n")

    check("tadpole self-consistency of the BARE single-plaquette series collapses to P=0 (trivial)",
          abs(tp_collapse.P) < mp.mpf("1e-20"),
          "u_0^4 = P_1plaq(beta*u_0^4) has only the trivial fixed point -- "
          "boosting the bare series alone does NOT reach 0.594")
    check("over-boost convention beta/<P> lands in the crossover, NOT at the comparator",
          tp_overboost.P is not None and abs(tp_overboost.P - MC_COMPARATOR) > mp.mpf("0.01"),
          f"P = {mp.nstr(tp_overboost.P, 6)} (convention-dependent; not a derivation of 0.594)")
    check("the z=6 mean-field/Drouffe-Itzykson self-consistent branch is the blocked 0.8740",
          abs(P_1plaq(mp.mpf("31.5")) - mp.mpf("0.8740")) < mp.mpf("1e-3"),
          f"P_1plaq(31.5) = {mp.nstr(P_1plaq(mp.mpf('31.5')), 8)} (research map: blocked)")
    print("  => FINDING (tadpole): boosting the single-plaquette series alone either collapses")
    print("     (P=0) or, convention-dependent, lands at the blocked 0.611/0.874 -- it does NOT")
    print("     independently reach 0.594. A tadpole test therefore lives in the connected-")
    print("     coefficient PATTERN it implies (geometric tail), tested predictively in Section 4.")

    # -----------------------------------------------------------------------
    section("4. LIVE predictive verdicts against d_5..d_11")
    print("  The old harness was waiting on exact d_6. The current frontier has d_5..d_11,")
    print("  so this section performs leave-one-out predictions against the exact coefficients.")
    print("  FALSIFY/SUPPORT labels are ansatz-test outcomes, not runner failures.\n")

    exact_series = phys
    n_known = len(exact_series.contiguous())
    highest = 4 + n_known
    print(f"  Exact contiguous connected coefficients supplied: d_5 .. d_{highest} ({n_known} total).")

    print("\n  4a. tadpole/geometric single-ratio test:")
    tadpole_results = {}
    for top in range(7, 12):
        sub = ConnectedSeries(lowest_order=5)
        for n in range(5, top):
            sub.set_coeff(n, mp_fraction(EXACT_CONNECTED[n]))
        pred_tad, m_tad = tadpole_geometric_predict_next(sub)
        exact_top = mp_fraction(EXACT_CONNECTED[top])
        print(f"      from d_5..d_{top - 1}, tadpole predicts d_{top} [{m_tad}]")
        tadpole_results[top] = compare_against_exact(
            pred_tad,
            exact_top,
            "tadpole/geometric",
            f"d_{top}",
        )
    check("tadpole/geometric ansatz is falsified by the current coefficient frontier",
          all(result is False for result in tadpole_results.values()),
          "every leave-one-out test d_7..d_11 misses the exact coefficient outside the 5% window")
    check("tadpole/geometric gets the d_9 sign wrong",
          (mp_fraction(EXACT_CONNECTED[8]) / mp_fraction(EXACT_CONNECTED[7])) * mp_fraction(EXACT_CONNECTED[8]) > 0
          and EXACT_CONNECTED[9] < 0,
          "single-ratio prediction from d_7,d_8 is positive, exact d_9 is negative")

    print("\n  4b. d-log-Pade predictive test:")
    dlog_results = {}
    for top in range(9, 12):
        sub = ConnectedSeries(lowest_order=5)
        for n in range(5, top):
            sub.set_coeff(n, mp_fraction(EXACT_CONNECTED[n]))
        pred_dl, m_dl = dlog_pade_predict_next(sub)
        exact_top = mp_fraction(EXACT_CONNECTED[top])
        print(f"      from d_5..d_{top - 1}, d-log-Pade predicts d_{top} [{m_dl}]")
        dlog_results[top] = compare_against_exact(
            pred_dl,
            exact_top,
            "d-log-Pade",
            f"d_{top}",
        )
    sa, sg = dlog_pade_singularity(exact_series.shifted_h(), 2)
    print(f"      [2/2] d-log-Pade nearest singularity from d_5..d_10: "
          f"|beta_c| = {mp.nstr(sa, 7)}, arg = {mp.nstr(sg, 6)}")
    check("d-log-Pade is active on the current frontier",
          set(dlog_results) == {9, 10, 11} and all(result is not None for result in dlog_results.values()),
          "exact d_5..d_11 activate predictions for d_9,d_10,d_11")
    check("d-log-Pade is not support-stable across the current frontier",
          dlog_results[9] is False and dlog_results[10] is True and dlog_results[11] is False,
          "d_9 fails, d_10 is a one-order support hit, d_11 fails badly; no stable closure")
    check("d-log-Pade nearest singularity remains a diagnostic, not a beta=6 value proof",
          sa is not None and abs(sg) > mp.mpf("0.5") and sa < BETA,
          f"[2/2] gives |beta_c|={mp.nstr(sa, 7)} < 6 and off-axis arg={mp.nstr(sg, 5)}")

    print("\n  4c. SELF-TEST of the comparison machinery on SYNTHETIC coefficients (CI guard).")
    print("      Proves the comparator fires SUPPORT for a consistent next coefficient and")
    print("      FALSIFY for an inconsistent one.")
    base5 = mp.mpf(D5.numerator) / mp.mpf(D5.denominator)
    bstar = mp.mpf("5.7")
    # (i) a synthetic series with a single real pole at beta*=5.7: d_{n+1}=d_n/beta*
    geo = ConnectedSeries(lowest_order=5)
    for i in range(3):
        geo.set_coeff(5 + i, base5 / bstar ** i)
    geo_known = ConnectedSeries(lowest_order=5)
    for n, v in geo.contiguous()[:-1]:
        geo_known.set_coeff(n, v)
    pred_geo, _ = tadpole_geometric_predict_next(geo_known)
    v_support = compare_against_exact(pred_geo, geo.contiguous()[-1][1],
                                      "self-test SUPPORT (geometric d_7)", "d_7")
    check("comparison machinery returns SUPPORT for a geometric-consistent next coefficient",
          v_support is True, "tadpole predictor reproduces the exact next coeff of a pure single-pole series")
    # (ii) a synthetic series whose next coeff is deliberately OFF the geometric pattern
    v_falsify = compare_against_exact(pred_geo, geo.contiguous()[-1][1] * mp.mpf("1.5"),
                                      "self-test FALSIFY (off-pattern d_7)", "d_7")
    check("comparison machinery returns FALSIFY when the next coefficient breaks the ansatz pattern",
          v_falsify is False, "a 50% deviation from the predicted coeff exceeds the 5% support window -> FALSIFY")

    # -----------------------------------------------------------------------
    section("5. Padé continuation spread from the current d_5..d_11 frontier")
    print("  Recompute the normalized B(beta)=Delta/(d_5 beta^5) Padé diagnostics from")
    print("  the seven exact coefficients. These are diagnostics only, not a bound or a")
    print("  derivation of the Monte-Carlo comparator.\n")

    base = mp_fraction(D5)
    b_coeffs = [mp_fraction(EXACT_CONNECTED[n]) / base for n in range(5, 12)]

    def eval_poly(coefs: list[mp.mpf], x: mp.mpf) -> mp.mpf:
        return sum(coefs[i] * x ** i for i in range(len(coefs)))

    def pade_p6(L: int, M: int) -> mp.mpf:
        coeffs = b_coeffs[: L + M + 1]
        P, Q = mp.pade(coeffs, L, M)
        B6 = eval_poly(P, BETA) / eval_poly(Q, BETA)
        return P1_AT_6 + base * BETA ** 5 * B6

    pade_values = {
        (2, 3): pade_p6(2, 3),
        (3, 2): pade_p6(3, 2),
        (3, 3): pade_p6(3, 3),
        (2, 4): pade_p6(2, 4),
        (4, 2): pade_p6(4, 2),
    }
    for key, value in pade_values.items():
        print(f"    [{key[0]}/{key[1]}] -> <P>(6) = {mp.nstr(value, 12)}")

    full_span = max(pade_values.values()) - min(pade_values.values())
    high_order = [pade_values[(3, 3)], pade_values[(2, 4)], pade_values[(4, 2)]]
    high_span = max(high_order) - min(high_order)
    print(f"\n    full spread = {mp.nstr(min(pade_values.values()), 8)} .. "
          f"{mp.nstr(max(pade_values.values()), 8)} (width {mp.nstr(full_span, 6)})")
    print(f"    highest-order [3/3],[2/4],[4/2] cluster = "
          f"{mp.nstr(min(high_order), 8)} .. {mp.nstr(max(high_order), 8)} "
          f"(width {mp.nstr(high_span, 6)})")
    check("current Padé values reproduce the d_11 continuation-spread diagnostic",
          abs(pade_values[(2, 3)] - mp.mpf("0.589858289")) < mp.mpf("1e-7")
          and abs(pade_values[(3, 3)] - mp.mpf("0.537903703")) < mp.mpf("1e-7")
          and abs(pade_values[(2, 4)] - mp.mpf("0.514032403")) < mp.mpf("1e-7"),
          "[2/3], [3/3], and [2/4] match the current coefficient-packet diagnostics")
    check("seven-coefficient Padé continuation is ambiguous, not converged to 0.5934",
          full_span > mp.mpf("0.05") and max(high_order) < mp.mpf("0.55"),
          f"full span width {mp.nstr(full_span, 5)}; highest-order cluster below 0.55")
    check("0.594 remains a comparator, not a derivation input",
          all(abs(v - MC_COMPARATOR) > mp.mpf("0.004") for v in high_order),
          "highest-order approximants sit away from the comparator and are computed only from exact coefficients")

    # -----------------------------------------------------------------------
    section("6. Honest test summary")
    print("  * The d-log-Pade METHOD is sound on a controlled complex-pair proxy: it localizes")
    print("    the singularity (|beta_c|->5.70, off-axis) and reconstructs Delta(6) to <1e-3 by")
    print("    [10/10], and its predictive next-coefficient call is exact to ~1e-11 on the proxy.")
    print("  * On the PHYSICAL series, the current exact frontier is d_5..d_11.")
    print("    The old waiting-on-d_6 state is stale and has been retired by this runner.")
    print("  * Tadpole/boosted-PT of the BARE single-plaquette series does NOT reach 0.594: it")
    print("    collapses to 0 or, convention-dependent, lands on the blocked 0.611 / 0.8740,")
    print("    and its connected-coefficient single-ratio pattern is falsified by d_7..d_11.")
    print("  * d-log-Pade is active but not support-stable: d_9 fails, d_10 is a one-order")
    print("    support hit, and d_11 fails badly. The seven-coefficient Padé continuation")
    print("    spread is diagnostic/ambiguous, not a closure or a physical value bound.")
    print("  * TEST STATUS: CURRENT-FRONTIER VERDICT. This harness evaluates the route; it")
    print("    does NOT close beta=6. 0.594 is a Monte-Carlo comparator, never a derivation input.")

    section(f"SCORECARD: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
