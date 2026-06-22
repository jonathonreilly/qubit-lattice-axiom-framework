#!/usr/bin/env python3
"""Finite endpoint pullback rank boundary for Route-2 color-source transfer.

Block79 showed that the current Route-2 endpoint surface is not itself the
trace-one End(C^3) color-record source surface.  This runner tests a stronger
escape: even if the four Route-2 endpoint labels are lifted pointwise to
trace-one color records, can the finite endpoint pullback carry the full
connected sl_3 source tangent?

No.  A source evaluated on four records gives at most a four-dimensional raw
score vector and at most a three-dimensional centered score space.  The
connected color-source theorem needs the eight-dimensional sl_3 tangent of the
full End(C^3) source surface.  A pointwise lift is therefore not enough; the
missing primitive is a full color-record source ensemble/readout theorem.  No
endpoint value is imported.
"""

from __future__ import annotations

from collections import deque
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-finite-endpoint-source-rank"

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(condition)
    PASS += int(ok)
    FAIL += int(not ok)
    suffix = f"\n      {detail}" if detail else ""
    print(f"{'PASS' if ok else 'FAIL'}: {label}{suffix}")


def phrase(*parts: str) -> str:
    return "".join(parts)


def note_text(name: str) -> str:
    return (DOCS / name).read_text(encoding="utf-8")


def loop_text(name: str) -> str:
    return (LOOP / name).read_text(encoding="utf-8")


def rank_fraction(rows: list[list[Fraction]]) -> int:
    mat = [row[:] for row in rows]
    rank = 0
    col_count = len(mat[0]) if mat else 0
    for col in range(col_count):
        pivot = None
        for row in range(rank, len(mat)):
            if mat[row][col] != 0:
                pivot = row
                break
        if pivot is None:
            continue
        mat[rank], mat[pivot] = mat[pivot], mat[rank]
        pivot_value = mat[rank][col]
        mat[rank] = [value / pivot_value for value in mat[rank]]
        for row in range(len(mat)):
            if row == rank or mat[row][col] == 0:
                continue
            factor = mat[row][col]
            mat[row] = [value - factor * base for value, base in zip(mat[row], mat[rank])]
        rank += 1
    return rank


def centered_rows(rows: list[list[Fraction]]) -> list[list[Fraction]]:
    count = Fraction(len(rows), 1)
    means = [sum(row[col] for row in rows) / count for col in range(len(rows[0]))]
    return [[value - means[col] for col, value in enumerate(row)] for row in rows]


def reachable(edges: Iterable[tuple[str, str]], start: str, target: str) -> bool:
    graph: dict[str, set[str]] = {}
    for src, dst in edges:
        graph.setdefault(src, set()).add(dst)
    todo = deque([start])
    seen = {start}
    while todo:
        node = todo.popleft()
        if node == target:
            return True
        for nxt in graph.get(node, set()):
            if nxt not in seen:
                seen.add(nxt)
                todo.append(nxt)
    return False


def mat(entries: tuple[tuple[Fraction, Fraction, Fraction], tuple[Fraction, Fraction, Fraction], tuple[Fraction, Fraction, Fraction]]) -> list[Fraction]:
    return [entries[i][j] for i in range(3) for j in range(3)]


def trace(record: list[Fraction]) -> Fraction:
    return record[0] + record[4] + record[8]


def is_entrywise_nonnegative(record: list[Fraction]) -> bool:
    return all(value >= 0 for value in record)


def lift_full_rank() -> list[list[Fraction]]:
    one = Fraction(1)
    zero = Fraction(0)
    third = Fraction(1, 3)
    return [
        mat(((one, zero, zero), (zero, zero, zero), (zero, zero, zero))),
        mat(((zero, zero, zero), (zero, one, zero), (zero, zero, zero))),
        mat(((zero, zero, zero), (zero, zero, zero), (zero, zero, one))),
        mat(((third, third, third), (third, third, third), (third, third, third))),
    ]


