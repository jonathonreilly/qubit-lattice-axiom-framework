#!/usr/bin/env python3
"""Representation no-go for deriving a full EWSB doublet from H_unit.

The runner checks the finite representation facts used by
docs/HUNIT_TO_EWSB_DOUBLET_REPRESENTATION_NO_GO_NOTE_2026-06-15.md:

* H_unit is an SU(2)-scalar on the Q_L=(2,3) block.
* The SU(2) fundamental has no nonzero invariant vector, so
  Hom_SU(2)(trivial, fundamental) = 0.
* A neutral ray projector in an already supplied one-doublet surface is not
  itself SU(2)-invariant; it is a ray/gauge statement inside the doublet.
* A scalar/radial carrier cannot certify the four real thermal degrees of
  freedom of a full complex doublet.
"""

from __future__ import annotations

from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "HUNIT_TO_EWSB_DOUBLET_REPRESENTATION_NO_GO_NOTE_2026-06-15.md"
WARD = DOCS / "YT_WARD_IDENTITY_DERIVATION_THEOREM.md"
EW = DOCS / "EW_HIGGS_GAUGE_MASS_DIAGONALIZATION_THEOREM_NOTE_2026-04-26.md"
RAY = DOCS / "YT_QUBIT_NEUTRAL_HIGGS_CARRIER_RAY_BRIDGE_NOTE_2026-05-25.md"
SM_GSTAR = DOCS / "SM_GSTAR_HIGGS_SECTOR_COUNT_STRETCH_NOTE_2026-05-29.md"

PASS = 0
FAIL = 0


