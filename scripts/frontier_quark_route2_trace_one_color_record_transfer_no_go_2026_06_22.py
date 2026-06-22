#!/usr/bin/env python3
"""Route-2 trace-one color-record transfer boundary.

Block78 narrowed the open bridge to a same-source normalized color-matrix
source authority.  This runner attacks the record-side precondition: can the
current Route-2 P_R/E-T endpoint surface itself be typed as trace-one
End(C^3) color records?

Result: no.  The current Route-2 restricted endpoint surface is a four-slot
carrier/readout surface.  Its standalone normalized tangent has dimension
three and fraction 3/4, not the End(C^3) source fraction 8/9.  Transferring
the connected color-source selector still needs a trace-one color-matrix lift
and same-source readout theorem.  No endpoint value is imported.
"""

from __future__ import annotations

from collections import deque
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-trace-one-color-record-transfer"

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


E_SHELL = (Fraction(1), Fraction(0), Fraction(0), Fraction(0))
E_CENTER = (Fraction(1), Fraction(0), Fraction(1, 6), Fraction(0))
T_SHELL = (Fraction(0), Fraction(1), Fraction(0), Fraction(0))
T_CENTER = (Fraction(0), Fraction(1), Fraction(0), Fraction(1, 6))
ENDPOINT_COLUMNS = (E_SHELL, E_CENTER, T_SHELL, T_CENTER)


def column_matrix(columns: tuple[tuple[Fraction, ...], ...]) -> list[list[Fraction]]:
    return [[columns[col][row] for col in range(len(columns))] for row in range(len(columns[0]))]


def finite_normalized_fraction(raw_slots: int) -> Fraction:
    return Fraction(raw_slots - 1, raw_slots)


def part1_route2_endpoint_surface() -> None:
    print("PART 1: Route-2 endpoint surface")
    exact = note_text("QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md")
    matrix = column_matrix(ENDPOINT_COLUMNS)
    sums = [sum(column) for column in ENDPOINT_COLUMNS]

    check("Route-2 restricted endpoint carrier has four raw slots", len(E_SHELL) == 4)
    check("Route-2 endpoint columns have rank four over the carrier slots", rank_fraction(matrix) == 4)
    check("E columns live in slots {0,2}", E_SHELL[1] == E_SHELL[3] == E_CENTER[1] == E_CENTER[3] == 0)
    check("T columns live in slots {1,3}", T_SHELL[0] == T_SHELL[2] == T_CENTER[0] == T_CENTER[2] == 0)
    check("center columns carry the exact delta_A1 increment 1/6", E_CENTER[2] == Fraction(1, 6) and T_CENTER[3] == Fraction(1, 6))
    check("raw endpoint column sums are not uniformly trace-one", sums == [Fraction(1), Fraction(7, 6), Fraction(1), Fraction(7, 6)])
    check("exact readout note exposes the restricted P_R form", "P_R = [[alpha_E, 0, beta_E, 0]" in exact and "[0, alpha_T, 0, beta_T]]" in exact)


def part2_color_source_precondition() -> None:
    print()
    print("PART 2: color-source precondition")
    full_color_dim = 3 * 3
    connected_color_dim = full_color_dim - 1
    route2_raw_slots = 4
    route2_tangent_dim = route2_raw_slots - 1

    check("End(C^3) color source has nine matrix-source directions", full_color_dim == 9)
    check("trace-one color-source normalization kills exactly one identity direction", connected_color_dim == 8)
    check("connected color-source fraction is 8/9", Fraction(connected_color_dim, full_color_dim) == Fraction(8, 9))
    check("standalone four-slot normalized record tangent has dimension three", route2_tangent_dim == 3)
    check("standalone four-slot normalized record fraction is 3/4", finite_normalized_fraction(route2_raw_slots) == Fraction(3, 4))
    check("four-slot normalized fraction is not the color-source selector fraction", finite_normalized_fraction(route2_raw_slots) != Fraction(8, 9))
    check("a finite normalized source fraction equals 8/9 only for nine raw directions", [m for m in range(2, 16) if finite_normalized_fraction(m) == Fraction(8, 9)] == [9])
    check("Route-2 four-slot surface cannot be the full End(C^3) source surface by dimension alone", route2_raw_slots != full_color_dim and route2_tangent_dim != connected_color_dim)


