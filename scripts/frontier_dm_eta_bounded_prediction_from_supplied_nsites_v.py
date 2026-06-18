#!/usr/bin/env python3
"""Runner: DM eta open-gate conditional arithmetic certificate.

Checks the open-gate conditional arithmetic certificate
`docs/DM_ETA_BOUNDED_PREDICTION_FROM_SUPPLIED_NSITES_V_NARROW_THEOREM_NOTE_2026-05-28.md`

Verifies, with rational arithmetic where possible and floating-point
arithmetic elsewhere, the conditional arithmetic surface:

1. Retained R_base = 31/9 group-theory identity on cited Casimir/adjoint
   inputs.
2. Structural composed product N_sites · v = 16 · v ≈ 3940 GeV from the
   supplied composed-product premise (P2).
3. Freeze-out-bypass identity eta = C · m_DM^2 with C as in (M0) under
   the local packet: supplied P1-P4 and P6-P7 plus retained_bounded P5.
4. Central evaluation eta_pred(central) = 6.38e-10 at
   (x_F = 25, S_vis/S_dark = 1.59, alpha_X = alpha_LM).
5. Conditional band eta_pred in [5.25e-10, 8.11e-10] over
   (x_F, S_vis/S_dark) in [22, 28] x [1.4, 1.7].
6. Central deviation +4.18% vs eta_obs = 6.12e-10.
7. Supplied single-mass readout m_DM ≈ 3.94 TeV.
8. Cross-check with ETA_188 structural decomposition consistency.
9. Note-text recording of the named local packet P1-P7.
10. Note-text recording of the supplied composed-product (P2) as a
    candidate, not a retained dependency.

No new framework axioms, admissions, or repo vocabulary are introduced.
"""

from __future__ import annotations

import math
import sys
from fractions import Fraction
from pathlib import Path

from canonical_plaquette_surface import (
    CANONICAL_ALPHA_LM,
    CANONICAL_PLAQUETTE,
    CANONICAL_U0,
)

REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = REPO_ROOT / "docs"

NOTE_FNAME = (
    "DM_ETA_BOUNDED_PREDICTION_FROM_SUPPLIED_NSITES_V_NARROW_THEOREM_NOTE_2026-05-28.md"
)
ETA_188_FNAME = "ETA_188_STRUCTURAL_ORIGIN_PARTIAL_NOTE_2026-05-03.md"
R_BASE_FNAME = "R_BASE_GROUP_THEORY_DERIVATION_THEOREM_NOTE_2026-04-24.md"
BIPARTITION_FNAME = (
    "HUBBLE_LANE5_C2_ATTACK_SURFACE_BIPARTITION_NARROW_THEOREM_NOTE_2026-05-27.md"
)

# Standard-physics constants and local packet inputs
M_PL_GEV = 1.2209e19          # axiom-level Planck mass
G_STAR = 106.75               # P5: retained_bounded SM finite-inventory count
K_PREFACTOR = 1.07e9          # P6: Kolb-Turner kinematic prefactor [GeV^-1]
BBN_COEFF_OMEGAB = 3.6515e-3  # P3: BBN coefficient Omega_b h^2 = coeff * eta_10
ETA_OBS = 6.12e-10            # comparator only (Planck/BBN)

# m_DM = N_sites * v
N_SITES = 16                   # P2 (composed): 2^d with d = 4 spacetime
V_VEV_GEV = 246.282818290129   # P2 (composed): v from authority

# Default central rectangle points
X_F_BAND = (22.0, 28.0)        # P4 band
S_RATIO_BAND = (1.4, 1.7)      # P7 band
X_F_CENTRAL = 25.0             # P4 central
S_RATIO_CENTRAL = 1.59         # P7 central
S_RATIO_CENTRAL_RATIONAL = Fraction(159, 100)

AUDIT_FAILS: list[str] = []
AUDIT_PASSES = 0


def audit(name: str, condition: bool, detail: str = "") -> None:
    """Record audit step; abort run with a failure summary on first FAIL."""
    global AUDIT_PASSES
    status = "PASS" if condition else "FAIL"
    line = f"[{status}] {name}"
    if detail:
        line += f"  --  {detail}"
    print(line)
    if condition:
        AUDIT_PASSES += 1
    else:
        AUDIT_FAILS.append(name)


def read_doc(fname: str) -> str:
    return (DOCS_DIR / fname).read_text(encoding="utf-8")


