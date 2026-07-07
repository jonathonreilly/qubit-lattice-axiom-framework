#!/usr/bin/env python3
from __future__ import annotations

import ast
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

SOURCE_NEEDLES = {
    "docs/MINIMAL_AXIOMS_2026-06-29.md": [
        "Only records are readable. A readout value is determined by record content\nalone.",
        "For any finite collection of pairwise-disjoint records, scalar readout\n`I` is additive, with `I(empty)=0`.",
    ],
    "docs/GRADED_CONSTRAINT_PROGRAM_AND_RECORD_INFLUENCE_CRITERION_2026-07-04.md": [
        "The form of the weights is a theorem target, not a postulate.",
        "If grading\n  exists, is additive over exclusive alternatives, and does not depend on which\n  compatible menu embeds an alternative, then Gleason-type uniqueness forces\n  the quadratic (Born) form.",
        "The known dimension-2 exception is exactly one\n  `M_2` site alone; neighbor composites are `M_4` and above, where the theorem\n  holds \u2014 the lattice, which the axioms supply for free, is what eliminates the\n  loophole.",
        "This is a theorem target, not a landed result: the landed Class D\n  proposal `docs/GRADED_CONSTRAINT_PRIMITIVE_REGISTRATION_PROPOSAL_2026-07-04.md`\n  records that any live use must arrive as a fresh, self-contained conditional\n  note through review/audit.",
    ],
    "docs/COLOR_SINGLET_RECORDS_G2_FACTORIZATION_SITE_LOCAL_LOCKING_BOUNDED_THEOREM_NOTE_2026-07-06.md": [
        "MARGINAL-READ (named premise, introduced here): record-visible data about an\nedge state is represented at the state level by single-site reduced density\nmatrices.",
    ],
    "docs/GAUGE_FACTOR_PRESERVATION_RECORD_TYPED_SELECTOR_CONDITIONAL_DECOMPOSITION_BOUNDED_THEOREM_NOTE_2026-07-06.md": [
        "REGISTERED-FACTOR (named premise, introduced here):\nthe record/readout structure registers a fixed factor subalgebra of the local domain; equivalently, the split\n  M_3 tensor I_2 / I_3 tensor M_2\nis record-typed data.",
    ],
}


def mat_zero(rows: int, cols: int) -> list[list[Fraction]]:
    return [[Fraction(0) for _ in range(cols)] for _ in range(rows)]


def mat_identity(n: int) -> list[list[Fraction]]:
    out = mat_zero(n, n)
    for i in range(n):
        out[i][i] = Fraction(1)
    return out


def mat_basis(n: int, row: int, col: int) -> list[list[Fraction]]:
    out = mat_zero(n, n)
    out[row][col] = Fraction(1)
    return out


