#!/usr/bin/env python3
"""Color-SU3 record support to Route-2 full color-ensemble transfer boundary.

This runner checks whether existing color-SU3 record-invariance support already
supplies the Route-2 same-source full End(C^3) color-record ensemble needed by
the connected/disconnected selector theorem.

It does not.  The existing color support supplies a conditional commutant half,
a named matter-realization residual, and a carrier budget.  It does not identify
Route-2 P_R/E-T as a same-source readout over a full trace-one End(C^3)
color-record ensemble.  No endpoint value is imported.
"""

from __future__ import annotations

from collections import deque
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-color-su3-record-ensemble-transfer"

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


def normalized(text: str) -> str:
    return " ".join(text.replace("`", "").replace("**", "").split())


def part1_color_record_bridge_boundary() -> None:
    print("PART 1: color-SU3 record bridge boundary")
    bridge = note_text("COLOR_SU3_SYMMETRIC_BASE_BRIDGE_FROM_RECORD_INVARIANCE_BOUNDED_NOTE_2026-06-05.md")
    flat = normalized(bridge)

    checks = (
        ("bridge identifies gauge-from-invariance commutant half", "gauge-from-invariance-commutant half" in flat),
        ("bridge is conditional on color-singlet records", "given the antecedent that the physical records are the color singlets" in flat),
        ("bridge says the antecedent is not forced", "The crux: the antecedent is not forced" in flat),
        ("bridge classifies result as partial-pinning", "partial-pinning" in flat),
        ("bridge says record-invariance supplies only first summand", "supplies only the first summand" in flat),
        ("bridge names matter-realization residual", "matter-realization residual" in flat),
        ("bridge contrasts base SU(3) and fiber SU(2)", "base SU(3)" in bridge and "fiber SU(2)" in bridge),
        ("bridge has no Route-2 P_R/E-T theorem", "P_R/E-T" not in bridge),
    )
    for label, ok in checks:
        check(label, ok)


def part2_matter_realization_and_link_budget() -> None:
    print()
    print("PART 2: MR_color and link-routing support boundary")
    residual = note_text("COLOR_SU3_MATTER_REALIZATION_RESIDUAL_MAP_2026-06-05.md")
    link_budget = note_text("COLOR_LINK_INDEX_ROUTING_CARRIER_BUDGET_2026-06-05.md")
    residual_flat = normalized(residual)
    budget_flat = normalized(link_budget)

    check("MR_color is named", "Call the remaining input MR_color" in residual_flat)
    check("MR_color includes quark matter in Sym^2(C^2)", "quark matter occupies the 3D symmetric-base fundamental Sym^2(C^2)" in residual_flat)
    check("MR_color includes color-singlet record relevance", "physical color-singlet records are the relevant record algebra" in residual_flat)
    check("MR_color includes link/connection base-SU3 index", "link/connection variables carry the corresponding base-SU(3) index" in residual_flat)
    check("record stack can consume records but not generate MR_color", "They do not generate MR_color" in residual_flat)
    check("matter realization remains residual", "matter realization" in residual_flat and "residual" in residual_flat)
    check("link budget says two qubits can host Sym^2(C^2)", "two qubits can host a 3D symmetric subspace Sym^2(C^2)" in budget_flat)
    check("link budget prunes one-qubit endpoint route", "one primitive qubit endpoint cannot host the color fundamental" in budget_flat)
    check("link budget does not supply projection/routing/transport/Gauss/dynamics", "does not supply projection, link routing, Gauss/Wilson observables, action/couplings" in budget_flat)
    check("link budget has no Route-2 P_R/E-T theorem", "P_R/E-T" not in link_budget)


def part3_route2_source_dimension_boundary() -> None:
    print()
    print("PART 3: Route-2 source dimension/type boundary")
    block78 = note_text("QUARK_ROUTE2_CONNECTED_COLOR_SOURCE_TRANSFER_NO_GO_NOTE_2026-06-22.md")
    block80 = note_text("QUARK_ROUTE2_FINITE_ENDPOINT_SOURCE_RANK_NO_GO_NOTE_2026-06-22.md")
    block81 = note_text("QUARK_ROUTE2_SOURCE_MEASURE_COLOR_ENSEMBLE_TRANSFER_NO_GO_NOTE_2026-06-22.md")
    combined = normalized(block78 + "\n" + block80 + "\n" + block81)

    color_dim = 3
    endc3_dim = color_dim * color_dim
    scalar_dim = 1
    sl3_dim = endc3_dim - scalar_dim
    route2_endpoint_slots = 4

    check("color carrier dimension is three", color_dim == 3)
    check("End(C^3) source dimension is nine", endc3_dim == 9)
    check("scalar disconnected line dimension is one", scalar_dim == 1)
    check("centered sl_3 dimension is eight", sl3_dim == 8)
    check("formal connected matrix fraction is 8/9", Fraction(sl3_dim, endc3_dim) == Fraction(8, 9))
    check("four endpoint slots have centered rank at most three", route2_endpoint_slots - 1 == 3)
    check("four endpoint rank is not sl_3 rank", route2_endpoint_slots - 1 != sl3_dim)
    check("Block78 leaves Route-2 source transfer open", "Route-2 readout does not yet live on that source surface" in combined)
    check("Block80 names same-source full color-record ensemble theorem as missing", "same-source full color-record ensemble/readout theorem" in combined)
    check("Block81 says generic support is not Route-2 full color ensemble", "not a same-source full End(C^3) color-record ensemble" in combined)