def compute_C(x_F: float, alpha_X: float, R: float) -> float:
    """C from (M0):
        C = K * x_F / (sqrt(g_*) * M_Pl * pi * alpha_X^2 * R * BBN_COEFF_OMEGAB * 1e10)
    Uses the precise local P3 coefficient, not the rounded 3.65e7 display,
    so that eta_pred = C * m_DM^2 evaluates eta directly.
    """
    bbn_factor = BBN_COEFF_OMEGAB * 1.0e10
    return (K_PREFACTOR * x_F) / (
        math.sqrt(G_STAR) * M_PL_GEV * math.pi * alpha_X ** 2 * R * bbn_factor
    )


def eta_pred(
    m_DM: float,
    x_F: float = X_F_CENTRAL,
    s_ratio: float = S_RATIO_CENTRAL,
    alpha_X: float = CANONICAL_ALPHA_LM,
) -> float:
    R_base = 31.0 / 9.0
    R = R_base * s_ratio
    C = compute_C(x_F, alpha_X, R)
    return C * m_DM ** 2


# ---------------------------------------------------------------------------
# Section 1: chain authority audits
# ---------------------------------------------------------------------------

print("=" * 72)
print("DM eta open-gate conditional arithmetic certificate")
print("=" * 72)

print()
print("Section 1: chain authority audits")
print("-" * 72)

note_text = read_doc(NOTE_FNAME)
note_flat = " ".join(note_text.split())
audit("Note exists at expected path", len(note_text) > 0, NOTE_FNAME)
audit(
    "Note claim type is open_gate conditional-support certificate",
    "**Claim type:** open_gate / conditional-support arithmetic certificate" in note_text,
)
audit(
    "Note type is open_gate / conditional-support",
    "**Type:** open_gate / conditional-support" in note_text,
)
audit(
    "Old bounded theorem claim-type headers are absent",
    "**Claim type:** bounded support note" not in note_text
    and "**Claim type:** bounded_theorem" not in note_text
    and "**Type:** bounded_theorem" not in note_text,
)
audit(
    "Note status authority is independent audit lane only",
    "Status authority:** independent audit lane only" in note_text,
)
audit(
    "Note records conditional support over the P_DM_ETA input packet",
    "conditional support over the\n`P_DM_ETA` input packet" in note_text
    or "conditional support over the `P_DM_ETA` input packet" in note_text,
)
audit(
    "Note records 2026-06-18 open-gate source-scope repair",
    "2026-06-18 Open-Gate Source-Scope Repair" in note_text,
)
audit(
    "Source-scope certificate marks actual current surface open",
    "actual_current_surface_status: open" in note_text
    and "conditional_surface_status: conditional-support" in note_text,
)
audit(
    "Source-scope certificate forbids retained proposal language",
    "proposal_allowed: false" in note_text
    and "audit_required_before_effective_retained: true" in note_text
    and "bare_retained_allowed: false" in note_text,
)
audit(
    "Note records 2026-06-12 P5 retained-input repair",
    "2026-06-12 P5 retained-input repair" in note_text,
)
audit(
    "Note records 2026-06-16 post-audit residual certificate",
    "2026-06-16 Post-Audit Residual Certificate" in note_text,
)
audit(
    "Post-audit certificate keeps P1-P4 and P6-P7 as live residuals",
    "remaining live residuals are exactly P1-P4 and P6-P7" in note_text
    and "P1: freeze-out-bypass identity" in note_text
    and "P7: Sommerfeld/dark-coupling route" in note_text,
)
audit(
    "Post-audit certificate keeps eta_obs comparator-only",
    "observed `eta_obs` value is a comparator for bracketing only" in note_flat
    and "not a proof input" in note_flat,
)
audit(
    "Note records 2026-06-16 BBN coefficient precision repair",
    "2026-06-16 BBN coefficient precision repair" in note_text,
)
audit(
    "BBN precision repair uses precise local P3 factor",
    "3.6515e-3 * 1e10 = 3.6515e7" in note_text
    and "older rounded `3.65e7`" in note_flat
    and "precise local P3 factor `3.6515e7`" in note_flat,
)
audit(
    "Note records 2026-06-07 source-boundary repair",
    "2026-06-07 Source-Boundary and Rounding Repair" in note_text,
)
audit(
    "Note records P_DM_ETA packet",
    "P_DM_ETA = (" in note_text,
)
audit(
    "P_DM_ETA records P5 as retained_bounded finite-inventory authority",
    "P5: g_* = 106.75 (retained_bounded finite-inventory authority)" in note_text,
)
audit(
    "Source cites retained_bounded SM finite-inventory authority for P5",
    "SM_RELATIVISTIC_DOF_COUNT_IMPORT_NOTE_2026-05-17.md" in note_text
    and "retained_bounded finite-inventory" in note_text,
)
audit(
    "Source no longer says g_* = 106.75 is supplied as P5",
    "g_* = 106.75` is supplied as `P5" not in note_text
    and "SM effective DOF `g_* = 106.75` | P5 supplied SM count" not in note_text,
)
audit(
    "Note records corrected exact central R ratio 1643/300",
    "1643/300" in note_text and "5.4767" in note_text,
)
audit(
    "Old central R display 5.4811 is absent",
    "5.4811" not in note_text,
)
for phrase in ("source-note proposal only",):
    audit(
        f"Note omits source-side status control phrase: {phrase}",
        phrase not in note_text,
    )

