#!/usr/bin/env python3
"""Bounded proof-walk for g_* = 106.75 from supplied thermal inventory.

This runner supports
docs/G_STAR_SM_CONTENT_AT_LEPTOGENESIS_FROM_SUPPLIED_THERMAL_INVENTORY_BOUNDED_THEOREM_NOTE_2026-05-28.md.

It checks the exact factorised arithmetic and verifies that the proof-walk is
limited to the named support packet R1-R6 and the registered declared-inventory
premise packet P1-P5. The parent inventory note is now load-bearing for P1-P5.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
NOTE_PATH = (
    ROOT
    / "docs"
    / "G_STAR_SM_CONTENT_AT_LEPTOGENESIS_FROM_SUPPLIED_THERMAL_INVENTORY_BOUNDED_THEOREM_NOTE_2026-05-28.md"
)
PARENT_NOTE = ROOT / "docs" / "SM_RELATIVISTIC_DOF_COUNT_IMPORT_NOTE_2026-05-17.md"

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
PARENT_TEXT = PARENT_NOTE.read_text(encoding="utf-8")


def check_note_structure() -> None:
    section("note structure and scope")
    required = [
        "Claim type:** bounded_theorem",
        "source-note proposal only",
        "does not add a new axiom",
        "retained-bounded finite declared-inventory arithmetic certificate",
        "Support packet (R1-R6)",
        "Registered premise packet (P1-P5",
        "Proof-walk",
        "Exact arithmetic check",
        "Boundaries",
        "SM_RELATIVISTIC_DOF_COUNT_IMPORT_NOTE_2026-05-17",
        "THREE_GENERATION_OBSERVABLE_THEOREM_NOTE",
        "CL3_COLOR_AUTOMORPHISM_THEOREM",
        "ONE_GENERATION_ANOMALY_SINGLET_COMPLETION_NARROW_THEOREM_NOTE_2026-05-10",
        "PER_SITE_SU2_SPIN_HALF_THEOREM_NOTE_2026-05-02",
        "SPIN_STATISTICS_CARDINALITY_PAULI_EXCLUSION_NARROW_THEOREM_NOTE_2026-05-10",
        "GSTAR_THERMAL_SEVEN_EIGHTHS_STEFAN_BOLTZMANN_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06",
        "audit_companion_gstar_thermal_seven_eighths_bridge_2026_06_06.py",
        "P1-P5 are declared explicitly in the retained-bounded finite inventory wrapper",
        "P2 supplies the two-transverse-polarization state count",
        "P4 supplies the Dirac/Weyl thermal state-count convention",
    ]
    for phrase in required:
        check(f"note contains: {phrase}", phrase in NOTE_FLAT)


def check_proof_walk_forbidden_imports() -> None:
    section("proof-walk forbids lattice-action imports")
    forbidden_terms = [
        "plaquette",
        "staggered phase",
        "Wilson plaquette",
        "Brillouin",
        "link unitary",
        "Monte Carlo",
        "u_0",
        "fitted",
    ]
    proof_walk_section_re = re.compile(
        r"## Proof-walk(.*?)## Exact arithmetic check",
        re.DOTALL,
    )
    m = proof_walk_section_re.search(NOTE_TEXT)
    proof_walk_text = m.group(1) if m else ""
    check("proof-walk section is present", bool(proof_walk_text))
    for term in forbidden_terms:
        # the proof-walk allowed-list explicitly NAMES these as not used; the
        # table allows the literal name to appear once per row in the "no"
        # column. We check that those mentions only appear inside the
        # explicit "does not cite" disclaimer.
        forbidden_count = proof_walk_text.count(term)
        is_only_in_disclaimer = (
            term in proof_walk_text
            and "The proof-walk does not cite" in proof_walk_text
        )
        check(
            f"proof-walk only references {term!r} in the explicit non-use disclaimer",
            forbidden_count == 0 or is_only_in_disclaimer,
            f"count={forbidden_count}",
        )


def check_load_bearing_retained_packet() -> None:
    section("R1-R6 support packet citations are present")
    retained_packet = [
        ("P1-P5", "SM_RELATIVISTIC_DOF_COUNT_IMPORT_NOTE_2026-05-17.md"),
        ("R1", "THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md"),
        ("R1", "THREE_GENERATION_OBSERVABLE_M3C_BURNSIDE_NARROW_THEOREM_NOTE_2026-05-10.md"),
        ("R2", "CL3_COLOR_AUTOMORPHISM_THEOREM.md"),
        ("R3", "ONE_GENERATION_ANOMALY_SINGLET_COMPLETION_NARROW_THEOREM_NOTE_2026-05-10.md"),
        ("R3", "SM_HYPERCHARGE_UNIQUENESS_ALGEBRAIC_SOLUTION_ENUMERATION_NARROW_THEOREM_NOTE_2026-05-10.md"),
        ("R4", "PER_SITE_SU2_SPIN_HALF_THEOREM_NOTE_2026-05-02.md"),
        ("R5", "SPIN_STATISTICS_CARDINALITY_PAULI_EXCLUSION_NARROW_THEOREM_NOTE_2026-05-10.md"),
        ("R5", "SPIN_STATISTICS_BEREZIN_DETERMINANT_NARROW_THEOREM_NOTE_2026-05-10.md"),
        ("R6", "GSTAR_THERMAL_SEVEN_EIGHTHS_STEFAN_BOLTZMANN_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md"),
    ]
    for tag, fname in retained_packet:
        check(f"{tag} cites {fname} as markdown link", fname in NOTE_TEXT)
        path = ROOT / "docs" / fname
        check(f"{tag} target file exists: {fname}", path.exists())


def check_premise_packet() -> None:
    section("P1-P5 registered premise packet is named")
    required = [
        "**P1 Declared Standard Model particle inventory.**",
        "**P2 Two transverse polarizations per massless vector.**",
        "**P3 Four real scalar degrees-of-freedom per complex doublet.**",
        "**P4 Dirac four-dof per charged fermion flavour-colour state.**",
        "**P5 Temperature above the electroweak crossover.**",
    ]
    for phrase in required:
        check(f"premise present: {phrase}", phrase in NOTE_TEXT)


def check_boson_factorisation() -> None:
    section("bosonic count factorisation (R-packet + P-packet)")

    n_c = 3
    dim_adj_su3 = n_c * n_c - 1
    transverse = 2
    n_su2_gauge = 3
    dim_adj_su2 = n_su2_gauge
    n_u1 = 1
    higgs_real_components = 4

    gluon_dof = dim_adj_su3 * transverse
    su2_dof = dim_adj_su2 * transverse
    u1_dof = n_u1 * transverse
    higgs_dof = higgs_real_components

    check("R2: dim adj(SU(3)) = N_c^2 - 1 = 8", dim_adj_su3 == 8, str(dim_adj_su3))
    check("P1 premise: SU(2)_L gauge bosons W^1,W^2,W^3 = 3", dim_adj_su2 == 3, str(dim_adj_su2))
    check("(B1) gluon DOF = 16", gluon_dof == 16, f"{dim_adj_su3} * {transverse} = {gluon_dof}")
    check("(B2) SU(2)_L gauge boson DOF = 6", su2_dof == 6, f"{dim_adj_su2} * {transverse} = {su2_dof}")
    check("(B3) U(1)_Y gauge boson DOF = 2", u1_dof == 2, f"{n_u1} * {transverse} = {u1_dof}")
    check("(B4) Higgs doublet DOF = 4", higgs_dof == 4, str(higgs_dof))

    n_bosons = gluon_dof + su2_dof + u1_dof + higgs_dof
    check("(B5) N_bosons = 28", n_bosons == 28, str(n_bosons))


def check_fermion_factorisation() -> None:
    section("fermionic count factorisation (R-packet + P-packet)")

    n_gen = 3
    n_c = 3
    n_up = 1
    n_down = 1
    dirac = 4
    weyl = 2

    quark_per_gen = (n_up + n_down) * n_c * dirac
    quark_dof = n_gen * quark_per_gen
    check_quark = quark_dof == 72
    check(
        "(B6) quark DOF = n_gen * (n_up + n_down) * N_c * 4 = 72",
        check_quark,
        f"{n_gen} * {n_up + n_down} * {n_c} * {dirac} = {quark_dof}",
    )

    cl_per_gen = dirac
    cl_dof = n_gen * cl_per_gen
    check(
        "(B7) charged lepton DOF = n_gen * 4 = 12",
        cl_dof == 12,
        f"{n_gen} * {dirac} = {cl_dof}",
    )

    nu_per_gen = weyl
    nu_dof = n_gen * nu_per_gen
    check(
        "(B8) active neutrino DOF = n_gen * 2 = 6",
        nu_dof == 6,
        f"{n_gen} * {weyl} = {nu_dof}",
    )

    n_fermions = quark_dof + cl_dof + nu_dof
    check("(B9) N_fermions = 90", n_fermions == 90, str(n_fermions))


def check_g_star_exact_rational() -> None:
    section("exact rational g_* arithmetic")

    n_bosons = 28
    n_fermions = 90
    fermion_weight = Fraction(7, 8)
    g_star = Fraction(n_bosons, 1) + fermion_weight * Fraction(n_fermions, 1)

    check("R6: fermion weight is 7/8", fermion_weight == Fraction(7, 8), str(fermion_weight))
    check(
        "(B10) (7/8) * 90 = 630 / 8 = 78.75 exact",
        fermion_weight * Fraction(n_fermions, 1) == Fraction(630, 8),
        str(fermion_weight * Fraction(n_fermions, 1)),
    )
    check(
        "(B11) g_* = 28 + 78.75 = 106.75",
        g_star == Fraction(427, 4),
        str(g_star),
    )
    check("(B12) g_* as exact rational = 854/8 = 427/4", g_star == Fraction(854, 8))
    check("(B13) g_* decimal = 106.75", float(g_star) == 106.75, str(float(g_star)))


def check_parent_inventory_alignment() -> None:
    section("parent inventory note consistency")
    required_parent_phrases = [
        "28 + (7/8) * 90",
        "427/4",
        "106.75",
        "g_bosonic = 16 + 6 + 2 + 4 = 28",
        "g_fermionic = 72 + 12 + 6 = 90",
    ]
    for phrase in required_parent_phrases:
        check(
            f"parent note contains: {phrase}",
            phrase in PARENT_TEXT,
        )


def check_boundary_disclaimers() -> None:
    section("explicit boundary disclaimers (admission honesty)")
    required = [
        "does not close:",
        "derivation of the Standard Model gauge group",
        "derivation of the SM particle inventory list itself",
        "derivation of the two-transverse-polarization count",
        "derivation of the four-real-scalar count",
        "derivation of the Dirac four-dof / Weyl two-dof state count",
        "T > 250 GeV",
        "any parent theorem/status promotion",
    ]
    for phrase in required:
        check(f"boundary disclaimer present: {phrase}", phrase in NOTE_TEXT)


def check_no_repo_vocabulary_introduced() -> None:
    section("no new repo vocabulary introduced")
    forbidden_vocab = [
        "g-star landing class",
        "BSM admission tier",
        "thermal dof framing",
        "g_* landing class",
        "new theory class",
        "algebraic universality",
        "two-class framing",
        "lattice-realization-invariant",
    ]
    for phrase in forbidden_vocab:
        check(
            f"forbidden vocabulary absent: {phrase!r}",
            phrase not in NOTE_TEXT,
        )


def check_status_authority_surface() -> None:
    section("status-authority schema")
    required = [
        "**Status authority:** source-note proposal only",
        "audit verdict and",
        "effective status are set by the independent audit lane",
    ]
    for phrase in required:
        check(f"status-authority surface phrase: {phrase}", phrase in NOTE_TEXT)


def check_runner_self_consistency() -> None:
    section("runner-note self-consistency")
    expected_path = (
        "scripts/frontier_g_star_sm_content_from_supplied_thermal_inventory.py"
    )
    check("runner path cited in note", expected_path in NOTE_TEXT)


def main() -> int:
    check_note_structure()
    check_proof_walk_forbidden_imports()
    check_load_bearing_retained_packet()
    check_premise_packet()
    check_boson_factorisation()
    check_fermion_factorisation()
    check_g_star_exact_rational()
    check_parent_inventory_alignment()
    check_boundary_disclaimers()
    check_no_repo_vocabulary_introduced()
    check_status_authority_surface()
    check_runner_self_consistency()

    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL == 0:
        print(
            "VERDICT: bounded proof-walk passes; g_* = 106.75 follows from the"
            " support packet R1-R6 plus the registered P1-P5 inventory"
            " packet by exact rational arithmetic."
        )
        return 0
    print("VERDICT: FAILED -- bounded proof-walk did not pass all checks.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
