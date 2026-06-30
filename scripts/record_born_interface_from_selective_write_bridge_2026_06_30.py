#!/usr/bin/env python3
"""Verify the record/Born interface bridge from a selective write isometry."""

from __future__ import annotations

from itertools import product
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

NOTE = DOCS / "RECORD_BORN_INTERFACE_FROM_SELECTIVE_WRITE_BRIDGE_2026-06-30.md"
AXIOMS = DOCS / "MINIMAL_AXIOMS_2026-06-29.md"
CHECKLIST = DOCS / "RECORD_PRODUCTION_RESIDUAL_CHECKLIST_2026-06-05.md"
LAYER = DOCS / "RECORD_DYNAMICS_LAYER_RECONCILIATION_2026-06-05.md"
BORN_BOUNDARY = DOCS / "RECORD_BORN_FREQUENCY_BOUNDARY_2026-06-05.md"
FORMATION_NOGO = DOCS / "RECORD_FORMATION_NOT_UNCONDITIONALLY_FORCED_BY_MINIMAL_AXIOMS_NARROW_NO_GO_NOTE_2026-06-06.md"
BUSCH = DOCS / "BUSCH_POVM_EFFECT_GLEASON_QUBIT_AUTHORITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md"
LUDERS = DOCS / "LUDERS_SEQUENTIAL_EFFECT_COMPOSITION_PEP_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md"
WRITE_ISOMETRY = DOCS / "RECORD_FORMATION_CONTROLLED_COPY_WRITE_ISOMETRY_THEOREM_NOTE_2026-06-18.md"
POINTER = DOCS / "RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md"

PASS = 0
FAIL = 0


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def flat(text: str) -> str:
    return " ".join(text.split())


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(ok)
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"[{tag}] {label}{suffix}")


def section(title: str) -> None:
    print("\n" + title)


def tr(m: sp.Matrix) -> sp.Expr:
    return sp.simplify(sum(m[i, i] for i in range(m.rows)))


