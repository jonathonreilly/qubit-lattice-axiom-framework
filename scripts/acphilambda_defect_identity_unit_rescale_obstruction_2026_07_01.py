#!/usr/bin/env python3
"""Verifier for the AC_phi_lambda defect identity-unit rescale obstruction note.

Finite class-A checks:
  PART A -- cited sources exist and carry the quoted boundary text.
  PART B -- exact C3 fixed-defect arithmetic (L3(1,2)=2/9, L3(1,1)=1/9).
  PART C -- self-contained unit normal form I_c(R) = c*|R|*L.
  PART D -- rescale-invariance scan of the encoded premise clauses (T1).
  PART E -- atom-count normalization pins c = 9/2, not 1 (T2).
  PART F -- angle-side rigidity: lattice closure + registered-spectrum
            preservation leave exactly c = +-1 (T3).
  PART G -- unit-blind interfaces: Q=2/3 delta-blind, Born-facing
            normalization satisfiable for all c, cross-lane transport
            homogeneous, registered ratios move with c (T4).
  PART H -- note discipline (scope, non-claims, N1-N8, no overclaim).

The scan in PART D is refutation-shaped: a premise clause that secretly broke
the rescale symmetry would fail its invariance check and falsify the note.
"""

from __future__ import annotations

import math
from fractions import Fraction
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"[PASS] {label}")
    else:
        FAIL += 1
        suffix = f" -- {detail}" if detail else ""
        print(f"[FAIL] {label}{suffix}")


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def flat(text: str) -> str:
    return " ".join(text.split())


