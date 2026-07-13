#!/usr/bin/env python3
"""Countermodels showing Record additivity leaves the R-eta unit free."""

from __future__ import annotations

import itertools
from fractions import Fraction
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ACPHILAMBDA_R_ETA_DIRECT_LICENSE_HCLASS_HUNIT_NON_SUPPLY_NO_GO_NOTE_2026-07-04.md"
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE_REFERENCE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC_ISOTROPY = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: object = "") -> None:
    global PASS, FAIL
    if bool(ok):
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f"  ({detail})" if detail != "" else ""
    print(f"  [{tag}] {label}{suffix}")


def section(title: str) -> None:
    print(f"\n{title}\n{'-' * len(title)}")


def readout(beta: Fraction, h: Fraction, records: frozenset[tuple[int, int, int]]) -> Fraction:
    return beta * h * len(records)


def main() -> int:
    print("Record additivity and the R-eta unit-calibration countermodel")
    print("=" * 72)

    h = Fraction(2, 9)
    beta_target = Fraction(1, 1)
    beta_counter = Fraction(2, 1)
    empty: frozenset[tuple[int, int, int]] = frozenset()
    r = frozenset({(0, 0, 0), (1, 0, 0)})
    s = frozenset({(0, 1, 0), (0, 0, 1), (1, 1, 0)})
    singleton = frozenset({(0, 0, 0)})
    cycle = frozenset({(0, 0, 0), (1, 0, 0), (0, 1, 0)})

    section("Part A: exact beta family")
    betas = [Fraction(1, 3), Fraction(1, 2), beta_target, Fraction(3, 2), beta_counter]
    check("tested beta family is strictly positive", all(beta > 0 for beta in betas))
    check("empty record reads zero for every tested beta", all(readout(beta, h, empty) == 0 for beta in betas))
    check(
        "finite disjoint additivity holds for every tested beta",
        all(readout(beta, h, r | s) == readout(beta, h, r) + readout(beta, h, s) for beta in betas),
    )
    check("target singleton eta angle is 2/9", readout(beta_target, h, singleton) == Fraction(2, 9))
    check("countermodel singleton eta angle is 4/9", readout(beta_counter, h, singleton) == Fraction(4, 9))
    check(
        "N1 numerical_or_finite_case mechanism: finite singleton point evaluation; "
        "N1 numerical_or_finite_case attempt: finite cardinality formula at n=1; "
        "N1 numerical_or_finite_case outcome: finite beta-one and beta-two singleton readouts remain distinct",
        len(singleton) == 1
        and readout(beta_target, h, singleton) == h
        and readout(beta_counter, h, singleton) == 2 * h
        and readout(beta_target, h, singleton) != readout(beta_counter, h, singleton),
    )
    check("target cycle holonomy is 2/3", readout(beta_target, h, cycle) == Fraction(2, 3))
    check("countermodel cycle holonomy is 4/3", readout(beta_counter, h, cycle) == Fraction(4, 3))
    check("target and countermodel share the same h", h == Fraction(2, 9))
    check("target and countermodel are distinct", readout(beta_target, h, cycle) != readout(beta_counter, h, cycle))

    section("Part B: content and symmetry")
    translated = frozenset((x + 7, y - 4, z + 2) for x, y, z in cycle)
    rotated = frozenset((-y, x, z) for x, y, z in cycle)
    check("readout is translation invariant", all(readout(beta, h, translated) == readout(beta, h, cycle) for beta in betas))
    check("readout is proper-cubic-rotation invariant", all(readout(beta, h, rotated) == readout(beta, h, cycle) for beta in betas))
    check(
        "readout is cycle-position permutation invariant",
        all(
            readout(beta, h, frozenset(order)) == readout(beta, h, cycle)
            for beta in betas
            for order in itertools.permutations(cycle)
        ),
    )
    check("real readout is conjugation even", all(complex(readout(beta, h, cycle)).conjugate() == complex(readout(beta, h, cycle)) for beta in betas))
    check("readout depends on record collection through cardinality", readout(beta_target, h, r) == 2 * h and readout(beta_target, h, s) == 3 * h)

    section("Part C: arbitrary finite additivity")
    for n in range(6):
        records = frozenset((i, 0, 0) for i in range(n))
        check(f"cardinality formula holds at n={n}", readout(beta_counter, h, records) == beta_counter * h * n)
    a = frozenset({(10, 0, 0)})
    b = frozenset({(11, 0, 0), (12, 0, 0)})
    c = frozenset({(13, 0, 0), (14, 0, 0), (15, 0, 0)})
    check(
        "three-way disjoint additivity",
        readout(beta_counter, h, a | b | c)
        == readout(beta_counter, h, a) + readout(beta_counter, h, b) + readout(beta_counter, h, c),
    )

    section("Part D: rhetoric-resolution lifts")
    check(
        "per_element: singleton record indicator preserves distinct beta-one and beta-two readouts",
        readout(beta_target, h, singleton) == h
        and readout(beta_counter, h, singleton) == 2 * h,
    )

    site_family = frozenset({(-2, 1, 0), (0, 0, 0), (3, -1, 2), (4, 4, -3)})
    translated_family = frozenset((x + 9, y - 6, z + 5) for x, y, z in site_family)
    check(
        "per_site: translated finite-site records preserve symmetry while leaving beta free",
        all(
            readout(beta, h, translated_family) == readout(beta, h, site_family)
            for beta in (beta_target, beta_counter)
        )
        and readout(beta_target, h, site_family) != readout(beta_counter, h, site_family),
    )

    mode_records = frozenset((0, 0, mode) for mode in range(5))
    low_modes = frozenset((0, 0, mode) for mode in range(2))
    high_modes = mode_records - low_modes
    check(
        "per_mode: disjoint finite-mode decomposition preserves additivity while leaving beta free",
        low_modes.isdisjoint(high_modes)
        and all(
            readout(beta, h, mode_records)
            == readout(beta, h, low_modes) + readout(beta, h, high_modes)
            for beta in (beta_target, beta_counter)
        )
        and readout(beta_target, h, mode_records) != readout(beta_counter, h, mode_records),
    )

    check(
        "per_block: disjoint record blocks preserve additivity for both beta normalizations",
        all(
            readout(beta, h, r | s) == readout(beta, h, r) + readout(beta, h, s)
            for beta in (beta_target, beta_counter)
        )
        and readout(beta_target, h, r | s) != readout(beta_counter, h, r | s),
    )

    lattice_records = frozenset(
        (x, y, z)
        for x in range(2)
        for y in range(2)
        for z in range(2)
    )
    even_sites = frozenset(site for site in lattice_records if sum(site) % 2 == 0)
    odd_sites = lattice_records - even_sites
    check(
        "lattice_wide: finite lattice partition preserves both laws while beta remains unselected",
        even_sites.isdisjoint(odd_sites)
        and all(
            readout(beta, h, lattice_records)
            == readout(beta, h, even_sites) + readout(beta, h, odd_sites)
            for beta in (beta_target, beta_counter)
        )
        and readout(beta_target, h, lattice_records)
        != readout(beta_counter, h, lattice_records),
    )
    check(
        "N2 wall readout bridge: W_unit beta-one and beta-two singleton laws share h but remain distinct",
        readout(beta_target, h, singleton) == h
        and readout(beta_counter, h, singleton) == 2 * h
        and readout(beta_target, h, singleton)
        != readout(beta_counter, h, singleton),
    )

    section("Part E: coordinate-convention steelman")
    u_sym, h_sym, beta_sym = sp.symbols("u h beta", positive=True)
    delta_sym = beta_sym * h_sym
    ratio_invariant = sp.simplify((u_sym * delta_sym) / (u_sym * h_sym) - beta_sym) == 0
    residual_covariant = sp.simplify(
        (u_sym * delta_sym - u_sym * h_sym)
        - u_sym * h_sym * (beta_sym - 1)
    ) == 0
    relative_hits_identity = sp.simplify(delta_sym / beta_sym - h_sym) == 0
    unit_scales = [Fraction(1, 3), Fraction(1, 1), Fraction(2, 1), Fraction(7, 2)]
    print("N1 route coordinate_convention")
    print(
        "  N7 convention mechanism: same-observable common-unit rescaling"
    )
    print(
        "  ATTEMPTED N7 convention attempt: multiply h and abs(delta_beta) by "
        "the same positive unit factor"
    )
    print(
        "  N7 convention outcome: beta=abs(delta_beta)/h remains invariant "
        "and the W_unit readout bridge is not selected"
    )
    check(
        "N7 steelman argument: N7 convention mechanism: same-observable common-unit rescaling; "
        "ATTEMPTED N7 convention attempt: multiply h and abs(delta_beta) by the same positive unit factor; "
        "N7 convention outcome: beta=abs(delta_beta)/h remains invariant and the W_unit readout bridge is not selected",
        ratio_invariant and residual_covariant,
    )
    check(
        "N7 relative-normalization guard: beta=2 reaches beta=1 by rescaling abs(delta_beta) without h, which is not a common-unit convention",
        relative_hits_identity and Fraction(1, 2) != Fraction(1, 1),
    )
    check("coordinate unit scales are positive", all(unit > 0 for unit in unit_scales))
    check(
        "coordinate_convention ATTEMPTED: common-unit rescaling preserves the beta-one ratio",
        all(
            (unit * readout(beta_target, h, singleton)) / (unit * h) == beta_target
            for unit in unit_scales
        ),
    )
    check(
        "coordinate_convention ATTEMPTED: common-unit rescaling preserves the beta-two ratio",
        all(
            (unit * readout(beta_counter, h, singleton)) / (unit * h) == beta_counter
            for unit in unit_scales
        ),
    )
    check(
        "same-coordinate beta-one readout equals the fixed-locus density",
        all(unit * readout(beta_target, h, singleton) == unit * h for unit in unit_scales),
    )
    check(
        "same-coordinate beta-two readout remains distinct from the fixed-locus density",
        all(unit * readout(beta_counter, h, singleton) != unit * h for unit in unit_scales),
    )
    check(
        "same-observable identity is equivalent to beta one in the tested positive family",
        all(
            all(
                (unit * readout(beta, h, singleton) == unit * h)
                == (beta == beta_target)
                for unit in unit_scales
            )
            for beta in betas
        ),
    )
    print(
        "N7 coordinate steelman resolved by current-cycle computation: a common "
        "coordinate change leaves beta invariant; a separate same-observable "
        "theorem could set beta=1 but is not a units convention"
    )

    section("Part F: source and axiom guards")
    note = NOTE.read_text(encoding="utf-8")
    axioms = AXIOMS.read_text(encoding="utf-8")
    scale_reference = SCALE_REFERENCE.read_text(encoding="utf-8")
    kinetic_isotropy = KINETIC_ISOTROPY.read_text(encoding="utf-8")
    scale_flat = " ".join(scale_reference.split())
    kinetic_flat = " ".join(kinetic_isotropy.split())
    note_flat = " ".join(note.split())
    check("current Record axiom contains empty-zero", "I(empty)=0" in axioms)
    check("current Record axiom contains finite additivity", "scalar readout `I` is additive" in " ".join(axioms.split()))
    check("current axioms withhold physical-observable identification", "source/action and physical-observable identification" in axioms)
    check("scale reference withholds dimensionless readout content", "no mass ratio, coupling, mixing angle, phase, selector, readout bridge" in scale_flat)
    check("kinetic isotropy withholds phase and readout bridge", "No mass ratio, coupling, mixing angle, phase, or selector is supplied" in kinetic_flat and "readout bridge" in kinetic_flat)
    check("note grants h-class explicitly", "Grant the R-eta h-class hypothesis" in note)
    check(
        "note states the positive beta countermodel",
        "Every positive real `beta`" in note and "I_beta(R) = beta h N(R)" in note,
    )
    check("note matches singleton eta angle and cycle holonomy", "|delta_beta| = I_beta({x}) = beta h" in note and "Phi_beta = I_beta(C) = 3 beta h" in note)
    check("note limits claim to current finite-record surface", "finite-record, current-surface" in note)
    check("note preserves a future same-observable theorem", "future same-observable holonomy theorem" in note)
    check("note does not force r", "does not force\n`r=1/2`" in note)
    check("N1 contains eight attempted routes", note.count("| ATTEMPTED |") == 8)
    check(
        "N2 collapses to one readout-bridge wall",
        "single structured audit-packet wall label is `readout bridge`" in note_flat
        and "`W_unit` is the charged-lepton lane alias" in note_flat,
    )
    check("N3 records the required phrase scan", "The proof text was scanned for" in note)
    check("N4 uses no prior negative witness", "No prior no-go row is cited as evidence" in note)
    check("N5 names tested resolutions", "empty collection, a singleton eta-angle" in note and "three-record cycle holonomy" in note)
    check("N6 records convention and theorem paths", "convention-only coordinate ratification" in note and "same-observable determinant-line/holonomy theorem" in note)
    check(
        "N7 contains the executable coordinate steelman",
        "same-observable common-unit rescaling" in note_flat
        and "ATTEMPTED N7 convention attempt: multiply `h` and `abs(delta_beta)`" in note_flat
        and "ratio is `Phi_u/H_u = beta`" in note_flat
        and "same-observable identity" in note_flat
        and "readout bridge, or empirical fit is supplied by it" in note_flat,
    )
    check("N8 considers historical withdrawal, derivation, primitive, and coordinate mechanisms", "historical AC(ii) governance adoption and withdrawal" in note and "theta mass-side split" in note and "scale-reference primitive" in note and "registered mass-coordinate reconstruction" in note)
    check("discipline gate records PASS", "**Gate result: PASS.**" in note)

    print("\n" + "=" * 72)
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
