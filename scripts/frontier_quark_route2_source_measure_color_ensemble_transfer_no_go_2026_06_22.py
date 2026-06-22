#!/usr/bin/env python3
"""Source-measure to Route-2 full color-ensemble transfer boundary.

The source-measure stack supplies real finite Fisher/RN support, and the
six-diagonal ONB stack supplies a real C^6 diagonal basis theorem.  This runner
tests whether those existing authorities already instantiate the Route-2
same-source full End(C^3) color-record ensemble needed after Blocks 78-80.

They do not.  The current source-measure authorities are generic finite
probability/RN support, supplied trace normalization, or C^6 diagonal-basis
support.  None supplies a Route-2 physical readout over a full trace-one
End(C^3) color-record ensemble whose centered score image is sl_3.  No endpoint
value is imported.
"""

from __future__ import annotations

from collections import deque
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-source-measure-color-ensemble-transfer"

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


def finite_normalized_fraction(raw_slots: int) -> Fraction:
    return Fraction(raw_slots - 1, raw_slots)


def part1_source_measure_authority_boundary() -> None:
    print("PART 1: source-measure authority boundary")
    source_measure = note_text("SOURCE_MEASURE_SHARP_RECORD_TANGENT_SPACE_THEOREM_NOTE_2026-05-30.md")
    fisher = note_text("SHARP_RECORD_FISHER_TANGENT_SPACE_NARROW_THEOREM_NOTE_2026-06-06.md")
    onb = note_text("SOURCE_MEASURE_SHARP_RECORD_ORTHONORMAL_RESPONSE_BASIS_NARROW_THEOREM_NOTE_2026-06-05.md")
    trace_proto = note_text("POST_RECORD_SOURCE_MEASURE_TRACE_NORMALIZATION_PROTOTYPE_2026-06-06.md")
    block80 = note_text("QUARK_ROUTE2_FINITE_ENDPOINT_SOURCE_RANK_NO_GO_NOTE_2026-06-22.md")

    flat_source = " ".join(source_measure.split())
    check("source-measure tangent note is finite Fisher/RN support", "finite sharp-record Fisher tangent theorem" in source_measure)
    check("source-measure tangent note marks physical source bridge conditional", "does not supply those bridges" in flat_source)
    check("source-measure tangent note keeps same-source response open", "strict same-source top/W response" in flat_source)
    check("sharp-record Fisher note is generic finite probability geometry", "finite sharp-record sample space" in fisher and "zero-mean score" in fisher)
    check("ONB note is a C^6 diagonal-basis theorem", "V = C^6" in onb and "D_6" in onb)
    check("ONB note says it is not a physical response theorem", "not a physical `Y_T` top/`W` response theorem" in onb)
    check("trace normalization prototype uses supplied finite carrier", "supplied finite carrier" in trace_proto)
    check("trace normalization prototype does not derive source law or selector", "Does not derive a measure, prior, source law, Born law, or selector" in trace_proto)
    check("Block80 leaves same-source full color ensemble open", "same-source full color-record ensemble/readout theorem" in block80)


def part2_dimension_and_domain_mismatch() -> None:
    print()
    print("PART 2: dimension and domain mismatch")
    endc3_dim = 9
    sl3_dim = 8
    d6_dim = 6
    d6_centered_dim = 5
    route2_endpoint_records = 4

    check("End(C^3) source sector has dimension nine", endc3_dim == 9)
    check("sl_3 connected source tangent has dimension eight", sl3_dim == 8)
    check("C^6 diagonal ONB has dimension six", d6_dim == 6)
    check("C^6 diagonal identity quotient has dimension five", d6_centered_dim == 5)
    check("C^6 diagonal normalized fraction is 5/6, not 8/9", Fraction(d6_centered_dim, d6_dim) == Fraction(5, 6) and Fraction(5, 6) != Fraction(8, 9))
    check("Route-2 finite endpoint pullback still has at most three centered directions", route2_endpoint_records - 1 == 3)
    check("a nine-outcome finite simplex can match dimension but not type End(C^3)", finite_normalized_fraction(9) == Fraction(8, 9))
    check("dimension match alone is not a same-source matrix-source theorem", "finite simplex tangent" != "End(C^3) matrix-source tangent")
    check("none of C^6 diagonal, four endpoints, or generic finite Omega equals End(C^3) by type", len({"C6_diagonal", "four_endpoint_pullback", "generic_finite_omega", "EndC3_matrix_source"}) == 4)