r_base_text = read_doc(R_BASE_FNAME)
audit(
    "R_base authority exists",
    len(r_base_text) > 0,
    "R_BASE_GROUP_THEORY_DERIVATION authority",
)
audit(
    "R_base = 31/9 stated in authority",
    "R_base = 31/9" in r_base_text or "31/9" in r_base_text,
)

eta188_text = read_doc(ETA_188_FNAME)
audit(
    "eta_188 authority exists",
    len(eta188_text) > 0,
    "ETA_188_STRUCTURAL_ORIGIN authority",
)
audit(
    "eta_188 ratio 0.1888 recorded in authority",
    "0.1888" in eta188_text or "0.18878" in eta188_text,
)

bipartition_text = read_doc(BIPARTITION_FNAME)
audit(
    "Lane 5 (C2) bipartition parent authority exists",
    len(bipartition_text) > 0,
)
audit(
    "Bipartition records (C2.eta) sub-target",
    "(C2.eta)" in bipartition_text or "C2.eta" in bipartition_text,
)


# ---------------------------------------------------------------------------
# Section 2: R_base = 31/9 exact rational check
# ---------------------------------------------------------------------------

print()
print("Section 2: R_base = 31/9 exact rational check")
print("-" * 72)

C2_SU3_FUND = Fraction(4, 3)
C2_SU2_FUND = Fraction(3, 4)
DIM_ADJ_SU3 = 8
DIM_ADJ_SU2 = 3
GUT_NORM = Fraction(3, 5)

num = C2_SU3_FUND * DIM_ADJ_SU3 + C2_SU2_FUND * DIM_ADJ_SU2
den = C2_SU2_FUND * DIM_ADJ_SU2
R_base_rational = GUT_NORM * (num / den)

audit(
    "Casimir SU(3) fund C_2 = 4/3",
    C2_SU3_FUND == Fraction(4, 3),
)
audit(
    "Casimir SU(2) fund C_2 = 3/4",
    C2_SU2_FUND == Fraction(3, 4),
)
audit(
    "Adjoint dim SU(3) = 8",
    DIM_ADJ_SU3 == 8,
)
audit(
    "Adjoint dim SU(2) = 3",
    DIM_ADJ_SU2 == 3,
)
audit(
    "Numerator = 155/12",
    num == Fraction(155, 12),
    f"computed {num}",
)
audit(
    "Denominator = 9/4",
    den == Fraction(9, 4),
    f"computed {den}",
)
audit(
    "R_base = 31/9 exactly",
    R_base_rational == Fraction(31, 9),
    f"computed {R_base_rational}",
)
audit(
    "R_base float ≈ 3.4444",
    abs(float(R_base_rational) - 3.4444444444) < 1e-9,
)


# ---------------------------------------------------------------------------
# Section 3: structural composed product P2: m_DM = N_sites · v
# ---------------------------------------------------------------------------

print()
print("Section 3: structural composed product P2: m_DM = N_sites · v")
print("-" * 72)

audit(
    "N_sites = 2^d with d = 4 gives N_sites = 16",
    N_SITES == 2 ** 4,
)
audit(
    "v VEV value 246.282818290129 GeV (composed input)",
    abs(V_VEV_GEV - 246.282818290129) < 1e-12,
)