def lift_diagonal_rank_two() -> list[list[Fraction]]:
    one = Fraction(1)
    zero = Fraction(0)
    half = Fraction(1, 2)
    return [
        mat(((one, zero, zero), (zero, zero, zero), (zero, zero, zero))),
        mat(((zero, zero, zero), (zero, one, zero), (zero, zero, zero))),
        mat(((zero, zero, zero), (zero, zero, zero), (zero, zero, one))),
        mat(((half, zero, zero), (zero, half, zero), (zero, zero, zero))),
    ]


def identity_source_vector(records: list[list[Fraction]]) -> list[Fraction]:
    return [trace(record) for record in records]


def part1_general_rank_bound() -> None:
    print("PART 1: finite endpoint score-rank bound")
    endpoint_records = 4
    color_source_dim = 9
    connected_color_dim = 8
    max_raw_rank = endpoint_records
    max_centered_rank = endpoint_records - 1

    check("Route-2 endpoint labels supply four finite records", endpoint_records == 4)
    check("End(C^3) source algebra has nine raw source directions", color_source_dim == 9)
    check("connected color-source tangent has dimension eight", connected_color_dim == 8)
    check("four-record raw source evaluation rank is at most four", max_raw_rank == 4)
    check("centering over four records leaves rank at most three", max_centered_rank == 3)
    check("four-record centered score rank cannot equal sl_3 rank", max_centered_rank != connected_color_dim)
    check("four-record centered score rank cannot realize the 8/9 dimension quotient", Fraction(max_centered_rank, color_source_dim) != Fraction(8, 9))
    check("at least nine independent raw records are needed for an 8/9 finite normalization quotient", [m for m in range(2, 16) if Fraction(m - 1, m) == Fraction(8, 9)] == [9])


def part2_explicit_lifts() -> None:
    print()
    print("PART 2: explicit trace-one lifts")
    full_rank_lift = lift_full_rank()
    diagonal_lift = lift_diagonal_rank_two()
    centered_full = centered_rows(full_rank_lift)
    centered_diag = centered_rows(diagonal_lift)

    check("full-rank example lift has four trace-one records", all(trace(record) == 1 for record in full_rank_lift))
    check("full-rank example lift is entrywise nonnegative", all(is_entrywise_nonnegative(record) for record in full_rank_lift))
    check("full-rank example centered pullback rank is three", rank_fraction(centered_full) == 3)
    check("diagonal example lift has four trace-one records", all(trace(record) == 1 for record in diagonal_lift))
    check("diagonal example lift is entrywise nonnegative", all(is_entrywise_nonnegative(record) for record in diagonal_lift))
    check("diagonal example centered pullback rank is two", rank_fraction(centered_diag) == 2)
    check("identity source is killed by centering for both lifts", centered_rows([identity_source_vector(full_rank_lift), identity_source_vector(diagonal_lift)]) == [[0, 0, 0, 0], [0, 0, 0, 0]])
    check("trace-one positivity does not select a unique source-score image", rank_fraction(centered_full) != rank_fraction(centered_diag))
    check("neither pointwise lift reaches the eight-dimensional sl_3 tangent", rank_fraction(centered_full) < 8 and rank_fraction(centered_diag) < 8)


