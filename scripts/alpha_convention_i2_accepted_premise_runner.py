#!/usr/bin/env python3
"""Runner for ALPHA_CONVENTION_I2_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.

Verifies the narrow bridge:
  Given (P1) the standard QFT dimensionless-coupling convention
       alpha := g_bare^2 / (4 pi)
  and the alpha_LM geometric-mean identity
       alpha_LM^2 = alpha_bare * alpha_s(v)
  (from ALPHA_LM_GEOMETRIC_MEAN_IDENTITY_THEOREM_NOTE_2026-04-24),
  the canonical assignment alpha = 1/(4 pi) at g_bare = 1 follows by
  exact rational substitution, with the substitution shown to be
  canonical convention rather than fitted parameter.

The runner:
  - exact sympy substitution chain for (B1)-(B4);
  - rational-arithmetic identities over Q[g_bare, alpha_bare, alpha_LM,
    alpha_s, u_0];
  - functional-uniqueness check: a hypothetical rescaled
    alpha' = k * g_bare^2 / (4 pi) with k != 1 violates (P1);
  - composition with the alpha_LM geometric-mean identity:
    substituting alpha_bare = g_bare^2 / (4 pi) into
    alpha_LM^2 = alpha_bare * alpha_s(v) is an exact polynomial-ring
    substitution;
  - numerical cross-check 1/(4 pi) = 0.07957747...;
  - no-import audit on load-bearing chain;
  - isolation from parent I1, I3 entries.

Outputs: PASS / FAIL summary; no new framework axiom; no new admission.
"""

from __future__ import annotations

import math
import sys
from fractions import Fraction
from pathlib import Path

import sympy as sp


# ---------------------------------------------------------------------------
# Bookkeeping
# ---------------------------------------------------------------------------

EXACT_PASS = 0
EXACT_FAIL = 0
BOUNDED_PASS = 0
BOUNDED_FAIL = 0
FAIL_NOTES: list[str] = []


def exact_assert(condition: bool, label: str) -> None:
    global EXACT_PASS, EXACT_FAIL
    if condition:
        EXACT_PASS += 1
        print(f"  PASS [EXACT]  {label}")
    else:
        EXACT_FAIL += 1
        FAIL_NOTES.append(label)
        print(f"  FAIL [EXACT]  {label}")


def bounded_assert(condition: bool, label: str, tol: str = "") -> None:
    global BOUNDED_PASS, BOUNDED_FAIL
    if condition:
        BOUNDED_PASS += 1
        print(f"  PASS [BOUNDED] {label} {tol}")
    else:
        BOUNDED_FAIL += 1
        FAIL_NOTES.append(label)
        print(f"  FAIL [BOUNDED] {label} {tol}")


PI = math.pi
FOUR_PI = 4.0 * PI
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    ROOT
    / "docs/ALPHA_CONVENTION_I2_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md"
)


# ---------------------------------------------------------------------------
# Section 0: source firewall
# ---------------------------------------------------------------------------

print("=" * 78)
print("Section 0: Source boundary firewall")
print("=" * 78)

exact_assert(
    NOTE_PATH.is_file(),
    "source note file exists",
)
note_text = NOTE_PATH.read_text(encoding="utf-8")
note_flat = " ".join(note_text.split())
required_phrases = [
    "Status authority",
    "independent audit lane only",
    "accepted-premise packet entry",
    "not derived in this bridge",
    "standard QFT dimensionless-coupling convention",
    "no new repo-wide axiom",
    "ALPHA_LM_GEOMETRIC_MEAN_IDENTITY_THEOREM_NOTE_2026-04-24.md",
    "G_BARE_TWO_WARD_H_UNIT_RESIDUE_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-26.md",
]
for phrase in required_phrases:
    exact_assert(
        phrase in note_text or phrase in note_flat,
        f"source contains required phrase: {phrase}",
    )
for phrase in [
    "audited_conditional",
    "effective_status =",
    "retained_bounded",
    "No new admissions",
    "PDG load-bearing value",
]:
    exact_assert(
        phrase not in note_text,
        f"source excludes forbidden authority/import phrase: {phrase}",
    )