def matmul(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    rows = len(a)
    mid = len(b)
    cols = len(b[0])
    out = mat_zero(rows, cols)
    for i in range(rows):
        for k in range(mid):
            if a[i][k] == 0:
                continue
            for j in range(cols):
                out[i][j] += a[i][k] * b[k][j]
    return out


def mat_trace(a: list[list[Fraction]]) -> Fraction:
    return sum(a[i][i] for i in range(len(a)))


def mat_equal(a: list[list[Fraction]], b: list[list[Fraction]]) -> bool:
    return a == b


def kron(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    rows = len(a) * len(b)
    cols = len(a[0]) * len(b[0])
    out = mat_zero(rows, cols)
    for i, row in enumerate(a):
        for j, value in enumerate(row):
            for k, brow in enumerate(b):
                for ell, bvalue in enumerate(brow):
                    out[i * len(b) + k][j * len(b[0]) + ell] = value * bvalue
    return out


def partial_trace_partner(rho: list[list[Fraction]]) -> list[list[Fraction]]:
    out = mat_zero(2, 2)
    for site_row in range(2):
        for site_col in range(2):
            total = Fraction(0)
            for partner in range(2):
                total += rho[2 * site_row + partner][2 * site_col + partner]
            out[site_row][site_col] = total
    return out


def rank_q(matrix: list[list[Fraction]]) -> int:
    if not matrix:
        return 0
    a = [row[:] for row in matrix]
    rows = len(a)
    cols = len(a[0])
    rank = 0
    for col in range(cols):
        pivot = None
        for row in range(rank, rows):
            if a[row][col] != 0:
                pivot = row
                break
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        pivot_value = a[rank][col]
        a[rank] = [value / pivot_value for value in a[rank]]
        for row in range(rows):
            if row == rank or a[row][col] == 0:
                continue
            factor = a[row][col]
            a[row] = [a[row][c] - factor * a[rank][c] for c in range(cols)]
        rank += 1
        if rank == rows:
            break
    return rank


def verify_source_needles() -> str:
    count = 0
    for relpath, needles in SOURCE_NEEDLES.items():
        text = (ROOT / relpath).read_text(encoding="utf-8")
        for needle in needles:
            assert needle in text, f"missing source quote in {relpath}: {needle!r}"
            count += 1
    return f"files=4 needles={count}"


def partial_trace_first(rho: list[list[Fraction]]) -> list[list[Fraction]]:
    # Marginal on the SECOND factor: trace out the first tensor slot.
    out = mat_zero(2, 2)
    for site_row in range(2):
        for site_col in range(2):
            total = Fraction(0)
            for partner in range(2):
                total += rho[2 * partner + site_row][2 * partner + site_col]
            out[site_row][site_col] = total
    return out


def verify_partial_trace_restriction() -> str:
    id2 = mat_identity(2)
    rho_basis = [mat_basis(4, row, col) for row in range(4) for col in range(4)]
    site_basis = [mat_basis(2, row, col) for row in range(2) for col in range(2)]
    checked = 0
    for rho in rho_basis:
        rho_site = partial_trace_partner(rho)
        rho_site2 = partial_trace_first(rho)
        for observable in site_basis:
            lifted = kron(observable, id2)
            left = mat_trace(matmul(rho, lifted))
            right = mat_trace(matmul(rho_site, observable))
            assert left == right
            lifted2 = kron(id2, observable)
            left2 = mat_trace(matmul(rho, lifted2))
            right2 = mat_trace(matmul(rho_site2, observable))
            assert left2 == right2
            checked += 2
    return f"basis_pairs={checked} over_Q both_factors"


def verify_registered_factor_bookkeeping() -> str:
    id2 = mat_identity(2)
    basis = [mat_basis(2, row, col) for row in range(2) for col in range(2)]
    lifted_identity = kron(id2, id2)
    assert mat_equal(lifted_identity, mat_identity(4))
    checked = 0
    for left in basis:
        for right in basis:
            lifted_product = matmul(kron(left, id2), kron(right, id2))
            product_lifted = kron(matmul(left, right), id2)
            assert mat_equal(lifted_product, product_lifted)
            checked += 1
    return f"typed_subalgebra_closure_products={checked}"


def bloch_frame_value(point: tuple[Fraction, Fraction, Fraction]) -> Fraction:
    z = point[2]
    return (Fraction(1) + z * z * z) / 2


def verify_m2_frame_counterexample() -> str:
    q = Fraction
    base_points = [
        (q(3, 5), q(0), q(4, 5)),
        (q(0), q(3, 5), q(4, 5)),
        (q(4, 5), q(0), q(-3, 5)),
        (q(0), q(1), q(0)),
        (q(1), q(0), q(0)),
        (q(0), q(0), q(1)),
    ]
    all_points = []
    for point in base_points:
        x, y, z = point
        assert x * x + y * y + z * z == 1
        antipode = (-x, -y, -z)
        assert bloch_frame_value(point) + bloch_frame_value(antipode) == 1
        all_points.append(point)
        all_points.append(antipode)

    system = [[x, y, z] for x, y, z in all_points]
    rhs = [[z * z * z] for _, _, z in all_points]
    augmented = [row[:] + rhs_row for row, rhs_row in zip(system, rhs)]
    rank_a = rank_q(system)
    rank_aug = rank_q(augmented)
    assert rank_a == 3
    assert rank_aug == 4
    return f"antipodal_pairs={len(base_points)} rankA={rank_a} rankAug={rank_aug}"


def verify_ast_self_scan() -> str:
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source)
    forbidden_imports = {"subprocess", "socket", "urllib", "requests", "http", "ftplib"}
    forbidden_calls = {"write_text", "write_bytes", "unlink", "rename", "replace", "mkdir", "rmdir"}
    checked_calls = 0
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                root_name = alias.name.split(".")[0]
                assert root_name not in forbidden_imports, f"forbidden import {alias.name}"
        elif isinstance(node, ast.ImportFrom):
            root_name = (node.module or "").split(".")[0]
            assert root_name not in forbidden_imports, f"forbidden import {node.module}"
        elif isinstance(node, ast.Call):
            checked_calls += 1
            if isinstance(node.func, ast.Name) and node.func.id == "open":
                mode = "r"
                if len(node.args) >= 2 and isinstance(node.args[1], ast.Constant):
                    mode = str(node.args[1].value)
                for keyword in node.keywords:
                    if keyword.arg == "mode" and isinstance(keyword.value, ast.Constant):
                        mode = str(keyword.value.value)
                assert not any(flag in mode for flag in ("w", "a", "x", "+")), "write-mode open"
            if isinstance(node.func, ast.Attribute):
                assert node.func.attr not in forbidden_calls, f"forbidden call {node.func.attr}"
    return f"ast_calls={checked_calls} read_only"


def main() -> int:
    checks = [
        ("source quote audit", verify_source_needles),
        ("T1 partial-trace restriction", verify_partial_trace_restriction),
        ("T1 registered-factor bookkeeping", verify_registered_factor_bookkeeping),
        ("T2 M2 frame additivity and no-density obstruction", verify_m2_frame_counterexample),
        ("AST self-scan", verify_ast_self_scan),
        ("declaration inputs", lambda: "Gleason_external_not_reproved Born_not_derived"),
    ]
    passed = 0
    failed = 0
    for label, check in checks:
        try:
            details = check()
        except Exception as exc:  # noqa: BLE001
            failed += 1
            print(f"[FAIL] {label} -- {exc}")
        else:
            passed += 1
            print(f"[PASS] {label} -- {details}")
    print(
        "DECLARATION FRAME-EXT=conditional_premise "
        "gap=FINITE-ADDITIVITY-TO-FRAME "
        "composite_REP_requires_external_Gleason"
    )
    print(f"TOTAL PASS={passed} FAIL={failed}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
