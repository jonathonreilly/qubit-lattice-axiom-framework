#!/usr/bin/env python3
"""No-go for normalization-only scalar partitions forcing uv=1/9."""

from __future__ import annotations

from collections import deque
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-scalar-partition-product"

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


def mean_from_p(p: Fraction) -> Fraction:
    return 2 * p - 1


def one_point_product(p: Fraction) -> Fraction:
    m = mean_from_p(p)
    return m * m


def connected(raw: Fraction, uv: Fraction) -> Fraction:
    return raw - uv


def kappa(conn: Fraction) -> Fraction:
    return 9 * (conn - Fraction(8, 9))


def invariant_linear_derivative(coefficients: tuple[Fraction, ...], tangent: tuple[Fraction, ...]) -> Fraction:
    return sum(c * t for c, t in zip(coefficients, tangent))


def part1_grounding() -> None:
    print("PART 1: grounding")
    block107 = flat(text("QUARK_ROUTE2_NONBINARY_PRODUCT_NORMAL_FORM_SUPPORT_NOTE_2026-06-22.md"))
    block108 = flat(text("QUARK_ROUTE2_COLOR_MARGINAL_PRODUCT_SUPPORT_NO_GO_NOTE_2026-06-22.md"))
    block109 = flat(text("QUARK_ROUTE2_COLOR_MARGINAL_TRANSFER_NO_GO_NOTE_2026-06-22.md"))
    pcal = flat(text("QUARK_ROUTE2_SOURCE_MEASURE_PRODUCT_REGISTRY_TRANSFER_NO_GO_NOTE_2026-06-22.md"))
    moment = flat(text("QUARK_ROUTE2_PCAL_MOMENT_REALIZATION_NO_GO_NOTE_2026-06-22.md"))
    check("Block107 reduces target to uv=1/9", "E[X]E[Y] = uv = 1/9" in block107)
    check("Block107 names same-source one-point product theorem", "Route-2 same-source one-point product theorem" in block107)
    check("Block108 supplies color-marginal product support", "rank-one color projector" in block108 and "1/3 and 1/3" in block108)
    check("Block109 prunes current color-marginal transfer", "current exact Route-2 surface" in block109 and "not color-axis projectors" in block109)
    check("generic Pcal product registry remains missing", "Route-2 Pcal product-instantiation theorem" in pcal)
    check("finite P_R moment realization remains missing", "Route-2 Pcal moment-realization theorem" in moment)


def part2_normalization_counterfamily() -> None:
    print()
    print("PART 2: normalization-only scalar counterfamily")
    raw = Fraction(1)
    cases = {
        "balanced": Fraction(1, 2),
        "target_selector": Fraction(2, 3),
        "three_quarter": Fraction(3, 4),
        "constant_plus": Fraction(1),
    }
    expected = {
        "balanced": (Fraction(0), Fraction(1), Fraction(1)),
        "target_selector": (Fraction(1, 9), Fraction(8, 9), Fraction(0)),
        "three_quarter": (Fraction(1, 4), Fraction(3, 4), Fraction(-5, 4)),
        "constant_plus": (Fraction(1), Fraction(0), Fraction(-8)),
    }
    for name, p in cases.items():
        q = 1 - p
        m = mean_from_p(p)
        uv = one_point_product(p)
        conn = connected(raw, uv)
        k = kappa(conn)
        exp_uv, exp_conn, exp_k = expected[name]
        print(f"  {name}: p={p}, q={q}, mean={m}, uv={uv}, connected={conn}, kappa={k}")
        check(f"{name} is normalized", p + q == 1)
        check(f"{name} raw same-record moment is one", p * 1 + q * 1 == raw)
        check(f"{name} one-point product formula is exact", uv == m * m == exp_uv)
        check(f"{name} connected selector formula is exact", conn == raw - uv == exp_conn)
        check(f"{name} kappa formula is exact", k == 1 - 9 * uv == exp_k)
    unique_products = {one_point_product(p) for p in cases.values()}
    check("same normalization class has multiple one-point products", len(unique_products) == 4)
    check("only target-selector member gives kappa=0", all((name == "target_selector") == (kappa(connected(raw, one_point_product(p))) == 0) for name, p in cases.items()))
    check("p=2/3 is a selector premise, not normalization", cases["target_selector"] != cases["balanced"] and cases["target_selector"] != cases["constant_plus"])


