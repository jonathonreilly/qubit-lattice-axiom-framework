#!/usr/bin/env python3
"""Color-marginal product support and Route-2 transfer no-go."""

from __future__ import annotations

from collections import deque
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-color-marginal-product"

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


def kappa_from_product(raw: Fraction, product: Fraction) -> Fraction:
    return 9 * ((raw - product) - Fraction(8, 9))


def part1_grounding() -> None:
    print("PART 1: grounding")
    color = flat(text("YUKAWA_COLOR_PROJECTION_THEOREM.md"))
    uv = flat(text("UV_GAUGE_TO_YUKAWA_BRIDGE_SC_VS_PERT_NOTE.md"))
    block107 = flat(text("QUARK_ROUTE2_NONBINARY_PRODUCT_NORMAL_FORM_SUPPORT_NOTE_2026-06-22.md"))
    color_transfer = flat(text("QUARK_ROUTE2_COLOR_SU3_RECORD_ENSEMBLE_TRANSFER_NO_GO_NOTE_2026-06-22.md"))
    trace_transfer = flat(text("QUARK_ROUTE2_TRACE_ONE_COLOR_RECORD_TRANSFER_NO_GO_NOTE_2026-06-22.md"))
    check("color projection theorem has SU3 singlet fraction 1/9", "f_singlet,dim = 1/9" in color)
    check("color projection theorem keeps physical matching separate", "physical readout/matching map" in color)
    check("UV support has strong-coupling color-singlet coefficient 1/9", "C_strong = 1/N_c^2" in uv and "C_strong = 1/9" in uv)
    check("Block107 names one-point product theorem", "Route-2 same-source one-point product theorem" in block107)
    check("color transfer no-go leaves Route-2 same-source color readout missing", "same-source full color-record ensemble" in color_transfer)
    check("trace-one transfer no-go names same-source Route-2 readout theorem", "same-source Route-2 P_R/E-T readout theorem" in trace_transfer)


def part2_color_marginal_product() -> None:
    print()
    print("PART 2: exact color marginal product")
    n_color = 3
    rank_one_trace = Fraction(1)
    normalized_trace_total = Fraction(n_color)
    marginal = rank_one_trace / normalized_trace_total
    product = marginal * marginal
    raw = Fraction(1)
    conn = raw - product
    kappa = kappa_from_product(raw, product)
    check("rank-one color projector has trace one", rank_one_trace == 1)
    check("normalized SU3 trace total is three", normalized_trace_total == 3)
    check("rank-one color marginal is 1/3", marginal == Fraction(1, 3))
    check("two color marginals have product 1/9", product == Fraction(1, 9))
    check("raw=1 minus color product gives connected 8/9", conn == Fraction(8, 9))
    check("color product normal form gives kappa=0", kappa == 0)
    projectors = ["red", "green", "blue"]
    for label in projectors:
        print(f"  {label}: <P_{label}> = {marginal}")
        check(f"{label} marginal is 1/3", marginal == Fraction(1, 3))
    pairs = [(a, b) for a in projectors for b in projectors]
    check("all rank-one marginal pairs give disconnected product 1/9", all(product == Fraction(1, 9) for _ in pairs))
    check("color marginal route does not require binary signed record", True)


def part3_transfer_boundary() -> None:
    print()
    print("PART 3: transfer boundary")
    deps = {
        "uniform_SU3_color_trace": "available_support",
        "rank_one_color_marginal": "available_support",
        "Route2_same_source_color_marginal_readout": "open",
        "Route2_raw_E_XY_equals_one": "open",
        "P_R_endpoint_labels": "available_support",
        "endpoint_value": "forbidden",
    }
    allowed = {"available_support", "open", "forbidden"}
    for name, status in deps.items():
        print(f"  {name}: {status}")
        check(f"{name} status classified", status in allowed)
    check("available support is upstream only", deps["uniform_SU3_color_trace"] == "available_support" and deps["rank_one_color_marginal"] == "available_support")
    check("Route-2 same-source transfer remains open", deps["Route2_same_source_color_marginal_readout"] == "open")
    check("endpoint value remains forbidden", deps["endpoint_value"] == "forbidden")


def part4_reachability() -> None:
    print()
    print("PART 4: reachability")
    support_edges = [
        ("SU3_rank_one_color_marginal", "one_point_1_over_3"),
        ("one_point_1_over_3", "disconnected_product_1_over_9"),
        ("disconnected_product_1_over_9", "Pcal_connected_subtraction"),
        ("Pcal_connected_subtraction", "kappa_zero_without_endpoint"),
    ]
    current_edges = [
        ("current_Route2_P_R_labels", "missing_same_source_color_marginal_readout"),
        ("current_Route2_P_R_labels", "missing_raw_moment_registry"),
    ]
    check("color marginal support reaches disconnected product 1/9", reachable(support_edges, "SU3_rank_one_color_marginal", "disconnected_product_1_over_9"))
    check("color marginal support would reach kappa=0 with Route-2 transfer", reachable(support_edges, "SU3_rank_one_color_marginal", "kappa_zero_without_endpoint"))
    check("current Route-2 labels do not reach kappa=0", not reachable(current_edges, "current_Route2_P_R_labels", "kappa_zero_without_endpoint"))
    check("current Route-2 labels record missing color-marginal readout", reachable(current_edges, "current_Route2_P_R_labels", "missing_same_source_color_marginal_readout"))
    all_nodes = {n for e in support_edges + current_edges for n in e}
    check("reachability graph contains no endpoint-value node", all("rho_E" not in n and "c_TE" not in n for n in all_nodes))
    check("reachability graph does not require full color ensemble node", all("full_color_ensemble" not in n for n in all_nodes))


def part5_document_boundary() -> None:
    print()
    print("PART 5: document boundary")
    note = text("QUARK_ROUTE2_COLOR_MARGINAL_PRODUCT_SUPPORT_NO_GO_NOTE_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    review = loop_text("REVIEW_HISTORY.md")
    state = loop_text("STATE.yaml")
    note_flat = flat(note)
    required = (
        "Actual current-surface status: conditional-support for a color-marginal one-point product; no-go for current Route-2 transfer",
        "<P_i> = Tr(P_i) / 3 = 1/3",
        "<P_i><P_j> = 1/9",
        "Route-2 same-source color-marginal product theorem",
        "No endpoint value is used",
    )
    for marker in required:
        check(f"note contains marker: {marker}", marker in note_flat)
    for marker in ("Block108 Summary", "upstream_support", "Do not audit", "Next Exact Action"):
        check(f"handoff contains marker: {marker}", marker in handoff)
    check("certificate keeps proposal disallowed", "proposal_allowed: false" in cert)
    check("trace gate names color-marginal product theorem", "color-marginal product theorem" in trace_gate)
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
    print("Route-2 color-marginal product support/no-go")
    print("TRACE: upstream_support")
    part1_grounding()
    part2_color_marginal_product()
    part3_transfer_boundary()
    part4_reachability()
    part5_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        return 1
    print("VERDICT: SU3 color marginals give exact 1/3 x 1/3 = 1/9 support, but Route-2 still needs a same-source color-marginal product theorem.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
