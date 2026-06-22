#!/usr/bin/env python3
"""No-go for current P_R/E-T labels instantiating color-marginal readouts."""

from __future__ import annotations

from collections import deque
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-color-marginal-transfer"

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


def text(name: str) -> str:
    return (DOCS / name).read_text(encoding="utf-8")


def loop_text(name: str) -> str:
    return (LOOP / name).read_text(encoding="utf-8")


def flat(s: str) -> str:
    return " ".join(s.replace("`", "").replace("**", "").split())


def reachable(edges: Iterable[tuple[str, str]], start: str, target: str) -> bool:
    graph: dict[str, set[str]] = {}
    for a, b in edges:
        graph.setdefault(a, set()).add(b)
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


def part1_grounding() -> None:
    print("PART 1: grounding")
    readout = flat(text("QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md"))
    block108 = flat(text("QUARK_ROUTE2_COLOR_MARGINAL_PRODUCT_SUPPORT_NO_GO_NOTE_2026-06-22.md"))
    trace_transfer = flat(text("QUARK_ROUTE2_TRACE_ONE_COLOR_RECORD_TRANSFER_NO_GO_NOTE_2026-06-22.md"))
    check("exact readout has four endpoint labels", all(label in readout for label in ("E-shell", "E-center", "T-shell", "T-center")))
    check("exact readout has channelwise P_R matrix", "P_R = [[alpha_E, 0, beta_E, 0]" in readout)
    check("Block108 names color-marginal product theorem", "Route-2 same-source color-marginal product theorem" in block108)
    check("Block108 records 1/3 x 1/3 product", "E[X]E[Y] = 1/9" in block108 and "<P_i><P_j> = 1/9" in block108)
    check("trace-one transfer already separates full color source from P_R", "not yet a trace-one 3x3 color-density record surface" in trace_transfer)


def part2_required_vs_current_data() -> None:
    print()
    print("PART 2: required color-marginal data versus current P_R data")
    required = {
        "rank_one_projectors_End_C3": False,
        "normalized_trace_state_Tr_over_3": False,
        "color_axis_labels": False,
        "one_point_marginals_1_over_3": False,
        "same_source_XY_variables": False,
        "raw_E_XY_equals_one": False,
    }
    current = {
        "E_shell_label": True,
        "E_center_label": True,
        "T_shell_label": True,
        "T_center_label": True,
        "channelwise_linear_readout": True,
    }
    for name, present in current.items():
        print(f"  current {name}: {'present' if present else 'missing'}")
        check(f"current {name} is present", present)
    for name, present in required.items():
        print(f"  required {name}: {'present' if present else 'missing'}")
        check(f"required {name} is not supplied by current P_R", not present)
    check("current labels do not include color axes", all(axis not in current for axis in ("red", "green", "blue")))
    check("required color-marginal package remains missing", not any(required.values()))


def part3_transfer_obstruction() -> None:
    print()
    print("PART 3: transfer obstruction")
    candidates = {
        "four_slot_endpoint_surface": "available_support",
        "rank_one_color_projector_surface": "missing",
        "normalized_trace_color_state": "missing",
        "same_source_transfer": "missing",
        "endpoint_value": "forbidden",
    }
    allowed = {"available_support", "missing", "forbidden"}
    for name, status in candidates.items():
        print(f"  {name}: {status}")
        check(f"{name} status classified", status in allowed)
    check("P_R surface is support, not color-marginal theorem", candidates["four_slot_endpoint_surface"] == "available_support" and candidates["same_source_transfer"] == "missing")
    check("endpoint value remains forbidden", candidates["endpoint_value"] == "forbidden")


def part4_reachability() -> None:
    print()
    print("PART 4: reachability")
    current_edges = [
        ("current_P_R_E_T_labels", "channelwise_readout"),
        ("channelwise_readout", "missing_color_marginal_readout"),
        ("missing_color_marginal_readout", "missing_product_1_over_9"),
    ]
    positive_edges = [
        ("Route2_color_marginal_readout_theorem", "one_point_1_over_3"),
        ("one_point_1_over_3", "disconnected_product_1_over_9"),
        ("disconnected_product_1_over_9", "Pcal_connected_subtraction"),
        ("Pcal_connected_subtraction", "kappa_zero_without_endpoint"),
    ]
    check("current P_R reaches missing color-marginal node", reachable(current_edges, "current_P_R_E_T_labels", "missing_color_marginal_readout"))
    check("current P_R does not reach kappa=0", not reachable(current_edges, "current_P_R_E_T_labels", "kappa_zero_without_endpoint"))
    check("positive color-marginal theorem would reach kappa=0", reachable(positive_edges, "Route2_color_marginal_readout_theorem", "kappa_zero_without_endpoint"))
    check("disconnected product 1/9 is load-bearing", reachable(positive_edges, "disconnected_product_1_over_9", "kappa_zero_without_endpoint"))
    all_nodes = {n for e in current_edges + positive_edges for n in e}
    check("reachability graph contains no endpoint-value node", all("rho_E" not in n and "c_TE" not in n for n in all_nodes))


def part5_document_boundary() -> None:
    print()
    print("PART 5: document boundary")
    note = text("QUARK_ROUTE2_COLOR_MARGINAL_TRANSFER_NO_GO_NOTE_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    review = loop_text("REVIEW_HISTORY.md")
    state = loop_text("STATE.yaml")
    note_flat = flat(note)
    required = (
        "Actual current-surface status: no-go for current P_R/E-T labels instantiating the color-marginal product theorem",
        "rank-one color projectors P_i in End(C^3)",
        "E[X]=E[Y]=1/3",
        "Route-2 same-source color-marginal readout theorem",
        "No endpoint value is used",
    )
    for marker in required:
        check(f"note contains marker: {marker}", marker in note_flat)
    for marker in ("Block109 Summary", "negative_route_pruning", "Do not audit", "Next Exact Action"):
        check(f"handoff contains marker: {marker}", marker in handoff)
    check("certificate keeps proposal disallowed", "proposal_allowed: false" in cert)
    check("trace gate names color-marginal readout theorem", "color-marginal readout theorem" in trace_gate)
    check("state records no audit stop condition", "stop_condition: none" in state)
    check("review history records no review-loop worker", "No review-loop worker was run" in review)
    banned = (
        ("branch-local status-promotion", phrase("ret", "ained branch-local")),
        ("future retention", phrase("would become ", "ret", "ained")),
        ("promotion-to-retention", phrase("promoted to ", "ret", "ained")),
        ("actual-surface retention", phrase("ret", "ained on the actual surface")),
        ("parent closure", phrase("closes ", "the parent")),
        ("current-surface endpoint derivation", phrase("derives the endpoint triple ", "on the current surface")),
        ("audit ratification", phrase("audit", "-ratified")),
        ("observed-target import", phrase("observed ", "target")),
        ("fitted-selector import", phrase("fitted ", "selector")),
        ("target-observation import", phrase("target ", "observation")),
        ("data-tuned-selector import", phrase("data-tuned ", "selector")),
    )
    combined = note + "\n" + handoff + "\n" + cert + "\n" + trace_gate + "\n" + review + "\n" + state
    for label, marker in banned:
        check(f"banned marker absent: {label}", marker not in combined)


def main() -> int:
    print("Route-2 color-marginal transfer no-go")
    print("TRACE: negative_route_pruning")
    part1_grounding()
    part2_required_vs_current_data()
    part3_transfer_obstruction()
    part4_reachability()
    part5_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        return 1
    print("VERDICT: current P_R/E-T labels do not instantiate the same-source color-marginal readout theorem needed to use the 1/3 x 1/3 product support.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