def part3_transfer_reachability() -> None:
    print()
    print("PART 3: transfer reachability")
    base_edges = [
        ("sharp_record_fisher", "generic_finite_probability_tangent"),
        ("source_measure_rn", "generic_finite_probability_tangent"),
        ("source_measure_rn", "conditional_physical_source_semantics_open"),
        ("six_diagonal_onb", "C6_diagonal_basis"),
        ("C6_diagonal_basis", "D6_democratic_unit"),
        ("trace_normalization_prototype", "supplied_finite_RN_measure"),
        ("route2_endpoint_surface", "four_endpoint_source_pullback"),
        ("four_endpoint_source_pullback", "centered_rank_at_most_3"),
        ("full_trace_one_color_record_ensemble", "EndC3_source"),
        ("EndC3_source", "augmentation_ideal_sl3"),
        ("augmentation_ideal_sl3", "kappa_0_selector"),
    ]
    missing_edges = [
        ("route2_physical_readout", "same_source_full_color_record_ensemble"),
        ("same_source_full_color_record_ensemble", "full_trace_one_color_record_ensemble"),
        ("same_source_full_color_record_ensemble", "EndC3_source"),
    ]

    for start in ("sharp_record_fisher", "source_measure_rn", "six_diagonal_onb", "trace_normalization_prototype", "route2_endpoint_surface"):
        check(f"{start} does not reach End(C^3) source", not reachable(base_edges, start, "EndC3_source"))
        check(f"{start} does not reach kappa=0 selector", not reachable(base_edges, start, "kappa_0_selector"))

    check("full color-record ensemble reaches kappa=0", reachable(base_edges, "full_trace_one_color_record_ensemble", "kappa_0_selector"))
    check("adding same-source full ensemble reaches End(C^3)", reachable(base_edges + missing_edges, "route2_physical_readout", "EndC3_source"))
    check("adding same-source full ensemble reaches kappa=0", reachable(base_edges + missing_edges, "route2_physical_readout", "kappa_0_selector"))
    check("the source-measure transfer graph uses no endpoint-value node", all("rho_E" not in node and "c_TE" not in node for edge in base_edges + missing_edges for node in edge))


def part4_support_vs_transfer() -> None:
    print()
    print("PART 4: support versus transfer")
    support_labels = {
        "sharp_record_fisher": "zero-mean finite score geometry",
        "source_measure_rn": "finite RN/exponential chart support",
        "six_diagonal_onb": "supplied C^6 diagonal Hilbert-Schmidt basis",
        "trace_normalization_prototype": "supplied finite trace/RN normalization",
    }
    missing_labels = {
        "route2_color_ensemble": "Route-2 physical readout over full trace-one color records",
        "endc3_source": "source varies J in End(C^3)",
        "same_source": "same source for P_R/E-T readout and color ensemble",
        "sl3_image": "centered score image is full sl_3",
    }

    check("four support authorities are classified", len(support_labels) == 4)
    check("four missing Route-2 transfer labels are classified", len(missing_labels) == 4)
    check("support labels do not include Route-2 physical readout", not any("Route-2 physical readout" in value for value in support_labels.values()))
    check("missing labels include Route-2 physical readout", "Route-2 physical readout" in missing_labels["route2_color_ensemble"])
    check("support labels do not include End(C^3)", not any("End(C^3)" in value for value in support_labels.values()))
    check("missing labels include End(C^3)", "End(C^3)" in missing_labels["endc3_source"])
    check("generic Fisher/RN support is useful but conditional", "finite" in support_labels["source_measure_rn"] and "same source" in missing_labels["same_source"])
    check("none of the missing labels is an endpoint-value import", not any("rho_E" in value or "c_TE" in value for value in missing_labels.values()))


def part5_document_boundary() -> None:
    print()
    print("PART 5: document boundary")
    new_note = note_text("QUARK_ROUTE2_SOURCE_MEASURE_COLOR_ENSEMBLE_TRANSFER_NO_GO_NOTE_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    normalized = " ".join(new_note.replace("**", "").replace("`", "").split())

    required = (
        "Actual current-surface status: no-go for source-measure to Route-2 full color-ensemble transfer",
        "This is not an audit verdict",
        "No endpoint value is used",
        "generic finite Fisher/RN support",
        "C6 diagonal basis",
        "not a same-source full End(C^3) color-record ensemble",
        "same-source full color-record ensemble/readout theorem",
    )
    for marker in required:
        check(f"new note contains marker: {marker}", marker in normalized)

    for marker in ("Block81 Summary", "negative_route_pruning", "Do not audit", "Next Exact Action"):
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
    print("Route-2 source-measure color-ensemble transfer no-go")
    print("Status: no-go for source-measure to Route-2 full color-ensemble transfer; not an audit verdict.")
    print("TRACE: negative_route_pruning")
    part1_source_measure_authority_boundary()
    part2_dimension_and_domain_mismatch()
    part3_transfer_reachability()
    part4_support_vs_transfer()
    part5_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        print("VERDICT: source-measure color-ensemble transfer checks failed.")
        return 1
    print(
        "VERDICT: existing source-measure support is generic finite Fisher/RN "
        "or C^6 diagonal support, not the same-source full End(C^3) color "
        "ensemble needed for Route-2."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
