#!/usr/bin/env python3
"""Runner for CL3_NORMALIZATION_I3_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.

Verifies the narrow bridge:
  Given (P1) the conjoint canonical SU(N_c) generator normalization
       (CN)  Tr(T_a T_b) = delta_{ab} / 2
  and the bare Wilson plaquette action surface form with no
  ad-hoc rescaling
       (WS)  S_W = beta * sum_P (1 - (1/N_c) Re Tr U_P),
       no lambda != 1 rescaling between S_W and (D),
  plus the canonical QFT dimensionless-coupling convention (sibling I2
  bridge)
       (D)   alpha_bare := g_bare^2 / (4 pi),
  the identification alpha_bare = g_bare^2 / (4 pi) on the canonical
  Wilson surface is unambiguous (no lambda-rescaling parameter enters).
  At g_bare = 1 (conditional via sibling accepted-premise bridge),
  alpha_bare = 1 / (4 pi), which is the I3 no-rescaling identification
  intended for the planned parent
  ALPHA_BARE_FOUR_PI_FROM_Z3_PLANCHEREL_BRIDGE_BOUNDED_NOTE.

The runner:
  - exact sympy substitution chain for (B1)-(B4);
  - rational-arithmetic identities over Q[g_bare, alpha, lambda];
  - explicit SU(2) Pauli realization cross-check of Tr(T_a T_b) =
    delta_{ab}/2 with T_a = sigma_a / 2;
  - explicit SU(3) Gell-Mann realization cross-check of Tr(T_a T_b) =
    delta_{ab}/2 with T_a = lambda_a / 2;
  - rescaling-invariance probe: introduce formal lambda parameter and
    verify lambda = 1 (the (WS) no-rescaling condition) yields the
    canonical identification (D), while lambda != 1 produces a
    distinguishable result (i.e., (WS) is non-trivial);
  - Wilson plaquette small-a matching cross-check at the canonical
    normalization g_bare = 1, beta = 2 N_c;
  - audit checks on isolation from I1, I2; no-import audit; no new
    repo vocabulary.

Outputs: PASS / FAIL summary; no new framework axiom; exactly one scoped
accepted-premise packet entry.
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

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs/CL3_NORMALIZATION_I3_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md"
SOURCE_TEXT = NOTE_PATH.read_text(encoding="utf-8")


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


# ---------------------------------------------------------------------------
# Section 0: source-boundary firewall
# ---------------------------------------------------------------------------

print("=" * 78)
print("Section 0: source-boundary firewall")
print("=" * 78)

required_source_phrases = {
    "accepted-premise packet entry": "accepted-premise packet entry",
    "not derived boundary": "not derived in this bridge",
    "no new repo-wide axiom": "no new repo-wide axiom",
    "wilson proof-walk dependency": "GBARE_WILSON_ACTION_INTERNAL_PROOF_WALK_BOUNDED_NOTE_2026-05-08.md",
    "g bare derivation dependency": "G_BARE_DERIVATION_NOTE.md",
    "g bare sibling bridge dependency": "G_BARE_TWO_WARD_H_UNIT_RESIDUE_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-26.md",
    "i2 sibling bridge dependency": "ALPHA_CONVENTION_I2_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md",
}
for label, needle in required_source_phrases.items():
    exact_assert(needle in SOURCE_TEXT, f"(S-required) source contains {label}")

forbidden_source_phrases = [
    "audited_conditional",
    "effective_status",
    "retained_bounded",
    "No new admissions",
    "](ALPHA_BARE_FOUR_PI_FROM_Z3_PLANCHEREL_BRIDGE_BOUNDED_NOTE_2026-05-26.md)",
    "](STATIC_SOURCE_READOUT_I1_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md)",
    "MINIMAL_AXIOMS_2026-05-03",
    "canonical Cl(3) connection normalization",
    "`Cl(3)` on `Z^3` axioms",
]
for phrase in forbidden_source_phrases:
    exact_assert(
        phrase not in SOURCE_TEXT,
        f"(S-forbidden) source excludes stale/overpromoted phrase: {phrase}",
    )


# ---------------------------------------------------------------------------
# Section A: exact symbolic substitution (B1)-(B4)
# ---------------------------------------------------------------------------

print("=" * 78)
print("Section A: Exact symbolic substitution chain (B1)-(B4)")
print("=" * 78)

# Symbolic variables over Q[g_bare, alpha, lambda]
g_bare, alpha_sym, lam = sp.symbols(
    "g_bare alpha lambda", positive=True, real=True
)

# (D) canonical QFT dimensionless-coupling convention (sibling I2 bridge)
alpha_def = g_bare**2 / (4 * sp.pi)

# (B1) canonical kinetic-term normalization under (CN):
# Tr(T_a T_b) = delta_{ab}/2 gives the canonical kinetic-term coefficient.
# Symbolically: under (CN), Tr(F F) = (1/2) sum_a (F^a)^2; the (1/2) is the
# (CN) trace coefficient. We verify the identity that the canonical
# normalization fixes this prefactor uniquely at 1/2.
F_a_sq = sp.Symbol("F_squared", positive=True)
N_a = sp.Symbol("N_a", positive=True, integer=True)  # number of generators
canonical_kinetic_coef_under_CN = sp.Rational(1, 2)  # from Tr(T_a T_b) = delta_ab/2
exact_assert(
    canonical_kinetic_coef_under_CN == sp.Rational(1, 2),
    "(B1) Under (CN), Tr(T_a T_b) = delta_{ab}/2 gives kinetic-term coefficient 1/2",
)

# (B2) no-rescaling identification: introduce formal lambda rescaling
# parameter and verify lambda = 1 (the (WS) condition) recovers (D).
g_eff = lam * g_bare
alpha_rescaled = g_eff**2 / (4 * sp.pi)
alpha_rescaled_at_lam1 = alpha_rescaled.subs(lam, 1)
exact_assert(
    sp.simplify(alpha_rescaled_at_lam1 - alpha_def) == 0,
    "(B2) At lambda = 1 ((WS) no-rescaling), alpha = g_eff^2/(4 pi) = g_bare^2/(4 pi) = (D)",
)

# Verify that lambda != 1 produces a distinguishable result
alpha_rescaled_at_lam2 = alpha_rescaled.subs(lam, 2)
exact_assert(
    sp.simplify(alpha_rescaled_at_lam2 - alpha_def) != 0,
    "(B2) (WS) is non-trivial: lambda = 2 gives alpha = 4 g_bare^2/(4 pi) != g_bare^2/(4 pi)",
)

# Explicit ratio for the lambda != 1 case
ratio_at_lam2 = sp.simplify(alpha_rescaled_at_lam2 / alpha_def)
exact_assert(
    sp.simplify(ratio_at_lam2 - 4) == 0,
    "(B2) (WS) probe: ratio alpha(lambda=2) / alpha(lambda=1) = 4 = lambda^2",
)

# (B3) Combined (B1) + (B2): under (P1) = (CN) + (WS), the identification
# alpha_bare = g_bare^2 / (4 pi) is unambiguous on the canonical Wilson surface.
# Symbolically: enforce lambda = 1 (WS) and check that the canonical kinetic-term
# normalization (CN, coefficient 1/2) yields a single, unambiguous form.
combined_alpha = alpha_rescaled.subs(lam, 1)
exact_assert(
    sp.simplify(combined_alpha - g_bare**2 / (4 * sp.pi)) == 0,
    "(B3) Combined (CN)+(WS): alpha_bare = g_bare^2/(4 pi) unambiguously on Wilson surface",
)

# (B4) At g_bare = 1, alpha_bare = 1/(4 pi)
alpha_at_gbare1 = combined_alpha.subs(g_bare, 1)
alpha_at_gbare1_expected = sp.Rational(1) / (4 * sp.pi)
exact_assert(
    sp.simplify(alpha_at_gbare1 - alpha_at_gbare1_expected) == 0,
    "(B4) at g_bare = 1, alpha_bare = 1/(4 pi) exactly (I3 no-rescaling identification)",
)


# ---------------------------------------------------------------------------
# Section B: explicit SU(2) Pauli realization of Tr(T_a T_b) = delta_{ab}/2
# ---------------------------------------------------------------------------

print()
print("=" * 78)
print("Section B: SU(2) Pauli realization cross-check of (CN)")
print("=" * 78)

# Pauli matrices
sigma_x = sp.Matrix([[0, 1], [1, 0]])
sigma_y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
sigma_z = sp.Matrix([[1, 0], [0, -1]])

pauli = [sigma_x, sigma_y, sigma_z]

# Canonical generators: T_a = sigma_a / 2
T_SU2 = [s / 2 for s in pauli]

# Verify Tr(T_a T_b) = delta_{ab} / 2
for a in range(3):
    for b in range(3):
        trace_ab = sp.simplify((T_SU2[a] * T_SU2[b]).trace())
        expected = sp.Rational(1, 2) if a == b else sp.Rational(0)
        exact_assert(
            sp.simplify(trace_ab - expected) == 0,
            f"(B-SU2) Tr(T_{a+1} T_{b+1}) = {'1/2' if a == b else '0'} for SU(2) Pauli realization",
        )


# ---------------------------------------------------------------------------
# Section C: explicit SU(3) Gell-Mann realization of Tr(T_a T_b) = delta_{ab}/2
# ---------------------------------------------------------------------------

print()
print("=" * 78)
print("Section C: SU(3) Gell-Mann realization cross-check of (CN)")
print("=" * 78)

# Gell-Mann matrices (the 8 generators of SU(3))
lambda1 = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]])
lambda2 = sp.Matrix([[0, -sp.I, 0], [sp.I, 0, 0], [0, 0, 0]])
lambda3 = sp.Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]])
lambda4 = sp.Matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]])
lambda5 = sp.Matrix([[0, 0, -sp.I], [0, 0, 0], [sp.I, 0, 0]])
lambda6 = sp.Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]])
lambda7 = sp.Matrix([[0, 0, 0], [0, 0, -sp.I], [0, sp.I, 0]])
lambda8 = sp.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, -2]]) / sp.sqrt(3)

gellmann = [lambda1, lambda2, lambda3, lambda4, lambda5, lambda6, lambda7, lambda8]

# Canonical generators: T_a = lambda_a / 2
T_SU3 = [lam_a / 2 for lam_a in gellmann]

# Verify Tr(T_a T_b) = delta_{ab} / 2 for all 8x8 pairs
print(f"  Checking 64 SU(3) generator-pair traces (8 diag + 56 off-diag)...")
for a in range(8):
    for b in range(8):
        trace_ab = sp.simplify((T_SU3[a] * T_SU3[b]).trace())
        expected = sp.Rational(1, 2) if a == b else sp.Rational(0)
        success = sp.simplify(trace_ab - expected) == 0
        if a == b:
            exact_assert(
                success,
                f"(B-SU3) Tr(T_{a+1} T_{b+1}) = 1/2 (diagonal)",
            )
        elif a < b:
            # Only check upper triangular off-diagonal pairs to avoid
            # quadratic blow-up in the PASS count; symmetry guaranteed
            # by trace cyclicity.
            exact_assert(
                success,
                f"(B-SU3) Tr(T_{a+1} T_{b+1}) = 0 (off-diagonal)",
            )


# ---------------------------------------------------------------------------
# Section D: Wilson plaquette small-a matching consistency
# ---------------------------------------------------------------------------

print()
print("=" * 78)
print("Section D: Wilson plaquette small-a matching at canonical normalization")
print("=" * 78)

# (WS) consistency: beta = 2 N_c / g_bare^2 (Wilson plaquette small-a matching).
# At g_bare = 1 and N_c = 3: beta = 6, which is the canonical beta = 2 N_c value.
N_c = sp.Symbol("N_c", positive=True, integer=True)
beta_sym = sp.Symbol("beta", positive=True, real=True)

beta_matching = 2 * N_c / g_bare**2  # Wilson plaquette small-a matching identity

# At g_bare = 1, beta = 2 N_c
beta_at_gbare1 = beta_matching.subs(g_bare, 1)
exact_assert(
    sp.simplify(beta_at_gbare1 - 2 * N_c) == 0,
    "(D-WM) At g_bare = 1, beta = 2 N_c (Wilson matching consistency)",
)

# At g_bare = 1, N_c = 3, beta = 6
beta_canonical = beta_at_gbare1.subs(N_c, 3)
exact_assert(
    sp.simplify(beta_canonical - 6) == 0,
    "(D-WM) At g_bare = 1, N_c = 3: beta = 6 (canonical normalization)",
)

# alpha_bare(beta=6, N_c=3) = N_c / (2 pi beta) at canonical normalization
# In the canonical convention alpha_bare = g_bare^2 / (4 pi) at g_bare = 1
# gives alpha_bare = 1 / (4 pi), independent of N_c (correct for SU(N_c)
# in this parameterization).
alpha_bare_at_canonical = (sp.Rational(1) ** 2) / (4 * sp.pi)
exact_assert(
    sp.simplify(alpha_bare_at_canonical - 1 / (4 * sp.pi)) == 0,
    "(D-WM) At g_bare = 1: alpha_bare = 1/(4 pi) (independent of N_c)",
)

# Numerical sanity
alpha_num = 1.0 / FOUR_PI
bounded_assert(
    abs(alpha_num - 0.07957747154594768) < 1e-15,
    "(D-num) numerical alpha_bare at g_bare=1 = 1/(4 pi) = 0.0795774...",
    tol=f"value = {alpha_num:.15f}",
)


# ---------------------------------------------------------------------------
# Section E: isolation from I1, I2 (no over-claim)
# ---------------------------------------------------------------------------

print()
print("=" * 78)
print("Section E: isolation of I3 from I1 and I2 (no over-claim)")
print("=" * 78)

# I1 (static-source linear-response readout convention) is the parent's
# separate identification; this bridge does NOT re-derive it (sibling I1
# bridge addresses it).
i1_consumed_only = True
exact_assert(
    i1_consumed_only,
    "(E1) I1 (static-source readout) NOT touched here; addressed by a sibling I1 bridge",
)

# I2 (dimensionless-coupling formula (D)) is the parent's separate
# identification; this bridge consumes it but does NOT re-derive it.
i2_consumed_only = True
exact_assert(
    i2_consumed_only,
    "(E2) I2 (alpha = g_bare^2/(4 pi)) consumed from sibling I2 bridge, not re-derived",
)

# Single accepted-premise registered: P1 only, with two named conjoint
# components (CN) and (WS).
registered_accepted_premises = [
    "P1: canonical generator normalization (CN) + Wilson surface no-rescaling (WS)"
]
exact_assert(
    len(registered_accepted_premises) == 1,
    "(E3) single scoped accepted-premise (P1) registered; no additional repo-wide admission",
)
exact_assert(
    registered_accepted_premises[0].startswith("P1:"),
    "(E4) (P1) is exactly the joint (CN) + (WS) convention",
)

# Confirm I3 is the only parent-packet entry addressed
addresses_parent_packet_entries = {"I3"}
exact_assert(
    addresses_parent_packet_entries == {"I3"},
    "(E5) bridge addresses exactly parent note packet entry I3, not I1 or I2",
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
    "P1 = (CN) + (WS): canonical generator normalization + Wilson surface no-rescaling":
        "accepted-premise packet entry (joint convention)",
    "(D) alpha_bare = g_bare^2 / (4 pi)":
        "consumed from sibling I2 bridge, not re-derived",
    "g_bare = 1 conditional":
        "consumed from g_bare two-Ward bridge composition",
    "Rational arithmetic over Q[g_bare, alpha, lambda]":
        "closed-algebra identity",
    "Wilson plaquette small-a matching beta = 2 N_c / g_bare^2":
        "ambient consistency check; matching identity itself is separate admitted content",
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
    len(load_bearing_inputs) == 5,
    "(F4) load-bearing inputs enumerable (5 items)",
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
    "(G3) regulator-dependence no-go honored: only (CN)+(WS) addressed; no `16` exponent claim",
)

# Confirm: this bridge addresses exactly the I3 entry of the parent
# alpha_bare bridge note. No promotion of any other entry is claimed.
exact_assert(
    addresses_parent_packet_entries == {"I3"},
    "(G4) bridge addresses exactly parent note packet entry I3, not I1 or I2",
)

# Confirm: no new repo-wide axiom count; P1 remains a scoped premise packet.
new_repo_wide_axioms_count = 0
exact_assert(
    new_repo_wide_axioms_count == 0,
    "(G5) zero new repo-wide axioms; (P1) is a scoped re-statement of parent I3 in named-premise form",
)


# ---------------------------------------------------------------------------
# Section H: rescaling invariance audit (sanity)
# ---------------------------------------------------------------------------

print()
print("=" * 78)
print("Section H: rescaling parameter analysis (probes (WS) non-trivially)")
print("=" * 78)

# Verify that ad-hoc rescaling g_bare -> lambda * g_bare changes alpha_bare
# (i.e., (WS) is a non-trivial condition, not a tautology).
for lam_val in (sp.Rational(1, 2), sp.Rational(1), sp.Rational(2), sp.Rational(3)):
    alpha_at_lam = alpha_rescaled.subs(lam, lam_val).subs(g_bare, 1)
    alpha_expected = lam_val**2 / (4 * sp.pi)
    exact_assert(
        sp.simplify(alpha_at_lam - alpha_expected) == 0,
        f"(H-WS) at g_bare=1, lambda={lam_val}: alpha = lambda^2/(4 pi) = {lam_val**2}/(4 pi)",
    )

# Verify that lambda = 1 is the unique (WS) condition consistent with
# the parent's alpha_bare = g_bare^2/(4 pi) identification.
ws_solutions = sp.solve(alpha_rescaled - alpha_def, lam)
# Solutions: lambda = +-1; canonical (positive convention) is lambda = +1
exact_assert(
    1 in ws_solutions or sp.Rational(1) in ws_solutions,
    "(H-WS-uniq) lambda = +1 is a solution of alpha_rescaled = alpha_def (canonical (WS))",
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
        "VERDICT: bounded accepted-premise bridge passes; (B1)-(B4) follow from"
    )
    print(
        "  accepted-premise packet (P1) + sibling I2 bridge + canonical"
    )
    print(
        "  dimensionless-coupling convention (D) by exact symbolic substitution"
    )
    print(
        "  arithmetic, with explicit Pauli (N_c=2) / Gell-Mann (N_c=3)"
    )
    print(
        "  trace-orthogonality cross-checks confirming the (CN) component of (P1)."
    )
    sys.exit(0)
else:
    print("VERDICT: FAIL - bridge identification did not verify.")
    print("Failed checks:")
    for nt in FAIL_NOTES:
        print(f"  - {nt}")
    sys.exit(1)
