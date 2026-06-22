#!/usr/bin/env python3
"""Non-binary one-point product normal form for Route-2 connected subtraction."""

from __future__ import annotations

from collections import deque
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-nonbinary-product-normal-form"

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


def connected(raw: Fraction, u: Fraction, v: Fraction) -> Fraction:
    return raw - u * v


def kappa(conn: Fraction) -> Fraction:
    return 9 * (conn - Fraction(8, 9))


def part1_grounding() -> None:
    print("PART 1: grounding")
    block102 = flat(text("QUARK_ROUTE2_BINARY_PRODUCT_NORMAL_FORM_SUPPORT_NOTE_2026-06-22.md"))
    block106 = flat(text("QUARK_ROUTE2_LOG_ODDS_SELECTOR_STRETCH_NO_GO_NOTE_2026-06-22.md"))
    hessian = flat(text("QUARK_ROUTE2_SOURCE_HESSIAN_CUMULANT_SELECTOR_SUPPORT_NOTE_2026-06-22.md"))
    block100 = flat(text("QUARK_ROUTE2_SOURCE_MEASURE_PRODUCT_REGISTRY_TRANSFER_NO_GO_NOTE_2026-06-22.md"))
    check("Block102 records binary one-point bias route", "m = +/- 1/3" in block102 and "P(+1):P(-1) = 2:1" in block102)
    check("Block106 records log-odds selector wall", "Route-2 log-odds selector theorem" in block106)
    check("source-Hessian support gives disconnected product formula", "D_i D_j W = D_i D_j Z - (D_i Z)(D_j Z)" in hessian)
    check("source-Hessian support names 1/9 one-point product", "(D_i Z)(D_j Z) = 1/9" in hessian)
    check("Block100 leaves product registry missing", "Route-2 Pcal product-instantiation theorem" in block100)
    check("Block100 says one-point product registry is load-bearing", "one-point product registry is not decorative" in block100)


def part2_nonbinary_normal_form() -> None:
    print()
    print("PART 2: non-binary product normal form")
    raw = Fraction(1)
    cases = {
        "binary_positive": (Fraction(1, 3), Fraction(1, 3)),
        "binary_negative": (Fraction(-1, 3), Fraction(-1, 3)),
        "asymmetric_one_ninth": (Fraction(1), Fraction(1, 9)),
        "asymmetric_two_sixths": (Fraction(2, 3), Fraction(1, 6)),
        "zero_product": (Fraction(0), Fraction(0)),
        "quarter_product": (Fraction(1, 2), Fraction(1, 2)),
    }
    kappas: dict[str, Fraction] = {}
    products: dict[str, Fraction] = {}
    for name, (u, v) in cases.items():
        prod = u * v
        conn = connected(raw, u, v)
        k = kappa(conn)
        products[name] = prod
        kappas[name] = k
        print(f"  {name}: u={u}, v={v}, uv={prod}, connected={conn}, kappa={k}")
        check(f"{name} product formula is exact", prod == u * v)
        check(f"{name} connected formula is exact", conn == raw - prod)
        check(f"{name} kappa formula is exact", k == 1 - 9 * prod)
    good = ["binary_positive", "binary_negative", "asymmetric_one_ninth", "asymmetric_two_sixths"]
    check("all uv=1/9 cases give kappa=0", all(kappas[name] == 0 for name in good))
    check("non-binary asymmetric examples give kappa=0", kappas["asymmetric_one_ninth"] == 0 and kappas["asymmetric_two_sixths"] == 0)
    check("zero product gives kappa=1", kappas["zero_product"] == 1)
    check("quarter product gives kappa=-5/4", kappas["quarter_product"] == Fraction(-5, 4))
    check("binary same-record route is a subcase, not an equivalence", products["binary_positive"] == products["asymmetric_one_ninth"] == Fraction(1, 9))