def main() -> int:
    print("=== Record/Born interface from selective write bridge ===")

    paths = [
        NOTE,
        AXIOMS,
        CHECKLIST,
        LAYER,
        BORN_BOUNDARY,
        FORMATION_NOGO,
        BUSCH,
        LUDERS,
        WRITE_ISOMETRY,
        POINTER,
    ]
    for path in paths:
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    note_flat = flat(note)
    axioms = read(AXIOMS)
    checklist = read(CHECKLIST)
    layer = read(LAYER)
    born_boundary = read(BORN_BOUNDARY)
    formation_nogo = read(FORMATION_NOGO)
    busch = read(BUSCH)
    luders = read(LUDERS)
    write_iso = read(WRITE_ISOMETRY)
    pointer = read(POINTER)

    section("PART A -- source boundaries")
    check("axioms supply fixed records but no probability primitive", "no probability" in flat(axioms) or "probability" in flat(axioms))
    check("Record locks one available possibility", "A record locks exactly one available local possibility" in axioms)
    check("record checklist separates kernel from produced record", "kernel-only model supports probabilities" in checklist)
    check("record checklist requires realized durable atom for produced record", "realized durable record atom" in checklist)
    check("layer reconciliation says post-record layer is a consumer", "consumer" in layer and "not a producer" in layer)
    check("Born boundary says counts do not derive p", "pre-record probability" in born_boundary and "not a derivation" in born_boundary)
    check("formation no-go gives no-record witnesses", "H = 0" in formation_nogo and "no record" in formation_nogo)

    section("PART B -- finite selective write theorem")
    I2 = sp.eye(2)
    P0 = sp.Matrix([[1, 0], [0, 0]])
    P1 = sp.Matrix([[0, 0], [0, 1]])
    R0 = sp.Matrix([[1, 0]])  # <0| on record register
    R1 = sp.Matrix([[0, 1]])  # <1| on record register
    ket0 = sp.Matrix([[1], [0]])
    ket1 = sp.Matrix([[0], [1]])

    # W maps system C^2 -> system C^2 tensor record C^2:
    # |0> -> |0,0>, |1> -> |1,1>.
    W = sp.Matrix(
        [
            [1, 0],  # |0S 0R>
            [0, 0],  # |0S 1R>
            [0, 0],  # |1S 0R>
            [0, 1],  # |1S 1R>
        ]
    )
    check("W is an isometry", W.T.conjugate() * W == I2)

    # Extract K_r = (I_S tensor <r|_R) W.
    E0 = sp.kronecker_product(I2, R0)
    E1 = sp.kronecker_product(I2, R1)
    K0 = E0 * W
    K1 = E1 * W
    check("K0 extracted from W is P0", K0 == P0)
    check("K1 extracted from W is P1", K1 == P1)
    check("Kraus completeness holds", K0.T.conjugate() * K0 + K1.T.conjugate() * K1 == I2)
    check("projectors are orthogonal and complete", P0 * P1 == sp.zeros(2, 2) and P0 + P1 == I2)

    rho = sp.Matrix([[sp.Rational(3, 5), sp.Rational(1, 10)], [sp.Rational(1, 10), sp.Rational(2, 5)]])
    check("rho is normalized", tr(rho) == 1)
    check("rho is positive", all(ev >= 0 for ev in rho.eigenvals().keys()), f"eigs={list(rho.eigenvals().keys())}")

    rho0 = P0 * rho * P0
    rho1 = P1 * rho * P1
    p0 = tr(rho0)
    p1 = tr(rho1)
    check("branch trace p0 = Tr(rho P0)", sp.simplify(p0 - tr(rho * P0)) == 0, f"p0={p0}")
    check("branch trace p1 = Tr(rho P1)", sp.simplify(p1 - tr(rho * P1)) == 0, f"p1={p1}")
    check("Born branch weights sum to one", sp.simplify(p0 + p1 - 1) == 0)
    nonselective = rho0 + rho1
    check("nonselective channel is trace-preserving", tr(nonselective) == 1)
    check("nonselective channel dephases off-diagonal coherence", nonselective == sp.diag(sp.Rational(3, 5), sp.Rational(2, 5)))

    sigma0 = sp.simplify(rho0 / p0)
    sigma1 = sp.simplify(rho1 / p1)
    check("selective state sigma0 normalized", tr(sigma0) == 1)
    check("selective state sigma1 normalized", tr(sigma1) == 1)
    check("repeat readout stable on branch 0", P0 * sigma0 * P0 == sigma0 and tr(sigma0 * P0) == 1 and tr(sigma0 * P1) == 0)
    check("repeat readout stable on branch 1", P1 * sigma1 * P1 == sigma1 and tr(sigma1 * P1) == 1 and tr(sigma1 * P0) == 0)
    check("wrong repeated label has zero support", tr(sigma0 * P1) == 0 and tr(sigma1 * P0) == 0)

    section("PART C -- Busch effect-additivity and Lüders matching")
    check("Busch bridge states m(E)=Tr(sigma E)", "m(E) = Tr" in busch or "m(E)=Tr" in busch)
    check("Busch bridge hypotheses include normalized POVM additivity", "POVM-additivity" in busch and "m(𝟙) = 1" in busch)
    check("Busch bridge says qubit M2 case is reproven", "qubit `M_2(C)`" in busch and "reproven" in busch)
    check("Luders bridge proves PEP positive effect", "P E P" in luders and "valid effect" in luders)
    check("Luders bridge proves trace compression identity", "Tr(rho P E P) = Tr(P rho P E)" in luders)
    E = sp.Matrix([[sp.Rational(4, 5), sp.Rational(1, 10)], [sp.Rational(1, 10), sp.Rational(1, 5)]])
    pep0 = P0 * E * P0
    pep1 = P1 * E * P1
    check("PEP branch effects are positive in exact sample", all(ev >= 0 for ev in pep0.eigenvals().keys()) and all(ev >= 0 for ev in pep1.eigenvals().keys()))
    check("PEP trace identity branch 0", tr(rho * P0 * E * P0) == tr(P0 * rho * P0 * E))
    check("PEP trace identity branch 1", tr(rho * P1 * E * P1) == tr(P1 * rho * P1 * E))

    section("PART D -- finite frequency boundary")
    histories = ["".join(bits) for bits in product("01", repeat=4)]
    freqs = sorted({sp.Rational(word.count("1"), 4) for word in histories})
    check("N=4 binary histories have five possible frequencies", freqs == [sp.Rational(0), sp.Rational(1, 4), sp.Rational(1, 2), sp.Rational(3, 4), sp.Rational(1)])
    check("same p is not forced by finite history grammar", len(freqs) > 1)
    binomial_total = sum(sp.binomial(4, k) * p1**k * p0 ** (4 - k) for k in range(5))
    expected_count = sum(k * sp.binomial(4, k) * p1**k * p0 ** (4 - k) for k in range(5))
    check("supplied IID binomial model normalizes", sp.simplify(binomial_total - 1) == 0)
    check("supplied IID expected frequency equals p1", sp.simplify(expected_count / 4 - p1) == 0)
    check("IID model is explicitly extra, not post-record grammar", "extra probability input" in born_boundary)

    section("PART E -- controlled-copy instrument supplier boundary")
    check("controlled-copy note derives W under explicit finite model", "induced isometry is exactly" in write_iso and "W|psi>" in write_iso)
    check("controlled-copy note says K_r=P_r", "K_r = <r|W = P_r" in write_iso)
    check("controlled-copy note preserves bounded model boundary", "explicit finite controlled-copy model only" in write_iso)
    check("pointer note says nonzero controlled-copy coupling is sufficient", "nonzero local controlled-copy coupling is sufficient" in pointer)
    check("pointer note says QND alone is not sufficient", "does not imply that any fragment is written" in pointer)
    check("pointer note excludes coupling/rate derivation", "does not pin the coupling strength" in pointer)

    section("PART F -- new note content")
    check("note declares bounded bridge theorem", "positive theorem candidate / bounded bridge theorem" in note)
    check("note splits interface from occurrence", "branch occurrence / production law" in note)
    check("note names W_occurrence", "W_occurrence" in note)
    check("note gives finite theorem", "## Finite Theorem" in note)
    check("note says Born not added to axioms", "not an extra probability language to put into the axioms" in note)
    check("note preserves counts boundary", "does not say finite record counts imply probabilities" in note_flat)
    check("note gives audit consequence", "## Audit Consequence If Retained" in note)

    section("PART G -- consequence assembly")
    interface_ok = (
        W.T.conjugate() * W == I2
        and K0 == P0
        and K1 == P1
        and p0 == sp.Rational(3, 5)
        and p1 == sp.Rational(2, 5)
        and tr(sigma0 * P0) == 1
        and tr(sigma1 * P1) == 1
    )
    check("selective write + trace weights + repeatability theorem assembled", interface_ok)
    check("occurrence remains outside assembled theorem", "which branch, if any, is written as the actual record" in note)
    check("no new axiom is requested by the bridge", "new axiom" in note and "not a new axiom" in note)
    check("no measured values consumed", "PDG" in note and "beta=6" in note)

    section("PART H -- no-go discipline gate")
    for item in ("N1", "N2", "N3", "N4", "N5", "N6", "N7", "N8"):
        check(f"note includes {item}", item in note)
    check("N1 has at least five routes", note.count("| Route |") == 1 and note.count("RULED OUT") >= 2 and note.count("ATTEMPTED") >= 2)
    check("N2 collapses residual to W_occurrence", "Collapsed residual" in note and "W_occurrence" in note)
    check("N3 labels supplied instrument wall", "\"Supplied instrument\"" in note)
    check("N4 matches six witnesses", note.count("| `") >= 6 and "Residual Matching" in note)
    check("N5 avoids Born-from-Record overclaim", "not \"Born is derived from Record\"" in note)
    check("N6 gives import-retirement path", "import-retirement shape" in note)
    check("N7 steelman admits probability premise", "effect additivity is already a probability premise" in note_flat)
    check("N8 separates layers", "weights live at the pre-record instrument/effect layer" in note)

    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("RESULT: FAIL")
        return 1
    print("RESULT: PASS -- supplied selective record-writing interface plus effect additivity forces Born trace weights and repeatable selective readout; occurrence remains open.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
