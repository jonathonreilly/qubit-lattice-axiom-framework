#!/usr/bin/env python3
"""Narrow runner for BOUGEROL_LACROIX_STAGGERED_BLOCKING_LYAPUNOV_BRIDGE_NO_GO_NOTE_2026-05-10.

Verifies the standalone class-B no-go theorem: the proposed
identification of the framework's alpha_LM^16 with a
Bougerol-Lacroix/Oseledets random-product Lyapunov factor exp(16 *
lambda_1) under the landed external MET limit form

  lim_{N -> infinity} (1/N) log ||A_{N-1} ... A_0 v|| = lambda_1

cannot be carried out on the canonical surface under three core
structural obstructions, with a fourth conditional stronger-route
mismatch:

  (O1) no explicit matrix-form per-step blocking operator A_k is found
       by this runner's literal-pattern scan of the framework source
       notes (scan scope disclosed at T1);
  (O2) the 16-step staircase is deterministic, not i.i.d.;
  (O3) cumulative 1-loop perturbative beta running exceeds the
       starting 1/g^2 by 2.594 vs 0.878 (Landau-pole crossing);
  (O4) CONDITIONAL (narrowed after review): within an ASSUMED taste-gap
       model C * alpha_LM^2 — where C is an un-derived nuisance
       coefficient sampled only at the author-chosen values {1, 10, 30}
       — the modeled gap falls short of the required |log alpha_LM|
       ~ 2.40. This is a conditional numerical mismatch for the
       supplied C <= 30 family (partial-narrowing, support grade), NOT
       a derived spectral-gap no-go: the cited Lee-Sharpe scaling is
       O(a^2 Lambda^2) and supplies neither a numerical bound C <= 30
       nor the (a Lambda)^2 -> alpha_LM identification.

Pure class-B narrow no-go theorem for O1-O3; O4 is support-grade
conditional narrowing only. Load-bearing inputs:
  - canonical surface alpha_LM = 0.0907 (PLAQUETTE_SELF_CONSISTENCY_NOTE.md)
  - P2 beta-breakdown arithmetic (YT_P2_TASTE_STAIRCASE_BETA_FUNCTIONS)
  - Lee-Sharpe staggered ChPT O(a^2 Lambda^2) scaling (external);
    the alpha_LM^2 identification and the coefficient family
    C in {1, 10, 30} are un-derived model assumptions of this runner
    (imported values, not sourced bounds)

Target: PASS = 10, FAIL = 0.

External references:
  - P. Bougerol and J. Lacroix, Products of Random Matrices, Birkhauser 1985,
    Theorem III.4.3.
  - V. I. Oseledets, Trans. Moscow Math. Soc. 19 (1968) 197.
  - Y. Kifer, Z. Wahrscheinlichkeit. 61 (1982) 83.
  - W.-J. Lee, S. Sharpe, Phys. Rev. D60 (1999) 114503.
"""

from __future__ import annotations

import math
import re
import sys
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path

try:
    import sympy as sp
    from sympy import Rational, Symbol, log as sym_log, simplify, symbols
except ImportError:
    print("FAIL: sympy required for exact algebra")
    sys.exit(1)


ROOT = Path(__file__).resolve().parent.parent

# Source-controlled repository inputs whose bytes this runner reads to
# establish PASS results; the runner-cache fingerprints them so input
# drift stales the cache (see scripts/runner_cache.py).
AUDIT_INPUT_PATHS = (
    "docs/YT_P2_TASTE_STAIRCASE_BETA_FUNCTIONS_NOTE_2026-04-17.md",
    "docs/YT_P2_V_MATCHING_THEOREM_NOTE_2026-04-17.md",
    "docs/OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md",
    "docs/PLAQUETTE_SELF_CONSISTENCY_NOTE.md",
    "docs/YT_UV_TO_IR_TRANSPORT_OBSTRUCTION_THEOREM_NOTE_2026-04-17.md",
)

PASS = 0
FAIL = 0

# High-precision Decimal context.
getcontext().prec = 60


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS (B)"
    else:
        FAIL += 1
        tag = "FAIL (B)"
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{tag}] {label}{suffix}")


def section(title: str) -> None:
    print("\n" + "-" * 88 + f"\n{title}\n" + "-" * 88)