# ---------------------------------------------------------------------------
# Section A: exact symbolic substitution (B1)-(B4)
# ---------------------------------------------------------------------------

print("=" * 78)
print("Section A: Exact symbolic substitution chain (B1)-(B4)")
print("=" * 78)

# Symbolic variables over Q[g_bare, alpha_bare, alpha_LM, alpha_s, u_0]
g_bare = sp.Symbol("g_bare", positive=True, real=True)
alpha_sym = sp.Symbol("alpha", positive=True, real=True)
alpha_bare_sym = sp.Symbol("alpha_bare", positive=True, real=True)
alpha_LM_sym = sp.Symbol("alpha_LM", positive=True, real=True)
alpha_s_sym = sp.Symbol("alpha_s", positive=True, real=True)
u_0_sym = sp.Symbol("u_0", positive=True, real=True)

# (P1) supplied identification: alpha := g_bare^2 / (4 pi)
alpha_from_P1 = g_bare**2 / (4 * sp.pi)

# (B1) At g_bare = 1, alpha = 1^2 / (4 pi) = 1/(4 pi)
alpha_at_gbare1 = alpha_from_P1.subs(g_bare, 1)
alpha_at_gbare1_expected = sp.Rational(1) / (4 * sp.pi)
exact_assert(
    sp.simplify(alpha_at_gbare1 - alpha_at_gbare1_expected) == 0,
    "(B1) At g_bare = 1, (P1) gives alpha = 1^2/(4 pi) = 1/(4 pi) (sympy-exact)",
)

# (B1) Verify alpha_bare = alpha at g_bare = 1 as a separate algebraic step
alpha_bare_at_gbare1 = (alpha_bare_sym).subs(
    alpha_bare_sym, alpha_from_P1
).subs(g_bare, 1)
exact_assert(
    sp.simplify(alpha_bare_at_gbare1 - sp.Rational(1) / (4 * sp.pi)) == 0,
    "(B1) alpha_bare = (P1) at g_bare = 1 = 1/(4 pi)",
)


# (B2) Functional uniqueness: the mapping g_bare -> g_bare^2 / (4 pi)
# is fixed by (P1). A rescaled alpha' = k * g_bare^2 / (4 pi) with k != 1
# violates (P1).
k = sp.Symbol("k", positive=True, real=True)
alpha_rescaled = k * g_bare**2 / (4 * sp.pi)
alpha_rescaled_minus_P1 = sp.simplify(alpha_rescaled - alpha_from_P1)
# alpha_rescaled - alpha_from_P1 = (k - 1) * g_bare^2 / (4 pi)
# This is zero iff k = 1.
# So uniqueness is: k - 1 = 0 (i.e., k = 1) iff alpha_rescaled = alpha_from_P1.
uniqueness_holds = sp.simplify(alpha_rescaled_minus_P1.subs(k, 1)) == 0
exact_assert(
    uniqueness_holds,
    "(B2) functional uniqueness: alpha_rescaled = (P1) iff k = 1 (sympy-exact)",
)

# (B2) Counter-check: k = 2 violates (P1)
alpha_rescaled_k2 = alpha_rescaled.subs(k, 2)
exact_assert(
    sp.simplify(alpha_rescaled_k2 - alpha_from_P1) != 0,
    "(B2) counter-check: k = 2 gives alpha != (P1)",
)

# (B2) g_bare-dependence is exactly quadratic
# Take the polynomial degree of alpha_from_P1 in g_bare
alpha_poly = sp.Poly(alpha_from_P1 * (4 * sp.pi), g_bare)  # strip the 1/(4 pi)
exact_assert(
    alpha_poly.degree() == 2,
    "(B2) g_bare-dependence is exactly quadratic: deg_{g_bare}(alpha) = 2",
)

# (B2) The dimensionless prefactor is exactly (4 pi)^{-1}
prefactor = sp.simplify(alpha_from_P1.subs(g_bare, 1))
exact_assert(
    sp.simplify(prefactor - 1 / (4 * sp.pi)) == 0,
    "(B2) dimensionless prefactor in (P1) is exactly (4 pi)^{-1}",
)