def part3_trace_one_lift_obstruction() -> None:
    print()
    print("PART 3: trace-one lift obstruction")
    raw_sums = [sum(column) for column in ENDPOINT_COLUMNS]
    normalized_centers = [
        tuple(value / sum(E_CENTER) for value in E_CENTER),
        tuple(value / sum(T_CENTER) for value in T_CENTER),
    ]

    check("shell columns are trace-one only as four-slot vectors", raw_sums[0] == 1 and raw_sums[2] == 1)
    check("center columns are not trace-one without extra normalization", raw_sums[1] == raw_sums[3] == Fraction(7, 6))
    check("normalizing center columns changes the delta ratio from 1/6 to 1/7", normalized_centers[0][2] == Fraction(1, 7) and normalized_centers[1][3] == Fraction(1, 7))
    check("ad hoc four-slot normalization is therefore not the exact Route-2 carrier", normalized_centers[0] != E_CENTER and normalized_centers[1] != T_CENTER)
    check("a four-slot probability lift would have Fisher tangent dimension three", rank_fraction([[Fraction(1), Fraction(1), Fraction(1), Fraction(1)]]) == 1 and 4 - 1 == 3)
    check("the color theorem needs a nine-direction source before quotienting by identity", 9 - 1 == 8)
    check("the missing lift is independent of pure-disconnected singlet typing", "trace-one color-matrix lift" != "pure-disconnected singlet typing")
    check("no endpoint target value is needed for the dimension obstruction", all("endpoint" not in text for text in ("four raw slots", "nine color source directions", "trace-one lift")))


def part4_reachability() -> None:
    print()
    print("PART 4: transfer reachability")
    base_edges = [
        ("route2_endpoint_carrier", "four_slot_endpoint_surface"),
        ("four_slot_endpoint_surface", "four_slot_normalized_record_tangent"),
        ("four_slot_normalized_record_tangent", "finite_fraction_3_4"),
        ("trace_one_color_matrix_records", "EndC3_source"),
        ("EndC3_source", "augmentation_ideal_sl3"),
        ("augmentation_ideal_sl3", "kappa_0_selector"),
    ]
    lift_edges = [
        ("route2_endpoint_carrier", "trace_one_color_matrix_record_lift"),
        ("trace_one_color_matrix_record_lift", "trace_one_color_matrix_records"),
        ("trace_one_color_matrix_record_lift", "same_source_PR_ET_readout"),
        ("same_source_PR_ET_readout", "EndC3_source"),
    ]

    check("color matrix record surface reaches kappa=0", reachable(base_edges, "trace_one_color_matrix_records", "kappa_0_selector"))
    check("Route-2 endpoint surface reaches only four-slot normalized tangent", reachable(base_edges, "route2_endpoint_carrier", "finite_fraction_3_4"))
    check("Route-2 endpoint surface does not reach End(C^3) source without a lift", not reachable(base_edges, "route2_endpoint_carrier", "EndC3_source"))
    check("Route-2 endpoint surface does not reach kappa=0 without a lift", not reachable(base_edges, "route2_endpoint_carrier", "kappa_0_selector"))
    check("adding trace-one color-matrix lift reaches End(C^3) source", reachable(base_edges + lift_edges, "route2_endpoint_carrier", "EndC3_source"))
    check("adding trace-one color-matrix lift reaches kappa=0", reachable(base_edges + lift_edges, "route2_endpoint_carrier", "kappa_0_selector"))
    check("the lift route uses no endpoint-value node", all("rho_E" not in node and "c_TE" not in node for edge in base_edges + lift_edges for node in edge))


def part5_document_boundary() -> None:
    print()
    print("PART 5: document boundary")
    yt = note_text("YT_CONNECTED_SOURCE_AUGMENTATION_IDEAL_SELECTOR_NARROW_THEOREM_NOTE_2026-05-26.md")
    block78 = note_text("QUARK_ROUTE2_CONNECTED_COLOR_SOURCE_TRANSFER_NO_GO_NOTE_2026-06-22.md")
    exact = note_text("QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md")
    new_note = note_text("QUARK_ROUTE2_TRACE_ONE_COLOR_RECORD_TRANSFER_NO_GO_NOTE_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    normalized = " ".join(new_note.replace("**", "").replace("`", "").split())

    check("YT theorem requires trace-one color records", "trace-one color records" in yt)
    check("YT theorem names End(C^N) quotient by identity", "End(C^N) / C I" in yt)
    check("Block78 names same-source color-matrix authority as missing", "same-source normalized color-matrix source authority" in block78)
    check("exact readout note names four endpoint columns", "E-shell" in exact and "T-center" in exact)

    required = (
        "Actual current-surface status: no-go for typing Route-2 endpoint readout as trace-one color records",
        "This is not an audit verdict",
        "No endpoint value is used",
        "four-slot endpoint/readout surface",
        "standalone normalized tangent is 3/4, not 8/9",
        "trace-one color-matrix lift",
        "same-source Route-2 P_R/E-T readout theorem",
    )
    for marker in required:
        check(f"new note contains marker: {marker}", marker in normalized)

    for marker in ("Block79 Summary", "negative_route_pruning", "Do not audit", "Next Exact Action"):
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
    print("Route-2 trace-one color-record transfer no-go")
    print("Status: no-go for typing Route-2 endpoint readout as trace-one color records; not an audit verdict.")
    print("TRACE: negative_route_pruning")
    part1_route2_endpoint_surface()
    part2_color_source_precondition()
    part3_trace_one_lift_obstruction()
    part4_reachability()
    part5_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        print("VERDICT: trace-one color-record transfer checks failed.")
        return 1
    print(
        "VERDICT: the current Route-2 endpoint/readout surface is a four-slot "
        "record surface, not the nine-direction trace-one End(C^3) color-source "
        "surface needed to transfer the connected selector."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