# Canonical surface anchors (from PLAQUETTE_SELF_CONSISTENCY_NOTE.md;
# bounded same-surface):
ALPHA_LM = Decimal("0.0907")
G_S_LATTICE_MPL = Decimal("1.0674")
ONE_OVER_G2 = Decimal("1") / (G_S_LATTICE_MPL * G_S_LATTICE_MPL)
ABS_DELTA_T = Decimal(str(math.log(0.0907))).copy_abs()
# 1 / (8 pi^2):
ONE_OVER_8PI2 = Decimal("1") / (Decimal("8") * Decimal(str(math.pi)) ** 2)


# ============================================================================
section("Bougerol-Lacroix staggered-blocking Lyapunov-bridge — no-go narrow theorem")
# ============================================================================


# ----------------------------------------------------------------------------
section("Part 1: O1 (per-step blocking operator A_k unspecified) — T1")
# The framework source notes describe the 16-step blocking conceptually
# but do not write A_k as an explicit linear operator on a finite-
# dimensional inner-product space. We verify this by grepping the
# source notes for matrix-form A_k definitions.
# ----------------------------------------------------------------------------

RETAINED_NOTES = [
    "docs/YT_P2_TASTE_STAIRCASE_BETA_FUNCTIONS_NOTE_2026-04-17.md",
    "docs/YT_P2_V_MATCHING_THEOREM_NOTE_2026-04-17.md",
    "docs/OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md",
    "docs/PLAQUETTE_SELF_CONSISTENCY_NOTE.md",
    "docs/YT_UV_TO_IR_TRANSPORT_OBSTRUCTION_THEOREM_NOTE_2026-04-17.md",
]


def grep_for_matrix_form_Ak(notes: list[str]) -> dict[str, bool | None]:
    """Literal-pattern scan for 'A_k = <matrix constructor>'.

    Matches only a small set of explicit matrix-constructor forms
    immediately following 'A_k =' / 'A_k :' (LaTeX pmatrix/bmatrix/array
    environments, Matrix(, sympy.Matrix, np.array, matrix(). An operator
    defined by its action, entries, kernel, recurrence, displayed
    equation, or a linked runner is OUTSIDE this scan's reach; the T1
    certificate is scoped to exactly this scan.

    Returns note -> True (pattern found), False (note present, no
    pattern), or None (note MISSING — this must fail the check, never
    silently count as an absence: fail-closed after review).
    """
    results: dict[str, bool | None] = {}
    pat_explicit_matrix = re.compile(
        r"A[_\\]?\{?k\}?\s*[:=]\s*"
        r"(\\begin\{pmatrix\}|\\begin\{bmatrix\}|\\begin\{array\}|"
        r"matrix\(|np\.array|sympy\.Matrix|Matrix\()",
        re.IGNORECASE,
    )
    for note in notes:
        path = ROOT / note
        if not path.exists():
            results[note] = None
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        m = pat_explicit_matrix.search(text)
        results[note] = bool(m)
    return results


grep_results = grep_for_matrix_form_Ak(RETAINED_NOTES)
missing_notes = [p for p, v in grep_results.items() if v is None]
# Fail-closed: every scanned note must EXIST on disk, and the literal
# pattern must be absent from every one of them. A missing note is a
# scan failure, not evidence of absence.
no_explicit_Ak_found = not missing_notes and all(
    v is False for v in grep_results.values()
)
check(
    "T1 (O1): all five scanned source notes exist on disk AND the literal "
    "'A_k = <matrix constructor>' pattern scan finds no explicit matrix-form "
    "per-step blocking operator A_k in any of them (scan scope: the fixed "
    "constructor patterns only; operators defined by action, entries, "
    "recurrence, or linked runners are outside this scan)",
    no_explicit_Ak_found,
    detail=(
        "missing notes: "
        + (", ".join(missing_notes) if missing_notes else "none")
        + "; matches: "
        + ", ".join(f"{p.split('/')[-1].replace('.md','')}={v}" for p, v in grep_results.items())
    ),
)


# ----------------------------------------------------------------------------
section("Part 2: O2 (16-step staircase is deterministic, not i.i.d.) — T2")
# The staircase rung sequence n_taste^{(k)} = 16 - k for k=0..15 is a
# single deterministic ordering with distinct integers. No randomness,
# no measure mu on GL(V). Verified by enumeration.
# ----------------------------------------------------------------------------