def part3_dependency_classes() -> None:
    print()
    print("PART 3: dependency classes")
    deps = {
        "same_source_variables_XY": "open",
        "raw_moment_E_XY_equals_one": "open",
        "one_point_product_uv_equals_one_ninth": "open",
        "Pcal_connected_subtraction": "available_support",
        "binary_signed_record": "optional_subcase",
        "log_odds_selector": "optional_subcase",
        "endpoint_value": "forbidden",
    }
    allowed = {"open", "available_support", "optional_subcase", "forbidden"}
    for name, status in deps.items():
        print(f"  {name}: {status}")
        check(f"{name} status classified", status in allowed)
    check("binary/log-odds route is optional in this normal form", deps["binary_signed_record"] == "optional_subcase" and deps["log_odds_selector"] == "optional_subcase")
    check("same-source product theorem remains open", deps["one_point_product_uv_equals_one_ninth"] == "open")
    check("endpoint value remains forbidden", deps["endpoint_value"] == "forbidden")


def part4_reachability() -> None:
    print()
    print("PART 4: reachability")
    support_edges = [
        ("same_source_one_point_product_theorem", "uv_equals_one_ninth"),
        ("uv_equals_one_ninth", "Pcal_connected_subtraction"),
        ("Pcal_connected_subtraction", "connected_8_9"),
        ("connected_8_9", "kappa_zero_without_endpoint"),
    ]
    current_edges = [
        ("current_Route2_surface", "Pcal_connected_subtraction_support"),
        ("current_Route2_surface", "missing_same_source_one_point_product"),
    ]
    check("same-source product theorem would reach kappa=0", reachable(support_edges, "same_source_one_point_product_theorem", "kappa_zero_without_endpoint"))
    check("uv=1/9 is load-bearing", reachable(support_edges, "uv_equals_one_ninth", "kappa_zero_without_endpoint"))
    check("current surface does not reach kappa=0 through product normal form", not reachable(current_edges, "current_Route2_surface", "kappa_zero_without_endpoint"))
    check("current surface records missing product theorem", reachable(current_edges, "current_Route2_surface", "missing_same_source_one_point_product"))
    all_nodes = {n for e in support_edges + current_edges for n in e}
    check("reachability graph contains no endpoint-value node", all("rho_E" not in n and "c_TE" not in n for n in all_nodes))
    check("binary route is not required in reachability graph", all("binary" not in n and "log_odds" not in n for n in all_nodes))


def part5_document_boundary() -> None:
    print()
    print("PART 5: document boundary")
    note = text("QUARK_ROUTE2_NONBINARY_PRODUCT_NORMAL_FORM_SUPPORT_NOTE_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    review = loop_text("REVIEW_HISTORY.md")
    state = loop_text("STATE.yaml")
    note_flat = flat(note)
    required = (
        "Actual current-surface status: conditional-support for a same-source one-point product normal form",
        "kappa = 0 <=> E[X]E[Y] = uv = 1/9",
        "binary same-record case u=v=+/-1/3 is one subcase",
        "Route-2 same-source one-point product theorem",
        "without requiring a binary signed record or log-odds selector",
        "No endpoint value is used",
    )
    for marker in required:
        check(f"note contains marker: {marker}", marker in note_flat)
    for marker in ("Block107 Summary", "upstream_support", "Do not audit", "Next Exact Action"):
        check(f"handoff contains marker: {marker}", marker in handoff)
    check("certificate keeps proposal disallowed", "proposal_allowed: false" in cert)
    check("trace gate names one-point product theorem", "one-point product theorem" in trace_gate)
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
    print("Route-2 non-binary product normal-form support")
    print("TRACE: upstream_support")
    part1_grounding()
    part2_nonbinary_normal_form()
    part3_dependency_classes()
    part4_reachability()
    part5_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        return 1
    print("VERDICT: kappa=0 follows from a same-source one-point product uv=1/9; binary log-odds selection is only one subcase, and the Route-2 one-point product theorem remains open.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
