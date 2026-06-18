#!/usr/bin/env python3
"""Open-gate runner: FRW + adiabatic-expansion cosmological-backdrop boundary.

The runner checks only:

1. source-firewall phrases (the named-premise block C1-C3, the
   "admission bridge not derivation" disclaimer, the "no new
   admissions" statement, and the context surfaces all appear in the source note);
2. the decomposition arithmetic of the bridge --- enumerate the
   load-bearing ingredients of the cosmological backdrop, partition
   them into (a) framework-derivable / conditional-on-retained-chain
   and (b) local supplied premises, and verify the partition is
   exact and disjoint;
3. that the runner does not consume any Wilson-action, Monte Carlo,
   PDG, or fitted observational input.

It deliberately does not use cosmological observational comparators
(Planck 2018 H_0, Omega_Lambda, etc.), fitted values, Monte Carlo
data, or any lattice-action input. Numerical comparisons appear only
to verify partition counts.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = (
    "frw_adiabatic_expansion_cosmological_backdrop_open_gate_note_2026-05-28"
)
RUNNER_PATH = (
    "scripts/frontier_frw_adiabatic_expansion_cosmological_backdrop_open_gate.py"
)
NOTE_PATH = (
    ROOT
    / "docs/FRW_ADIABATIC_EXPANSION_COSMOLOGICAL_BACKDROP_OPEN_GATE_NOTE_2026-05-28.md"
)

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS, FAIL
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS += 1
    else:
        FAIL += 1
    msg = f"{status}: {name}"
    if detail:
        msg += f" ({detail})"
    print(msg)
    return condition


def part0_source_firewall() -> str:
    print("\n== Part 0: source firewall ==")
    note = NOTE_PATH.read_text(encoding="utf-8")
    note_normalized = " ".join(note.split())

    required = [
        "Supplied premise packet (not axioms, not registry premises)",
        "C1 Cosmological principle",
        "C2 Adiabatic expansion",
        "C3 Standard FRW equation-of-state sequence",
        "2026-06-18 C2 entropy-bookkeeping partial bridge",
        "FRW_C2_SOURCE_FREE_ENTROPY_BOOKKEEPING_BOUNDED_SUPPORT_NOTE_2026-06-18.md",
        "2026-06-18 C3 kinetic-label partial bridge",
        "FRW_C3_EOS_COMPONENT_LABELS_KINETIC_BRIDGE_BOUNDED_SUPPORT_NOTE_2026-06-18.md",
        "2026-06-18 C3 perfect-fluid lift partial bridge",
        "FRW_C3_KINETIC_COMPONENT_PERFECT_FLUID_LIFT_BOUNDED_SUPPORT_NOTE_2026-06-18.md",
        "does not derive C1 or C2",
        "does not derive that the real leptogenesis-to-CMB window is source-free",
        "does not derive the Standard Model `g_*S` table",
        "does not derive the full FRW backdrop",
        "does not derive real cosmological species allocation",
        "two partial finite C3 bridges named above",
        "partial finite C2 bookkeeping bridge",
        "no new repo-wide axiom is introduced",
        "introduces **no new admissions and no new repo-wide",
        "Status authority:** independent audit lane only",
        "Type:** open_gate",
        "proposal_allowed:** false",
        RUNNER_PATH,
    ]
    for phrase in required:
        check(f"source contains boundary phrase: {phrase}", phrase in note_normalized)

    # Forbidden = positive over-claim or imported-physics framing. Quoted
    # uses inside disclaimer language ("no new 'cosmological backdrop
    # class'") are NOT introductions of vocabulary; they are explicit
    # negations. We test for the introductory positive forms only.
    forbidden_introductions = [
        # introducing the class as a thing: "the cosmological backdrop
        # class is..." would be an introduction. Disclaimer-quoted use
        # ("no new \"cosmological backdrop class\"") is fine.
        "imported physics",
        "predicts that any of them will close",
        "promotes the parent",
        "retires the admission",
        "this is a new framework class",
    ]
    for phrase in forbidden_introductions:
        check(
            f"source note excludes over-claim phrase: {phrase}",
            phrase not in note,
        )

    context_surfaces = [
        "`S3_GENERAL_R_DERIVATION_NOTE.md`",
        "`COSMOLOGY_FRW_KINEMATIC_REDUCTION_THEOREM_NOTE_2026-04-24.md`",
        "`COSMOLOGY_OPEN_NUMBER_REDUCTION_THEOREM_NOTE_2026-04-26.md`",
        "`DARK_ENERGY_EOS_RETAINED_COROLLARY_THEOREM_NOTE.md`",
        "`DM_LEPTOGENESIS_TRANSPORT_DECOMPOSITION_THEOREM_NOTE_2026-04-16.md`",
        "`N_EFF_FROM_THREE_GENERATIONS_THEOREM_NOTE_2026-04-24.md`",
    ]
    for marker in context_surfaces:
        check(f"source lists context surface in non-link form: {marker}", marker in note)

    return note


def part1_partition() -> tuple[set[str], set[str]]:
    print("\n== Part 1: backdrop ingredient partition ==")
    framework_or_conditional = {
        "S^3 qualitative spatial topology",
        "FRW kinematic reduction surface",
        "cosmology open-number reduction (two structural DoF at fixed R)",
        "N_eff = 3.046 (3 active + 0.046 textbook correction)",
        "w_Lambda = -1 retained corollary",
    }
    supplied_C123 = {
        "C1: cosmological principle (homogeneity + isotropy beyond S^3)",
        "C2 residual: real no-injection era and g_*S table",
        "C3 residual: real species allocation into ideal EOS components",
    }
    intersection = framework_or_conditional & supplied_C123
    union = framework_or_conditional | supplied_C123
    check(
        "the framework-derivable/conditional set has 5 ingredients",
        len(framework_or_conditional) == 5,
        f"|FW/cond|={len(framework_or_conditional)}",
    )
    check(
        "the local supplied premise set has exactly 3 ingredients (C1-C3)",
        len(supplied_C123) == 3,
        f"|C1-C3|={len(supplied_C123)}",
    )
    check(
        "the two sets are disjoint (no ingredient is both derivable and admitted)",
        len(intersection) == 0,
        f"intersection={intersection}",
    )
    check(
        "the partition covers exactly 8 backdrop ingredients (5 + 3)",
        len(union) == 8,
        f"|union|={len(union)}",
    )
    return framework_or_conditional, supplied_C123


def part2_no_new_vocabulary(note: str) -> None:
    print("\n== Part 2: no new repo vocabulary ==")
    # The bridge must not INTRODUCE new tag classes. The disclaimer
    # ("introduces no new 'cosmological backdrop class', no new 'FRW
    # landing tier', ...") is a quoted negation: it lists the anti-pattern
    # vocabulary to be explicit that none is introduced. The runner checks
    # for forms that would constitute an introduction, e.g. unquoted
    # repeated use of the term as if it were a real category.
    anti_pattern_introductions = [
        # If the note tried to ship a new class, it would say something
        # like "the cosmological backdrop class includes..." or "as a
        # member of the FRW landing tier...". Those forms are what we
        # forbid; the negation form is fine.
        "the cosmological backdrop class includes",
        "as a member of the FRW landing tier",
        "two-class framing",
        "algebraic universality",
        "lattice-realization-invariant by definition",
    ]
    for phrase in anti_pattern_introductions:
        check(
            f"source does not introduce anti-pattern vocab: {phrase}",
            phrase not in note,
        )

    # Sanity: the disclaimer that explicitly negates the anti-pattern IS
    # present (the negation form is the standard repo move).
    check(
        "source includes the explicit no-new-vocabulary disclaimer",
        'no new "cosmological backdrop class"' in note
        and 'no new "FRW landing tier"' in note,
    )


def part3_no_audit_data_touch() -> None:
    print("\n== Part 3: no audit-data side-effects ==")
    # The bridge note must not modify audit-lane data files. The runner
    # cannot enforce this from inside the source firewall, but we record the
    # constraint as an explicit check that the note's content does not
    # reference modifying audit data.
    note = NOTE_PATH.read_text(encoding="utf-8")
    note_normalized = " ".join(note.split())
    # All three are forbidden in their positive ("we do this") form. The
    # source note discusses what it does NOT do; the runner verifies that
    # the corresponding negation phrases are present (with whitespace
    # normalization so wrapped lines don't false-negative).
    negations_required = [
        "does **not** add C1, C2, or C3 to",
        "It does **not** promote any",
        "by the audit lane on its own row",
    ]
    for phrase in negations_required:
        check(
            f"source contains audit-data-safe negation: {phrase}",
            phrase in note_normalized,
        )


def part4_no_lattice_or_fit_inputs() -> None:
    print("\n== Part 4: no lattice / fitted-value inputs ==")
    note = NOTE_PATH.read_text(encoding="utf-8")
    # Whitespace-normalize so hard line-breaks inside the note's disclaimer
    # paragraph don't cause false-negative substring lookups.
    note_normalized = " ".join(note.split())
    forbidden_inputs = [
        "Wilson plaquette action",
        "Monte Carlo measurement",
        "fitted observational value",
        "staggered phases",
        "Brillouin-zone labels",
        "link unitaries",
        "lattice scale `u_0`",
    ]
    for phrase in forbidden_inputs:
        check(
            f"source explicitly disclaims load-bearing use of: {phrase}",
            phrase in note_normalized,
        )


def part5_admission_boundary_recorded() -> None:
    print("\n== Part 5: admission boundary recorded honestly ==")
    note = NOTE_PATH.read_text(encoding="utf-8")
    note_normalized = " ".join(note.split())
    required_honest_scope = [
        "The finite source-free entropy and `g_*S T^3 a^3` bookkeeping behind C2 is now supported",
        "The ideal kinetic component labels `w_r = 1/3` and `w_m = 0` are now supported",
        "The finite component tensors for those ideal labels now assemble into the parent perfect-fluid form",
        "retires only narrow finite C2/C3 bookkeeping and label/lift imports",
        "does not retire the cosmological-backdrop admission",
        "records the admission boundary",
        "It does **not**",
        "open gate",
        "what would close this",
    ]
    for phrase in required_honest_scope:
        check(
            f"source records honest scope phrase: {phrase}",
            phrase in note_normalized,
        )


def part6_downstream_source_boundary_firewall() -> None:
    print("\n== Part 6: downstream source-boundary firewall ==")
    note = NOTE_PATH.read_text(encoding="utf-8")
    note_normalized = " ".join(note.split())
    required = [
        "Downstream Source-Boundary Firewall",
        "may not be cited downstream as a retained derivation",
        "C1-C3 also may not be moved into a registry, admission file, or premise file",
        "Future use must separately prove or explicitly admit",
    ]
    for phrase in required:
        check(
            f"source contains downstream firewall phrase: {phrase}",
            phrase in note_normalized,
        )
    blocked_targets = [
        "C1, the physical no-injection part of C2, or the real species-allocation part of C3",
        "FRW dynamics",
        "entropy conservation or adiabatic expansion",
        "observational cosmology parameters",
        "parent theorem status",
    ]
    for phrase in blocked_targets:
        check(
            f"firewall blocks downstream retained use for: {phrase}",
            phrase in note_normalized,
        )


def part6_result(fw_set: set[str], supplied_set: set[str]) -> None:
    print("\n== Result ==")
    print("Framework-derivable / conditional-on-retained-chain ingredients:")
    for entry in sorted(fw_set):
        print(f"  - {entry}")
    print("Local supplied premises retained as open:")
    for entry in sorted(supplied_set):
        print(f"  - {entry}")
    print(
        "Net retirement: finite C2 source-free entropy bookkeeping, the ideal "
        "non-Lambda kinetic EOS labels, and their finite perfect-fluid lift are "
        "narrowed to bounded support; C1, physical C2 no-injection, and real "
        "species allocation remain open."
    )
    print(
        "No new repo-wide axiom and no claim to derive C1, the physical "
        "no-injection part of C2, or the full real species-allocation part of C3."
    )


def main() -> int:
    print("FRW + ADIABATIC EXPANSION COSMOLOGICAL-BACKDROP OPEN GATE")
    note = part0_source_firewall()
    fw_set, admitted_set = part1_partition()
    part2_no_new_vocabulary(note)
    part3_no_audit_data_touch()
    part4_no_lattice_or_fit_inputs()
    part5_admission_boundary_recorded()
    part6_downstream_source_boundary_firewall()
    part6_result(fw_set, admitted_set)
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL == 0:
        print(
            "VERDICT: open gate passes; FRW + adiabatic backdrop decomposition "
            "is recorded as an unresolved C1-C3 premise boundary with partial "
            "bounded support for finite C2 entropy bookkeeping, the ideal "
            "non-Lambda C3 kinetic labels, and their finite perfect-fluid lift. "
            "No new admissions are introduced; no row's effective status is changed."
        )
        return 0
    print("VERDICT: open gate FAILED.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