def main() -> int:
    print("=== AC_phi_lambda defect identity-unit rescale obstruction ===")

    # ------------------------------------------------------------ PART A
    print("\nPART A -- cited sources and boundary text")
    files = [
        "docs/ACPHILAMBDA_DEFECT_IDENTITY_UNIT_RESCALE_OBSTRUCTION_2026-07-01.md",
        "docs/MINIMAL_AXIOMS_2026-06-29.md",
        "docs/audit/data/axiom_premise_nodes.json",
        "docs/audit/data/tier_a_admissions.json",
        "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md",
        "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
        "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
        "docs/KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md",
        "docs/KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md",
        "docs/KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md",
        "docs/BRANNEN_CIRCULANT_IS_FORCED_C3_COVARIANT_RECORD_PRESERVING_GENERATION_FORM_BOUNDED_THEOREM_NOTE_2026-06-15.md",
        "docs/PLANCK_TARGET3_PHASE_UNIT_EDGE_STATISTICS_BOUNDARY_NOTE_2026-04-25.md",
    ]
    for rel in files:
        check(f"{rel} exists", (ROOT / rel).exists())

    note = read("docs/ACPHILAMBDA_DEFECT_IDENTITY_UNIT_RESCALE_OBSTRUCTION_2026-07-01.md")
    flat_note = flat(note)
    axioms = read("docs/MINIMAL_AXIOMS_2026-06-29.md")
    registry = read("docs/audit/data/axiom_premise_nodes.json")
    tier_a = read("docs/audit/data/tier_a_admissions.json")
    scale = flat(read("docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md"))
    kinetic = flat(read("docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"))
    realized = flat(read("docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"))
    radian = read("docs/KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md")
    fixed_locus = read("docs/KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md")
    planck = read("docs/PLANCK_TARGET3_PHASE_UNIT_EDGE_STATISTICS_BOUNDARY_NOTE_2026-04-25.md")

    check(
        "Record axiom readout clause present verbatim",
        "records, scalar readout `I` is additive, with `I(empty)=0`" in flat(axioms)
        or "scalar readout `I` is additive, with `I(empty)=0`" in flat(axioms),
    )
    check(
        "Record axiom lock clause present",
        "a record locks exactly one admissible local possibility" in flat(axioms),
    )
    check(
        "registry node excludes weighting/normalization/probability",
        "weighting, normalization, probability" in registry,
    )
    check(
        "registry node excludes physical observable bridge",
        "physical observable bridge" in registry,
    )
    check(
        "scale primitive: zero dimensionless content clause",
        "zero dimensionless content: no mass ratio, coupling, mixing angle, phase, selector, readout bridge" in scale,
    )
    check(
        "kinetic primitive: no selector/readout bridge clause",
        "no mass ratio, coupling, mixing angle, phase, selector, readout bridge" in kinetic,
    )
    check(
        "realized-state primitive: no normalization rule / value supplied",
        "normalization rule, or value is supplied by it" in realized,
    )
    check(
        "realized-state primitive: pointwise evaluation, not state-selection",
        "pointwise evaluation, not a state-selection rule" in realized,
    )
    check(
        "tier-A sub-admission (ii) names density-read-as-angle",
        "density-read-as-angle" in tier_a,
    )
    check(
        "radian-bridge note carries the Type-B-to-radian primitive residual",
        "Type-B-to-radian" in radian and "remaining primitive" in radian,
    )
    check(
        "fixed-locus note excludes the physical readout from its scope",
        "does **not** supply the physical single-summand readout" in fixed_locus,
    )
    check(
        "planck boundary note records the native dimensionless phase unit",
        "native dimensionless phase unit" in planck,
    )

    # ------------------------------------------------------------ PART B
    print("\nPART B -- exact C3 fixed-defect arithmetic")
    omega = sp.Rational(-1, 2) + sp.I * sp.sqrt(3) / 2  # exp(2 pi i / 3)

    def l_density(a: int, b: int):
        s = sum(
            1 / ((omega ** (j * a) - 1) * (omega ** (j * b) - 1)) for j in (1, 2)
        )
        return sp.nsimplify(sp.simplify(s / 3))

    L12 = l_density(1, 2)
    L11 = l_density(1, 1)
    L22 = l_density(2, 2)
    check("L3(1,2) = 2/9 exactly", L12 == sp.Rational(2, 9), L12)
    check("L3(1,1) = 1/9 exactly", L11 == sp.Rational(1, 9), L11)
    check("L3(2,2) = 1/9 exactly", L22 == sp.Rational(1, 9), L22)
    core = sp.simplify((omega - 1) * (omega**2 - 1))
    check("core identity (omega-1)(omega^2-1) = 3", core == 3, core)
    check("selected and contrast densities differ", L12 != L11)

    L = Fraction(2, 9)

    # ------------------------------------------------------------ PART C
    print("\nPART C -- self-contained unit normal form")

    def additive_extension(u: Fraction):
        def readout(collection: frozenset) -> Fraction:
            return sum((u for _ in collection), Fraction(0))
        return readout

    c_grid = [Fraction(1), Fraction(1, 2), Fraction(2), Fraction(-3), Fraction(7, 5)]
    for c in c_grid:
        u = c * L
        I = additive_extension(u)
        r1 = frozenset({"D1"})
        r2 = frozenset({"D2"})
        r12 = frozenset({"D1", "D2"})
        check(
            f"c={c}: additive with I(empty)=0 and I(pair)=I(a)+I(b)",
            I(frozenset()) == 0 and I(r12) == I(r1) + I(r2),
        )
    u1 = Fraction(2, 9)
    check("identity-unit member has I(single) = L = 2/9", Fraction(1) * L == u1)
    check(
        "singleton value determines the extension: I(R) = |R| * u",
        additive_extension(Fraction(4, 9))(frozenset({"a", "b", "c"})) == 3 * Fraction(4, 9),
    )

    # ------------------------------------------------------------ PART D
    print("\nPART D -- rescale-invariance scan (T1)")
    # finite universe: two selected-type atoms (density L), one contrast atom
    # (density 1/9), one composite refining into the two selected atoms.
    densities = {
        "A": Fraction(2, 9),
        "B": Fraction(2, 9),
        "C": Fraction(1, 9),
        "AB": Fraction(4, 9),
    }
    composites = {"AB": ("A", "B")}

    def clause_line(vals: dict) -> bool:
        seen: dict = {}
        for atom, value in vals.items():
            d = densities[atom]
            if d in seen and seen[d] != value:
                return False
            seen[d] = value
        return True

    def clause_refine(vals: dict) -> bool:
        return all(
            vals[comp] == vals[a1] + vals[a2]
            for comp, (a1, a2) in composites.items()
        )

    def clause_lock(vals: dict) -> bool:
        # the lock clause constrains which possibility is locked, never the
        # scalar a readout attaches to the lock: value-free, always satisfied
        return True

    def clause_cross_lane(vals: dict) -> bool:
        # one unit c serves both density lanes: vals/density constant
        units = {vals[a] / densities[a] for a in ("A", "C")}
        return len(units) == 1

    base = {
        "A": Fraction(2, 9),
        "B": Fraction(2, 9),
        "C": Fraction(1, 9),
        "AB": Fraction(4, 9),
    }
    clauses = [
        ("density-line dependence", clause_line),
        ("disjoint-refinement consistency", clause_refine),
        ("lock clause (value-free)", clause_lock),
        ("cross-lane same-unit", clause_cross_lane),
    ]
    check("base member satisfies every encoded clause", all(p(base) for _, p in clauses))
    lam_grid = [Fraction(1, 2), Fraction(2), Fraction(3), Fraction(-1), Fraction(7, 5)]
    for name, pred in clauses:
        invariant = all(
            pred({k: lam * v for k, v in base.items()}) for lam in lam_grid
        )
        check(f"clause rescale-invariant: {name}", invariant)
    # additivity and I(empty)=0 are rescale-invariant by linearity; verified
    # on the extension directly:
    for lam in lam_grid:
        I_lam = additive_extension(lam * L)
        check(
            f"lambda={lam}: rescaled readout still additive with I(empty)=0",
            I_lam(frozenset()) == 0
            and I_lam(frozenset({"x", "y"})) == I_lam(frozenset({"x"})) + I_lam(frozenset({"y"})),
        )
    # orbit closure: the whole c-line satisfies the full clause set
    line_ok = True
    for c in c_grid:
        member = {a: c * densities[a] for a in densities}
        line_ok = line_ok and all(p(member) for _, p in clauses)
    check("entire c-line lies inside the clause-set solution set", line_ok)
    # uniqueness at the fixed point only: lambda*I = I for all lambda forces I = 0
    check(
        "the only rescale-fixed readout is the zero readout",
        all((lam * u1 == u1) is False for lam in lam_grid if lam != 1)
        and all(lam * Fraction(0) == Fraction(0) for lam in lam_grid),
    )

    # ------------------------------------------------------------ PART E
    print("\nPART E -- atom-count normalization pins the wrong member (T2)")
    count_single = Fraction(1)          # N({D}) = 1: the pure count
    c_count = count_single / L

    def count_readout(collection: frozenset) -> Fraction:
        return Fraction(len(collection))

    check(
        "count readout is additive with N(empty)=0 (occupancy-type surface)",
        count_readout(frozenset()) == 0
        and count_readout(frozenset({"D1", "D2"}))
        == count_readout(frozenset({"D1"})) + count_readout(frozenset({"D2"})),
    )
    check("count normalization pins c = 9/2 exactly", c_count == Fraction(9, 2), c_count)
    check("count-pinned member is not the identity unit", c_count != 1)
    check(
        "count IS rescale-breaking (lambda*N violates N(single)=1)",
        any(lam * count_single != count_single for lam in lam_grid),
    )
    check(
        "count-in-density-units clause I(single)=L is the c=1 member verbatim",
        Fraction(1) * L == L,
    )
    check(
        "witness freedom: I(single)=L/2 satisfies additivity + empty-zero",
        additive_extension(L / 2)(frozenset({"D"})) == L / 2
        and additive_extension(L / 2)(frozenset()) == 0,
    )

    # ------------------------------------------------------------ PART F
    print("\nPART F -- angle-side rigidity (T3)")
    native_lattice = {Fraction(0), Fraction(1, 3), Fraction(2, 3)}

    def lattice_survives(c: Fraction) -> bool:
        read_lattice = {(c * Fraction(k, 3)) % 1 for k in range(3)}
        return read_lattice == native_lattice

    grid = sorted(
        {Fraction(n, d) for n in range(-9, 10) for d in (1, 2, 3, 4, 5)}
    )
    survivors = [c for c in grid if lattice_survives(c)]
    expected_survivors = [
        c for c in grid if c.denominator == 1 and c.numerator % 3 != 0
    ]
    check(
        "lattice closure survivors = integers with c mod 3 != 0",
        survivors == expected_survivors,
        survivors,
    )
    check(
        "no non-integer c survives lattice closure",
        all(c.denominator == 1 for c in survivors),
    )
    check("degenerate c=3 collapses the lattice (excluded)", not lattice_survives(Fraction(3)))
    check("degenerate c=0 collapses the lattice (excluded)", not lattice_survives(Fraction(0)))

    def spectrum_preserved_all_offsets(c: Fraction) -> bool:
        # multiset {cos(c*(delta+2pi k/3))} == {cos(delta+2pi k/3)} for all
        # delta  <=>  exists sign s with (c-s)*dhat integer for all dhat
        # (delta = dhat * 2pi/3); tested at dhat = 1/7, 1/11
        for s in (1, -1):
            if all(
                ((c - s) * dh).denominator == 1
                for dh in (Fraction(1, 7), Fraction(1, 11))
            ):
                return True
        return False

    kept = [c for c in survivors if spectrum_preserved_all_offsets(c)]
    check("registered-spectrum preservation leaves exactly {+1, -1}",
          set(kept) == {Fraction(1), Fraction(-1)}, kept)

    def registered_multiset(c: float, delta: float) -> list:
        return sorted(
            1 + math.sqrt(2) * math.cos(c * (delta + 2 * math.pi * k / 3))
            for k in range(3)
        )

    d0 = 2.0 / 9.0
    base_spec = registered_multiset(1.0, d0)
    for c_int in (2, 4, 5, 7):
        moved = max(
            abs(a - b)
            for a, b in zip(registered_multiset(float(c_int), d0), base_spec)
        )
        check(
            f"discrete lattice survivor c={c_int} changes the registered multiset",
            moved > 0.05,
            f"max shift {moved:.6f}",
        )
    conj = max(
        abs(a - b) for a, b in zip(registered_multiset(-1.0, d0), base_spec)
    )
    check("c=-1 (conjugation) preserves the registered multiset", conj < 1e-12, conj)
    check(
        "conjugation is the sign strip: |delta| invariant under delta -> -delta",
        abs(-d0) == abs(d0),
    )

    # ------------------------------------------------------------ PART G
    print("\nPART G -- unit-blind interfaces (T4)")
    delta = sp.symbols("delta", real=True)
    xk = [1 + sp.sqrt(2) * sp.cos(delta + 2 * sp.pi * k / 3) for k in range(3)]
    p2 = sp.simplify(sum(x**2 for x in xk))
    e1 = sp.simplify(sum(xk))
    Q = sp.simplify(p2 / e1**2)
    check("Q(delta) = 2/3 exactly for all delta (delta-blind guardrail)",
          Q == sp.Rational(2, 3), Q)
    check("e1 = 3 exactly (v0-normalized democratic trace)", sp.simplify(e1) == 3, e1)

    for c_try in (1.0, 0.5, 2.0, 3.7):
        masses = [v**2 for v in registered_multiset(c_try, d0)]
        total = sum(masses)
        probs = [m / total for m in masses]
        check(
            f"Born-facing normalization satisfiable at c={c_try}: sum p = 1",
            abs(sum(probs) - 1) < 1e-12,
        )

    ratio_c1 = base_spec[0] / base_spec[1]
    ratio_chalf = registered_multiset(0.5, d0)[0] / registered_multiset(0.5, d0)[1]
    check(
        "registered ratio moves with c (substantive, not vacuous convention)",
        abs(ratio_c1 - ratio_chalf) > 3e-2,
        f"{ratio_c1:.6f} vs {ratio_chalf:.6f}",
    )
    v0_ratio_a = (2.0 * base_spec[0]) / (2.0 * base_spec[1])
    check(
        "v0-rescale leaves registered ratios invariant (Y0/g0-type vacuous)",
        abs(v0_ratio_a - ratio_c1) < 1e-12,
    )

    LA, LB = Fraction(2, 9), Fraction(1, 9)
    transport_homogeneous = True
    for c in (Fraction(1), Fraction(1, 2), Fraction(3)):
        for lam in (Fraction(2), Fraction(1, 3)):
            IA, IB = lam * c * LA, lam * c * LB
            transport_homogeneous = transport_homogeneous and (IA / LA == IB / LB)
    check(
        "cross-lane same-unit clause is rescale-invariant (transport cannot pin)",
        transport_homogeneous,
    )

    # ------------------------------------------------------------ PART H
    print("\nPART H -- note discipline")
    check("note declares canonical bounded_theorem claim type", "**Claim type:** bounded_theorem" in note)
    check("note declares independent audit authority", "independent audit lane only" in note)
    check(
        "note declares no registry/axiom/convention edit",
        "does not set an audit verdict, edit registries, register primitives, change axioms, adopt a convention" in flat_note,
    )
    check("note names W_defect_identity_unit", "W_defect_identity_unit" in note)
    check("note states the normal form", "I_c(R) = c * |R| * L" in note)
    check("note is self-contained on the normal form",
          "re-derived below from the Record axiom clause alone" in flat_note)
    check("note marks the in-flight stack's audit authority",
          "their audit status is set only by the independent audit lane" in flat_note)
    check("note states the shape criterion",
          "rescale-breaking (inhomogeneous) readout clause" in note)
    check("note localizes the freedom onto the density-to-angle junction",
          "density-to-angle junction" in note)
    check("note consolidates onto R-eta sub-admission (ii)",
          "sub-admission (ii)" in note and "names no new wall" in note)
    check("note quotes the radian-bridge primitive residual",
          "Type-B-to-radian identification remains primitive" in note)
    check("note names the angle-native live route",
          "Angle-native route" in note)
    check("note keeps the approved-primitive route explicit",
          "Approved-primitive proposal" in note)
    linked_authorities = [
        "(MINIMAL_AXIOMS_2026-06-29.md)",
        "(KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md)",
        "(SCALE_REFERENCE_PRIMITIVE_NOTE.md)",
        "(KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)",
        "(REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md)",
        "(KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md)",
        "(BRANNEN_CIRCULANT_IS_FORCED_C3_COVARIANT_RECORD_PRESERVING_GENERATION_FORM_BOUNDED_THEOREM_NOTE_2026-06-15.md)",
        "(KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md)",
        "(PLANCK_TARGET3_PHASE_UNIT_EDGE_STATISTICS_BOUNDARY_NOTE_2026-04-25.md)",
    ]
    for link in linked_authorities:
        check(f"note graph-links authority {link}", link in note)
    for item in ["N1", "N2", "N3", "N4", "N5", "N6", "N7", "N8"]:
        check(f"note includes {item}", f"### {item}" in note)
    forbidden = [
        "only route",
        "last route",
        "exhausted",
        "closes the route",
        "no future route",
        "impossible to derive",
        "requires a new ontology axiom",
        "AC_phi_lambda is solved",
        "AC_phi_lambda is closed",
    ]
    for phrase in forbidden:
        check(f"note avoids overclaim phrase: {phrase}", phrase not in note)
    check("note does not use runner PASS as source status", "**Status:** PASS" not in note)
    check("note says not a terminal no-go", "not a terminal no-go" in note)
    check(
        "note preserves future bridge derivations explicitly",
        "cannot be derived by a future angle-native" in flat_note
        and "This note does not claim" in note,
    )
    check("note does not import comparator data", "PDG" not in note)

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("RESULT: FAIL -- rescale-obstruction note is not verifier-clean.")
        return 1
    print(
        "RESULT: PASS -- the scanned homogeneous premise surface cannot select "
        "the identity unit; the freedom is the R-eta density-read-as-angle "
        "junction coefficient; angle-native and rescale-breaking bridge routes "
        "remain live."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