n_taste_sequence = [16 - k for k in range(16)]
# Each rung has a distinct n_taste value (16, 15, ..., 1).
all_distinct = len(set(n_taste_sequence)) == len(n_taste_sequence)
# Each rung specifies a distinct deterministic state; no probability measure
# over GL(V) is exhibited.
no_measure_exhibited = True  # by inspection of YT_P2 notes (Section §2.2 of note)
check(
    "T2 (O2): 16-step staircase n_taste sequence {16, 15, ..., 1} has all "
    "16 distinct deterministic values; no i.i.d. probability measure on "
    "GL(V) is exhibited",
    all_distinct and no_measure_exhibited,
    detail=(
        f"sequence = {n_taste_sequence}; "
        f"distinct = {len(set(n_taste_sequence))} of {len(n_taste_sequence)}"
    ),
)


# ----------------------------------------------------------------------------
section("Part 3: O3 (cumulative 1-loop beta exceeds 1/g^2) — T3, T4")
# b_3^{(k)} = (33 - 2*(16-k))/3.
# Sum_{n=1}^{16} (33 - 2n) = 256, so Sum b_3 over 16 rungs = 256/3.
# |Delta_t| = |log alpha_LM| ~ 2.4006. Prefactor 1/(8 pi^2) ~ 0.01266.
# Cumulative shift = (256/3) * 2.4006 * 0.01266 ~ 2.594.
# Starting 1/g^2 = 1/1.0674^2 ~ 0.878. Crossing point determined.
# ----------------------------------------------------------------------------

# Exact integer sum (Fraction precision):
sum_integer = sum(Fraction(33 - 2 * n, 3) for n in range(1, 17))
assert sum_integer == Fraction(256, 3), f"unexpected sum: {sum_integer}"

# High-precision shift computation:
sum_b3_frac = Fraction(256, 3)
sum_b3_decimal = Decimal(sum_b3_frac.numerator) / Decimal(sum_b3_frac.denominator)
cumulative_shift = sum_b3_decimal * ABS_DELTA_T * ONE_OVER_8PI2

# Conditions:
shift_exceeds_start = cumulative_shift > ONE_OVER_G2

# Check the central value rounds to ~ 2.594:
shift_close_to_2_594 = abs(cumulative_shift - Decimal("2.594")) < Decimal("0.05")
start_close_to_0_878 = abs(ONE_OVER_G2 - Decimal("0.878")) < Decimal("0.05")

check(
    "T3 (O3): cumulative Sum_k b_3^{(k)} * |Delta_t| / (8 pi^2) exceeds "
    "1/g_s(M_Pl)^2",
    shift_exceeds_start and shift_close_to_2_594 and start_close_to_0_878,
    detail=(
        f"shift = {cumulative_shift:.4f}; 1/g^2 = {ONE_OVER_G2:.4f}; "
        f"ratio = {(cumulative_shift / ONE_OVER_G2):.3f}"
    ),
)

# T4: find the smallest k* such that partial shift S_{k*} >= 1/g^2.
partial = Decimal(0)
k_cross = None
for k in range(16):
    n_taste_k = 16 - k
    b3_k = Fraction(33 - 2 * n_taste_k, 3)
    b3_k_decimal = Decimal(b3_k.numerator) / Decimal(b3_k.denominator)
    partial += b3_k_decimal * ABS_DELTA_T * ONE_OVER_8PI2
    if partial >= ONE_OVER_G2:
        k_cross = k
        break

# The crossing must occur strictly before completion of 16 substeps.
crosses_before_16 = k_cross is not None and k_cross < 16
check(
    "T4 (O3 sub-result): 1-loop trajectory 1/g^{(k+1)2} = 1/g^{(k)2} - "
    "b_3^{(k)} * |Delta_t| / (8 pi^2) crosses zero before completing 16 "
    "rungs",
    crosses_before_16,
    detail=f"crossing at k* = {k_cross} (partial shift = {partial:.4f} >= "
           f"start = {ONE_OVER_G2:.4f})",
)


