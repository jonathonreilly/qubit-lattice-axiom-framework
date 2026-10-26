#!/usr/bin/env python3
"""Conditional supplied-inventory arithmetic and finite counterfactuals.

No retained status or native physical inventory derivation is established.
The Dirac comparison is to supplied finite complex-matrix fixtures, not a
physical thermal count theorem. All original arithmetic predicates remain.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ['docs/SM_GSTAR_R_MATTER_RESIDUAL_REDUCTION_BOUNDED_NOTE_2026-05-29.md', 'docs/SM_RELATIVISTIC_DOF_COUNT_IMPORT_NOTE_2026-05-17.md', 'docs/GRAPH_FIRST_SU3_INTEGRATION_NOTE.md', 'docs/CL3_COLOR_AUTOMORPHISM_THEOREM.md', 'docs/NATIVE_GAUGE_CLOSURE_NOTE.md', 'docs/LHCM_MATTER_ASSIGNMENT_FROM_SU3_REPRESENTATION_NOTE_2026-05-02.md', 'docs/LEFT_HANDED_CHARGE_MATCHING_NOTE.md', 'docs/ONE_GENERATION_ANOMALY_SINGLET_COMPLETION_NARROW_THEOREM_NOTE_2026-05-10.md', 'docs/THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md', 'docs/THREE_GENERATION_OBSERVABLE_M3C_BURNSIDE_NARROW_THEOREM_NOTE_2026-05-10.md', 'docs/DIRAC_WEYL_FERMION_DOF_FROM_LORENTZ_AND_CHIRALITY_ADMISSION_BRIDGE_NOTE_2026-05-28.md', 'docs/SPIN_STATISTICS_CARDINALITY_PAULI_EXCLUSION_NARROW_THEOREM_NOTE_2026-05-10.md', 'docs/PER_SITE_SU2_SPIN_HALF_THEOREM_NOTE_2026-05-02.md', 'docs/ONE_GENERATION_MATTER_CLOSURE_NOTE.md']

from fractions import Fraction
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
NOTE_PATH = (
    ROOT
    / "docs"
    / "SM_GSTAR_R_MATTER_RESIDUAL_REDUCTION_BOUNDED_NOTE_2026-05-29.md"
)
SM_INVENTORY_PATH = ROOT / "docs" / "SM_RELATIVISTIC_DOF_COUNT_IMPORT_NOTE_2026-05-17.md"

PASS = 0
FAIL = 0


def check(name: str, ok: bool, detail: str = "") -> bool:
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    tag = "PASS" if ok else "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"  [{tag}] {name}{suffix}")
    return ok


def section(title: str) -> None:
    print()
    print("-" * 88)
    print(title)
    print("-" * 88)


NOTE_TEXT = NOTE_PATH.read_text(encoding="utf-8")
NOTE_FLAT = re.sub(r"\s+", " ", NOTE_TEXT)
SM_INVENTORY_TEXT = SM_INVENTORY_PATH.read_text(encoding="utf-8")


# ===========================================================================
# Supplied constants for the conditional arithmetic
# ===========================================================================

# Color count N_c = 3 (supplied color dimension).
N_C = 3
# SU(2)_L weak-doublet dimension = 2 (supplied dimension=2).
DIM_ISOSPIN_DOUBLET = 2
# Generation count (supplied generation count).
N_GEN = 3
# Weyl-to-dof particle/antiparticle factor, supplied by P4, not derived from finite Dirac/Weyl fixtures.
WEYL_DOF = 2
# Boson count (supplied total; no boson derivation here).
N_BOSONS = 28
# Fermion thermal weight 7/8 (supplied thermal weight).
W_F = Fraction(7, 8)


# ===========================================================================
# 1. Per-rep gauge-charged Weyl multiplicity breakdown
# ===========================================================================

section("1. Per-rep gauge-charged Weyl multiplicity breakdown")

# Gauge-charged left-handed + right-handed Weyl content per generation.
# Each entry: (rep (SU(3),SU(2)), Weyl multiplicity = product of rep dims).
Q_L = N_C * DIM_ISOSPIN_DOUBLET   # (3,2): color triplet x isospin doublet
u_R = N_C                          # (3,1)-conj: color triplet, isospin singlet
d_R = N_C                          # (3,1)-conj: color triplet, isospin singlet
L_L = DIM_ISOSPIN_DOUBLET          # (1,2): color singlet x isospin doublet
e_R = 1                            # (1,1): color singlet, isospin singlet

check("Q_L (3,2) Weyl multiplicity = N_c * 2 = 6", Q_L == 6, f"{Q_L}")
check("u_R (3,1) Weyl multiplicity = N_c = 3", u_R == 3, f"{u_R}")
check("d_R (3,1) Weyl multiplicity = N_c = 3", d_R == 3, f"{d_R}")
check("L_L (1,2) Weyl multiplicity = 2", L_L == 2, f"{L_L}")
check("e_R (1,1) Weyl multiplicity = 1", e_R == 1, f"{e_R}")

gauge_charged_weyl = Q_L + u_R + d_R + L_L + e_R
check(
    "gauge-charged Weyl per generation = 6+3+3+2+1 = 15",
    gauge_charged_weyl == 15,
    f"{gauge_charged_weyl}",
)

per_gen_dof = gauge_charged_weyl * WEYL_DOF
check(
    "per-generation thermalized dof = 15 * 2 = 30",
    per_gen_dof == 30,
    f"{per_gen_dof}",
)

n_fermions = N_GEN * per_gen_dof
check(
    "N_fermions = n_gen * 30 = 3 * 30 = 90",
    n_fermions == 90,
    f"{n_fermions}",
)

g_star = N_BOSONS + W_F * n_fermions
check(
    "g_* = 28 + (7/8) * 90 = 427/4 = 106.75",
    g_star == Fraction(427, 4) and float(g_star) == 106.75,
    f"{g_star} = {float(g_star)}",
)

# Colored vs uncolored gauge-charged Weyl decomposition (cross-check).
colored_weyl = Q_L + u_R + d_R     # 6 + 3 + 3 = 12
uncolored_charged_weyl = L_L + e_R  # 2 + 1 = 3
check(
    "colored gauge-charged Weyl = Q_L + u_R + d_R = 12",
    colored_weyl == 12,
    f"{colored_weyl}",
)
check(
    "uncolored gauge-charged Weyl = L_L + e_R = 3",
    uncolored_charged_weyl == 3,
    f"{uncolored_charged_weyl}",
)
check(
    "colored + uncolored = 15 gauge-charged Weyl",
    colored_weyl + uncolored_charged_weyl == gauge_charged_weyl,
)


# ===========================================================================
# 2. Source classes: supplied inputs and explicit inventory premises
# ===========================================================================

section("2. Source classes for R-MATTER arithmetic")

# Color triplet multiplicity = dim(SU(3) fundamental) = N_c = 3.
check(
    "color triplet multiplicity = N_c = 3 (supplied N_c=3)",
    N_C == 3,
)
# Isospin doublet multiplicity = dim(SU(2) fundamental) = 2.
check(
    "isospin doublet multiplicity = 2 (supplied dimension=2)",
    DIM_ISOSPIN_DOUBLET == 2,
)
# Q_L multiplicity is exactly the product of the two supplied dimensions.
check(
    "Q_L = (color 3) * (isospin 2) = 6 from the two supplied dimensions",
    Q_L == N_C * DIM_ISOSPIN_DOUBLET,
)
# LH per-rep assignment (2,3)=Q_L:6 + (2,1)=L_L:2 (supplied split).
lh_assignment = Q_L + L_L
check(
    "LH per-rep assignment (2,3)+(2,1) = 6+2 = 8 Weyl (supplied representation list)",
    lh_assignment == 8,
    f"{lh_assignment}",
)
# RH gauge-charged completion u_R:3 + d_R:3 + e_R:1 = 7.
# This is the registered P1 bounded inventory premise, with anomaly-singlet support.
rh_completion = u_R + d_R + e_R
check(
    "RH gauge-charged completion u_R+d_R+e_R = 3+3+1 = 7 (registered P1 inventory)",
    rh_completion == 7,
    f"{rh_completion}",
)
check(
    "LH(8) + RH(7) = 15 gauge-charged Weyl",
    lh_assignment + rh_completion == gauge_charged_weyl,
)
# Generation count (supplied).
check(
    "generation count n_gen = 3 (supplied generation count)",
    N_GEN == 3,
)
# Weyl-to-dof thermal factor (registered P4, Dirac/Weyl cross-check).
check(
    "Weyl-to-dof factor = 2 (registered P4 state-count convention)",
    WEYL_DOF == 2,
)


# ===========================================================================
# 3. The nu_R / I12 fork (the load-bearing residual): 106.75 vs 112
# ===========================================================================

section("3. nu_R / I12 fork (106.75 vs 112)")

# The supplied counterfactual inventory is 16 Weyl including the gauge-singlet nu_R.
nu_R = 1  # (1,1)_0 gauge singlet: zero color, zero isospin, zero hypercharge
full_matter_weyl = gauge_charged_weyl + nu_R
check(
    "supplied extended inventory = 15 gauge-charged + 1 nu_R singlet = 16 Weyl",
    full_matter_weyl == 16,
    f"{full_matter_weyl}",
)

# Thermalized count EXCLUDES nu_R (gauge singlet need not thermalize): 15 * 2 = 30 -> 106.75.
check(
    "thermalized (nu_R excluded): 15 Weyl * 2 = 30/gen",
    gauge_charged_weyl * WEYL_DOF == 30,
)
g_star_excluded = N_BOSONS + W_F * (N_GEN * gauge_charged_weyl * WEYL_DOF)
check(
    "thermalized (nu_R excluded): g_* = 106.75",
    g_star_excluded == Fraction(427, 4),
    f"{g_star_excluded} = {float(g_star_excluded)}",
)

# Counterfactual: nu_R thermalized Dirac -> 16 * 2 = 32/gen -> 96 -> g_* = 112.
per_gen_dirac = full_matter_weyl * WEYL_DOF
n_fermions_dirac = N_GEN * per_gen_dirac
g_star_dirac = N_BOSONS + W_F * n_fermions_dirac
check(
    "counterfactual nu_R thermalized Dirac: 16 Weyl * 2 = 32/gen",
    per_gen_dirac == 32,
    f"{per_gen_dirac}",
)
check(
    "counterfactual nu_R thermalized Dirac: N_fermions = 3 * 32 = 96",
    n_fermions_dirac == 96,
    f"{n_fermions_dirac}",
)
check(
    "counterfactual nu_R thermalized Dirac: g_* = 28 + (7/8)*96 = 112",
    g_star_dirac == Fraction(112),
    f"{g_star_dirac} = {float(g_star_dirac)}",
)
check(
    "I12 fork is load-bearing: 106.75 (excluded) != 112 (thermalized)",
    g_star_excluded != g_star_dirac,
    f"{float(g_star_excluded)} vs {float(g_star_dirac)}",
)
# The fork difference is exactly the nu_R contribution: 3 gens * 2 dof * (7/8).
fork_delta = g_star_dirac - g_star_excluded
check(
    "fork delta = n_gen * (nu_R Weyl) * 2 * 7/8 = 3 * 1 * 2 * 7/8 = 21/4 = 5.25",
    fork_delta == Fraction(21, 4) and float(fork_delta) == 5.25,
    f"{fork_delta} = {float(fork_delta)}",
)


# ===========================================================================
# 4. Branch-independence of the thermalized count
# ===========================================================================

section("4. Neutral-singlet branch-independence of the count")

# Supply the two inventory branches related by e_R <-> nu_R; this section
# does not prove a factorization or completeness theorem for anomaly solutions.
# Both supplied branches assign the SAME (1,1) singlet MULTIPLICITIES:
# one charged singlet (e_R-like, gauge-charged) and one neutral singlet (nu_R-like,
# gauge singlet). The branch only relabels WHICH singlet is e_R vs nu_R; the
# gauge-charged count is the same.
#
# Branch NEUTRAL (SM convention, Y(nu_R)=0): charged singlet e_R counted, nu_R excluded.
charged_singlet_neutral_branch = 1   # e_R gauge-charged
neutral_singlet_neutral_branch = 1   # nu_R gauge singlet (excluded)
gauge_charged_neutral_branch = (
    Q_L + u_R + d_R + L_L + charged_singlet_neutral_branch
)
# Branch SWAPPED (e_R <-> nu_R relabelling): the OTHER singlet is the gauge-charged one.
charged_singlet_swapped_branch = 1   # still exactly one gauge-charged singlet
neutral_singlet_swapped_branch = 1   # still exactly one gauge-singlet
gauge_charged_swapped_branch = (
    Q_L + u_R + d_R + L_L + charged_singlet_swapped_branch
)
check(
    "neutral-singlet branch: gauge-charged Weyl count = 15",
    gauge_charged_neutral_branch == 15,
    f"{gauge_charged_neutral_branch}",
)
check(
    "e_R<->nu_R swapped branch: gauge-charged Weyl count = 15 (same)",
    gauge_charged_swapped_branch == 15,
    f"{gauge_charged_swapped_branch}",
)
check(
    "thermalized count is branch-independent (both give 30/gen)",
    gauge_charged_neutral_branch * WEYL_DOF
    == gauge_charged_swapped_branch * WEYL_DOF
    == 30,
)
check(
    "each branch has exactly one charged + one neutral (1,1) singlet (same multiplicities)",
    charged_singlet_neutral_branch == charged_singlet_swapped_branch == 1
    and neutral_singlet_neutral_branch == neutral_singlet_swapped_branch == 1,
)


# Documentary comparisons, not proof or status checks.
DIRAC_WEYL_PATH = ROOT / "docs" / "DIRAC_WEYL_FERMION_DOF_FROM_LORENTZ_AND_CHIRALITY_ADMISSION_BRIDGE_NOTE_2026-05-28.md"
DIRAC_WEYL_TEXT = DIRAC_WEYL_PATH.read_text(encoding="utf-8")
check("Dirac comparison explicitly concerns finite supplied complex fixtures",
      "supplied complex matrices" in DIRAC_WEYL_TEXT and "finite fixtures" in DIRAC_WEYL_TEXT)
check("Dirac physical identification and ledger authority remain withdrawn",
      "physical identification remains open" in DIRAC_WEYL_TEXT
      and "no current ledger authority" in DIRAC_WEYL_TEXT)
for phrase in ["bounded_theorem", "supplied inventory", "P1/P4/P5", "106.75", "112",
               "physical state-count convention remains supplied", "no current ledger authority"]:
    check(f"documentary scope: {phrase}", phrase in NOTE_FLAT)
check("inventory source states literature-conditioned 28/90 scope (documentary only)",
      "literature-supplied inventory and thermal assumptions" in " ".join(SM_INVENTORY_TEXT.split())
      and "g_bosonic = 16 + 6 + 2 + 4 = 28" in SM_INVENTORY_TEXT
      and "g_fermionic = 72 + 12 + 6 = 90" in SM_INVENTORY_TEXT
      and "not a framework derivation of which particles nature contains" in " ".join(SM_INVENTORY_TEXT.split()))

HISTORICAL_CONTEXT_PATHS = ['docs/SM_RELATIVISTIC_DOF_COUNT_IMPORT_NOTE_2026-05-17.md', 'docs/GRAPH_FIRST_SU3_INTEGRATION_NOTE.md', 'docs/CL3_COLOR_AUTOMORPHISM_THEOREM.md', 'docs/NATIVE_GAUGE_CLOSURE_NOTE.md', 'docs/LHCM_MATTER_ASSIGNMENT_FROM_SU3_REPRESENTATION_NOTE_2026-05-02.md', 'docs/LEFT_HANDED_CHARGE_MATCHING_NOTE.md', 'docs/ONE_GENERATION_ANOMALY_SINGLET_COMPLETION_NARROW_THEOREM_NOTE_2026-05-10.md', 'docs/THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md', 'docs/THREE_GENERATION_OBSERVABLE_M3C_BURNSIDE_NARROW_THEOREM_NOTE_2026-05-10.md', 'docs/DIRAC_WEYL_FERMION_DOF_FROM_LORENTZ_AND_CHIRALITY_ADMISSION_BRIDGE_NOTE_2026-05-28.md', 'docs/SPIN_STATISTICS_CARDINALITY_PAULI_EXCLUSION_NARROW_THEOREM_NOTE_2026-05-10.md', 'docs/PER_SITE_SU2_SPIN_HALF_THEOREM_NOTE_2026-05-02.md', 'docs/ONE_GENERATION_MATTER_CLOSURE_NOTE.md']
for path in HISTORICAL_CONTEXT_PATHS:
    check(f"historical context file remains available (not authority): {path}",
          (ROOT / path).exists())
print("INFO: documentary existence and substring checks establish no mathematical or audit authority.")
print(f"RESULT: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
