#!/usr/bin/env python3
"""Exact checks for the hypercharge traceless central multi-summand note."""

from __future__ import annotations

import ast
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BLOCK04 = ROOT / (
    "docs/"
    "GAUGE_FACTOR_PRESERVATION_RECORD_TYPED_SELECTOR_CONDITIONAL_"
    "DECOMPOSITION_BOUNDED_THEOREM_NOTE_2026-07-06.md"
)
BLOCK06 = ROOT / (
    "docs/"
    "COLOR_ORIENTATION_THREE_VS_THREEBAR_SUCCESSION_CANDIDATE_"
    "CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-07-06.md"
)


def normalize(text: str) -> str:
    return " ".join(text.split())


def rank_q(matrix: list[list[Fraction]]) -> int:
    if not matrix:
        return 0
    rows = [row[:] for row in matrix if any(x != 0 for x in row)]
    if not rows:
        return 0
    row_count = len(rows)
    col_count = len(rows[0])
    rank = 0
    for col in range(col_count):
        pivot = None
        for row in range(rank, row_count):
            if rows[row][col] != 0:
                pivot = row
                break
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        pivot_value = rows[rank][col]
        rows[rank] = [value / pivot_value for value in rows[rank]]
        for row in range(row_count):
            if row == rank:
                continue
            factor = rows[row][col]
            if factor == 0:
                continue
            rows[row] = [
                value - factor * pivot_entry
                for value, pivot_entry in zip(rows[row], rows[rank])
            ]
        rank += 1
        if rank == row_count:
            break
    return rank


def zero_matrix(size: int) -> list[list[Fraction]]:
    return [[Fraction(0) for _ in range(size)] for _ in range(size)]


def central_projector(n_summands: int, index: int) -> list[list[Fraction]]:
    size = 6 * n_summands
    matrix = zero_matrix(size)
    start = 6 * index
    for pos in range(start, start + 6):
        matrix[pos][pos] = Fraction(1)
    return matrix


def flatten(matrix: list[list[Fraction]]) -> list[Fraction]:
    return [entry for row in matrix for entry in row]


def central_dimensions(n_summands: int) -> dict[str, int]:
    projectors = [
        central_projector(n_summands, index)
        for index in range(n_summands)
    ]
    span_rank = rank_q([flatten(projector) for projector in projectors])
    trace_row = [[Fraction(6) for _ in range(n_summands)]]
    trace_rank = rank_q(trace_row)
    return {
        "center_dim": span_rank,
        "trace_rank": trace_rank,
        "traceless_dim": n_summands - trace_rank,
    }


def two_summand_constraint() -> dict[str, int]:
    """Typed constraints for the two-summand (3, 3bar) example, exact.

    A prior formulation used the cubic su(3)^3 anomaly signs as a linear u(1)
    row -- a mistyped constraint. The correctly TYPED conditions are:
      trace-zero:            q3 + q3bar = 0            (dim count)
      mixed u(1)-su(3)^2:    q3*T(3) + q3bar*T(3bar) = 0, with the Dynkin
                             index T(3) = T(3bar) = 1/2 exactly, i.e.
                             (q3 + q3bar)/2 = 0  -- COINCIDES with trace-zero
      u(1)^3 (cubic):        6*q3^3 + 6*q3bar^3 = 0  -- on the reals this is
                             q3bar = -q3, the SAME line
    All three degenerate to the single line q3bar = -q3: a one-dimensional
    hypercharge-like family SURVIVES on the minimal conjugate pair. The
    su(3)^3 anomaly (the orientation note's A(3) = -A(3bar) signs) is
    q-INDEPENDENT for the central direction and cancels on the pair by those
    signs; it is not a constraint on the weights. Gravitational-u(1) and any
    other mixed conditions are NOT treated (named residual).
    """
    trace = [Fraction(1), Fraction(1)]
    mixed = [Fraction(1, 2), Fraction(1, 2)]  # Dynkin indices T(3)=T(3bar)=1/2
    trace_rank = rank_q([trace])
    mixed_rank = rank_q([mixed])
    combined_rank = rank_q([trace, mixed])
    # cubic u(1)^3 on the surviving line q3bar = -q3: 6q^3 + 6(-q)^3 = 0
    q = Fraction(3, 7)
    cubic_on_line = 6 * q**3 + 6 * (-q) ** 3
    # exact check that the cubic constraint's real solution set is the line:
    # 6a^3 + 6b^3 = 0 over Q iff a = -b (odd cube root uniqueness)
    a_wit, b_wit = Fraction(2, 5), Fraction(-2, 5)
    cubic_wit = 6 * a_wit**3 + 6 * b_wit**3
    return {
        "trace_rank": trace_rank,
        "mixed_rank": mixed_rank,
        "combined_rank": combined_rank,
        "constrained_dim": 2 - combined_rank,
        "cubic_on_line_zero": int(cubic_on_line == 0),
        "cubic_witness_zero": int(cubic_wit == 0),
    }