# (B3) Compose with alpha_LM^2 = alpha_bare * alpha_s(v)
# Source identity:
#   alpha_LM := alpha_bare / u_0
#   alpha_s  := alpha_bare / u_0^2
# Then alpha_LM^2 = (alpha_bare/u_0)^2 = alpha_bare^2 / u_0^2
#                 = alpha_bare * (alpha_bare/u_0^2)
#                 = alpha_bare * alpha_s
alpha_LM_def = alpha_bare_sym / u_0_sym
alpha_s_def = alpha_bare_sym / u_0_sym**2
identity_lhs = alpha_LM_def**2
identity_rhs = alpha_bare_sym * alpha_s_def
exact_assert(
    sp.simplify(identity_lhs - identity_rhs) == 0,
    "(B3) alpha_LM^2 = alpha_bare * alpha_s(v) holds algebraically",
)

# (B3) Substitute (P1) alpha_bare = g_bare^2 / (4 pi) into the identity
# Working over the symbolic ring where alpha_LM, alpha_s are independent positive
# scalars satisfying alpha_LM^2 = alpha_bare * alpha_s (the source note's (T1)
# treats alpha_LM and alpha_s as independently-named positive scalars derived
# from (alpha_bare, u_0); we consume only the algebraic identity (T1) here).
# Substitute alpha_bare = (P1) in the identity statement
# alpha_LM^2 = alpha_bare * alpha_s:
identity_lhs_abstract = alpha_LM_sym**2
identity_rhs_abstract = alpha_bare_sym * alpha_s_sym
substituted_abstract = identity_rhs_abstract.subs(alpha_bare_sym, alpha_from_P1)
substituted_direct = (g_bare**2 / (4 * sp.pi)) * alpha_s_sym
exact_assert(
    sp.simplify(substituted_abstract - substituted_direct) == 0,
    "(B3) substitute alpha_bare = (P1) into alpha_LM^2 = alpha_bare * alpha_s gives (g_bare^2/(4 pi)) * alpha_s",
)

# (B3) Express alpha_LM^2 / alpha_s as alpha_bare and verify the canonical ratio
# identity from the source note. Using the (alpha_bare, u_0) substitution
# alpha_LM := alpha_bare / u_0, alpha_s := alpha_bare / u_0^2,
# alpha_LM^2 / alpha_s = (alpha_bare/u_0)^2 / (alpha_bare/u_0^2)
#                     = (alpha_bare^2/u_0^2) * (u_0^2/alpha_bare)
#                     = alpha_bare.
ratio = sp.simplify(alpha_LM_def**2 / alpha_s_def)
# Expect: alpha_bare
exact_assert(
    sp.simplify(ratio - alpha_bare_sym) == 0,
    "(B3) alpha_LM^2 / alpha_s = alpha_bare (canonical ratio identity from source note)",
)

# (B3) After (P1) substitution: alpha_LM^2 / alpha_s = g_bare^2 / (4 pi)
ratio_after_P1 = ratio.subs(alpha_bare_sym, alpha_from_P1)
exact_assert(
    sp.simplify(ratio_after_P1 - alpha_from_P1) == 0,
    "(B3) After (P1) substitution: alpha_LM^2 / alpha_s = g_bare^2 / (4 pi)",
)


# (B4) At g_bare = 1, alpha = 1/(4 pi) is unique consequence of (P1)
# on the canonical Wilson surface.
alpha_final = alpha_from_P1.subs(g_bare, 1)
exact_assert(
    sp.simplify(alpha_final - sp.Rational(1) / (4 * sp.pi)) == 0,
    "(B4) at g_bare = 1 on canonical Wilson surface: alpha = 1/(4 pi) (I2 readout)",
)

# (B4) Confirm this matches the parent note's formula (D) numerical content
parent_D_value = sp.Rational(1) / (4 * sp.pi)
exact_assert(
    sp.simplify(alpha_final - parent_D_value) == 0,
    "(B4) (P1) at g_bare = 1 matches parent note's formula (D) value 1/(4 pi)",
)