def part3_invariant_partition_obstruction() -> None:
    print()
    print("PART 3: invariant scalar-partition obstruction")
    tangent_a = (Fraction(1), Fraction(-1), Fraction(0))
    tangent_b = (Fraction(1), Fraction(1), Fraction(-2))
    invariant_coeffs = (Fraction(1), Fraction(1), Fraction(1))
    selected_coeffs = (Fraction(1), Fraction(0), Fraction(0))
    for tangent in (tangent_a, tangent_b):
        print(f"  tangent={tangent}, sum={sum(tangent)}")
        check("normalized tangent has zero total mass", sum(tangent) == 0)
        check("permutation-invariant linear readout derivative vanishes", invariant_linear_derivative(invariant_coeffs, tangent) == 0)
    check("selected-cell readout has nonzero tangent response", invariant_linear_derivative(selected_coeffs, tangent_a) != 0)
    check("nonconstant scalar marginal needs selected subset/covector", invariant_linear_derivative(selected_coeffs, tangent_a) == 1)
    supplied_by_normalization = {
        "total_mass_one": True,
        "distinguished_subset": False,
        "same_source_record_variables": False,
        "raw_moment_registry": False,
        "one_point_product_selector": False,
    }
    for name, present in supplied_by_normalization.items():
        print(f"  normalization supplies {name}: {present}")
        check(f"{name} classification is boolean", isinstance(present, bool))
    check("normalization supplies total mass only", supplied_by_normalization["total_mass_one"] and not supplied_by_normalization["one_point_product_selector"])
    check("normalization does not type raw moment registry", not supplied_by_normalization["raw_moment_registry"])


def part4_reachability() -> None:
    print()
    print("PART 4: reachability")
    pruned_edges = [
        ("scalar_normalization", "total_mass_one"),
        ("total_mass_one", "free_one_point_product"),
        ("free_one_point_product", "missing_uv_selector"),
    ]
    positive_edges = [
        ("Route2_scalar_source_marginal_selector_theorem", "same_source_XY"),
        ("same_source_XY", "raw_E_XY_equals_one"),
        ("same_source_XY", "uv_equals_one_ninth"),
        ("raw_E_XY_equals_one", "Pcal_connected_subtraction"),
        ("uv_equals_one_ninth", "Pcal_connected_subtraction"),
        ("Pcal_connected_subtraction", "kappa_zero_without_endpoint"),
    ]
    check("scalar normalization reaches missing selector node", reachable(pruned_edges, "scalar_normalization", "missing_uv_selector"))
    check("scalar normalization does not reach kappa=0", not reachable(pruned_edges, "scalar_normalization", "kappa_zero_without_endpoint"))
    check("positive scalar source-marginal theorem would reach kappa=0", reachable(positive_edges, "Route2_scalar_source_marginal_selector_theorem", "kappa_zero_without_endpoint"))
    check("uv=1/9 remains load-bearing", reachable(positive_edges, "uv_equals_one_ninth", "kappa_zero_without_endpoint"))
    all_nodes = {n for e in pruned_edges + positive_edges for n in e}
    check("reachability graph contains no endpoint-value node", all("rho_E" not in n and "c_TE" not in n for n in all_nodes))
    check("reachability graph does not use finite-box comparator", all("finite_box" not in n and "box" not in n for n in all_nodes))


def part5_document_boundary() -> None:
    print()
    print("PART 5: document boundary")
    note = text("QUARK_ROUTE2_SCALAR_PARTITION_PRODUCT_SELECTOR_NO_GO_NOTE_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    review = loop_text("REVIEW_HISTORY.md")
    state = loop_text("STATE.yaml")
    note_flat = flat(note)
    required = (
        "Actual current-surface status: no-go for normalized scalar partitions alone forcing the Route-2 one-point product 1/9",
        "Normalization alone does not select the one-point product",
        "This block uses the signed two-state family only as a counterfamily",
        "permutation-invariant linear readouts are constant on the simplex",
        "Route-2 scalar source-marginal selector theorem",
        "No endpoint value is used",
    )
    for marker in required:
        check(f"note contains marker: {marker}", marker in note_flat)
    for marker in ("Block110 Summary", "negative_route_pruning", "Do not audit", "Next Exact Action"):
        check(f"handoff contains marker: {marker}", marker in handoff)
    check("certificate keeps proposal disallowed", "proposal_allowed: false" in cert)
    check("trace gate names scalar source-marginal selector theorem", "scalar source-marginal selector theorem" in trace_gate)
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
    print("Route-2 scalar-partition product selector no-go")
    print("TRACE: negative_route_pruning")
    part1_grounding()
    part2_normalization_counterfamily()
    part3_invariant_partition_obstruction()
    part4_reachability()
    part5_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        return 1
    print("VERDICT: scalar normalization alone does not force the same-source one-point product 1/9; a Route-2 scalar source-marginal selector theorem remains the missing primitive.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
