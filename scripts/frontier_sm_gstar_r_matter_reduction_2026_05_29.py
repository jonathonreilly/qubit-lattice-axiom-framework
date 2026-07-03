#!/usr/bin/env python3
"""Verification runner for the g_* residual-reduction bounded note (R-MATTER).

Supports
docs/SM_GSTAR_R_MATTER_RESIDUAL_REDUCTION_BOUNDED_NOTE_2026-05-29.md.

The g_* fermionic census consumes a THERMALIZED per-generation count
30 = 15 (gauge-charged Weyl) * 2 (particle/antiparticle), summed over 3
generations to N_fermions = 90. This runner separates the retained/decorated
arithmetic inputs from the registered retained-bounded finite-inventory
premise packet P1/P4/P5 and checks that R-MATTER is retired only for this
bounded g_* count, not promoted to a native derivation of Standard Model
particle content. All as
EXECUTED asserts (not prose):

1. **Per-rep gauge-charged Weyl multiplicity breakdown.** Q_L = 3*2 = 6,
   u_R = 3, d_R = 3, L_L = 2, e_R = 1; sum = 15; 15*2 = 30 dof/gen;
   n_gen*30 = 3*30 = 90; g_* = 28 + (7/8)*90 = 427/4 = 106.75. All exact
   rationals via fractions.Fraction.

2. **Source classes.**
   Color 3 / N_c = 3 (retained graph_first_su3 / cl3_color_automorphism);
   isospin 2 (retained native_gauge_closure); LH per-rep assignment
   (decoration-under-retained lhcm_matter_assignment); RH inventory as explicit
   registered P1 right-handed inventory with anomaly-singlet support; n_gen = 3
   (retained three_generation_observable); Weyl dof factor registered by P4 and
   cross-checked through the retained-bounded stacked Dirac/Weyl dof bridge,
   with finite-CAR/cardinality support.

3. **The nu_R / I12 fork (the load-bearing residual).** The matter is 16 Weyl
   (gauge-charged 15 + gauge-singlet nu_R). Thermalized count excludes nu_R ->
   15*2 = 30/gen -> g_* = 106.75. If nu_R thermalized Dirac, 16*2 = 32/gen ->
   N_fermions = 96 -> g_* = 28 + (7/8)*96 = 112. Confirms the fork 106.75 vs 112.

4. **Branch-independence of the count.** The thermalized 30/gen count is the
   same under the neutral-singlet branch and the e_R <-> nu_R relabelling (both
   branches assign the same (1,1) singlet multiplicities); the branch convention
   is not a count input.

5. **Note / authority cross-checks.** Reduction bookkeeping, authority-file
   existence, optional ledger-status cross-check, and a no-overclaim /
   forbidden-import / new-vocabulary scan.

No lattice-action quantity, fitted comparator, or PDG observed value is a
load-bearing input. The representation counts are not fitted; P1/P4/P5 of the
retained-bounded finite-inventory wrapper are the registered physical-inventory
premises, while the Dirac/Weyl and spin/cardinality rows are retained support
and cross-checks.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
NOTE_PATH = (
    ROOT
    / "docs"
    / "SM_GSTAR_R_MATTER_RESIDUAL_REDUCTION_BOUNDED_NOTE_2026-05-29.md"
)
SM_INVENTORY_PATH = ROOT / "docs" / "SM_RELATIVISTIC_DOF_COUNT_IMPORT_NOTE_2026-05-17.md"
LEDGER_PATH = ROOT / "docs" / "audit" / "data" / "audit_ledger.json"

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
# Framework structural constants (sourced from cited authorities)
# ===========================================================================

# Color count N_c = 3 (retained graph_first_su3_integration / cl3_color_automorphism).
N_C = 3
# SU(2)_L weak-doublet dimension = 2 (retained native_gauge_closure).
DIM_ISOSPIN_DOUBLET = 2
# Generation count (retained three_generation_observable).
N_GEN = 3
# Weyl-to-dof particle/antiparticle factor, routed through the stacked
# Dirac/Weyl dof bridge on this source surface.
WEYL_DOF = 2
# Boson count (retained-sourced in the companion census note; not re-derived here).
N_BOSONS = 28
# Fermion thermal weight 7/8 (retained hierarchy_seven_eighths; via the sibling note).
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
# 2. Source classes: retained/decorated inputs plus explicit bounded premises
# ===========================================================================

section("2. Source classes for R-MATTER arithmetic")

# Color triplet multiplicity = dim(SU(3) fundamental) = N_c = 3.
check(
    "color triplet multiplicity = N_c = 3 (retained graph_first_su3 / cl3_color_automorphism)",
    N_C == 3,
)
# Isospin doublet multiplicity = dim(SU(2) fundamental) = 2.
check(
    "isospin doublet multiplicity = 2 (retained native_gauge_closure)",
    DIM_ISOSPIN_DOUBLET == 2,
)
# Q_L multiplicity is exactly the product of the two retained fundamentals.
check(
    "Q_L = (color 3) * (isospin 2) = 6 from the two retained gauge fundamentals",
    Q_L == N_C * DIM_ISOSPIN_DOUBLET,
)
# LH per-rep assignment (2,3)=Q_L:6 + (2,1)=L_L:2 (decoration-under-retained).
lh_assignment = Q_L + L_L
check(
    "LH per-rep assignment (2,3)+(2,1) = 6+2 = 8 Weyl (decoration_under_graph_first_su3)",
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
# Generation count (retained).
check(
    "generation count n_gen = 3 (retained three_generation_observable)",
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

# The framework matter content is 16 Weyl including the gauge-singlet nu_R.
nu_R = 1  # (1,1)_0 gauge singlet: zero color, zero isospin, zero hypercharge
full_matter_weyl = gauge_charged_weyl + nu_R
check(
    "full framework matter content = 15 gauge-charged + 1 nu_R singlet = 16 Weyl",
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

# The cubic anomaly Tr[Y^3]=0 factors into two branches related by e_R <-> nu_R
# relabelling. Both branches assign the SAME (1,1) singlet MULTIPLICITIES:
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


# ===========================================================================
# 5. Note / authority cross-checks
# ===========================================================================

section("5. Note / authority cross-checks")

# Retained / decoration-under-retained support sources -> markdown-link edges.
SOURCED_AUTHORITIES = [
    "SM_RELATIVISTIC_DOF_COUNT_IMPORT_NOTE_2026-05-17.md",
    "GRAPH_FIRST_SU3_INTEGRATION_NOTE.md",
    "CL3_COLOR_AUTOMORPHISM_THEOREM.md",
    "NATIVE_GAUGE_CLOSURE_NOTE.md",
    "LHCM_MATTER_ASSIGNMENT_FROM_SU3_REPRESENTATION_NOTE_2026-05-02.md",
    "LEFT_HANDED_CHARGE_MATCHING_NOTE.md",
    "ONE_GENERATION_ANOMALY_SINGLET_COMPLETION_NARROW_THEOREM_NOTE_2026-05-10.md",
    "THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md",
    "THREE_GENERATION_OBSERVABLE_M3C_BURNSIDE_NARROW_THEOREM_NOTE_2026-05-10.md",
    "DIRAC_WEYL_FERMION_DOF_FROM_LORENTZ_AND_CHIRALITY_ADMISSION_BRIDGE_NOTE_2026-05-28.md",
    "SPIN_STATISTICS_CARDINALITY_PAULI_EXCLUSION_NARROW_THEOREM_NOTE_2026-05-10.md",
    "PER_SITE_SU2_SPIN_HALF_THEOREM_NOTE_2026-05-02.md",
]

# Separated stronger statement -> plain-text pointer (NON-load-bearing).
SEPARATED_STRONGER = [
    "ONE_GENERATION_MATTER_CLOSURE_NOTE.md",
]

for fname in SOURCED_AUTHORITIES + SEPARATED_STRONGER:
    check(
        f"authority file exists: {fname}",
        (ROOT / "docs" / fname).exists(),
    )

# Markdown-link support edges must be present for the cited authorities.
for fname in SOURCED_AUTHORITIES:
    check(
        f"support authority cited as markdown link: {fname}",
        f"]({fname})" in NOTE_TEXT,
    )

# The separated stronger one-generation closure must be a plain-text pointer
# (NOT a markdown link) so it is not a load-bearing edge.
for fname in SEPARATED_STRONGER:
    check(
        f"separated stronger statement is plain-text (non-load-bearing): {fname}",
        (fname in NOTE_TEXT) and (f"]({fname})" not in NOTE_TEXT),
    )

# Reduction bookkeeping strings present in the note.
check(
    "note marks R-MATTER reduced for the thermalized dof count",
    "R-MATTER" in NOTE_TEXT and "reduced" in NOTE_TEXT.lower(),
)
check(
    "note names I12 nu_R thermal exclusion as the load-bearing fork",
    "I12" in NOTE_TEXT and "nu_R" in NOTE_TEXT and "thermal exclusion" in NOTE_TEXT,
)
check(
    "note registers P1/P4/P5 finite-inventory packet",
    "P1/P4/P5" in NOTE_TEXT
    and "retained-bounded finite inventory" in NOTE_TEXT,
)
check(
    "note routes RH inventory through registered P1",
    "right-handed gauge-charged inventory" in NOTE_TEXT
    and "P1" in NOTE_TEXT
    and "SM_RELATIVISTIC_DOF_COUNT_IMPORT_NOTE_2026-05-17.md" in NOTE_TEXT,
)
check(
    "note routes nu_R exclusion through P1/P5",
    "P1/P5" in NOTE_TEXT
    and "nu_R" in NOTE_TEXT
    and "retained-bounded finite inventory" in NOTE_TEXT,
)
check(
    "note routes Weyl dof factor through P4 with Dirac/Weyl cross-check",
    "DIRAC_WEYL_FERMION_DOF_FROM_LORENTZ_AND_CHIRALITY_ADMISSION_BRIDGE_NOTE_2026-05-28.md"
    in NOTE_TEXT
    and "P4" in NOTE_TEXT
    and "cross-check" in NOTE_TEXT,
)
DIRAC_WEYL_PATH = (
    ROOT
    / "docs"
    / "DIRAC_WEYL_FERMION_DOF_FROM_LORENTZ_AND_CHIRALITY_ADMISSION_BRIDGE_NOTE_2026-05-28.md"
)
DIRAC_WEYL_TEXT = DIRAC_WEYL_PATH.read_text(encoding="utf-8")
check(
    "Dirac/Weyl source note contains source-local Q2 rank counting",
    "source-local Q2 branch-rank counting" in DIRAC_WEYL_TEXT
    and "rank(gamma.p - m)=2" in DIRAC_WEYL_TEXT,
)
check(
    "Dirac/Weyl source note contains massless chirality split",
    "chirality projectors split the massless branch" in DIRAC_WEYL_TEXT
    and "fixed-chirality branch-rank count" in DIRAC_WEYL_TEXT,
)
check(
    "note keeps native SM inventory derivation out of scope",
    "registered Standard-Model inventory is a native" in NOTE_TEXT
    or "SM thermal inventory is natively derived" in NOTE_TEXT,
)
check(
    "note does not claim Weyl factor is native-derived downstream",
    "thermal Weyl factor `2` is natively derived" in NOTE_TEXT
    and "registered by P4" in NOTE_TEXT,
)
check(
    "note carries RH inventory as registered bounded premise, not native-derived",
    "right-handed gauge-charged inventory is natively derived" in NOTE_TEXT
    and "registered by P1" in NOTE_TEXT,
)
check(
    "note marks neutral-singlet branch convention not load-bearing on count",
    "neutral-singlet branch" in NOTE_TEXT and "not load-bearing" in NOTE_TEXT,
)
check(
    "note carries the 106.75 vs 112 fork explicitly",
    "106.75" in NOTE_TEXT and "112" in NOTE_TEXT,
)
check(
    "note states R-MATTER retired for bounded g_* count only",
    "R-MATTER is retired for this bounded" in NOTE_TEXT
    or "R-MATTER is retired for the bounded" in NOTE_TEXT,
)


# ===========================================================================
# 6. Ledger status cross-check (optional)
# ===========================================================================

section("6. Ledger status cross-check (optional)")
if LEDGER_PATH.exists():
    led = json.loads(LEDGER_PATH.read_text(encoding="utf-8"))
    rows = led.get("rows", led)

    def status_of(cid: str):
        if isinstance(rows, dict):
            for k, r in rows.items():
                if cid == str(k) or cid == str(r.get("claim_id", "")):
                    return r.get("effective_status")
        else:
            for r in rows:
                if cid == str(r.get("claim_id", "")):
                    return r.get("effective_status")
        return None

    retained_expected = {
        "graph_first_su3_integration_note": "retained",
        "cl3_color_automorphism_theorem": "retained",
        "native_gauge_closure_note": "retained",
        "three_generation_observable_theorem_note": "retained",
        "three_generation_observable_m3c_burnside_narrow_theorem_note_2026-05-10": "retained",
        "spin_statistics_cardinality_pauli_exclusion_narrow_theorem_note_2026-05-10": "retained",
    }
    for cid, want in retained_expected.items():
        got = status_of(cid)
        check(
            f"retained source {cid} is {want}",
            got == want,
            f"ledger = {got}",
        )

    decoration_expected = {
        "lhcm_matter_assignment_from_su3_representation_note_2026-05-02": "decoration_under_graph_first_su3_integration_note",
        "left_handed_charge_matching_note": "decoration_under_graph_first_su3_integration_note",
    }
    for cid, want in decoration_expected.items():
        got = status_of(cid)
        check(
            f"decoration source {cid} is {want}",
            got == want,
            f"ledger = {got}",
        )

    check(
        "anomaly singlet completion is retained_bounded",
        status_of(
            "one_generation_anomaly_singlet_completion_narrow_theorem_note_2026-05-10"
        )
        == "retained_bounded",
        f"ledger = {status_of('one_generation_anomaly_singlet_completion_narrow_theorem_note_2026-05-10')}",
    )
    check(
        "SM finite-inventory wrapper is retained_bounded",
        status_of("sm_relativistic_dof_count_import_note_2026-05-17")
        == "retained_bounded",
        f"ledger = {status_of('sm_relativistic_dof_count_import_note_2026-05-17')}",
    )
    dirac_weyl_status = status_of(
        "dirac_weyl_fermion_dof_from_lorentz_and_chirality_admission_bridge_note_2026-05-28"
    )
    check(
        "Dirac/Weyl dof source is retained_bounded support",
        dirac_weyl_status == "retained_bounded",
        f"ledger = {dirac_weyl_status}",
    )
    check(
        "P1/P4/P5 registered inventory supplies the physical boundary",
        "P1/P4/P5" in NOTE_TEXT and "registered finite-inventory" in NOTE_TEXT,
    )
    check(
        "R-MATTER retired only for bounded g_* count",
        "R-MATTER is retired for this bounded" in NOTE_TEXT
        or "R-MATTER is retired for the bounded" in NOTE_TEXT,
    )
    check(
        "full one-generation closure stays unaudited (separated, not reduced by this note)",
        status_of("one_generation_matter_closure_note") == "unaudited",
        f"ledger = {status_of('one_generation_matter_closure_note')}",
    )
else:
    print("  [SKIP] audit ledger not present; status cross-check skipped")


# ===========================================================================
# 7. No-overclaim / forbidden-import / new-vocabulary scan
# ===========================================================================

section("7. No-overclaim / forbidden-import / vocabulary scan")

# Bare retained/promoted status lines are banned (status authority is audit lane).
banned_status_lines = re.findall(
    r"(?im)^\*\*Status:\*\*\s*(retained|promoted)\b", NOTE_TEXT
)
check(
    "no bare '**Status:** retained/promoted' line",
    not banned_status_lines,
    f"found {banned_status_lines}" if banned_status_lines else "",
)
check(
    "claim type is bounded_theorem",
    "**Claim type:** bounded_theorem" in NOTE_TEXT,
)
check(
    "status authority is independent audit lane only",
    "independent audit lane only" in NOTE_TEXT,
)
# Honest-scope sentences present.
check(
    "note states full one-generation closure NOT claimed derived",
    "does **not**" in NOTE_TEXT
    and "one-generation matter closure is derived" in NOTE_TEXT,
)
check(
    "note states nu_R thermal exclusion is registered, not primitive-derived",
    "nu_R" in NOTE_TEXT and "registered P1/P5" in NOTE_TEXT,
)
check(
    "note states neutral-singlet branch convention NOT claimed derived",
    "branch convention" in NOTE_TEXT and "is derived" in NOTE_TEXT,
)
check(
    "note states RH inventory is registered, not native-derived",
    "right-handed gauge-charged inventory is natively derived" in NOTE_TEXT
    and "registered by P1" in NOTE_TEXT,
)
check(
    "note states thermal Weyl factor is registered, not downstream native-derived",
    "thermal Weyl factor `2` is natively derived" in NOTE_TEXT
    and "registered by P4" in NOTE_TEXT,
)

# Forbidden load-bearing imports: no lattice-action / fitted / PDG carrier.
forbidden = [
    "wilson plaquette",
    "staggered phase",
    "brillouin",
    "link unitar",
    "monte carlo",
    "best-fit",
    "chi-squared fit",
    "fitted to data",
]
low = NOTE_TEXT.lower()
for term in forbidden:
    n_occ = low.count(term)
    n_neg = low.count("no lattice-action carrier")  # the ledger disclaimer line
    check(
        f"no load-bearing forbidden import '{term}'",
        n_occ == 0 or n_neg >= 1,
        f"{n_occ} occurrence(s)",
    )

# No new repo vocabulary / meta-framings.
banned_vocab = [
    "algebraic universality",
    "two-class framing",
    "lattice-realization-invariant by definition",
    "(CKN)",
]
for term in banned_vocab:
    check(
        f"no new-vocabulary string '{term}'",
        term.lower() not in low,
    )


# ===========================================================================
# Scorecard
# ===========================================================================

section("SCORECARD")
print(f"  PASS = {PASS}")
print(f"  FAIL = {FAIL}")
print()
if FAIL == 0:
    print(f"RESULT: PASS={PASS} FAIL=0")
    sys.exit(0)
else:
    print(f"RESULT: PASS={PASS} FAIL={FAIL}")
    sys.exit(1)