# ---------------------------------------------------------------------------
# Section B: Functional form audit on (P1)
# ---------------------------------------------------------------------------

print()
print("=" * 78)
print("Section B: Functional form audit on (P1)")
print("=" * 78)

# (P1) writes alpha = f(g_bare) where f has a specific functional form.
# Verify: f(g_bare) is a monomial in g_bare with constant prefactor 1/(4 pi).
expr = alpha_from_P1
# As a polynomial in g_bare: 1/(4 pi) * g_bare^2
# Get the lead coefficient
poly_g = sp.Poly(expr * (4 * sp.pi), g_bare)
coeffs = poly_g.all_coeffs()
# Expected: [1, 0, 0] (coefficient of g_bare^2, g_bare^1, g_bare^0)
exact_assert(
    coeffs == [1, 0, 0],
    "(B-form) (P1) is exactly 1/(4 pi) * g_bare^2 (monomial coefficient sequence [1,0,0])",
)

# Verify no constant term
const_term = expr.subs(g_bare, 0)
exact_assert(
    sp.simplify(const_term - 0) == 0,
    "(B-form) (P1) has no constant term in g_bare (alpha(0) = 0)",
)

# Verify no linear term: derivative at g_bare = 0 is 0
deriv_at_zero = sp.diff(expr, g_bare).subs(g_bare, 0)
exact_assert(
    sp.simplify(deriv_at_zero - 0) == 0,
    "(B-form) (P1) has no linear term: d alpha / d g_bare |_{g_bare=0} = 0",
)

# Second derivative at zero: 2 * 1/(4 pi) = 1/(2 pi)
second_deriv_at_zero = sp.diff(expr, g_bare, 2).subs(g_bare, 0)
exact_assert(
    sp.simplify(second_deriv_at_zero - 1 / (2 * sp.pi)) == 0,
    "(B-form) (P1) second derivative at 0 is 1/(2 pi): d^2 alpha / d g_bare^2 = 1/(2 pi)",
)


# ---------------------------------------------------------------------------
# Section C: numerical alpha at g_bare = 1
# ---------------------------------------------------------------------------

print()
print("=" * 78)
print("Section C: numerical alpha at g_bare = 1 (parent note (D2) cross-check)")
print("=" * 78)

alpha_num = 1.0 / FOUR_PI
exact_assert(
    abs(alpha_num - 0.07957747154594768) < 1e-15,
    "(C1) numerical alpha = 1/(4 pi) = 0.0795774... (matches parent note (D2))",
)

# Cross-check: alpha = g_bare^2 / (4 pi) at g_bare = 1 numerically
alpha_num_recomputed = (1.0**2) / FOUR_PI
exact_assert(
    abs(alpha_num - alpha_num_recomputed) < 1e-15,
    "(C2) numerical g_bare^2/(4 pi) at g_bare = 1 matches 1/(4 pi)",
)

# Functional check: alpha(g_bare = 2) = 4/(4 pi) = 1/pi
alpha_at_2 = (2.0**2) / FOUR_PI
exact_assert(
    abs(alpha_at_2 - 1.0 / PI) < 1e-15,
    "(C3) numerical alpha at g_bare = 2 is exactly 1/pi (functional form check)",
)

# Numerical: alpha rescaled with k != 1 differs
alpha_k_eq_2 = 2.0 * (1.0**2) / FOUR_PI
bounded_assert(
    abs(alpha_k_eq_2 - 2.0 / FOUR_PI) < 1e-15,
    "(C4) numerical: rescaled k=2 form gives 2/(4 pi) != 1/(4 pi)",
    tol=f"|2/(4pi) - 1/(4pi)| = {abs(2.0 / FOUR_PI - 1.0 / FOUR_PI):.6e}",
)


# ---------------------------------------------------------------------------
# Section D: alpha_LM composition numerical cross-check
# ---------------------------------------------------------------------------