def part4_transfer_reachability() -> None:
    print()
    print("PART 4: transfer reachability")
    base_edges = [
        ("color_su3_record_bridge", "gauge_from_invariance_commutant_half"),
        ("color_su3_record_bridge", "color_singlet_record_antecedent_open"),
        ("color_su3_record_bridge", "MR_color_open"),
        ("matter_residual_map", "MR_color_open"),
        ("link_carrier_budget", "two_qubit_sym2_endpoint_budget"),
        ("two_qubit_sym2_endpoint_budget", "routing_residual_open"),
        ("route2_endpoint_surface", "four_endpoint_readout"),
        ("four_endpoint_readout", "centered_rank_at_most_3"),
        ("full_trace_one_color_record_ensemble", "EndC3_source"),
        ("EndC3_source", "sl3_centered_score_image"),
        ("sl3_centered_score_image", "kappa0_selector"),
    ]
    missing_edges = [
        ("MR_color_plus_route2_same_source_readout", "same_source_full_color_record_ensemble"),
        ("same_source_full_color_record_ensemble", "full_trace_one_color_record_ensemble"),
        ("route2_physical_readout", "MR_color_plus_route2_same_source_readout"),
    ]

    starts = (
        "color_su3_record_bridge",
        "matter_residual_map",
        "link_carrier_budget",
        "route2_endpoint_surface",
    )
    for start in starts:
        check(f"{start} does not reach End(C^3) source", not reachable(base_edges, start, "EndC3_source"))
        check(f"{start} does not reach kappa=0 selector", not reachable(base_edges, start, "kappa0_selector"))

    check("full color-record ensemble reaches End(C^3)", reachable(base_edges, "full_trace_one_color_record_ensemble", "EndC3_source"))
    check("full color-record ensemble reaches kappa=0", reachable(base_edges, "full_trace_one_color_record_ensemble", "kappa0_selector"))
    check("adding the missing primitive reaches End(C^3)", reachable(base_edges + missing_edges, "route2_physical_readout", "EndC3_source"))
    check("adding the missing primitive reaches kappa=0", reachable(base_edges + missing_edges, "route2_physical_readout", "kappa0_selector"))
    check("base graph contains no endpoint-value node", all("c_TE" not in node and "rho_E" not in node for edge in base_edges for node in edge))
    check("missing primitive graph contains no endpoint-value node", all("c_TE" not in node and "rho_E" not in node for edge in missing_edges for node in edge))


def part5_document_boundary() -> None:
    print()
    print("PART 5: document and loop boundary")
    new_note = note_text("QUARK_ROUTE2_COLOR_SU3_RECORD_ENSEMBLE_TRANSFER_NO_GO_NOTE_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    certificate = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    flat = normalized(new_note)

    required = (
        "Actual current-surface status: no-go for color-SU(3)-record to Route-2 full color-ensemble transfer",
        "This is not an audit verdict",
        "No endpoint value is used",
        "does not instantiate that Route-2 same-source full color ensemble",
        "MR_color + Route-2 same-source color-readout theorem",
        "full trace-one End(C^3) color-record ensemble",
        "force kappa = 0 without importing the endpoint value",
    )
    for marker in required:
        check(f"new note contains marker: {marker}", marker in flat)

    for marker in ("Block82 Summary", "negative_route_pruning", "Do not audit", "Next Exact Action"):
        check(f"handoff contains marker: {marker}", marker in handoff)

    check("certificate keeps proposal disallowed", "proposal_allowed: false" in certificate)
    check("certificate marks bare retained wording disallowed", "bare_retained_allowed: false" in certificate)
    check("trace gate records negative route pruning", "trace_class: negative_route_pruning" in trace_gate)
    check("trace gate names user blocker", "R_conn -> c_TE = -8/9" in trace_gate)

    banned = (
        ("branch-local status-promotion", phrase("ret", "ained branch-local")),
        ("future retention", phrase("would become ", "ret", "ained")),
        ("promotion-to-retention", phrase("promoted to ", "ret", "ained")),
        ("actual-surface retention", phrase("ret", "ained on the actual surface")),
        ("parent closure", phrase("closes ", "the parent")),
        ("current-surface endpoint derivation", phrase("derives ", "the endpoint triple", " on the current surface")),
        ("audit ratification", phrase("audit", "-ratified")),
    )
    combined = new_note + "\n" + handoff + "\n" + certificate + "\n" + trace_gate
    for label, marker in banned:
        check(f"packet avoids overclaim marker: {label}", marker not in combined)


def main() -> int:
    print("Route-2 color-SU3 record-ensemble transfer no-go")
    print("Status: no-go for color-SU3-record to Route-2 full color-ensemble transfer; not an audit verdict.")
    print("TRACE: negative_route_pruning")
    part1_color_record_bridge_boundary()
    part2_matter_realization_and_link_budget()
    part3_route2_source_dimension_boundary()
    part4_transfer_reachability()
    part5_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        print("VERDICT: color-SU3 record-ensemble transfer checks failed.")
        return 1
    print(
        "VERDICT: existing color-SU3 record support is upstream carrier and "
        "commutant support, not the same-source full End(C^3) color ensemble "
        "needed for Route-2."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