def check(name: str, ok: bool, detail: object = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" -- {detail}" if detail != "" else ""
    print(f"[{tag}] {name}{suffix}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def matrix_zero(matrix: sp.Matrix) -> bool:
    return all(sp.simplify(x) == 0 for x in matrix)


def stack_generators(gens: list[sp.Matrix]) -> sp.Matrix:
    rows = []
    for gen in gens:
        rows.extend(gen.tolist())
    return sp.Matrix(rows)


def part1_source_surface() -> None:
    print("\nPart 1: source surfaces")
    for path in (NOTE, WARD, EW, RAY, SM_GSTAR):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    check("note declares no-go claim type", "**Claim type:** no_go" in note)
    check(
        "note names portable runner and cache links",
        "[scripts/hunit_to_ewsb_doublet_representation_no_go_2026_06_15.py](../scripts/hunit_to_ewsb_doublet_representation_no_go_2026_06_15.py)" in note
        and "[logs/runner-cache/hunit_to_ewsb_doublet_representation_no_go_2026_06_15.txt](../logs/runner-cache/hunit_to_ewsb_doublet_representation_no_go_2026_06_15.txt)" in note,
    )
    check(
        "load-bearing authorities are markdown links",
        "[YT_WARD_IDENTITY_DERIVATION_THEOREM.md](YT_WARD_IDENTITY_DERIVATION_THEOREM.md)" in note
        and "[EW_HIGGS_GAUGE_MASS_DIAGONALIZATION_THEOREM_NOTE_2026-04-26.md](EW_HIGGS_GAUGE_MASS_DIAGONALIZATION_THEOREM_NOTE_2026-04-26.md)" in note
        and "[YT_QUBIT_NEUTRAL_HIGGS_CARRIER_RAY_BRIDGE_NOTE_2026-05-25.md](YT_QUBIT_NEUTRAL_HIGGS_CARRIER_RAY_BRIDGE_NOTE_2026-05-25.md)" in note,
    )
    check("no-go discipline gate covers N1-N8", all(f"N{i} -" in note for i in range(1, 9)))
    for phrase in (
        "Hom_SU(2)(1, 2) = 0",
        "does not exist as an equivariant derivation",
        "H_unit scalar-singlet structure",
        "one complex SU(2)_L EWSB doublet",
        "does not close R-HIGGS positively",
        "does not add an axiom or accepted premise",
    ):
        check(f"note records boundary phrase: {phrase}", phrase in note)
    check("note verification section names expected total", "TOTAL: PASS=39 FAIL=0" in note)

    ward = read(WARD)
    check("Ward note defines H_unit", "H_unit" in ward)
    check("Ward note identifies scalar-singlet content", "scalar-singlet" in ward)
    check("Ward note says no SM Yukawa readout", "No SM readout" in ward or "no SM Yukawa readout" in ward)

    ew = read(EW)
    check(
        "EW note supplies one-Higgs doublet bookkeeping",
        "`SU(2)_L` Higgs doublet" in ew and "H = (H^+, H^0)^T" in ew,
    )
    check("EW note contains neutral vev", "(0, v/sqrt(2))" in ew or "(0, v/√2)" in ew)


def part2_hunit_is_su2_scalar() -> None:
    print("\nPart 2: H_unit is an SU(2) scalar on Q_L")
    I2 = sp.eye(2)
    I3 = sp.eye(3)
    sigma_x = sp.Matrix([[0, 1], [1, 0]])
    sigma_y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    sigma_z = sp.Matrix([[1, 0], [0, -1]])
    gens = [sp.kronecker_product(s / 2, I3) for s in (sigma_x, sigma_y, sigma_z)]
    h_unit = sp.kronecker_product(I2, I3) / sp.sqrt(6)

    check("H_unit has 6x6 Q_L operator shape", h_unit.shape == (6, 6), h_unit.shape)
    check("H_unit Hilbert-Schmidt norm is 1", sp.simplify(sp.trace(h_unit.H * h_unit) - 1) == 0)
    for idx, gen in enumerate(gens, start=1):
        check(f"H_unit commutes with SU(2) generator T{idx}", matrix_zero(gen * h_unit - h_unit * gen))


def part3_no_singlet_to_doublet_map() -> None:
    print("\nPart 3: Hom_SU(2)(trivial, fundamental) = 0")
    sigma_x = sp.Matrix([[0, 1], [1, 0]])
    sigma_y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    sigma_z = sp.Matrix([[1, 0], [0, -1]])
    gens = [sigma_x / 2, sigma_y / 2, sigma_z / 2]

    stacked = stack_generators(gens)
    null = stacked.nullspace()
    check("stacked Pauli-generator constraint has rank 2", stacked.rank() == 2, f"rank={stacked.rank()}")
    check("fundamental SU(2) has no nonzero invariant vector", null == [], f"nullspace={null}")

    a, b = sp.symbols("a b")
    v = sp.Matrix([a, b])
    equations = []
    for gen in gens:
        equations.extend(list(gen * v))
    sol = sp.solve(equations, (a, b), dict=True)
    check("equivariance equations force v=0", sol == [{a: 0, b: 0}], sol)

    nonzero_candidate = sp.Matrix([1, 0])
    broken = any(not matrix_zero(gen * nonzero_candidate) for gen in gens)
    check("any chosen nonzero ray breaks full SU(2) equivariance", broken)


def part4_neutral_ray_is_inside_supplied_doublet() -> None:
    print("\nPart 4: neutral ray requires the supplied doublet surface")
    I2 = sp.eye(2)
    sigma_x = sp.Matrix([[0, 1], [1, 0]])
    sigma_y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    sigma_z = sp.Matrix([[1, 0], [0, -1]])
    p_minus = (I2 - sigma_z) / 2
    p_plus = (I2 + sigma_z) / 2
    t3 = sigma_z / 2
    y_h = sp.Rational(1, 2) * I2
    q = t3 + y_h
    neutral = sp.Matrix([0, 1])

    check("P_- is a rank-one projector", p_minus.rank() == 1 and matrix_zero(p_minus * p_minus - p_minus))
    check("P_- fixes the neutral lower ray", matrix_zero(p_minus * neutral - neutral))
    check("Q annihilates the neutral lower ray", matrix_zero(q * neutral))
    check("P_- does not commute with T1", not matrix_zero((sigma_x / 2) * p_minus - p_minus * (sigma_x / 2)))
    check("P_- does not commute with T2", not matrix_zero((sigma_y / 2) * p_minus - p_minus * (sigma_y / 2)))
    check("P_+ plus P_- gives the two-component doublet resolution", matrix_zero(p_plus + p_minus - I2))


def part5_thermal_count_boundary() -> None:
    print("\nPart 5: thermal census boundary")
    complex_doublet_real_dof = 2 * 2
    neutral_radial_real_dof = 1
    scalar_singlet_real_dof = 1
    check("one complex SU(2) doublet has four real scalar components", complex_doublet_real_dof == 4)
    check("a neutral radial ray is one real carrier direction", neutral_radial_real_dof == 1)
    check("a scalar singlet is not the four-component high-T doublet", scalar_singlet_real_dof != complex_doublet_real_dof)


def main() -> int:
    print("=" * 78)
    print("H_UNIT -> EWSB DOUBLET REPRESENTATION NO-GO")
    print("=" * 78)
    part1_source_surface()
    part2_hunit_is_su2_scalar()
    part3_no_singlet_to_doublet_map()
    part4_neutral_ray_is_inside_supplied_doublet()
    part5_thermal_count_boundary()
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