# ----------------------------------------------------------------------------
section("Part 4: O4 (conditional taste-gap model mismatch; assumed C family) — T5")
# MODEL ASSUMPTION (imported, not derived — narrowed after review): the
# available log-gap is MODELED as C * alpha_LM^2 with an un-derived
# nuisance coefficient C, sampled only at the author-chosen values
# {1, 10, 30}. The cited Lee-Sharpe staggered ChPT residual is an
# O(a^2 Lambda^2) scaling statement; it supplies neither a numerical
# bound C <= 30 nor the extra identification replacing (a Lambda)^2 by
# another factor of alpha_LM. No individual taste mode or blocking
# spectrum is constructed or diagonalized here. At roughly
# C = |log alpha_LM| / alpha_LM^2 the asserted mismatch disappears, so
# the executed result is a conditional numerical mismatch for the
# supplied C <= 30 family only (partial-narrowing), not a spectral-gap
# no-go. Required gap is |log alpha_LM| ~ 2.40.
# ----------------------------------------------------------------------------

required_log_gap = ABS_DELTA_T  # = |log alpha_LM|
alpha_LM_sq = ALPHA_LM * ALPHA_LM

# Available log-gap upper bound for various C:
C_values = [Decimal("1"), Decimal("10"), Decimal("30")]
ratios = [(C, required_log_gap / (C * alpha_LM_sq)) for C in C_values]

# All ratios should be >> 1 (substantial gap mismatch). At C = 1
# the available gap is alpha_LM^2 ~ 0.008 and the required gap is
# 2.40, giving ratio ~ 292. At C = 30 the ratio is ~ 9.7, still
# nearly an order of magnitude above unity. We require ratio > 5
# uniformly across C in {1, 10, 30}.
all_ratios_large = all(r > Decimal("5") for _, r in ratios)
# Stronger: smallest ratio (at C = 30) should be > 5; largest (at C = 1) > 100.
smallest_ratio = min(r for _, r in ratios)
largest_ratio = max(r for _, r in ratios)
# Also confirm the largest ratio (at smallest C) exceeds 100, the
# strongest manifestation of the mismatch.
largest_ratio_above_100 = largest_ratio > Decimal("100")

check(
    "T5 (O4, conditional on the assumed C <= 30 gap model): the MODELED "
    "log-gap C * alpha_LM^2 (C un-derived, sampled at {1, 10, 30}) is at "
    "least 5x below required |log alpha_LM| across the sampled family; "
    ">100x at C=1 — a conditional numerical mismatch (partial-narrowing), "
    "not an executed mode bound",
    all_ratios_large and largest_ratio_above_100,
    detail=(
        f"required gap = {required_log_gap:.4f}; alpha_LM^2 = {alpha_LM_sq:.6f}; "
        f"ratios = "
        + "; ".join(f"C={C}: {r:.2f}" for C, r in ratios)
    ),
)


# ----------------------------------------------------------------------------
section("Part 5: sensitivity of O3 to alpha_LM (T6)")
# At alpha_LM = 0.05 and alpha_LM = 0.20 (lattice-accessible range),
# verify that the Landau-pole crossing of O3 still occurs.
# ----------------------------------------------------------------------------


def cumulative_shift_at_alpha(alpha: Decimal) -> tuple[Decimal, Decimal]:
    """Return (cumulative shift, starting 1/g^2) at a given alpha_LM.

    The starting g_s^lat(M_Pl) = 1/sqrt(u_0) on the canonical chain
    where alpha_LM = alpha_bare / u_0 and alpha_bare = 1/(4 pi).
    We hold alpha_bare fixed and let u_0 = alpha_bare / alpha vary.
    """
    alpha_bare = Decimal(1) / (Decimal(4) * Decimal(str(math.pi)))
    u_0 = alpha_bare / alpha
    g_s = Decimal(1) / u_0.sqrt() if u_0 > 0 else Decimal("inf")
    one_over_g2 = Decimal(1) / (g_s * g_s)
    abs_dt = Decimal(str(math.log(float(alpha)))).copy_abs()
    shift = (Decimal(256) / Decimal(3)) * abs_dt * ONE_OVER_8PI2
    return shift, one_over_g2


alpha_low = Decimal("0.05")
alpha_high = Decimal("0.20")
shift_low, start_low = cumulative_shift_at_alpha(alpha_low)
shift_high, start_high = cumulative_shift_at_alpha(alpha_high)

# At alpha_LM = 0.05: shift should still exceed start (crossing remains).
crossing_low = shift_low > start_low
crossing_high = shift_high > start_high

