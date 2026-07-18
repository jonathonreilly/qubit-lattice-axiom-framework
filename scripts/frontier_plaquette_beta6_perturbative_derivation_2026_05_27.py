#!/usr/bin/env python3
"""Pattern A runner-local diagnostic for the beta=6 perturbative packet note.

The runner exercises the algebraic content of the explicit runner-local SU(3)
Wilson-plaquette perturbative expansion at beta=6 GIVEN the source-wired
native matrix coefficient, explicit non-satisfying runner-local W-PHYS
comparison condition, and
other explicit runner-local inputs, and tests
whether tadpole-improvement plus finite-order truncation plus a Pade [m/n]
resummation reaches the explicit runner-local MC comparator <P>_MC = 0.5934 to any
controlled accuracy.

This is a RUNNER-LOCAL DIAGNOSTIC: only the native coefficient
w*s^2/(4n) is dependency-wired to the matrix theorem. The comparison
relation and physical Wilson dictionary are parts of W-PHYS; the NSPT
coefficient packet, MC comparator,
and F2 comparator remain explicit runner-local for this diagnostic only. The beta=6
diagnostic specialization, g_bare=1 specialization, and alpha_bare scale
notation are not downstream-licensed physical authorities. The runner reports
the resulting numerical landscape and a scale diagnostic. The verdict the
runner outputs is:

    (i) at beta=6 the listed truncations through n=16 saturate near
        <P>_PT = 0.919331, missing the explicit runner-local comparator by about 54.9%;
    (ii) Pade [m/n] resummations with m,n >= 1 and m+n <= 12 remain in the
         same band;
    (iii) tadpole-improved truncations (N <= 8, high branch) and
          tadpole-improved Pade grids (m,n >= 1, 3 <= m+n <= 8, high branch)
          saturate near <P> = 0.910550, missing the explicit runner-local comparator by
          about 53.4%;
    (iv) the result is conditional only for this finite weak-coupling /
         tadpole / Pade envelope over explicit runner-local inputs, not for the actual
         beta=6 plaquette surface or non-perturbative routes.

No new axiom, primitive, or repo vocabulary is proposed. No external
numerical target is consumed as a derivation input. The explicit runner-local MC comparator
<P>_MC = 0.5934 enters only as a diagnostic comparator.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import math
import sys

ROOT = Path(__file__).resolve().parent.parent
NOTE = ROOT / "docs" / "PLAQUETTE_BETA6_PERTURBATIVE_DERIVATION_BOUNDED_OBSTRUCTION_NOTE_2026-05-27.md"
WILSON_NOTE = ROOT / "docs" / "WILSON_SMALL_A_MATCHING_BETA_GBARE_NARROW_THEOREM_NOTE_2026-06-07.md"

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    print(f"{status}: {label}")
    if detail:
        print(f"      {detail}")


def section(title: str) -> None:
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78)


# ---------------------------------------------------------------------------
# Framework parameters
# ---------------------------------------------------------------------------
N_C = 3
BETA = 6.0
G2_BARE = 2.0 * N_C / BETA   # = 1 at beta=6
ALPHA_BARE = G2_BARE / (4.0 * math.pi)   # = 1/(4*pi)
MC_REFERENCE = 0.5934   # explicit runner-local comparator only; not a derivation input
F2_SCALE_PERCENT = 0.0833   # explicit runner-local F2 comparator; not reusable

# Census pins for the executed method grids (mutation-decisive against
# silent grid shrinkage or acceptance-filter drift).
PADE_EVALUATED_COUNT = 66
TI_PADE_CONVERGED_COUNT = 27

# Explicit runner-local NSPT coefficient packet for the Wilson plaquette in
# SU(3) pure gauge theory, in the convention
#   <P>(beta) = 1 - sum_{n>=1} w_n * (1/beta)^n .
# These values are explicit runner-local for this diagnostic only. They are NOT framework
# primitives, new axioms, retained-grade authorities, empirical selectors, or
# downstream-licensed values.
#
# w_1 is consumed by this runner as 4.0 / 9.0.
W_COEFFS_NSPT_SU3 = [
    None,                  # w_0 placeholder (not used)
    4.0 / 9.0,             # w_1
    0.20305,               # w_2
    0.16766,               # w_3
    0.18 ,                 # w_4
    0.236,                 # w_5
    0.336,                 # w_6
    0.510,                 # w_7
    0.806,                 # w_8
    1.30,                  # w_9
    2.14,                  # w_10
    3.59,                  # w_11
    6.13,                  # w_12
    10.65,                 # w_13
    18.78,                 # w_14
    33.51,                 # w_15
    60.50,                 # w_16
]

# ---------------------------------------------------------------------------
# Algebraic content checks
# ---------------------------------------------------------------------------


def test_framework_constants() -> None:
    section("C1: source-wired native coefficient + explicit W-PHYS condition")
    if not WILSON_NOTE.exists():
        check(
            f"defined matrix coefficient note {WILSON_NOTE.name} exists",
            False,
            f"path={WILSON_NOTE}",
        )
        return
    wilson_body = WILSON_NOTE.read_text()
    wilson_flat = " ".join(wilson_body.split())
    check(
        "matrix theorem supplies only the native w*s^2/(4n) coefficient",
        "w s^2/(4n)" in wilson_flat
        and "no comparison coefficient" in wilson_flat,
        "native coefficient is present without a target equation",
    )
    check(
        "matrix theorem does not contain a beta=6/g_bare specialization",
        "g_bare^2 = 1" not in wilson_flat and "beta = 6" not in wilson_flat,
        "physical specialization remains runner-local",
    )
    check(
        "matrix theorem leaves external targets and parameter equations outside scope",
        "Any comparison target" in wilson_flat
        and "requires separate authority" in wilson_flat,
        "the dependency supplies native Taylor algebra, not W-PHYS",
    )
    # beta = 2 N_c / g_bare^2; with g_bare = 1, beta = 6 at N_c = 3.
    beta_from_w_phys = 2.0 * N_C / 1.0
    check(
        "explicit W-PHYS condition gives beta=6 at N_c=3, g_bare=1",
        math.isclose(beta_from_w_phys, 6.0, rel_tol=1e-15),
        f"beta = {beta_from_w_phys}",
    )
    # g^2_bare at beta=6: g^2 = 2 N_c / beta = 1
    g2 = 2.0 * N_C / BETA
    check(
        "g_bare^2 = 2 N_c / beta = 1 at beta=6",
        math.isclose(g2, 1.0, rel_tol=1e-15),
        f"g^2 = {g2}",
    )
    # alpha_bare = g^2 / (4 pi) = 1/(4 pi)
    alpha = g2 / (4.0 * math.pi)
    check(
        "alpha_bare = g_bare^2/(4 pi) = 1/(4 pi) at beta=6",
        math.isclose(alpha, 1.0 / (4.0 * math.pi), rel_tol=1e-15),
        f"alpha_bare = {alpha:.8f}, 1/(4 pi) = {1.0/(4.0*math.pi):.8f}",
    )


def test_source_boundary_manifest() -> None:
    section("T0: explicit-input runner-local diagnostic license")
    if not NOTE.exists():
        check(f"note file {NOTE.name} exists for explicit-input checks", False, f"path={NOTE}")
        return
    body = NOTE.read_text()
    flat = " ".join(body.split())
    flat_lower = flat.lower()
    check(
        "note records 2026-06-12 source-boundary demotion",
        "2026-06-12 Source-Boundary Demotion" in body
        and "Explicit Runner-Local Inputs (runner-local diagnostic license)" in body,
        "demotion and explicit-input sections present",
    )
    check(
        "note records explicit runner-local finite packet I_PT",
        "source-wired native coefficient w*s^2/(4n)" in flat
        and "explicit non-satisfying runner-local W-PHYS comparison condition" in flat
        and "explicit runner-local w_1..w_16" in flat,
        "packet separates native algebra, W-PHYS, and runner-local values",
    )
    check(
        "note records only the native matrix coefficient as the explicit dependency",
        "## 2026-07-18 source-side correction: only the native matrix coefficient is wired" in body
        and "WILSON_SMALL_A_MATCHING_BETA_GBARE_NARROW_THEOREM_NOTE_2026-06-07.md" in body
        and "Depends on" in body,
        "W-PHYS remains an explicit non-satisfying condition rather than dependency-laundered",
    )
    check(
        "note licenses unresolved NSPT/MC/F2 inputs for this diagnostic only",
        "nspt coefficient packet" in flat_lower
        and "mc comparator" in flat_lower
        and "f2 comparator" in flat_lower
        and flat_lower.count("explicit runner-local for this diagnostic only") >= 3
        and flat_lower.count("not licensed for downstream reuse") >= 3
        and "does not derive wilson action-surface selection" in flat_lower
        and "or a reusable `alpha_bare` authority" in flat_lower,
        "remaining explicit runner-local inputs and alpha/beta boundaries carry no downstream license",
    )
    check(
        "note excludes actual beta=6 surface and non-perturbative route claims",
        "actual beta=6 plaquette surface" in body
        and "not evaluated or excluded by this diagnostic" in body
        and "strong-coupling" in body
        and "exact Wigner-Racah" in body,
        "diagnostic remains conditional and finite-route only",
    )
    check(
        "note firewalls retained beta=6 surface claim after demotion",
        "## 2026-06-12 source firewall: no retained beta=6 surface claim" in body
        and "do not derive the actual `beta = 6`\nplaquette surface" in body
        and "do not derive `g_bare = 1`" in body
        and "do not license any downstream beta=6\nWilson/Haar surface claim" in body
        and "source-side dependency wiring plus demotion" in body,
        "source repair remains diagnostic-only after the Wilson edge is wired",
    )
    check(
        "note explicitly elects explicit-input diagnostic option",
        "## 2026-06-15 source-boundary repair: second option elected" in body
        and "keep the row as\nan explicit-input runner-local diagnostic only" in body
        and "not a retained or\neffective-bounded authority" in body
        and "Only the native matrix\ncoefficient is sourced; the comparison relation and Wilson dictionary are\nrunner-local `W-PHYS`." in body,
        "source-boundary second option is source-locked",
    )
    check(
        "note scopes row as non-downstream-licensed runner-local diagnostic only",
        "## 2026-06-20 source-boundary repair: non-downstream-licensed scoping" in body
        and "non-downstream-licensed runner-local diagnostic only." in flat
        and "No downstream row may cite this row as a retained or effective-bounded bridge or as a derivation" in flat
        and "native matrix coefficient" in flat,
        "source-boundary non-downstream-licensed scoping present; not a citeable bridge/derivation",
    )
    check(
        "note records remaining promotion authorities as unsupplied/open",
        "remaining authorities required *for promotion* are explicitly **unsupplied / open** here" in flat
        and "NSPT coefficient packet" in flat
        and "Wilson action-surface selection" in flat
        and "g_bare = 1" in flat
        and "MC comparator" in flat
        and "F2 comparator" in flat
        and flat.count("(open)") >= 4
        and "not promotable" in flat
        and "not licensed as a citeable bridge/derivation" in flat,
        "NSPT packet, surface/g_bare specialization, MC comparator, and F2 comparator remain open; row not promotable",
    )
    check(
        "note keeps 0.5934 MC value fenced as comparator-only, never a proof input",
        "0.5934" in body
        and "never a proof input" in flat
        and "no comparator number in this note is licensed for downstream reuse" in flat,
        "MC value stays a fenced comparator, never a derivation/proof input",
    )
    check(
        "note blocks downstream reuse of explicit runner-local beta=6 inputs",
        "cannot cite this row for anything beyond the runner-local\ndiagnostic over the explicit runner-local packet" in body
        and "Downstream rows that need a beta=6 Wilson/Haar plaquette value" in body,
        "downstream authority must come from a separate retained/effective-bounded row",
    )
    check(
        "note keeps non-perturbative routes open",
        "strong-coupling" in body
        and "transfer-matrix" in body
        and "Wigner-Racah" in body
        and "Borel-conformal" in body
        and "Monte Carlo" in body
        and "not evaluated or excluded by this diagnostic" in body,
        "finite perturbative route only",
    )


def test_one_loop_value() -> None:
    section("T2: 1-loop weak-coupling value over explicit runner-local packet")
    # M5: <P>_WC = 1 - (N^2-1)/(8 N^2) * 4/beta = 1 - (8)/(8*9) * 4/6
    #            = 1 - (1/9) * (4/6) = 1 - 4/54 = 1 - 0.07407 = 0.92593
    p_wc_m5 = 1.0 - (N_C * N_C - 1) / (8.0 * N_C * N_C) * 4.0 / BETA
    check(
        "M5 1-loop weak-coupling: <P> = 1 - (N^2-1)/(8 N^2) * 4/beta = 0.9259",
        math.isclose(p_wc_m5, 0.9259, abs_tol=1e-4),
        f"<P>_M5 = {p_wc_m5:.6f}",
    )
    # Equivalent form: 1 - w_1 / beta with w_1 = (N^2-1)/(2 N^2) = 4/9
    p_w1 = 1.0 - W_COEFFS_NSPT_SU3[1] / BETA
    check(
        "equivalent: <P> = 1 - w_1/beta with w_1 = (N^2-1)/(2 N^2) = 4/9",
        math.isclose(p_wc_m5, p_w1, rel_tol=1e-12),
        f"<P>_w1 = {p_w1:.6f}, |diff| = {abs(p_wc_m5 - p_w1):.3e}",
    )
    # Exact-value pin: the plain one-loop value is the rational 25/27.
    # This pin is mutation-decisive against sign/series-form errors
    # (e.g. 1 + sum instead of 1 - sum).
    check(
        "pin: plain one-loop value equals 25/27 = 0.925926 exactly",
        abs(p_wc_m5 - 25.0 / 27.0) < 1e-12 and round(p_w1, 6) == 0.925926,
        f"<P>_1loop = {p_w1:.9f}, 25/27 = {25.0/27.0:.9f}",
    )
    # Distance to the explicit runner-local MC comparator at 1-loop.
    gap_1l = abs(p_wc_m5 - MC_REFERENCE)
    pct_1l = 100.0 * gap_1l / MC_REFERENCE
    check(
        "1-loop overshoots explicit runner-local MC comparator by ~56%",
        gap_1l > 0.3,
        f"gap = {gap_1l:.4f}, pct = {pct_1l:.2f}%",
    )


def truncated_series(coeffs, N: int, beta_val: float) -> float:
    """Compute <P>(beta) = 1 - sum_{n=1..N} w_n / beta^n."""
    total = 0.0
    for n in range(1, N + 1):
        total += coeffs[n] / (beta_val ** n)
    return 1.0 - total


def test_truncated_series_convergence() -> None:
    section("T3: truncated perturbative series at beta=6 (explicit runner-local coefficient packet)")
    # Walk the truncation order N from 1 to 16 and record <P>_PT(N).
    print(f"  explicit runner-local coefficient packet:")
    print(f"    w_1={W_COEFFS_NSPT_SU3[1]:.5f}  w_2={W_COEFFS_NSPT_SU3[2]:.5f}  w_3={W_COEFFS_NSPT_SU3[3]:.5f}")
    print(f"    w_4={W_COEFFS_NSPT_SU3[4]:.5f}  w_5={W_COEFFS_NSPT_SU3[5]:.5f}  w_6={W_COEFFS_NSPT_SU3[6]:.5f}")
    print(f"    w_7={W_COEFFS_NSPT_SU3[7]:.5f}  w_8={W_COEFFS_NSPT_SU3[8]:.5f}  w_9={W_COEFFS_NSPT_SU3[9]:.5f}")
    print(f"    w_10={W_COEFFS_NSPT_SU3[10]:.4f}  ...  w_16={W_COEFFS_NSPT_SU3[16]:.4f}")
    print(f"  truncated <P>_PT(N) at beta=6:")
    P_PT_values = []
    for N in range(1, 17):
        P_PT = truncated_series(W_COEFFS_NSPT_SU3, N, BETA)
        P_PT_values.append(P_PT)
        gap = P_PT - MC_REFERENCE
        pct = 100.0 * gap / MC_REFERENCE
        print(f"    N={N:2d}:  <P>_PT = {P_PT:.6f},  gap = {gap:+.5f},  pct = {pct:+.3f}%")

    # Find the closest-to-explicit runner-local-comparator truncation N* and report it.
    best_N = min(range(1, 17), key=lambda N: abs(P_PT_values[N-1] - MC_REFERENCE))
    best_P = P_PT_values[best_N - 1]
    best_gap = best_P - MC_REFERENCE
    best_pct = 100.0 * abs(best_gap) / MC_REFERENCE
    print(f"  best truncation: N*={best_N}, <P>_PT(N*) = {best_P:.6f}, pct = {best_pct:.3f}%")
    # The explicit-input diagnostic says this listed finite truncation walk
    # does not reach within 5% of the explicit runner-local MC comparator.
    check(
        "OBSTRUCTION: truncated series at beta=6 saturates at >40% gap from explicit runner-local comparator",
        best_pct > 40.0,
        f"<P>_PT(N*={best_N}) = {best_P:.6f}, explicit runner-local comparator = {MC_REFERENCE:.4f}, "
        f"pct = {best_pct:.3f}%; residual exceeds 40% inside the explicit runner-local coefficient packet",
    )
    # Exact-value pins: mutation-decisive against packet/series/engine errors.
    check(
        "pin: <P>_PT(N=16) = 0.919331 to six decimals",
        round(P_PT_values[15], 6) == 0.919331,
        f"<P>_PT(16) = {P_PT_values[15]:.9f}",
    )
    check(
        "pin: saturation |<P>_PT(N) - <P>_PT(16)| < 1e-4 for all N >= 6",
        all(abs(P_PT_values[N - 1] - P_PT_values[15]) < 1e-4 for N in range(6, 17)),
        "matches the note's stated saturation window",
    )
    # Coefficient-growth diagnostic over the explicit runner-local packet.
    ratios = [W_COEFFS_NSPT_SU3[n+1]/W_COEFFS_NSPT_SU3[n] for n in range(1, 16)]
    print(f"  coefficient ratios w_(n+1)/w_n:")
    for n, r in enumerate(ratios, start=1):
        print(f"    n={n:2d} -> n+1={n+1:2d}: ratio = {r:.4f}")
    growing = sum(1 for r in ratios[5:] if r > 1.5)
    check(
        "scale diagnostic: every coefficient ratio > 1.5 for n>=6",
        growing == len(ratios[5:]),
        f"{growing}/{len(ratios[5:])} ratios exceed 1.5 starting at n=6",
    )


def tadpole_fixed_point(
    N: int,
    seed: float = 0.5,
    damping: float = 0.5,
    tol: float = 1e-13,
    max_iter: int = 2000,
) -> tuple[float, bool]:
    """High-branch fixed point of P = 1 - sum_{n<=N} w_n / (BETA*P)^n.

    This is the runner-local mean-plaquette self-consistent substitution
    beta -> beta*P (a tadpole-improvement-type substitution; the coefficients
    w_n are consumed unchanged).  The damped iteration from the high seed
    tracks the weak-coupling (high-<P>) branch only; callers must assert the
    returned convergence flag and the branch location.
    """
    P_it = seed
    for _ in range(max_iter):
        beta_eff = BETA * P_it
        P_new = truncated_series(W_COEFFS_NSPT_SU3, N, beta_eff)
        if abs(P_new - P_it) < tol:
            return P_new, True
        P_it = damping * P_it + (1.0 - damping) * P_new
    return P_it, False


def test_tadpole_improvement_signature() -> None:
    section("T4: tadpole-substitution signature over explicit runner-local packet")
    # Tadpole-improved coupling: u_0 = <P>^(1/4)
    # If <P> equals the explicit runner-local comparator, then u_0 = 0.5934^(1/4).
    u_0_mc = MC_REFERENCE ** 0.25
    check(
        "u_0 = <P>_MC^(1/4) at explicit runner-local comparator gives u_0 = 0.87768",
        math.isclose(u_0_mc, 0.87768, abs_tol=1e-4),
        f"u_0 = {u_0_mc:.6f}",
    )
    # Runner-local mean-plaquette self-consistent substitution beta -> beta*P
    # applied to the unchanged coefficient packet.  The literature name
    # "tadpole improvement" is a naming comparator only; this runner proves
    # properties of the locally defined substitution, nothing about the
    # literature prescription itself.
    P_4, converged_4 = tadpole_fixed_point(4)
    check(
        "fixed-point iteration (N=4) converged",
        converged_4,
        f"<P>_TI(4) = {P_4:.9f}",
    )
    print(f"  self-consistent substitution <P>_TI (4-loop) = {P_4:.6f}")
    gap_ti = P_4 - MC_REFERENCE
    pct_ti = 100.0 * abs(gap_ti) / MC_REFERENCE
    check(
        "OBSTRUCTION: self-consistent <P>_TI(4-loop) saturates >40% gap",
        pct_ti > 40.0,
        f"<P>_TI = {P_4:.6f}, explicit runner-local comparator = {MC_REFERENCE:.4f}, "
        f"gap = {gap_ti:+.5f}, pct = {pct_ti:.3f}%",
    )

    # Higher-order self-consistent substitution: walk N from 1 to 8.
    print(f"  self-consistent substitution <P>_TI(N) for N=1..8:")
    best_pct = 1e9
    best_N = 0
    best_P = 0.0
    ti_values: dict[int, float] = {}
    all_converged = True
    max_equation_residual = 0.0
    for N in range(1, 9):
        P_it, converged = tadpole_fixed_point(N)
        ti_values[N] = P_it
        all_converged = all_converged and converged
        equation_residual = abs(
            P_it - truncated_series(W_COEFFS_NSPT_SU3, N, BETA * P_it)
        )
        max_equation_residual = max(max_equation_residual, equation_residual)
        gap = P_it - MC_REFERENCE
        pct = 100.0 * abs(gap) / MC_REFERENCE
        print(
            f"    N={N}: <P>_TI = {P_it:.6f}, gap = {gap:+.5f}, pct = {pct:.3f}%, "
            f"eq-residual = {equation_residual:.2e}"
        )
        if pct < best_pct:
            best_pct = pct
            best_N = N
            best_P = P_it

    check(
        "all fixed-point iterations N=1..8 converged (no silent last-iterate use)",
        all_converged,
        "every walk terminated by tolerance, not by iteration cap",
    )
    check(
        "every reported value satisfies its fixed-point equation to 1e-9",
        max_equation_residual < 1e-9,
        f"max |P - series(N, beta*P)| = {max_equation_residual:.2e}",
    )
    check(
        "branch scope: every selected fixed point exceeds 0.5 (high branch)",
        all(value > 0.5 for value in ti_values.values()),
        "the diagnostic tracks only the weak-coupling branch from seed 0.5",
    )
    check(
        "pin: <P>_TI(N=1) = 0.919435 to six decimals",
        round(ti_values[1], 6) == 0.919435,
        f"<P>_TI(1) = {ti_values[1]:.9f}",
    )
    check(
        "pin: <P>_TI(N=8) = 0.910550 to six decimals",
        round(ti_values[8], 6) == 0.910550,
        f"<P>_TI(8) = {ti_values[8]:.9f}",
    )

    print(f"  best self-consistent truncation: N*={best_N}, <P>_TI = {best_P:.6f}, pct = {best_pct:.3f}%")
    check(
        f"OBSTRUCTION: best tadpole-substitution truncation has |pct| > 40%",
        best_pct > 40.0,
        f"<P>_TI(N*={best_N}) = {best_P:.6f}, pct = {best_pct:.3f}%",
    )


def pade(coeffs, m, n, beta_val):
    """Compute Pade [m/n] of the truncated series f(x) = 1 + sum c_k x^k
    where x = 1/beta and c_k = -w_k for k>=1, evaluated at x = 1/beta_val.

    Returns the Pade approximant value or None if the system is ill-conditioned.
    """
    # f(x) ~ a_0 + a_1 x + ... + a_{m+n} x^(m+n)
    # P/Q with P(x) = p_0 + p_1 x + ... + p_m x^m, Q(x) = 1 + q_1 x + ... + q_n x^n
    # Solve Q*P/series consistency by linear system.
    import numpy as np

    M = m + n + 1
    if M > len(coeffs):
        return None
    a = [1.0] + [-coeffs[k] for k in range(1, M)]   # a[0]=1, a[k]=-w_k
    if len(a) < M:
        return None
    a = a[:M]

    # We want p_i and q_j with Q(x) f(x) = P(x) mod x^(m+n+1)
    # i.e. sum_{k <= m} f_{k - j} q_j = p_k  for k=0..m  (with q_0=1)
    # and  sum_{j=0..n} a_{k-j} q_j = 0       for k = m+1..m+n
    # Build A q = -b on the q_1..q_n unknowns, then back out p.
    A = np.zeros((n, n))
    b = np.zeros(n)
    for k in range(m + 1, m + n + 1):
        for j in range(1, n + 1):
            if 0 <= k - j < len(a):
                A[k - m - 1, j - 1] = a[k - j]
        b[k - m - 1] = -a[k]
    try:
        q_rest = np.linalg.solve(A, b)
    except np.linalg.LinAlgError:
        return None
    q = [1.0] + list(q_rest)
    p = []
    for k in range(0, m + 1):
        s = 0.0
        for j in range(0, min(k, n) + 1):
            s += a[k - j] * q[j]
        p.append(s)

    x = 1.0 / beta_val
    P_val = sum(p[k] * x**k for k in range(m + 1))
    Q_val = sum(q[j] * x**j for j in range(n + 1))
    if Q_val == 0.0:
        return None
    return P_val / Q_val


def test_pade_resummation() -> None:
    section("T5: Pade [m/n] resummation of the perturbative series")
    # Executed grid: m, n >= 1 with 2 <= m+n <= 12 (the [m/0] and [0/n]
    # edge families are NOT executed; the note scopes its claim to this grid).
    print(f"  Pade [m/n] for the truncated perturbative series at beta=6:")
    best_pct = 1e9
    best_mn = (0, 0)
    best_val = 0.0
    evaluated: list[tuple[int, int, float]] = []
    for total in range(2, 13):
        for m in range(1, total):
            n = total - m
            val = pade(W_COEFFS_NSPT_SU3, m, n, BETA)
            if val is None or math.isnan(val) or abs(val) > 5.0:
                continue
            evaluated.append((m, n, val))
            gap = val - MC_REFERENCE
            pct = 100.0 * abs(gap) / MC_REFERENCE
            print(f"    [{m}/{n}] (order {total}): <P>_Pade = {val:.6f}, gap = {gap:+.5f}, pct = {pct:.3f}%")
            if pct < best_pct and abs(val - 0.5) < 0.5:  # filter pathological values
                best_pct = pct
                best_mn = (m, n)
                best_val = val
    print(f"  best Pade: [{best_mn[0]}/{best_mn[1]}], <P>_Pade = {best_val:.6f}, pct = {best_pct:.3f}%")
    check(
        f"OBSTRUCTION: best Pade [{best_mn[0]}/{best_mn[1]}] resummation has |pct| > 40%",
        best_pct > 40.0,
        f"<P>_Pade = {best_val:.6f}, explicit runner-local comparator = {MC_REFERENCE:.4f}, pct = {best_pct:.3f}%",
    )
    # Mutation-decisive pins on the executed grid.
    check(
        "pin: best ordinary Pade approximant is [3/2]",
        best_mn == (3, 2),
        f"best_mn = {best_mn}",
    )
    check(
        "pin: best ordinary Pade value = 0.919330 to six decimals",
        round(best_val, 6) == 0.919330,
        f"best value = {best_val:.9f}",
    )
    p16 = truncated_series(W_COEFFS_NSPT_SU3, 16, BETA)
    high_order = [val for m, n, val in evaluated if m + n >= 6 and abs(val - 0.5) < 0.5]
    check(
        "pin: every accepted approximant with m+n>=6 lies within 1e-5 of <P>_PT(16)",
        bool(high_order)
        and all(abs(val - p16) < 1e-5 for val in high_order),
        f"{len(high_order)} accepted high-order approximants",
    )
    check(
        "grid census: executed ordinary grid produced the expected evaluation count",
        len(evaluated) == PADE_EVALUATED_COUNT,
        f"evaluated = {len(evaluated)}, expected = {PADE_EVALUATED_COUNT}",
    )
    return best_val, best_pct, best_mn


def test_tadpole_pade_combo() -> None:
    section("T6: tadpole-substitution Pade resummation (best combined attempt)")
    # Self-consistent: <P> = Pade[m/n] evaluated at beta_eff = beta * <P>.
    # Executed grid: m, n >= 1 with 3 <= m+n <= 8; the note scopes its claim
    # to this grid.  Iterations that leave the acceptance window or fail to
    # converge are recorded and excluded, never silently consumed.
    print(f"  Pade [m/n] self-consistent with tadpole substitution (beta_eff = beta * <P>):")
    best_pct = 1e9
    best_mn = (0, 0)
    best_P = 0.0
    converged_entries: list[tuple[int, int, float]] = []
    for total in range(3, 9):
        for m in range(1, total):
            n = total - m
            P_it = 0.6
            converged = False
            for it in range(2000):
                beta_eff = BETA * P_it
                val = pade(W_COEFFS_NSPT_SU3, m, n, beta_eff)
                if val is None or math.isnan(val) or abs(val - 0.5) > 0.5:
                    break
                if abs(val - P_it) < 1e-12:
                    converged = True
                    P_it = val
                    break
                P_it = 0.5 * P_it + 0.5 * val
            if not converged:
                continue
            converged_entries.append((m, n, P_it))
            gap = P_it - MC_REFERENCE
            pct = 100.0 * abs(gap) / MC_REFERENCE
            print(f"    [{m}/{n}]_TI: <P>_TI-Pade = {P_it:.6f}, gap = {gap:+.5f}, pct = {pct:.3f}%")
            if pct < best_pct:
                best_pct = pct
                best_mn = (m, n)
                best_P = P_it
    print(f"  best tadpole-substitution Pade: [{best_mn[0]}/{best_mn[1]}], <P> = {best_P:.6f}, pct = {best_pct:.3f}%")
    check(
        f"OBSTRUCTION: best tadpole-substitution Pade combination has |pct| > 40%",
        best_pct > 40.0,
        f"<P>_TI-Pade = {best_P:.6f}, explicit runner-local comparator = {MC_REFERENCE:.4f}, pct = {best_pct:.3f}%",
    )
    # Mutation-decisive pins on the executed combined grid.
    check(
        "pin: best tadpole-substitution Pade approximant is [3/2]",
        best_mn == (3, 2),
        f"best_mn = {best_mn}",
    )
    check(
        "pin: best tadpole-substitution Pade value = 0.910550 to six decimals",
        round(best_P, 6) == 0.910550,
        f"best value = {best_P:.9f}",
    )
    check(
        "branch scope: every converged combined value exceeds 0.5 (high branch)",
        all(value > 0.5 for _, _, value in converged_entries),
        "the combined walk tracks only the weak-coupling branch from seed 0.6",
    )
    check(
        "pin: every converged combined value lies within 2e-4 of 0.910550",
        bool(converged_entries)
        and all(abs(value - 0.910550) < 2e-4 for _, _, value in converged_entries),
        f"{len(converged_entries)} converged entries in the ~0.9106 band",
    )
    check(
        "grid census: combined grid produced the expected converged count",
        len(converged_entries) == TI_PADE_CONVERGED_COUNT,
        f"converged = {len(converged_entries)}, expected = {TI_PADE_CONVERGED_COUNT}",
    )
    return best_P, best_pct, best_mn


def test_scale_diagnostic() -> None:
    section("T7: finite-route residual and explicit runner-local scale diagnostic")
    # Runner-local scale diagnostic over explicit runner-local constants. This does not
    # license any matrix-element or comparator value downstream.
    b0_pure_gauge = 11.0 * N_C / 3.0   # = 11 for SU(3)
    alpha_lat = ALPHA_BARE
    n_star = 1.0 / (alpha_lat * b0_pure_gauge / 4.0)
    print(f"  pure-gauge b_0 = {b0_pure_gauge:.3f}")
    print(f"  alpha_lat at beta=6 = {alpha_lat:.6f}")
    print(f"  scale-diagnostic n* = {n_star:.2f}")
    check(
        "scale-diagnostic n* = 1/(alpha_lat b_0/4) in range [4, 8] at beta=6",
        4.0 < n_star < 8.0,
        f"n* = {n_star:.2f}",
    )
    # In the truncated series the contribution at order n is w_n/beta^n.
    # Within the explicit runner-local truncation used here the series remains
    # finite-range stabilized at a value different from the explicit runner-local comparator.
    # This runner records that finite-route residual; it does not identify the
    # residual with a particular matrix element.
    contributions = [W_COEFFS_NSPT_SU3[n] / BETA**n for n in range(1, 17)]
    min_contrib = min(contributions)
    min_n = contributions.index(min_contrib) + 1
    print(f"  smallest |w_n/beta^n| at n* = {min_n}: {min_contrib:.6e}")
    # The finite-route gap is the measured residual of the tested envelope.
    P_PT_summed = truncated_series(W_COEFFS_NSPT_SU3, 16, BETA)
    non_pert_gap = P_PT_summed - MC_REFERENCE
    pct_non_pert = 100.0 * abs(non_pert_gap) / MC_REFERENCE
    print(f"  perturbative summed value (N=16): {P_PT_summed:.6f}")
    print(f"  finite-route gap to comparator:   {non_pert_gap:+.5f} ({pct_non_pert:.3f}%)")
    print(f"  explicit runner-local F2 comparator:           {F2_SCALE_PERCENT:.4f}%")
    check(
        "finite-route gap to explicit runner-local comparator dominates over "
        "minimum-term residual",
        abs(non_pert_gap) > 100 * min_contrib,
        f"non_pert_gap = {non_pert_gap:+.5f}, min_term = {min_contrib:.3e}, ratio = "
        f"{abs(non_pert_gap)/min_contrib:.2e}",
    )
    check(
        "finite-route gap exceeds explicit runner-local F2 comparator (tested route does not reach explicit runner-local MC comparator)",
        pct_non_pert > F2_SCALE_PERCENT,
        f"gap = {pct_non_pert:.4f}%, F2 = {F2_SCALE_PERCENT:.4f}%, ratio = "
        f"{pct_non_pert/F2_SCALE_PERCENT:.1f}x",
    )
    # Input-integrity pins: the declared comparator constants themselves.
    # These are mutation-decisive against silent comparator drift (a broad
    # ">" inequality alone would stay green under large comparator changes).
    check(
        "input integrity: MC comparator constant is exactly 0.5934",
        MC_REFERENCE == 0.5934,
        f"MC_REFERENCE = {MC_REFERENCE}",
    )
    check(
        "input integrity: F2 comparator constant is exactly 0.0833",
        F2_SCALE_PERCENT == 0.0833,
        f"F2_SCALE_PERCENT = {F2_SCALE_PERCENT}",
    )
    check(
        "pin: N=16 route residual is ~659x the F2 comparator (in [655, 665])",
        655.0 < pct_non_pert / F2_SCALE_PERCENT < 665.0,
        f"ratio = {pct_non_pert/F2_SCALE_PERCENT:.1f}x",
    )


def test_honest_verdict() -> None:
    section("T8: honest verdict on the explicit-input diagnostic")
    # Compute the best result we got and emit the final residual.
    # Use the tadpole-improved Pade since that's the best combined method.
    best = float("inf")
    best_method = "none"
    best_val = 0.0
    # 1-loop alone
    p1 = 1.0 - W_COEFFS_NSPT_SU3[1] / BETA
    gap = abs(p1 - MC_REFERENCE)
    pct = 100.0 * gap / MC_REFERENCE
    if pct < best:
        best, best_method, best_val = pct, "1-loop", p1
    # Truncated PT walk
    for N in range(1, 17):
        p = truncated_series(W_COEFFS_NSPT_SU3, N, BETA)
        gap = abs(p - MC_REFERENCE)
        pct = 100.0 * gap / MC_REFERENCE
        if pct < best:
            best, best_method, best_val = pct, f"truncated_PT_N={N}", p
    # Tadpole-substitution truncated PT (converged fixed points only)
    for N in range(1, 9):
        P_it, converged = tadpole_fixed_point(N)
        if not converged:
            continue
        gap = abs(P_it - MC_REFERENCE)
        pct = 100.0 * gap / MC_REFERENCE
        if pct < best:
            best, best_method, best_val = pct, f"tadpole_PT_N={N}", P_it
    # Pade variants
    for total in range(2, 13):
        for m in range(1, total):
            n = total - m
            val = pade(W_COEFFS_NSPT_SU3, m, n, BETA)
            if val is None or math.isnan(val) or abs(val - 0.5) > 0.5:
                continue
            gap = abs(val - MC_REFERENCE)
            pct = 100.0 * gap / MC_REFERENCE
            if pct < best:
                best, best_method, best_val = pct, f"Pade[{m}/{n}]", val
    # Tadpole + Pade
    for total in range(3, 9):
        for m in range(1, total):
            n = total - m
            P_it = 0.6
            converged = False
            for it in range(2000):
                beta_eff = BETA * P_it
                val = pade(W_COEFFS_NSPT_SU3, m, n, beta_eff)
                if val is None or math.isnan(val) or abs(val - 0.5) > 0.5:
                    break
                if abs(val - P_it) < 1e-12:
                    converged = True
                    break
                P_it = 0.5 * P_it + 0.5 * val
            if not converged:
                continue
            gap = abs(P_it - MC_REFERENCE)
            pct = 100.0 * gap / MC_REFERENCE
            if pct < best:
                best, best_method, best_val = pct, f"tadpole+Pade[{m}/{n}]", P_it

    print(f"  HONEST best tested value: method = {best_method}")
    print(f"                            <P>_tested = {best_val:.6f}")
    print(f"                            explicit runner-local <P>_MC comparator = {MC_REFERENCE:.4f}")
    print(f"                            residual = {best_val - MC_REFERENCE:+.5f}")
    print(f"                            residual % = {best:.3f}%")
    print(f"                            explicit runner-local F2 comparator = {F2_SCALE_PERCENT:.4f}%")
    print(f"  Verdict: best tested residual ({best:.2f}%) "
          f"{'<' if best < F2_SCALE_PERCENT else '>'} explicit runner-local F2 comparator ({F2_SCALE_PERCENT:.4f}%)")
    if best < 5.0:
        verdict_label = "PARTIAL_DERIVATION_<5pct"
    elif best < 10.0:
        verdict_label = "WEAK_PARTIAL_<10pct"
    else:
        verdict_label = "RUNNER_LOCAL_OBSTRUCTION_>10pct"
    print(f"  Verdict label: {verdict_label}")

    # The explicit-input diagnostic: even the best tested finite-route
    # resummation does not reduce the residual below the explicit runner-local F2 comparator.
    check(
        "HONEST VERDICT: best tested value has residual > explicit runner-local F2 comparator",
        best > F2_SCALE_PERCENT,
        f"best tested = {best_val:.6f}, residual = {best:.4f}% > F2 = {F2_SCALE_PERCENT:.4f}%",
    )
    # Mutation-decisive pins on the winner of the whole tested envelope.
    check(
        "pin: best tested method is tadpole+Pade[3/2]",
        best_method == "tadpole+Pade[3/2]",
        f"best method = {best_method}",
    )
    check(
        "pin: best tested value = 0.910550 to six decimals",
        round(best_val, 6) == 0.910550,
        f"best value = {best_val:.9f}",
    )
    check(
        "pin: best residual is ~641x the F2 comparator (in [635, 650])",
        635.0 < best / F2_SCALE_PERCENT < 650.0,
        f"ratio = {best/F2_SCALE_PERCENT:.1f}x",
    )


def test_no_axiom_extension() -> None:
    section("T9: scope (no new axioms / primitives / vocabulary)")
    body_lower = NOTE.read_text().lower() if NOTE.exists() else ""
    plain_body = body_lower.replace("*", "")
    # The perturbative coefficients, MC comparator, and F2 comparator remain
    # explicit runner-local for this runner-local diagnostic only; the Wilson coefficient
    # is dependency-wired without promoting the beta=6 surface.
    check(
        "no new axiom or primitive introduced (Lattice/Qubit/Admissibility/Record baseline unchanged)",
        "does not propose a new axiom or framework primitive" in plain_body,
        "paired note refuses new axiom/primitive authority",
    )
    check(
        "no new repo vocabulary introduced",
        "does not introduce new repo vocabulary" in plain_body,
        "paired note uses existing labels: <P>, beta, w_n, alpha_bare, u_0, tadpole improvement, Pade",
    )
    check(
        "explicit runner-local MC comparator 0.5934 enters only as comparator (not derivation input)",
        "explicit runner-local mc comparator" in plain_body
        and "only a comparator" in plain_body
        and "not licensed for downstream reuse" in plain_body,
        "<P>_MC = 0.5934 used only in residual computation, never as authority or downstream license",
    )


def test_note_exists() -> None:
    section("T10: paired note exists with matching status authority disclaimer")
    if not NOTE.exists():
        check(f"note file {NOTE.name} exists", False, f"path={NOTE}")
        return
    body = NOTE.read_text()
    check(
        f"note file {NOTE.name} exists",
        len(body) > 0,
        f"length = {len(body)} chars",
    )
    check(
        "note declares Status authority: independent audit lane only",
        "Status authority" in body and "independent audit" in body.lower(),
        "audit-lane authority pattern present",
    )
    check(
        "note declares no new axioms / no new primitives",
        ("no new axiom" in body.lower() or "no new axioms" in body.lower())
        and ("no new" in body.lower()),
        "audit-discipline disclaimers present",
    )
    check(
        "note declares explicit runner-local MC comparator 0.5934 as comparator only",
        "explicit runner-local comparator" in body.lower() and "not licensed for downstream reuse" in body.lower(),
        "explicit runner-local comparator pattern present",
    )


# ---------------------------------------------------------------------------
# Run all tests
# ---------------------------------------------------------------------------


def main() -> int:
    print(
        "Plaquette beta=6 perturbative-derivation repaired diagnostic runner\n"
        "(Pattern A; companion-note paired)\n"
    )
    test_source_boundary_manifest()
    test_framework_constants()
    test_one_loop_value()
    test_truncated_series_convergence()
    test_tadpole_improvement_signature()
    test_pade_resummation()
    test_tadpole_pade_combo()
    test_scale_diagnostic()
    test_honest_verdict()
    test_no_axiom_extension()
    test_note_exists()
    print(f"\nTOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL > 0:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
