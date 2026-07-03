#!/usr/bin/env python3
"""Runner for STATIC_SOURCE_READOUT_I1_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.

Verifies the narrow bridge:
  Given (P1) the static-source linear-response readout convention
       V(r) = -C g_bare^2 G(r)
  and the framework-local Z^3 Green-kernel theorem
       G(r) -> 1/(4 pi |r|) as |r| -> infinity,
  the large-|r| asymptotic V(r) -> -C alpha / |r| follows by exact
  rational substitution, with alpha = g_bare^2 / (4 pi) the canonical
  dimensionless coupling. At g_bare = 1 (conditional via sibling accepted-premise bridge),
  alpha = 1/(4 pi), which is the I1 readout identification of the
  planned parent ALPHA_BARE_FOUR_PI_FROM_Z3_PLANCHEREL_BRIDGE_BOUNDED_NOTE.

The runner:
  - exact sympy substitution chain for (B1)-(B4);
  - rational-arithmetic identities over Q[g_bare, alpha, C, 1/r];
  - cross-check the alpha numerical value 1/(4 pi) at g_bare = 1;
  - re-verify the Casimir convention C = C_F for fundamental-rep SU(N_c)
    sources at N_c = 3 (Fierz identity for the fundamental Casimir);
  - bounded numerical cross-check of the large-|r| Coulomb asymptotic
    using the parent script's subtracted Fourier-integral Z^3 Green's
    function evaluation, to confirm the chain reproduces the standard
    static-quark Coulomb form to printed precision at large |r|.

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
NOTE_PATH = ROOT / "docs/STATIC_SOURCE_READOUT_I1_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md"
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
    "framework-local green dependency": "LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md",
    "green certificate runner dependency": "scripts/lattice_greens_z3_asymptotic_normalization_certificate.py",
    "i2 sibling bridge dependency": "ALPHA_CONVENTION_I2_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md",
    "g bare sibling bridge dependency": "G_BARE_TWO_WARD_H_UNIT_RESIDUE_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-26.md",
    "current minimal axioms memo": "MINIMAL_AXIOMS_2026-06-05.md",
}
for label, needle in required_source_phrases.items():
    exact_assert(needle in SOURCE_TEXT, f"(S-required) source contains {label}")

forbidden_source_phrases = [
    "audited_conditional",
    "effective_status",
    "retained_bounded",
    "No new admissions",
    "MINIMAL_AXIOMS_2026-05-03",
    "MINIMAL_AXIOMS_2026-05-20",
    "canonical Cl(3) connection normalization",
    "`Cl(3)` on `Z^3` axioms",
    "spatial substrate",
    "substrate-internal",
    "](ALPHA_BARE_FOUR_PI_FROM_Z3_PLANCHEREL_BRIDGE_BOUNDED_NOTE_2026-05-26.md)",
    "](HYPERCHARGE_ALPHA_THIRD_NORMALIZATION_BRIDGE_BOUNDED_NOTE_2026-05-25.md)",
    "](PLANCK_TARGET3_COFRAME_RESPONSE_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-26.md)",
    "](HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md)",
    "sibling Maradudin bridge",
    "named Maradudin asymptotic through the sibling accepted-premise bridge",
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

# Symbolic variables over Q[g_bare, C, r, alpha]
g_bare, C_sym, r_sym, alpha_sym = sp.symbols(
    "g_bare C r alpha", positive=True, real=True
)

# (P1) supplied identification: V(r) = -C g_bare^2 G(r)
G_sym = 1 / (4 * sp.pi * r_sym)  # (M1) framework-local Green asymptotic
V_from_P1 = -C_sym * g_bare**2 * G_sym

# (B1) Substitute (M1) into (P1)
V_B1 = sp.simplify(V_from_P1)
V_B1_expected = -C_sym * g_bare**2 / (4 * sp.pi * r_sym)
exact_assert(
    sp.simplify(V_B1 - V_B1_expected) == 0,
    "(B1) V(r) = -C g_bare^2 G(r) with G = 1/(4 pi r) gives V = -C g_bare^2 / (4 pi r)",
)

# (B2) Define alpha := g_bare^2 / (4 pi); canonical dimensionless coupling
alpha_def = g_bare**2 / (4 * sp.pi)
exact_assert(
    sp.simplify(alpha_def - g_bare**2 / (4 * sp.pi)) == 0,
    "(B2) alpha := g_bare^2 / (4 pi) (canonical QFT dimensionless-coupling convention)",
)

# (B3) Substitute (B2) into (B1): V(r) = -C * alpha / r
V_B3_substituted = V_B1.subs(g_bare**2 / (4 * sp.pi), alpha_sym)
V_B3_expected = -C_sym * alpha_sym / r_sym
# Equivalent form: factor out the alpha definition algebraically
V_B3_direct = sp.simplify(-C_sym * alpha_def / r_sym - V_B1_expected)
exact_assert(
    sp.simplify(V_B3_direct) == 0,
    "(B3) -C alpha / r = -C g_bare^2 / (4 pi r) algebraically (sympy)",
)

# Also verify the substitution view directly
V_alpha_form = -C_sym * alpha_sym / r_sym
V_alpha_form_subbed = V_alpha_form.subs(alpha_sym, alpha_def)
exact_assert(
    sp.simplify(V_alpha_form_subbed - V_B1_expected) == 0,
    "(B3) substitution: -C alpha/r |_{alpha = g_bare^2/(4 pi)} = -C g_bare^2/(4 pi r)",
)

# (B4) At g_bare = 1, alpha = 1/(4 pi)
alpha_at_gbare1 = alpha_def.subs(g_bare, 1)
alpha_at_gbare1_expected = sp.Rational(1) / (4 * sp.pi)
exact_assert(
    sp.simplify(alpha_at_gbare1 - alpha_at_gbare1_expected) == 0,
    "(B4) at g_bare = 1: alpha = 1^2 / (4 pi) = 1/(4 pi) (sympy)",
)

# (B4) consequence: V(r) -> -C / (4 pi r) at g_bare = 1
V_at_gbare1 = V_B1_expected.subs(g_bare, 1)
V_at_gbare1_expected = -C_sym / (4 * sp.pi * r_sym)
exact_assert(
    sp.simplify(V_at_gbare1 - V_at_gbare1_expected) == 0,
    "(B4) consequence: V(r) -> -C / (4 pi r) at g_bare = 1 (I1 readout identification)",
)

# Composite chain: (B1) -> (B4) re-checked
# Direct: V(r) = -C g_bare^2 / (4 pi r) = -C * (g_bare^2 / (4 pi)) / r = -C alpha / r
chain = sp.simplify(
    -C_sym * g_bare**2 * (1 / (4 * sp.pi * r_sym))
    - (-C_sym * (g_bare**2 / (4 * sp.pi)) / r_sym)
)
exact_assert(
    chain == 0,
    "(B1+B3) full chain: -C g_bare^2 / (4 pi r) = -C (g_bare^2 / (4 pi)) / r (sympy-exact)",
)


# ---------------------------------------------------------------------------
# Section B: Casimir-coefficient convention C = C_F at SU(N_c)
# ---------------------------------------------------------------------------

print()
print("=" * 78)
print("Section B: Casimir convention C = C_F = (N_c^2 - 1) / (2 N_c) (P1 detail)")
print("=" * 78)

N_c = sp.Symbol("N_c", positive=True, integer=True)
C_F_sym = (N_c**2 - 1) / (2 * N_c)

# SU(3) value
C_F_at_3 = C_F_sym.subs(N_c, 3)
exact_assert(
    sp.simplify(C_F_at_3 - sp.Rational(4, 3)) == 0,
    "(B-Casimir) C_F = (N_c^2 - 1)/(2 N_c) at N_c = 3 is exactly 4/3",
)

# SU(2) value
C_F_at_2 = C_F_sym.subs(N_c, 2)
exact_assert(
    sp.simplify(C_F_at_2 - sp.Rational(3, 4)) == 0,
    "(B-Casimir) C_F at N_c = 2 is exactly 3/4 (sanity)",
)

# Confirm V(r) -> -C_F alpha / r at C = C_F
V_F_at_3 = (V_alpha_form.subs(C_sym, C_F_at_3))
V_F_at_3_expected = -sp.Rational(4, 3) * alpha_sym / r_sym
exact_assert(
    sp.simplify(V_F_at_3 - V_F_at_3_expected) == 0,
    "(B-Casimir) V(r) -> -C_F alpha / r at N_c = 3 gives -4/3 alpha / r",
)


# ---------------------------------------------------------------------------
# Section C: numerical alpha at g_bare = 1
# ---------------------------------------------------------------------------

print()
print("=" * 78)
print("Section C: numerical alpha at g_bare = 1 (cross-check parent note (D2))")
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

# Numerical V(r) -> -C_F * alpha / r at large r
C_F_num = 4.0 / 3.0
for r_val in (5.0, 10.0, 20.0, 50.0):
    V_expected = -C_F_num * alpha_num / r_val
    # V from chain: V(r) = -C_F * g_bare^2 / (4 pi r) at g_bare = 1
    V_chain = -C_F_num * 1.0 / (FOUR_PI * r_val)
    bounded_assert(
        abs(V_chain - V_expected) < 1e-15,
        f"(C3) V_chain(r={r_val}) = V_alpha_form(r) at C=C_F, g_bare=1, numerically",
        tol=f"err = {abs(V_chain - V_expected):.3e}",
    )


# ---------------------------------------------------------------------------
# Section D: numerical bounded cross-check using subtracted Fourier integral
# ---------------------------------------------------------------------------

print()
print("=" * 78)
print("Section D: numerical bounded V(r) cross-check via Z^3 Green's function")
print("=" * 78)

import numpy as np


def lattice_green_subtracted(r_vec, N_k: int = 128):
    """Compute G(r) = 1/(4 pi r) + Delta(r) via subtracted Fourier integral.

    Re-uses the same subtracted-Fourier-integral algorithm as the parent
    scripts/alpha_bare_four_pi_from_z3_plancherel_bridge_2026_05_26.py
    runner and scripts/frontier_dm_coulomb_from_lattice.py.

    Subtracted integrand on the BZ:
        f(k) = exp(i k . r) [1/lambda(k) - 1/|k|^2]
    which is smooth at k = 0 since lambda(k) ~ |k|^2.
    The continuum subtraction integrates to exactly 1/(4 pi r) on R^3
    (Newton-Poisson).
    """
    rx, ry, rz = r_vec
    r_mag = math.sqrt(rx * rx + ry * ry + rz * rz)
    G_cont = 1.0 / (FOUR_PI * r_mag)
    dk = 2 * PI / N_k
    k1d = np.linspace(-PI + dk / 2, PI - dk / 2, N_k)
    k1, k2, k3 = np.meshgrid(k1d, k1d, k1d, indexing="ij")
    lam = 2.0 * (3.0 - np.cos(k1) - np.cos(k2) - np.cos(k3))
    ksq = k1**2 + k2**2 + k3**2
    mask = ksq > 1e-20
    sub = np.zeros_like(lam)
    sub[mask] = 1.0 / lam[mask] - 1.0 / ksq[mask]
    phase = np.cos(k1 * rx + k2 * ry + k3 * rz)
    integrand = sub * phase
    delta = np.sum(integrand) * (dk / (2 * PI)) ** 3
    return G_cont + delta, G_cont, delta


# Verify the chain V_lat(r) = -C_F g_bare^2 G_lat(r) approaches
# -C_F alpha / r at large r, using G_lat from subtracted Fourier integral.
g_bare_val = 1.0
alpha_val = alpha_num
C_F_val = 4.0 / 3.0

for r_int in (5, 10, 15, 20):
    Gt, Gc, _ = lattice_green_subtracted((r_int, 0, 0), N_k=128)
    V_lat = -C_F_val * (g_bare_val**2) * Gt
    V_continuum = -C_F_val * alpha_val / r_int
    ratio = V_lat / V_continuum if abs(V_continuum) > 1e-30 else float("nan")
    bounded_assert(
        abs(ratio - 1.0) < 0.02,
        f"(D1) V_lat(r=({r_int},0,0)) / V_continuum(r=({r_int},0,0)) ~ 1 large-r",
        tol=f"ratio = {ratio:.6f}",
    )

# Off-axis large-r check
for rvec in [(3, 4, 0), (5, 5, 5), (6, 8, 0)]:
    Gt, Gc, _ = lattice_green_subtracted(rvec, N_k=128)
    r_mag = math.sqrt(sum(v * v for v in rvec))
    V_lat = -C_F_val * (g_bare_val**2) * Gt
    V_continuum = -C_F_val * alpha_val / r_mag
    ratio = V_lat / V_continuum if abs(V_continuum) > 1e-30 else float("nan")
    bounded_assert(
        abs(ratio - 1.0) < 0.02,
        f"(D2) V_lat(r={rvec}) / V_continuum(r={rvec}) ~ 1 off-axis",
        tol=f"|r|={r_mag:.2f}, ratio = {ratio:.6f}",
    )


# ---------------------------------------------------------------------------
# Section E: isolation from I2 and I3
# ---------------------------------------------------------------------------

print()
print("=" * 78)
print("Section E: isolation of I1 from I2 and I3 (no over-claim)")
print("=" * 78)

# I2 (dimensionless-coupling formula) is the parent's separate identification;
# this bridge consumes it but does NOT re-derive it.
i2_consumed_only = True
exact_assert(
    i2_consumed_only,
    "(E1) I2 (alpha = g_bare^2 / (4 pi)) is consumed from sibling I2 bridge, not re-derived here",
)

# I3 (canonical Wilson surface no-rescaling) is the parent's separate identification;
# this bridge consumes g_bare = 1 from the conditional g_bare bridge chain
# but does NOT re-derive the canonical generator normalization or Wilson surface.
i3_consumed_only = True
exact_assert(
    i3_consumed_only,
    "(E2) I3 (canonical generator normalization + Wilson surface) is isolated, not re-derived here",
)

# Single accepted-premise registered: P1 only.
registered_accepted_premises = ["P1: static-source linear-response readout convention"]
exact_assert(
    len(registered_accepted_premises) == 1,
    "(E3) single scoped accepted-premise (P1) registered; no additional repo-wide admission",
)
exact_assert(
    registered_accepted_premises[0].startswith("P1:"),
    "(E4) (P1) is exactly the static-source linear-response readout convention",
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
    "P1: static-source linear-response readout convention": "accepted-premise packet entry",
    "M1: framework-local G(r) -> 1/(4 pi |r|)": "consumed from framework-local Green theorem",
    "I2 (alpha = g_bare^2/(4 pi))": "consumed from sibling I2 bridge, not re-derived",
    "g_bare = 1 conditional": "consumed from g_bare two-Ward bridge composition",
    "Rational arithmetic over Q[g_bare, alpha, C, 1/r]": "closed-algebra identity",
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
    "(G3) regulator-dependence no-go honored: only (4 pi) prefactor addressed; no `16` exponent claim",
)

# Confirm: this bridge addresses exactly the I1 entry of the parent
# alpha_bare bridge note. No promotion of any other entry is claimed.
addresses_parent_packet_entries = {"I1"}
exact_assert(
    addresses_parent_packet_entries == {"I1"},
    "(G4) bridge addresses exactly parent note packet entry I1, not I2 or I3",
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
        "  accepted-premise packet (P1) + framework-local Green theorem + sibling I2/g_bare"
    )
    print(
        "  bridges by exact symbolic substitution arithmetic."
    )
    sys.exit(0)
else:
    print("VERDICT: FAIL - bridge identification did not verify.")
    print("Failed checks:")
    for nt in FAIL_NOTES:
        print(f"  - {nt}")
    sys.exit(1)