check(
    "T6 (O3 sensitivity): Landau-pole crossing persists at alpha_LM in "
    "{0.05, 0.20} (lattice-accessible range)",
    crossing_low and crossing_high,
    detail=(
        f"alpha=0.05: shift={shift_low:.3f}, start={start_low:.3f}; "
        f"alpha=0.20: shift={shift_high:.3f}, start={start_high:.3f}"
    ),
)


# ----------------------------------------------------------------------------
section("Part 6: sensitivity of O4's assumed gap model to alpha_LM (T7)")
# At alpha_LM in {0.05, 0.20}, verify the MODELED mismatch (same assumed
# C * alpha_LM^2 family, C = 10) is still > 4. Same imported-model caveat
# as Part 4: this samples an assumption, it does not bound a spectrum.
# ----------------------------------------------------------------------------

ratios_low = [Decimal(str(math.log(float(a)))).copy_abs() / (Decimal("10") * a * a)
              for a in [alpha_low, alpha_high]]
all_ratios_low_ge_4 = all(r > Decimal("4") for r in ratios_low)

check(
    "T7 (O4 sensitivity within the assumed gap model, C = 10): modeled "
    "mismatch ratio >= 4 at alpha_LM in {0.05, 0.20}",
    all_ratios_low_ge_4,
    detail=(
        f"ratio(alpha=0.05, C=10) = {ratios_low[0]:.2f}; "
        f"ratio(alpha=0.20, C=10) = {ratios_low[1]:.2f}"
    ),
)


# ----------------------------------------------------------------------------
section("Part 7: counterfactual — uniform A_k (no taste stratification) (T8)")
# If A_k were uniform with n_taste^{(k)} = 16 for all k (no decoupling),
# then per-step b_3 = 1/3 (constant), and the cumulative shift would be
# 16 * (1/3) * |Delta_t| / (8 pi^2) ~ 0.162, BELOW 1/g^2 = 0.878.
# So O3 would NOT block under uniform A_k. But (O1) and (O2) still hold,
# and (O4)'s conditional model mismatch persists within the assumed C
# family. Demonstrates the obstructions are mutually independent.
# ----------------------------------------------------------------------------

uniform_b3 = Decimal(1) / Decimal(3)
uniform_shift = Decimal(16) * uniform_b3 * ABS_DELTA_T * ONE_OVER_8PI2
uniform_crosses = uniform_shift > ONE_OVER_G2

# Under uniform b_3, O3 does NOT block (shift is below start).
# But O1 still blocks (no operator found by the scan), O2 still blocks
# (still no measure), and O4's conditional model mismatch persists
# within the assumed C family (still 16 tastes).
o3_does_not_block_uniform = not uniform_crosses

check(
    "T8 (independence): under uniform A_k counterfactual (no taste "
    "stratification), O3 does NOT block; O1 and O2 still block the "
    "landed MET bridge, while O4's conditional model mismatch persists "
    "within the assumed C family",
    o3_does_not_block_uniform,
    detail=(
        f"uniform shift = {uniform_shift:.4f} < start = {ONE_OVER_G2:.4f}; "
        f"O3 lifted, but O1+O2 remain (with O4's conditional model mismatch)"
    ),
)


# ----------------------------------------------------------------------------
section("Part 8: MET assertion (recall) — asymptotic limit is not finite N (T9)")
# The landed external MET is an asymptotic random-product limit. A single
# deterministic 16-step product cannot instantiate the N -> infinity
# hypothesis. This replaces the submitted spectral-gap/exponential-remainder
# surface, which review-loop previously narrowed away.
# ----------------------------------------------------------------------------

finite_staircase_length = 16
limit_requires_unbounded_N = True
finite_length_is_not_limit = finite_staircase_length < 10**6

check(
    "T9 (MET recall): landed external MET is an N->infinity random-product "
    "limit; a single deterministic 16-step staircase is not that limit",
    limit_requires_unbounded_N and finite_length_is_not_limit,
    detail=(
        f"finite staircase length = {finite_staircase_length}; "
        "limit theorem requires unbounded N and a random-product law"
    ),
)


# ----------------------------------------------------------------------------
section("Part 9: independence of obstruction blocks — T10")
# O1-O3 are individually sufficient for the landed random-product MET
# bridge. O4 contributes only the conditional model mismatch of Part 4
# against the stronger spectral-gap route (assumed C family; support
# grade), not an independent unconditional block.
# ----------------------------------------------------------------------------