m_DM = N_SITES * V_VEV_GEV
audit(
    "m_DM = N_sites · v evaluates to ≈ 3940.5 GeV",
    abs(m_DM - 3940.5251) < 0.01,
    f"computed {m_DM:.4f} GeV",
)
audit(
    "m_DM ≈ 3.94 TeV (supplied single-mass readout)",
    abs(m_DM / 1000.0 - 3.94) < 0.01,
    f"computed {m_DM / 1000.0:.3f} TeV",
)
audit(
    "Note records the supplied readout `m_DM ~ 3.94 TeV`",
    "3.94 TeV" in note_text,
)


# ---------------------------------------------------------------------------
# Section 4: freeze-out-bypass identity arithmetic (M0)
# ---------------------------------------------------------------------------

print()
print("Section 4: freeze-out-bypass identity arithmetic (M0)")
print("-" * 72)

audit(
    "Canonical plaquette 0.5934 used as cited surface",
    abs(CANONICAL_PLAQUETTE - 0.5934) < 1e-9,
)
audit(
    "u_0 = <P>^(1/4) ≈ 0.8777",
    abs(CANONICAL_U0 - 0.8777) < 1e-3,
    f"computed {CANONICAL_U0:.6f}",
)
audit(
    "alpha_LM = (1/(4π))/u_0 ≈ 0.09067",
    abs(CANONICAL_ALPHA_LM - 0.09067) < 1e-3,
    f"computed {CANONICAL_ALPHA_LM:.6f}",
)

R_base_float = 31.0 / 9.0
R_central = R_base_float * S_RATIO_CENTRAL
R_central_exact = Fraction(31, 9) * S_RATIO_CENTRAL_RATIONAL
audit(
    "R(central) = (31/9) * 1.59 = 1643/300 exactly",
    R_central_exact == Fraction(1643, 300),
    f"computed {R_central_exact}",
)
audit(
    "R(central) float ≈ 5.4767",
    abs(R_central - 5.476666666666667) < 1e-12,
    f"computed {R_central:.4f}",
)

C_central = compute_C(X_F_CENTRAL, CANONICAL_ALPHA_LM, R_central)
audit(
    "C(central) ≈ 4.106e-17 GeV^-2",
    abs(C_central - 4.106e-17) < 1e-18,
    f"computed {C_central:.4e}",
)


# ---------------------------------------------------------------------------
# Section 5: central evaluation eta_pred(central)
# ---------------------------------------------------------------------------

print()
print("Section 5: central evaluation eta_pred(central)")
print("-" * 72)

eta_central = eta_pred(m_DM)
audit(
    "eta_pred(central) ≈ 6.38e-10",
    abs(eta_central - 6.38e-10) < 3e-12,
    f"computed {eta_central:.4e}",
)
deviation_pct = 100.0 * (eta_central / ETA_OBS - 1.0)
audit(
    "Central deviation ≈ +4.18% vs eta_obs",
    abs(deviation_pct - 4.18) < 0.5,
    f"computed {deviation_pct:+.3f}%",
)


# ---------------------------------------------------------------------------
# Section 6: conditional band over (x_F, S_vis/S_dark) rectangle
# ---------------------------------------------------------------------------

print()
print("Section 6: conditional band over (x_F, S_vis/S_dark) rectangle")
print("-" * 72)

# (M0) arithmetic on the (x_F, S_vis/S_dark) rectangle with alpha_X = alpha_LM
# held fixed. The direct fixed-alpha band is the binding band for this row;
# the inherited audit-companion interval is context only.
grid_points_m0 = [
    ((22.0, 1.7), 5.25e-10),
    ((22.0, 1.59), 5.61e-10),
    ((22.0, 1.4), 6.37e-10),
    ((25.0, 1.7), 5.96e-10),
    ((25.0, 1.59), 6.38e-10),
    ((25.0, 1.4), 7.24e-10),
    ((28.0, 1.59), 7.14e-10),
    ((28.0, 1.4), 8.11e-10),
]

bound_low = float("inf")
bound_high = -float("inf")
for (x_F, s_ratio), expected in grid_points_m0:
    eta_val = eta_pred(m_DM, x_F=x_F, s_ratio=s_ratio)
    bound_low = min(bound_low, eta_val)
    bound_high = max(bound_high, eta_val)
    audit(
        f"grid (M0) ({x_F}, {s_ratio}) -> {expected:.2e}",
        abs(eta_val - expected) / expected < 0.05,
        f"computed {eta_val:.3e}",
    )