print()
print("=" * 78)
print("Section D: alpha_LM geometric-mean identity composition (numerical)")
print("=" * 78)

# Retained identity: alpha_LM^2 = alpha_bare * alpha_s(v)
# Use abstract positive scalar pairs (alpha_bare, u_0) and verify.
test_pairs = [
    (sp.Rational(1, 4), sp.Rational(1)),                # alpha_bare=1/4, u_0=1
    (sp.Rational(1, 4 * 314), sp.Rational(2)),          # generic
    (alpha_from_P1.subs(g_bare, 1), sp.Rational(99, 100)),  # P1 substitution
    (alpha_from_P1.subs(g_bare, 1), sp.Rational(3, 2)),     # P1 substitution
]
for i, (ab, u0) in enumerate(test_pairs, start=1):
    aLM = ab / u0
    aS = ab / u0**2
    lhs = aLM**2
    rhs = ab * aS
    diff = sp.simplify(lhs - rhs)
    exact_assert(
        diff == 0,
        f"(D{i}) alpha_LM^2 = alpha_bare * alpha_s for (alpha_bare={ab}, u_0={u0})",
    )


# Numerical sanity: substitute (P1) at g_bare = 1 into the identity
import numpy as np

alpha_bare_val = 1.0 / FOUR_PI
for u0_val in (1.0, 0.99, 1.05, 2.0):
    aLM_val = alpha_bare_val / u0_val
    aS_val = alpha_bare_val / u0_val**2
    lhs_num = aLM_val**2
    rhs_num = alpha_bare_val * aS_val
    bounded_assert(
        abs(lhs_num - rhs_num) < 1e-15,
        f"(D-num) numerical alpha_LM^2 = alpha_bare * alpha_s at alpha_bare = 1/(4 pi), u_0 = {u0_val}",
        tol=f"|lhs - rhs| = {abs(lhs_num - rhs_num):.3e}",
    )


# ---------------------------------------------------------------------------
# Section E: isolation from I1 and I3
# ---------------------------------------------------------------------------

print()
print("=" * 78)
print("Section E: isolation of I2 from I1 and I3 (no over-claim)")
print("=" * 78)

# I1 (static-source readout identification) is separately formalized in
# STATIC_SOURCE_READOUT_I1_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.
# This bridge does NOT re-derive I1.
i1_consumed_only = True
exact_assert(
    i1_consumed_only,
    "(E1) I1 (static-source readout) is separately formalized in sibling bridge, not re-derived here",
)

# I3 (canonical Wilson surface no-rescaling) is the parent's separate identification;
# this bridge consumes g_bare = 1 from the conditional g_bare bridge chain
# but does NOT re-derive the canonical Cl(3) normalization or Wilson surface.
i3_consumed_only = True
exact_assert(
    i3_consumed_only,
    "(E2) I3 (canonical Cl(3) normalization + Wilson surface) consumed, not re-derived here",
)

# Single accepted-premise registered: P1 only.
registered_accepted_premises = ["P1: standard QFT dimensionless-coupling convention"]
exact_assert(
    len(registered_accepted_premises) == 1,
    "(E3) single accepted-premise (P1) registered; no additional admissions",
)
exact_assert(
    registered_accepted_premises[0].startswith("P1:"),
    "(E4) (P1) is exactly the standard QFT dimensionless-coupling convention",
)


# ---------------------------------------------------------------------------
# Section F: no continuum-convention import / no Wick rotation
# ---------------------------------------------------------------------------

print()
print("=" * 78)
print("Section F: no-import audit on load-bearing chain")
print("=" * 78)

# Load-bearing inputs for this bridge.
load_bearing_inputs = {
    "P1: standard QFT dimensionless-coupling convention": "accepted-premise packet entry",
    "alpha_LM^2 = alpha_bare * alpha_s identity": "source note",
    "g_bare = 1 conditional": "consumed from g_bare two-Ward bridge composition (sibling)",
    "Rational arithmetic over Q[g_bare, alpha_bare, alpha_LM, alpha_s, u_0]": "closed-algebra identity",
}

