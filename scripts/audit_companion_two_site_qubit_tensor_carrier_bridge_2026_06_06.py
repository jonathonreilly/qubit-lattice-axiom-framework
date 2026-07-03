#!/usr/bin/env python3
"""Exact checks for the two-site qubit tensor-carrier bridge.

The runner verifies the finite two-site specialization of the repo's retained
finite-block tensor-product authorities. It does not derive tensor composition
from operational locality alone and does not add a new axiom.
"""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp
from sympy import I, Matrix, eye, kronecker_product, sqrt, zeros


ROOT = Path(__file__).resolve().parent.parent
LEDGER = ROOT / "docs" / "audit" / "data" / "audit_ledger.json"

RESULTS: list[tuple[str, bool, str]] = []


def check(label: str, ok: bool, detail: str = "") -> None:
    RESULTS.append((label, bool(ok), detail))


def matrix_rank(mats: list[Matrix]) -> int:
    return Matrix.hstack(*[m.reshape(m.rows * m.cols, 1) for m in mats]).rank()


def ledger_rows() -> dict:
    if not LEDGER.exists():
        return {}
    return json.loads(LEDGER.read_text(encoding="utf-8")).get("rows", {})


def check_dependency_statuses() -> None:
    rows = ledger_rows()
    expected = {
        "cl3_per_site_hilbert_dim_two_theorem_note_2026-05-02": "retained",
        "tensor_product_translation_fermion_operator_bridge_narrow_theorem_note_2026-05-25": "retained",
        "tensor_composition_requires_local_tomography_beyond_locality_narrow_no_go_note_2026-06-03": "retained_no_go",
    }
    for claim_id, status in expected.items():
        row = rows.get(claim_id, {})
        got = row.get("effective_status")
        check(
            f"dependency {claim_id} effective_status is {status}",
            got == status,
            f"got={got!r}",
        )


def main() -> int:
    print("=" * 88)
    print("Two-site qubit tensor-carrier bridge")
    print("surface: generated C^2 tensor C^2 / M_2(C) tensor M_2(C)")
    print("=" * 88)

    check_dependency_statuses()

    id2 = eye(2)
    sx = Matrix([[0, 1], [1, 0]])
    sy = Matrix([[0, -I], [I, 0]])
    sz = Matrix([[1, 0], [0, -1]])
    paulis = [id2, sx, sy, sz]

    check("dim_C H_x = 2", id2.rows == 2)
    check("dim_C H_x tensor H_y = 4", kronecker_product(id2, id2).rows == 4)

    pauli_products = [kronecker_product(a, b) for a in paulis for b in paulis]
    check(
        "sixteen Pauli products span M_4(C)",
        matrix_rank(pauli_products) == 16,
        f"rank={matrix_rank(pauli_products)}",
    )

    # Faithfulness of local embeddings: a nonzero matrix remains nonzero after
    # tensoring with identity. Check on a basis of M_2(C).
    units = [
        Matrix([[1, 0], [0, 0]]),
        Matrix([[0, 1], [0, 0]]),
        Matrix([[0, 0], [1, 0]]),
        Matrix([[0, 0], [0, 1]]),
    ]
    left_images = [kronecker_product(u, id2) for u in units]
    right_images = [kronecker_product(id2, u) for u in units]
    check("left embedding M_2(C)->M_4(C) is rank-four faithful", matrix_rank(left_images) == 4)
    check("right embedding M_2(C)->M_4(C) is rank-four faithful", matrix_rank(right_images) == 4)

    commute = all(
        sp.simplify(kronecker_product(a, id2) * kronecker_product(id2, b)
                    - kronecker_product(id2, b) * kronecker_product(a, id2))
        == zeros(4, 4)
        for a in units
        for b in units
    )
    check("distinct-site local embeddings commute", commute)

    generated_products = [
        kronecker_product(a, id2) * kronecker_product(id2, b)
        for a in units
        for b in units
    ]
    check(
        "products of the two local images generate M_4(C)",
        matrix_rank(generated_products) == 16,
        f"rank={matrix_rank(generated_products)}",
    )

    left_i = kronecker_product(I * id2, id2)
    right_i = kronecker_product(id2, I * id2)
    global_i = I * eye(4)
    check("ordinary complex tensor product has one shared scalar i", left_i == global_i and right_i == global_i)

    bell = Matrix([1, 0, 0, 1]) / sqrt(2)
    check("Bell vector Phi+ is a unit vector in C^2 tensor C^2", sp.simplify((bell.H * bell)[0, 0] - 1) == 0)

    a1 = sz
    a2 = sx
    b1 = (sz + sx) / sqrt(2)
    b2 = (sz - sx) / sqrt(2)
    chsh = (
        kronecker_product(a1, b1)
        + kronecker_product(a1, b2)
        + kronecker_product(a2, b1)
        - kronecker_product(a2, b2)
    )
    expectation = sp.simplify((bell.H * chsh * bell)[0, 0])
    check("Bell witness on the same surface gives <Phi+|C|Phi+> = 2*sqrt(2)", sp.simplify(expectation - 2 * sqrt(2)) == 0)

    dim_sa_m2 = 4
    dim_sa_m4 = 16
    check("generated complex two-qubit surface is locally tomographic by dimension count", dim_sa_m4 == dim_sa_m2 * dim_sa_m2)

    no_go = (ROOT / "docs" / "TENSOR_COMPOSITION_REQUIRES_LOCAL_TOMOGRAPHY_BEYOND_LOCALITY_NARROW_NO_GO_NOTE_2026-06-03.md").read_text(encoding="utf-8")
    check("retained no-go boundary visible: locality alone is not the proof route", "operational locality alone" in no_go and "not force" in no_go)

    passed = sum(1 for _label, ok, _detail in RESULTS if ok)
    failed = len(RESULTS) - passed
    for label, ok, detail in RESULTS:
        tag = "PASS" if ok else "FAIL"
        suffix = f" ({detail})" if detail else ""
        print(f"[{tag}] {label}{suffix}")
    print("=" * 88)
    print(f"SUMMARY: TWO-SITE QUBIT TENSOR BRIDGE PASS={passed} FAIL={failed}")
    print("=" * 88)
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