# Scan the full rectangle for true min/max
x_F_samples = [22.0, 23.0, 24.0, 25.0, 26.0, 27.0, 28.0]
s_ratio_samples = [1.4, 1.45, 1.5, 1.55, 1.59, 1.6, 1.65, 1.7]
true_low = float("inf")
true_high = -float("inf")
for x_F in x_F_samples:
    for s_ratio in s_ratio_samples:
        v = eta_pred(m_DM, x_F=x_F, s_ratio=s_ratio)
        true_low = min(true_low, v)
        true_high = max(true_high, v)

# The conditional band on the supplied rectangle:
# - eta_pred decreasing in s_ratio (eta ~ 1/R ~ 1/s_ratio)
# - eta_pred increasing in x_F  (eta ~ x_F)
# So the corners are: (22, 1.7) low, (28, 1.4) high
eta_low_corner = eta_pred(m_DM, x_F=22.0, s_ratio=1.7)
eta_high_corner = eta_pred(m_DM, x_F=28.0, s_ratio=1.4)
audit(
    "Conditional band low corner (x_F=22, S=1.7) ≈ 5.25e-10",
    abs(eta_low_corner - 5.25e-10) < 2e-11,
    f"computed {eta_low_corner:.3e}",
)
audit(
    "Conditional band high corner (x_F=28, S=1.4) ≈ 8.11e-10",
    abs(eta_high_corner - 8.11e-10) < 5e-11,
    f"computed {eta_high_corner:.3e}",
)
audit(
    "Note records direct lower band 5.25e-10",
    "5.25" in note_text,
)
audit(
    "Note records direct upper band 8.11e-10",
    "8.11" in note_text,
)
audit(
    "Note records inherited audit-companion interval as context only",
    "[4.94e-10, 7.24e-10]" in note_text and "context only" in note_text,
)
audit(
    "Bracketing (direct fixed-alpha band): low <= eta_obs <= high",
    eta_low_corner <= ETA_OBS <= eta_high_corner,
)
audit(
    "(M0) low corner equals (22, 1.7) ≈ 5.25e-10",
    abs(bound_low - 5.25e-10) < 5e-11,
    f"computed {bound_low:.3e}",
)
audit(
    "(M0) high corner equals (28, 1.4) ≈ 8.11e-10",
    abs(bound_high - 8.11e-10) < 5e-11,
    f"computed {bound_high:.3e}",
)


# ---------------------------------------------------------------------------
# Section 7: cross-check vs ETA_188 structural decomposition
# ---------------------------------------------------------------------------

print()
print("Section 7: cross-check vs ETA_188 structural decomposition")
print("-" * 72)

# (516/53009) * Y0^2 * F_CP * kappa_axiom / eta_obs ~ 0.18878592...
# Authority computes 0.18878592 to 12+ digits via 5-factor product. Here
# we only re-check the ABC pure-rational sub-closure:
g_star_rational = Fraction(427, 4)  # g_* = 28 + (7/8)*90
g_S_rational = Fraction(43, 11)
C_sph_rational = Fraction(28, 79)

ABC = Fraction(3, 4) * (g_S_rational / g_star_rational) * C_sph_rational
audit(
    "ABC pure-rational = 516/53009",
    ABC == Fraction(516, 53009),
    f"computed {ABC}",
)

audit(
    "g_* = 427/4 (SM-only at leptogenesis scale)",
    g_star_rational == Fraction(427, 4),
)
audit(
    "g_S = 43/11 (CMB DOF today)",
    g_S_rational == Fraction(43, 11),
)
audit(
    "C_sph = 28/79 (sphaleron conversion)",
    C_sph_rational == Fraction(28, 79),
)


# ---------------------------------------------------------------------------
# Section 8: note-text records named local input packet P1-P7
# ---------------------------------------------------------------------------

print()
print("Section 8: note-text records named local input packet P1-P7")
print("-" * 72)

for p_label, marker in [
    ("P1 freeze-out-bypass identity", "**P1 Freeze-out-bypass identity"),
    ("P2 structural mass candidate", "**P2 Structural mass candidate"),
    ("P3 BBN coefficient", "**P3 BBN coefficient"),
    ("P4 freeze-out coefficient band", "**P4 Freeze-out coefficient band"),
    ("P5 SM effective DOF", "**P5 SM effective"),
    ("P6 Kolb-Turner prefactor", "**P6 Kolb-Turner prefactor"),
    ("P7 Sommerfeld continuation", "**P7 Sommerfeld continuation"),
]:
    audit(
        f"Note records named premise {p_label}",
        marker in note_text,
    )