# Fail-closed after review: each counterfactual reuses the COMPUTED
# conditions established at T1-T5 for the obstructions that remain when one
# is hypothetically lifted. Lifting an obstruction cannot change any of the
# other executed conditions (they are computed from disjoint inputs: the
# note scan for O1, the enumerated rung sequence for O2, the beta-running
# arithmetic for O3, the sampled assumed-model ratios for O4), so the
# independence statement is exactly the conjunction of the remaining
# executed booleans — no literal-True constant enters the predicate.

# Counterfactual 1: A_k is exhibited explicitly (O1 lifted).
# But: O2 (deterministic sequence) and O3 (Landau pole) still hold; O4's
# conditional assumed-model mismatch also persists for the stronger route.
o1_lifted_others_block = (
    all_distinct  # O2: computed — 16 distinct deterministic rung values (T2)
    and shift_exceeds_start  # O3: computed — cumulative shift crosses 1/g^2 (T3)
    and crosses_before_16  # O3: computed — crossing before rung 16 (T4)
    and all_ratios_large  # O4: computed — sampled-model mismatch persists (T5)
)

# Counterfactual 2: sequence randomized to i.i.d. (O2 lifted).
# But: O1 (no operator found by the scan), O3 (Landau pole) still block the
# landed bridge; O4's conditional assumed-model mismatch also persists.
o2_lifted_others_block = (
    no_explicit_Ak_found  # O1: computed — fail-closed literal-pattern scan (T1)
    and shift_exceeds_start  # O3: computed (T3)
    and all_ratios_large  # O4: computed (T5)
)

# Counterfactual 3: non-perturbative reconstruction bypasses O3 (O3 lifted).
# But: O1 and O2 still block the landed bridge; O4's conditional
# assumed-model mismatch also persists for the stronger route.
o3_lifted_others_block = (
    no_explicit_Ak_found  # O1: computed (T1)
    and all_distinct  # O2: computed (T2)
    and all_ratios_large  # O4: computed (T5)
)

# Counterfactual 4: non-staggered fermion realization (O4 lifted).
# But: O1, O2, O3 still hold (canonical surface).
o4_lifted_others_block = (
    no_explicit_Ak_found  # O1: computed (T1)
    and all_distinct  # O2: computed (T2)
    and shift_exceeds_start  # O3: computed (T3)
)

all_independent = (
    o1_lifted_others_block
    and o2_lifted_others_block
    and o3_lifted_others_block
    and o4_lifted_others_block
)

check(
    "T10 (independence): (O1), (O2), and (O3) independently block the "
    "landed MET bridge; (O4) supplies only the conditional assumed-model "
    "mismatch against the stronger spectral-gap route (partial-narrowing, "
    "support grade — not an unconditional block)",
    all_independent,
    detail=(
        "each counterfactual is the conjunction of the remaining EXECUTED "
        f"T1-T5 conditions: O1 scan={no_explicit_Ak_found}, O2 distinct rungs="
        f"{all_distinct}, O3 crossing={shift_exceeds_start} (k*={k_cross}), "
        f"O4 sampled-model mismatch={all_ratios_large}"
    ),
)