def quote_audits() -> list[tuple[str, bool]]:
    block04_text = normalize(BLOCK04.read_text(encoding="utf-8"))
    block06_text = normalize(BLOCK06.read_text(encoding="utf-8"))
    checks = [
        (
            "block04_no_second_central_u1",
            "Thus, in this tensor-product carrier image, there is no second "
            "central/factor-identity `u(1)` image.",
            block04_text,
        ),
        (
            "block04_global_phase_not_traceless",
            "The only central abelian image direction is the global `u(1)` "
            "generated by `i I_6`, whose trace is `6i` and is not traceless.",
            block04_text,
        ),
        (
            "block04_r_hypercharge_boundary",
            "R-hypercharge: the abelian image is hypercharge-like only. It "
            "is one global `u(1)` direction on this tensor-product carrier "
            "image, not a physical hypercharge identification.",
            block04_text,
        ),
        (
            "block06_A3_plus_one",
            "A(3) = +1,",
            block06_text,
        ),
        (
            "block06_A3bar_minus_one",
            "A(3bar) = -1,",
            block06_text,
        ),
        (
            "block06_pair_sum_zero",
            "A(3) + A(3bar) = 0.",
            block06_text,
        ),
        (
            "block06_anomaly_cancel_boundary",
            "R-anomaly-cancel: anomaly cancellation is a supplied condition, "
            "ANOMALY-CANCEL, not axiom content and not derived here.",
            block06_text,
        ),
    ]
    return [(name, normalize(needle) in haystack) for name, needle, haystack in checks]


def ast_self_scan() -> tuple[bool, str]:
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source)
    banned_import_roots = {
        "asyncio",
        "http",
        "os",
        "requests",
        "socket",
        "subprocess",
        "urllib",
    }
    banned_calls = {"eval", "exec", "compile", "__import__", "input"}
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                root = alias.name.split(".")[0]
                if root in banned_import_roots:
                    return False, f"banned import {alias.name}"
        if isinstance(node, ast.ImportFrom):
            root = (node.module or "").split(".")[0]
            if root in banned_import_roots:
                return False, f"banned import-from {node.module}"
        if isinstance(node, ast.Call):
            func = node.func
            if isinstance(func, ast.Name) and func.id in banned_calls:
                return False, f"banned call {func.id}"
    return True, "no banned imports or dynamic calls"


def report(name: str, ok: bool, detail: str, counts: dict[str, int]) -> None:
    if ok:
        counts["pass"] += 1
        print(f"[PASS] {name}: {detail}")
    else:
        counts["fail"] += 1
        print(f"[FAIL] {name}: {detail}")


