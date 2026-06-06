#!/usr/bin/env python3
"""Six diagonal E_ii operators: finite orthonormal-basis reproof.

This runner checks only the pure diagonal component-response lemma for
V = C^6:

    O_i = E_ii, i = 1..6, form an orthonormal basis of the diagonal subspace
    D_6 under <A,B>_HS = Tr(A^dagger B), resolve I_6, reconstruct every
    diagonal operator, and have the democratic unit
    O_dem = (1/sqrt(6)) sum_i O_i.

It deliberately does not identify these six coordinates with physical Y_T
top/W response directions, source semantics, g_bare, F_Htt, y_33, y_t, or any
Standard-Model source coefficient. Those bridges are outside this narrowed row.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "audit_companion_source_measure_sharp_record_onb_2026_06_05.json"

NOTE = DOCS / "SOURCE_MEASURE_SHARP_RECORD_ORTHONORMAL_RESPONSE_BASIS_NARROW_THEOREM_NOTE_2026-06-05.md"
TARGET_NOTE = DOCS / "SOURCE_MEASURE_SHARP_RECORD_TANGENT_SPACE_THEOREM_NOTE_2026-05-30.md"

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, ok: bool, detail: Any = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if ok:
        PASS_COUNT += 1
        tag = "PASS"
    else:
        FAIL_COUNT += 1
        tag = "FAIL"
    suffix = f": {detail}" if detail != "" else ""
    print(f"[{tag}] {name}{suffix}")


def info(name: str, detail: Any = "") -> None:
    suffix = f": {detail}" if detail != "" else ""
    print(f"[INFO] {name}{suffix}")


def is_zero(expr: sp.Expr) -> bool:
    return sp.simplify(expr) == 0


DIM = 6


def diagonal_response_operators_sympy() -> list[sp.Matrix]:
    """O_i = E_ii as exact sympy matrices."""
    ops = []
    for i in range(DIM):
        matrix = sp.zeros(DIM, DIM)
        matrix[i, i] = 1
        ops.append(matrix)
    return ops


def vector_response_operators_sympy() -> list[sp.Matrix]:
    """Equivalent coordinate realization of the diagonal subspace D_6."""
    return [sp.eye(DIM)[:, i] for i in range(DIM)]


def adjacent_swap_matrix(i: int) -> sp.Matrix:
    matrix = sp.eye(DIM)
    matrix[i, i] = 0
    matrix[i + 1, i + 1] = 0
    matrix[i, i + 1] = 1
    matrix[i + 1, i] = 1
    return matrix


def part1_source_boundary() -> dict[str, Any]:
    """Check that the companion note is narrowed to the finite E_ii lemma."""
    print("\nPart 1: source-note boundary")
    check("companion note exists", NOTE.exists(), NOTE.relative_to(ROOT))
    if not NOTE.exists():
        info("boundary checks skipped because companion note is absent")
        return {"note_present": False}

    text = NOTE.read_text(encoding="utf-8")
    check("note declares pure diagonal component-response lemma", "pure diagonal component-response lemma" in text)
    check("note says it is not a physical Y_T/top/W response theorem", "not a physical `Y_T` top/`W` response theorem" in text)
    check("note says it does not derive g_bare", "does not derive `g_bare`" in text)
    check(
        "old same-source Y_T/top/W basis phrase is absent",
        "same-source orthonormal `Y_T` top/`W` response basis" not in text,
    )
    check(
        "old top/W form-factor matching claim is absent",
        "matching the top/`W` form factor" not in text,
    )
    if TARGET_NOTE.exists():
        info(f"context target present: {TARGET_NOTE.relative_to(ROOT)}")
    else:
        info(f"context target absent: {TARGET_NOTE.relative_to(ROOT)}")
    return {"note_present": True}


def part2_fixed_diagonal_carrier() -> dict[str, Any]:
    """Construct the six diagonal matrix units on one fixed C^6."""
    print("\nPart 2: fixed C^6 diagonal carrier")
    check("ambient vector space dimension is fixed to 6", DIM == 6, DIM)

    ops = diagonal_response_operators_sympy()
    check("there are exactly six operators O_i", len(ops) == 6, len(ops))
    check("all six O_i act on the same C^6 ambient space", all(op.shape == (DIM, DIM) for op in ops))
    check("each O_i is Hermitian", all(op.H == op for op in ops))
    check("each O_i is idempotent", all(op * op == op for op in ops))

    supports = [
        tuple((r, c) for r in range(DIM) for c in range(DIM) if ops[i][r, c] != 0)
        for i in range(DIM)
    ]
    check("each O_i has exactly one nonzero diagonal entry", all(len(support) == 1 for support in supports), supports)
    check("the six supports are distinct", len(set(supports)) == DIM)
    return {"dim": DIM, "operator_count": len(ops)}


def part3_orthonormal_gram_sympy() -> dict[str, Any]:
    """Hilbert-Schmidt Gram G_ij = Tr(O_i^dagger O_j) = I_6."""
    print("\nPart 3: Hilbert-Schmidt Gram = I_6")
    ops = diagonal_response_operators_sympy()
    gram = sp.zeros(DIM, DIM)
    for i in range(DIM):
        for j in range(DIM):
            gram[i, j] = sp.trace(ops[i].H * ops[j])

    check("HS Gram matrix equals the 6x6 identity", gram == sp.eye(DIM), gram)
    check("each O_i has unit HS norm", all(gram[i, i] == 1 for i in range(DIM)))
    check(
        "distinct O_i are HS-orthogonal",
        all(gram[i, j] == 0 for i in range(DIM) for j in range(DIM) if i != j),
    )

    vecs = vector_response_operators_sympy()
    vector_gram = sp.Matrix(DIM, DIM, lambda i, j: (vecs[i].H * vecs[j])[0])
    check("coordinate-vector realization gives the same identity Gram", vector_gram == sp.eye(DIM), vector_gram)
    return {"gram_is_identity": True}


def part4_diagonal_completeness_sympy() -> dict[str, Any]:
    """Rank, identity resolution, and exact reconstruction in D_6."""
    print("\nPart 4: diagonal completeness and reconstruction")
    ops = diagonal_response_operators_sympy()
    flat = sp.Matrix([[ops[k][r, c] for r in range(DIM) for c in range(DIM)] for k in range(DIM)])
    rank = flat.rank()
    check("the six O_i are linearly independent", rank == DIM, rank)
    check("rank equals dim(D_6) = 6", rank == 6)

    resolution = sp.zeros(DIM, DIM)
    for op in ops:
        resolution += op
    check("the six O_i resolve the identity: sum_i O_i = I_6", resolution == sp.eye(DIM), resolution)

    d = sp.symbols("d0:6")
    diagonal = sp.diag(*d)
    coeffs = [sp.trace(ops[i].H * diagonal) for i in range(DIM)]
    reconstructed = sp.zeros(DIM, DIM)
    for i in range(DIM):
        reconstructed += coeffs[i] * ops[i]
    check("HS coefficients recover the diagonal entries d_i", [sp.simplify(coeffs[i] - d[i]) for i in range(DIM)] == [0] * DIM)
    check("every symbolic diagonal operator reconstructs exactly", sp.simplify(reconstructed - diagonal) == sp.zeros(DIM, DIM))
    return {"rank": int(rank), "resolves_identity": True}


def part5_democratic_diagonal_unit_sympy() -> dict[str, Any]:
    """O_dem = (1/sqrt(6)) sum_i O_i is the unit S_6-fixed diagonal vector."""
    print("\nPart 5: democratic diagonal unit")
    vecs = vector_response_operators_sympy()
    o_dem = sp.zeros(DIM, 1)
    for vector in vecs:
        o_dem += vector
    o_dem = o_dem / sp.sqrt(DIM)

    norm2 = sp.simplify((o_dem.H * o_dem)[0])
    check("O_dem has unit HS norm", is_zero(norm2 - 1), norm2)
    check("all six components of O_dem equal 1/sqrt(6)", all(is_zero(o_dem[i] - 1 / sp.sqrt(6)) for i in range(DIM)), list(o_dem))
    check("component amplitude is 1/sqrt(6)", is_zero((vecs[0].H * o_dem)[0] - 1 / sp.sqrt(6)))

    for i in range(DIM - 1):
        check(f"O_dem is invariant under adjacent coordinate swap {i}<->{i + 1}", adjacent_swap_matrix(i) * o_dem == o_dem)

    fixed_equations = sp.Matrix(
        [[1 if c == r else -1 if c == r + 1 else 0 for c in range(DIM)] for r in range(DIM - 1)]
    )
    fixed_rank = fixed_equations.rank()
    fixed_nullity = DIM - fixed_rank
    check("adjacent-swap fixed subspace has nullity one", fixed_nullity == 1, {"rank": fixed_rank, "nullity": fixed_nullity})

    lam = sp.symbols("lambda", positive=True)
    norm_lam = sp.simplify(((lam * o_dem).H * (lam * o_dem))[0])
    check("lambda*O_dem has HS norm lambda^2", is_zero(norm_lam - lam**2), norm_lam)
    check("unit-response condition selects lambda = 1", sp.solve(sp.Eq(norm_lam, 1), lam) == [1])
    return {"democratic_amplitude": "1/sqrt(6)", "fixed_nullity": int(fixed_nullity)}


def part6_numpy_cross_check() -> dict[str, Any]:
    """Independent floating-point checks of the same finite identities."""
    print("\nPart 6: numpy cross-check")
    ops = [np.zeros((DIM, DIM), dtype=float) for _ in range(DIM)]
    for i in range(DIM):
        ops[i][i, i] = 1.0

    gram = np.array([[np.trace(ops[i].T @ ops[j]) for j in range(DIM)] for i in range(DIM)])
    gram_err = float(np.max(np.abs(gram - np.eye(DIM))))
    check("numpy HS Gram = I_6 to 1e-12", gram_err < 1e-12, gram_err)

    flat = np.array([ops[k].reshape(-1) for k in range(DIM)])
    rank = int(np.linalg.matrix_rank(flat, tol=1e-9))
    check("numpy rank of the six O_i is 6", rank == DIM, rank)

    resolution_err = float(np.max(np.abs(sum(ops) - np.eye(DIM))))
    check("numpy identity resolution holds to 1e-12", resolution_err < 1e-12, resolution_err)

    diagonal_entries = np.array([1.25, -2.0, 0.5, 3.0, -4.5, 6.75])
    diagonal = np.diag(diagonal_entries)
    coeffs = np.array([np.trace(ops[i].T @ diagonal) for i in range(DIM)])
    reconstructed = sum(coeffs[i] * ops[i] for i in range(DIM))
    recon_err = float(np.max(np.abs(reconstructed - diagonal)))
    check("numpy diagonal reconstruction holds to 1e-12", recon_err < 1e-12, recon_err)
    return {"gram_max_err": gram_err, "rank": rank, "resolution_err": resolution_err, "recon_err": recon_err}


def main() -> int:
    print("=" * 80)
    print("SIX DIAGONAL E_ii OPERATORS — FINITE ORTHONORMAL-BASIS REPROOF")
    print("=" * 80)
    result: dict[str, Any] = {}
    result["source_boundary"] = part1_source_boundary()
    result["fixed_carrier"] = part2_fixed_diagonal_carrier()
    result["gram"] = part3_orthonormal_gram_sympy()
    result["completeness"] = part4_diagonal_completeness_sympy()
    result["democratic_unit"] = part5_democratic_diagonal_unit_sympy()
    result["numpy"] = part6_numpy_cross_check()
    result["summary"] = {
        "pass": PASS_COUNT,
        "fail": FAIL_COUNT,
        "load_bearing": "finite E_ii diagonal-basis theorem only",
        "physical_bridges_claimed": False,
    }

    try:
        OUTPUT.parent.mkdir(parents=True, exist_ok=True)
        OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(f"\nwrote {OUTPUT.relative_to(ROOT)}")
    except OSError as exc:  # pragma: no cover - output is a convenience only
        info(f"could not write output json (non-fatal): {exc}")

    print("\n" + "=" * 80)
    print(f"TOTAL: {PASS_COUNT} PASS / {FAIL_COUNT} FAIL")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