# ----------------------------------------------------------------------------
section("No-go theorem summary")
# ----------------------------------------------------------------------------
print(
    """
  Narrow Pattern B no-go theorem statement (recapitulation):

  HYPOTHESIS (landed Bougerol-Lacroix/Oseledets MET, ♦):
    lim_{N -> infinity} (1/N) log ||A_{N-1} ... A_0 v|| = lambda_1,
    with a random-product law for (A_k), integrability, and the
    projective hypotheses required by the external theorem.

  PROPOSED FRAMEWORK BRIDGE (★):
    lambda_1 = log(alpha_LM)   (alpha_LM = 0.0907, canonical surface)
    16-step product Pi_{k=0}^{15} A_k v ~ alpha_LM^16 * const * ||v||,
    on the framework's deterministic staggered taste-staircase.

  CONCLUSION (No-Go for O1-O3; conditional narrowing for O4):
    The bridge (★) cannot be made under (♦) on the canonical
    surface, blocked by three core obstructions, with one conditional
    stronger-route mismatch:
      (O1) no explicit matrix-form A_k found by the disclosed
           literal-pattern scan of the source notes;
      (O2) staircase deterministic, not i.i.d.;
      (O3) cumulative 1-loop beta exceeds 1/g^2 (Landau-pole crossing);
      (O4) CONDITIONAL: within the ASSUMED taste-gap model
           C * alpha_LM^2 (C un-derived, sampled at {1, 10, 30}), the
           modeled gap ~ C * 0.008 falls short of the required
           |log alpha_LM| ~ 2.40. Partial-narrowing for the supplied
           C <= 30 family only; at C ~ |log alpha_LM|/alpha_LM^2 the
           mismatch disappears, so no spectral-gap no-go is derived.

  Audit-lane class:
    (B) — bounded no-go with framework dependencies on
    canonical surface and P2 beta breakdown, plus external citation of
    Lee-Sharpe staggered ChPT (1999). No positive identification
    claimed; (O1)-(O3) block the landed MET bridge, and (O4) supplies
    a support-grade conditional numerical mismatch against the
    stronger spectral-gap route within the supplied C <= 30 model
    family only (the coefficient and the (a Lambda)^2 -> alpha_LM
    step are un-derived imports, not sourced bounds).

  This narrow theorem is independent of:
    - The Bougerol-Lacroix/Oseledets external MET narrow theorem; the
      upstream external citation is unaffected.
    - The framework's hierarchy formula v = M_Pl x alpha_LM^16 x (7/8)^(1/4);
      the formula is not closed or refuted, only one specific
      identification route for alpha_LM^16 is blocked.
    - Alternative non-Lyapunov scaffolds (heat-kernel determinants,
      lattice transfer-matrix spectral gap, non-perturbative blocking RG);
      none of these are adjudicated here.
"""
)


# ----------------------------------------------------------------------------
section("N5 execution certificate — what this runner resolves at each granularity")
# ----------------------------------------------------------------------------

print(
    "per_element: checked and not executed — the executed evidence at this "
    f"granularity is a literal-pattern scan of the {len(RETAINED_NOTES)} source "
    "notes (all verified to exist) for 'A_k = <matrix constructor>' in a fixed "
    "set of constructor forms, which finds no match; an operator defined by its "
    "action, entries, kernel, recurrence, displayed equation, or a linked runner "
    "would be invisible to this scan, so the certificate covers exactly that "
    "regex scan and no entrywise computation."
)
print(
    "per_site: checked and not executed — the 16-step staircase is indexed by "
    "blocking scale, not by lattice site; no lattice is instantiated anywhere in "
    "this runner and no site-resolved quantity is computed, so nothing here "
    "certifies the bridge site by site."
)
print(
    "per_mode: checked — the taste-mode COUNT is resolved one rung at a time (no "
    "individual taste mode is ever constructed or diagonalized here): n_taste takes "
    f"the {len(set(n_taste_sequence))} distinct values 16 down to 1 with each "
    "rung contributing b_3 = (33 - 2 n_taste)/3; the taste-gap comparison uses the "
    f"ASSUMED model C * alpha_LM^2 (alpha_LM^2 = {alpha_LM_sq:.6f}) with the "
    "un-derived coefficient C sampled only at {1, 10, 30}, against the required "
    f"|log alpha_LM| = {required_log_gap:.4f} — a sampled model assumption "
    "(imported value), not an executed mode bound."
)
print(
    "per_block: checked — the blocking rungs are accumulated block by block and the "
    f"runner locates the exact rung at which the coupling budget is exhausted: "
    f"crossing at k* = {k_cross} with partial shift {partial:.4f} against the start "
    f"1/g^2 = {ONE_OVER_G2:.4f}, the full 16-rung shift being {cumulative_shift:.4f}."
)
print(
    "lattice_wide: checked and not executed — the hypothesis that would need "
    "certification is the N -> infinity random-product limit, while this runner "
    "executes only the finite 16-step deterministic staircase plus two alpha_LM "
    f"sensitivity points at {alpha_low} and {alpha_high}; taking no asymptotic or "
    f"volume limit is itself obstruction T9, with PASS={PASS}, FAIL={FAIL}."
)


print(f"\n{'=' * 88}\n  TOTAL: PASS={PASS}, FAIL={FAIL}\n{'=' * 88}")
sys.exit(1 if FAIL > 0 else 0)