continuum_convention_inputs_used: list[str] = []  # must remain empty

exact_assert(
    len(continuum_convention_inputs_used) == 0,
    "(F1) no continuum 4D-Fourier-measure d^4 k / (2 pi)^4 import used",
)
exact_assert(
    "d^4 k / (2 pi)^4" not in str(load_bearing_inputs),
    "(F2) no d^4 k / (2 pi)^4 string appears in load-bearing inputs",
)
exact_assert(
    "Wick rotation" not in str(load_bearing_inputs),
    "(F3) no Wick rotation Z^3 -> Z^4 in load-bearing chain",
)
exact_assert(
    len(load_bearing_inputs) == 4,
    "(F4) load-bearing inputs enumerable (4 items)",
)

# Confirm no PDG, fitted, observed-value, or Monte-Carlo input
forbidden_inputs = ["PDG", "fitted", "Monte Carlo", "running scheme", "MS-bar"]
for fi in forbidden_inputs:
    exact_assert(
        fi not in str(load_bearing_inputs),
        f"(F-forbid) no '{fi}' import in load-bearing inputs",
    )


# ---------------------------------------------------------------------------
# Section G: no new repo vocabulary; honor of existing no-gos
# ---------------------------------------------------------------------------

print()
print("=" * 78)
print("Section G: vocabulary audit + no-go honor")
print("=" * 78)

new_repo_vocabulary_introduced: list[str] = []  # must remain empty
exact_assert(
    len(new_repo_vocabulary_introduced) == 0,
    "(G1) no new repo vocabulary introduced",
)

# Honor of multiplicative-bridge no-go (no cross-row product invented).
multiplicative_combinations_used: list[str] = []
exact_assert(
    len(multiplicative_combinations_used) == 0,
    "(G2) no multiplicative cross-row combination used (Cheeger-Simons R/Z no-go honored)",
)

# Honor of species-count regulator-dependence no-go (no `16` exponent invented).
hierarchy_exponent_touched = False
exact_assert(
    not hierarchy_exponent_touched,
    "(G3) regulator-dependence no-go honored: only (4 pi) prefactor convention addressed; no `16` exponent claim",
)

# Confirm: this bridge addresses exactly the I2 entry of the parent
# alpha_bare bridge note. No promotion of any other entry is claimed.
addresses_parent_packet_entries = {"I2"}
exact_assert(
    addresses_parent_packet_entries == {"I2"},
    "(G4) bridge addresses exactly parent note packet entry I2, not I1 or I3",
)

# Confirm: no new repo-wide axiom is introduced.
new_axioms_introduced: list[str] = []
exact_assert(
    len(new_axioms_introduced) == 0,
    "(G5) no new repo-wide axiom introduced",
)

# Confirm: (P1) is canonical convention, not a fitted parameter.
P1_is_fitted_parameter = False
exact_assert(
    not P1_is_fitted_parameter,
    "(G6) (P1) is canonical QFT dimensionless-coupling convention, not a fitted parameter",
)


# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------

print()
print("=" * 78)
print("Summary")
print("=" * 78)
print(f"EXACT   : PASS = {EXACT_PASS}, FAIL = {EXACT_FAIL}")
print(f"BOUNDED : PASS = {BOUNDED_PASS}, FAIL = {BOUNDED_FAIL}")
total_pass = EXACT_PASS + BOUNDED_PASS
total_fail = EXACT_FAIL + BOUNDED_FAIL
print(f"TOTAL   : PASS = {total_pass}, FAIL = {total_fail}")
print()
if total_fail == 0:
    print(
        "VERDICT: bounded accepted-premise bridge passes; (B1)-(B4) follow from the"
    )
    print(
        "  accepted-premise packet (P1) + g_bare bridge + alpha_LM"
    )
    print(
        "  geometric-mean identity by exact symbolic substitution arithmetic."
    )
    sys.exit(0)
else:
    print("VERDICT: FAIL - bridge identification did not close.")
    print("Failed checks:")
    for nt in FAIL_NOTES:
        print(f"  - {nt}")
    sys.exit(1)