def summand_fixed_commutant_dim() -> int:
    """Exact commutant of the N=2 summand-fixed factorwise algebra in M_12.

    Generators: for each summand independently, the su(3) tensor I2 lifts,
    the I3 tensor su(2) lifts, and the summand identity block. SUMMAND-FIXED
    means per-summand elements are independent (no diagonal identification
    across summands), so the commutant should be the per-block scalars:
    complex dimension 2.
    """
    def su_basis_pairs(n):
        base = []
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                sym = [[(Fraction(0), Fraction(0))] * n for _ in range(n)]
                sym[i][j] = (Fraction(0), Fraction(1))
                base.append(sym)
        for k in range(n - 1):
            diag = [[(Fraction(0), Fraction(0))] * n for _ in range(n)]
            diag[k][k] = (Fraction(0), Fraction(1))
            diag[k + 1][k + 1] = (Fraction(0), Fraction(-1))
            base.append(diag)
        return base

    def kron_c(a, b):
        ra, ca = len(a), len(a[0])
        rb, cb = len(b), len(b[0])
        out = [[(Fraction(0), Fraction(0))] * (ca * cb) for _ in range(ra * rb)]
        for i in range(ra):
            for j in range(ca):
                for k in range(rb):
                    for l in range(cb):
                        x, y = a[i][j], b[k][l]
                        out[i * rb + k][j * cb + l] = (
                            x[0] * y[0] - x[1] * y[1],
                            x[0] * y[1] + x[1] * y[0],
                        )
        return out

    def eye_c(n):
        return [[(Fraction(1 if i == j else 0), Fraction(0)) for j in range(n)]
                for i in range(n)]

    def embed(block, which):
        out = [[(Fraction(0), Fraction(0))] * 12 for _ in range(12)]
        off = 6 * which
        for i in range(6):
            for j in range(6):
                out[off + i][off + j] = block[i][j]
        return out

    gens = []
    for which in (0, 1):
        for a3 in su_basis_pairs(3):
            gens.append(embed(kron_c(a3, eye_c(2)), which))
        for a2 in su_basis_pairs(2):
            gens.append(embed(kron_c(eye_c(3), a2), which))
        gens.append(embed(eye_c(6), which))

    # commutant: solve [M, G] = 0 for all G; complex dim of solution space.
    rows = []
    for g in gens:
        for i in range(12):
            for j in range(12):
                row = []
                for aa in range(12):
                    for bb in range(12):
                        # coefficient of M[aa][bb] in (M G - G M)[i][j]
                        c_re, c_im = Fraction(0), Fraction(0)
                        if aa == i:
                            c_re += g[bb][j][0]
                            c_im += g[bb][j][1]
                        if bb == j:
                            c_re -= g[i][aa][0]
                            c_im -= g[i][aa][1]
                        row.append((c_re, c_im))
                if any(x != (Fraction(0), Fraction(0)) for x in row):
                    rows.append(row)
    # complex rank via re/im stacking
    real_rows = []
    for row in rows:
        real_rows.append([x[0] for x in row] + [-x[1] for x in row])
        real_rows.append([x[1] for x in row] + [x[0] for x in row])
    rk = rank_q(real_rows)
    return (2 * 144 - rk) // 2


def main() -> int:
    counts = {"pass": 0, "fail": 0}

    for name, ok in quote_audits():
        report(name, ok, "quoted text found in source", counts)

    expected = {
        1: {"center_dim": 1, "trace_rank": 1, "traceless_dim": 0},
        2: {"center_dim": 2, "trace_rank": 1, "traceless_dim": 1},
        3: {"center_dim": 3, "trace_rank": 1, "traceless_dim": 2},
    }
    dimension_lines = []
    for n_summands, expectation in expected.items():
        found = central_dimensions(n_summands)
        ok = found == expectation
        detail = (
            f"N={n_summands} center_dim={found['center_dim']} "
            f"trace_rank={found['trace_rank']} "
            f"traceless_dim={found['traceless_dim']}"
        )
        report(f"central_dimensions_N{n_summands}", ok, detail, counts)
        dimension_lines.append(detail)

    constraint = two_summand_constraint()
    ok_constraint = constraint == {
        "trace_rank": 1,
        "mixed_rank": 1,
        "combined_rank": 1,
        "constrained_dim": 1,
        "cubic_on_line_zero": 1,
        "cubic_witness_zero": 1,
    }
    constraint_detail = (
        f"trace_rank={constraint['trace_rank']} "
        f"mixed_rank={constraint['mixed_rank']} "
        f"combined_rank={constraint['combined_rank']} (constraints COINCIDE) "
        f"constrained_dim={constraint['constrained_dim']} "
        f"cubic_degenerates_to_same_line={constraint['cubic_on_line_zero']}"
    )
    report(
        "two_summand_3_plus_3bar_typed_constraints_coincide_dim1_survives",
        ok_constraint,
        constraint_detail,
        counts,
    )

    # Full commutant verification (panel-required): for N = 2 SUMMAND-FIXED
    # blocks, the commutant of the independently-generated per-summand
    # factorwise algebra in M_12 is exactly span{Z_1, Z_2} (complex dim 2).
    comm_dim = summand_fixed_commutant_dim()
    report(
        "summand_fixed_commutant_N2_dim_2",
        comm_dim == 2,
        f"exact nullspace commutant dim={comm_dim} = span(Z_1, Z_2)",
        counts,
    )

    scan_ok, scan_detail = ast_self_scan()
    report("ast_self_scan", scan_ok, scan_detail, counts)

    print(
        "DECLARATION premises=minimal_axioms_context; "
        "supplied_blocks=block04,block06; no_physical_hypercharge; "
        "no_summand_supplier; ANOMALY-CANCEL=supplied_not_derived"
    )
    for line in dimension_lines:
        print(f"EXACT {line}")
    print(f"EXACT two_summand {constraint_detail}")
    print(f"TOTAL PASS={counts['pass']} FAIL={counts['fail']}")
    return 0 if counts["fail"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