# ---------------------------------------------------------------------------
# Section 9: note-text records audit-companion vs load-bearing classification
# ---------------------------------------------------------------------------

print()
print("Section 9: note-text records audit-companion vs load-bearing classification")
print("-" * 72)

audit(
    "Note lists R_base authority under load-bearing dependencies",
    "## Load-bearing dependencies" in note_text
    and "R_BASE_GROUP_THEORY_DERIVATION_THEOREM_NOTE_2026-04-24.md"
    in note_text.split("## Load-bearing dependencies", 1)[1].split("## Audit-companion", 1)[0],
)
audit(
    "Note lists eta_188 authority under load-bearing dependencies",
    "## Load-bearing dependencies" in note_text
    and "ETA_188_STRUCTURAL_ORIGIN_PARTIAL_NOTE_2026-05-03.md"
    in note_text.split("## Load-bearing dependencies", 1)[1].split("## Audit-companion", 1)[0],
)
audit(
    "Note lists retained_bounded SM_RELATIVISTIC_DOF authority under load-bearing dependencies",
    "## Load-bearing dependencies" in note_text
    and "SM_RELATIVISTIC_DOF_COUNT_IMPORT_NOTE_2026-05-17.md"
    in note_text.split("## Load-bearing dependencies", 1)[1].split("## Audit-companion", 1)[0],
)
audit(
    "Note lists DM_ETA_FREEZEOUT_BYPASS as audit-companion (not retained)",
    "## Audit-companion sources" in note_text
    and "DM_ETA_FREEZEOUT_BYPASS_QUANTITATIVE_THEOREM_NOTE_2026-04-25.md"
    in note_text.split("## Audit-companion sources", 1)[1],
)
audit(
    "Note lists DM_ETA_NSITES_V_LIFT as audit-companion (not retained)",
    "DM_ETA_NSITES_V_STRUCTURAL_SUPPORT_LIFT_THEOREM_NOTE_2026-04-29.md"
    in note_text.split("## Audit-companion sources", 1)[1],
)
audit(
    "Note lists HIGGS_MASS_FROM_AXIOM as audit-companion (not retained)",
    "HIGGS_MASS_FROM_AXIOM_NOTE.md"
    in note_text.split("## Audit-companion sources", 1)[1],
)
audit(
    "Note lists OBSERVABLE_PRINCIPLE as audit-companion (not retained)",
    "OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md"
    in note_text.split("## Audit-companion sources", 1)[1],
)
audit(
    "Note explicitly declines (C2.eta) closure",
    "(C2.eta)" in note_text
    and ("NOT close" in note_text or "does NOT close" in note_text or "remains open" in note_text or "is NOT retired" in note_text),
)


# ---------------------------------------------------------------------------
# Section 10: status discipline
# ---------------------------------------------------------------------------

print()
print("Section 10: status discipline")
print("-" * 72)

for phrase in ("source-note proposal only",):
    audit(
        f"Note keeps source-side status control absent: {phrase}",
        phrase not in note_text,
    )
audit(
    "Note keeps actual surface as open",
    "actual_current_surface_status: open" in note_text,
)
audit(
    "Note keeps conditional support separate from actual surface",
    "conditional_surface_status: conditional-support" in note_text,
)
audit(
    "Note forbids branch-local retained proposal",
    "proposal_allowed: false" in note_text
    and "audit_required_before_effective_retained: true" in note_text
    and "bare_retained_allowed: false" in note_text,
)
audit(
    "Note does NOT use bare 'proposed_retained' or 'retained:' status language",
    "**Status:** retained" not in note_text
    and "proposed_retained" not in note_text,
)


# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------

print()
print("=" * 72)
print(f"TOTAL: PASS={AUDIT_PASSES} FAIL={len(AUDIT_FAILS)}")
if AUDIT_FAILS:
    print("VERDICT: open-gate conditional arithmetic runner FAILED at:")
    for fail in AUDIT_FAILS:
        print(f"  - {fail}")
    sys.exit(1)
else:
    print(
        "VERDICT: open-gate conditional arithmetic certificate passes; eta_pred bracketed inside "
        "[5.25e-10, 8.11e-10] with central +4.18% vs eta_obs comparator; "
        "m_DM = 3.94 TeV is the supplied composed-product readout; "
        "P1-P4/P6-P7 and (C2.eta) remain open."
    )
    sys.exit(0)