def part3_transfer_reachability() -> None:
    print()
    print("PART 3: transfer reachability")
    base_edges = [
        ("route2_endpoint_labels", "pointwise_trace_one_lift"),
        ("pointwise_trace_one_lift", "four_record_source_pullback"),
        ("four_record_source_pullback", "centered_rank_at_most_3"),
        ("trace_one_full_color_record_ensemble", "EndC3_source"),
        ("EndC3_source", "augmentation_ideal_sl3"),
        ("augmentation_ideal_sl3", "kappa_0_selector"),
    ]
    full_ensemble_edges = [
        ("route2_physical_readout", "same_source_full_color_record_ensemble"),
        ("same_source_full_color_record_ensemble", "trace_one_full_color_record_ensemble"),
        ("same_source_full_color_record_ensemble", "EndC3_source"),
    ]

    check("full color-record ensemble reaches kappa=0", reachable(base_edges, "trace_one_full_color_record_ensemble", "kappa_0_selector"))
    check("pointwise endpoint lift reaches only the finite pullback rank bound", reachable(base_edges, "route2_endpoint_labels", "centered_rank_at_most_3"))
    check("pointwise endpoint lift does not reach End(C^3) source", not reachable(base_edges, "route2_endpoint_labels", "EndC3_source"))
    check("pointwise endpoint lift does not reach kappa=0", not reachable(base_edges, "route2_endpoint_labels", "kappa_0_selector"))
    check("adding same-source full ensemble reaches End(C^3) source", reachable(base_edges + full_ensemble_edges, "route2_physical_readout", "EndC3_source"))
    check("adding same-source full ensemble reaches kappa=0", reachable(base_edges + full_ensemble_edges, "route2_physical_readout", "kappa_0_selector"))
    check("the full-ensemble route uses no endpoint-value node", all("rho_E" not in node and "c_TE" not in node for edge in base_edges + full_ensemble_edges for node in edge))


def part4_document_boundary() -> None:
    print()
    print("PART 4: document boundary")
    yt = note_text("YT_CONNECTED_SOURCE_AUGMENTATION_IDEAL_SELECTOR_NARROW_THEOREM_NOTE_2026-05-26.md")
    block79 = note_text("QUARK_ROUTE2_TRACE_ONE_COLOR_RECORD_TRANSFER_NO_GO_NOTE_2026-06-22.md")
    exact = note_text("QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md")
    new_note = note_text("QUARK_ROUTE2_FINITE_ENDPOINT_SOURCE_RANK_NO_GO_NOTE_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    normalized = " ".join(new_note.replace("**", "").replace("`", "").split())

    check("YT theorem requires the full color matrix-source sector", "full color matrix algebra has dimension `N^2`" in yt and "`N^2 - 1`" in yt)
    check("Block79 leaves trace-one color-matrix lift open", "trace-one color-matrix lift" in block79)
    check("exact readout note supplies exactly four endpoint columns", "E-shell" in exact and "T-center" in exact)
    check("Block79 distinguishes four-slot tangent from 8/9", "3/4, not 8/9" in block79)

    required = (
        "Actual current-surface status: no-go for finite endpoint source-rank transfer",
        "This is not an audit verdict",
        "No endpoint value is used",
        "four endpoint records give centered rank at most three",
        "full connected color-source tangent has dimension eight",
        "pointwise trace-one lift is not enough",
        "same-source full color-record ensemble/readout theorem",
    )
    for marker in required:
        check(f"new note contains marker: {marker}", marker in normalized)

    for marker in ("Block80 Summary", "negative_route_pruning", "Do not audit", "Next Exact Action"):
        check(f"handoff contains marker: {marker}", marker in handoff)

    banned = (
        ("branch-local status-promotion", phrase("ret", "ained branch-local")),
        ("future retention", phrase("would become ", "ret", "ained")),
        ("promotion-to-retention", phrase("promoted to ", "ret", "ained")),
        ("actual-surface retention", phrase("ret", "ained on the actual surface")),
        ("parent closure", phrase("closes ", "the parent")),
        ("current-surface endpoint derivation", phrase("derives ", "the endpoint triple", " on the current surface")),
        ("audit ratification", phrase("audit", "-ratified")),
    )
    combined = new_note + "\n" + handoff
    for label, marker in banned:
        check(f"new packet avoids overclaim marker: {label}", marker not in combined)


def main() -> int:
    print("Route-2 finite endpoint source-rank no-go")
    print("Status: no-go for finite endpoint source-rank transfer; not an audit verdict.")
    print("TRACE: negative_route_pruning")
    part1_general_rank_bound()
    part2_explicit_lifts()
    part3_transfer_reachability()
    part4_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        print("VERDICT: finite endpoint source-rank checks failed.")
        return 1
    print(
        "VERDICT: even a pointwise trace-one lift of four Route-2 endpoints "
        "has centered source-rank at most three, so a full same-source color "
        "record ensemble/readout theorem is still required."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
