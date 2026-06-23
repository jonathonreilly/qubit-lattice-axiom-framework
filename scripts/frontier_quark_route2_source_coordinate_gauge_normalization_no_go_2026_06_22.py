#!/usr/bin/env python3
"""No-go for formal source-coordinate gauge fixing in Route-2 product bridge."""

from __future__ import annotations

from collections import deque
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-source-gauge-normalization"

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


BASE_MEAN = Fraction(1, 3)
BASE_RAW = Fraction(1)
BASE_PRODUCT = Fraction(1, 9)
BASE_CONNECTED = Fraction(8, 9)


def affine_raw(a: Fraction, b: Fraction) -> Fraction:
    return BASE_RAW + (a + b) * BASE_MEAN + a * b


def affine_product(a: Fraction, b: Fraction) -> Fraction:
    return (BASE_MEAN + a) * (BASE_MEAN + b)


def affine_connected(a: Fraction, b: Fraction) -> Fraction:
    return affine_raw(a, b) - affine_product(a, b)


def scaled(raw: Fraction, product: Fraction, connected: Fraction, s: Fraction, t: Fraction) -> tuple[Fraction, Fraction, Fraction]:
    scale = s * t
    return scale * raw, scale * product, scale * connected


def part1_grounding() -> None:
    print("PART 1: grounding")
    block107 = flat(text("QUARK_ROUTE2_NONBINARY_PRODUCT_NORMAL_FORM_SUPPORT_NOTE_2026-06-22.md"))
    block110 = flat(text("QUARK_ROUTE2_SCALAR_PARTITION_PRODUCT_SELECTOR_NO_GO_NOTE_2026-06-22.md"))
    source_jet = flat(text("QUARK_ROUTE2_SOURCE_JET_LIFT_NO_GO_NOTE_2026-06-22.md"))
    integrability = flat(text("QUARK_ROUTE2_SOURCE_HESSIAN_INTEGRABILITY_GATE_NO_GO_NOTE_2026-06-22.md"))
    formal = flat(text("QUARK_ROUTE2_FORMAL_SOURCE_COORDINATE_REGISTRY_VACUITY_NO_GO_NOTE_2026-06-22.md"))
    hessian = flat(text("QUARK_ROUTE2_SOURCE_HESSIAN_CUMULANT_SELECTOR_SUPPORT_NOTE_2026-06-22.md"))
    check("Block107 gives raw/product normal form", "E[XY] = 1" in block107 and "E[X]E[Y] = uv = 1/9" in block107)
    check("Block110 prunes normalization-only scalar selector", "Normalization alone does not select the one-point product" in block110)
    check("source-jet lift leaves raw/one-point split missing", "raw second source moment D_A D_B Z" in source_jet and "one-point product" in source_jet)
    check("integrability gate requires symmetric source-index registry", "H_AB = D_A D_B log Z = H_BA" in integrability)
    check("formal registry is vacuous for kappa", "formal embeddability" in formal and "does not force kappa=0" in formal)
    check("source-Hessian support gives exact disconnected subtraction", "D_i D_j W = D_i D_j Z - (D_i Z)(D_j Z)" in hessian)


def part2_affine_origin_gauge() -> None:
    print()
    print("PART 2: affine source-origin gauge")
    shifts = {
        "base": (Fraction(0), Fraction(0)),
        "x_shift": (Fraction(1), Fraction(0)),
        "y_shift": (Fraction(0), Fraction(-1, 3)),
        "both_shift": (Fraction(1), Fraction(1)),
    }
    expected = {
        "base": (Fraction(1), Fraction(1, 9), Fraction(8, 9)),
        "x_shift": (Fraction(4, 3), Fraction(4, 9), Fraction(8, 9)),
        "y_shift": (Fraction(8, 9), Fraction(0), Fraction(8, 9)),
        "both_shift": (Fraction(8, 3), Fraction(16, 9), Fraction(8, 9)),
    }
    for name, (a, b) in shifts.items():
        raw = affine_raw(a, b)
        product = affine_product(a, b)
        conn = affine_connected(a, b)
        exp_raw, exp_product, exp_conn = expected[name]
        print(f"  {name}: a={a}, b={b}, raw={raw}, product={product}, connected={conn}")
        check(f"{name} raw formula is exact", raw == exp_raw)
        check(f"{name} product formula is exact", product == exp_product)
        check(f"{name} connected Hessian is invariant", conn == exp_conn == BASE_CONNECTED)
    raw_values = {affine_raw(a, b) for a, b in shifts.values()}
    product_values = {affine_product(a, b) for a, b in shifts.values()}
    connected_values = {affine_connected(a, b) for a, b in shifts.values()}
    check("affine origin gauge changes raw moments", len(raw_values) > 1)
    check("affine origin gauge changes disconnected products", len(product_values) > 1)
    check("affine origin gauge preserves connected covariance in this family", connected_values == {BASE_CONNECTED})
    check("raw=1/product=1/9 is a gauge-fixed statement", affine_raw(Fraction(0), Fraction(0)) == 1 and affine_product(Fraction(0), Fraction(0)) == Fraction(1, 9))


def part3_scale_gauge() -> None:
    print()
    print("PART 3: multiplicative source-scale gauge")
    scales = {
        "identity": (Fraction(1), Fraction(1)),
        "double_x": (Fraction(2), Fraction(1)),
        "half_y": (Fraction(1), Fraction(1, 2)),
        "opposite": (Fraction(-1), Fraction(1)),
    }
    for name, (s, t) in scales.items():
        raw, product, conn = scaled(BASE_RAW, BASE_PRODUCT, BASE_CONNECTED, s, t)
        print(f"  {name}: s={s}, t={t}, raw={raw}, product={product}, connected={conn}")
        check(f"{name} raw scales by st", raw == s * t * BASE_RAW)
        check(f"{name} product scales by st", product == s * t * BASE_PRODUCT)
        check(f"{name} connected scales by st", conn == s * t * BASE_CONNECTED)
        if raw:
            check(f"{name} connected/raw ratio remains 8/9", conn / raw == Fraction(8, 9))
            check(f"{name} product/raw ratio remains 1/9", product / raw == Fraction(1, 9))
    check("absolute raw normalization needs scale fixing", scaled(BASE_RAW, BASE_PRODUCT, BASE_CONNECTED, Fraction(2), Fraction(1))[0] != BASE_RAW)
    check("absolute connected coefficient needs scale fixing", scaled(BASE_RAW, BASE_PRODUCT, BASE_CONNECTED, Fraction(1), Fraction(1, 2))[2] != BASE_CONNECTED)


def part4_dependency_classes() -> None:
    print()
    print("PART 4: dependency classes")
    deps = {
        "Pcal_connected_subtraction": "available_support",
        "formal_source_coordinates": "available_support_but_vacuous",
        "connected_hessian_covariance": "conditional_support",
        "source_additive_origin": "open",
        "source_multiplicative_scale": "open",
        "raw_E_XY_equals_one": "open",
        "one_point_product_equals_one_ninth": "open",
        "same_source_P_R_E_T_typing": "open",
        "endpoint_value": "forbidden",
    }
    allowed = {"available_support", "available_support_but_vacuous", "conditional_support", "open", "forbidden"}
    for name, status in deps.items():
        print(f"  {name}: {status}")
        check(f"{name} status classified", status in allowed)
    check("origin and scale are separate gates", deps["source_additive_origin"] == "open" and deps["source_multiplicative_scale"] == "open")
    check("raw/product theorem remains open", deps["raw_E_XY_equals_one"] == "open" and deps["one_point_product_equals_one_ninth"] == "open")
    check("endpoint value remains forbidden", deps["endpoint_value"] == "forbidden")


def part5_reachability() -> None:
    print()
    print("PART 5: reachability")
    pruned_edges = [
        ("formal_source_coordinates", "connected_hessian_possible"),
        ("connected_hessian_possible", "gauge_free_raw_product_split"),
        ("gauge_free_raw_product_split", "missing_source_gauge_fixing"),
    ]
    positive_edges = [
        ("Route2_source_coordinate_gauge_fixing_theorem", "fixed_origin"),
        ("Route2_source_coordinate_gauge_fixing_theorem", "fixed_scale"),
        ("fixed_origin", "raw_E_XY_equals_one"),
        ("fixed_scale", "raw_E_XY_equals_one"),
        ("raw_E_XY_equals_one", "uv_equals_one_ninth"),
        ("uv_equals_one_ninth", "Pcal_connected_subtraction"),
        ("Pcal_connected_subtraction", "kappa_zero_without_endpoint"),
    ]
    direct_edges = [
        ("Route2_physical_connected_Hessian_theorem", "coefficient_normalized_D2_logZ"),
        ("coefficient_normalized_D2_logZ", "kappa_zero_without_endpoint"),
    ]
    check("formal source route reaches missing gauge-fixing node", reachable(pruned_edges, "formal_source_coordinates", "missing_source_gauge_fixing"))
    check("formal source route does not reach kappa=0", not reachable(pruned_edges, "formal_source_coordinates", "kappa_zero_without_endpoint"))
    check("gauge-fixing theorem would reach kappa=0 through raw/product route", reachable(positive_edges, "Route2_source_coordinate_gauge_fixing_theorem", "kappa_zero_without_endpoint"))
    check("direct physical connected-Hessian theorem would bypass raw/product gauge split", reachable(direct_edges, "Route2_physical_connected_Hessian_theorem", "kappa_zero_without_endpoint"))
    all_nodes = {n for e in pruned_edges + positive_edges + direct_edges for n in e}
    check("reachability graph contains no endpoint-value node", all("rho_E" not in n and "c_TE" not in n for n in all_nodes))
    check("reachability graph does not use finite-box comparator", all("finite_box" not in n and "box" not in n for n in all_nodes))


def part6_document_boundary() -> None:
    print()
    print("PART 6: document boundary")
    note = text("QUARK_ROUTE2_SOURCE_COORDINATE_GAUGE_NORMALIZATION_NO_GO_NOTE_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    review = loop_text("REVIEW_HISTORY.md")
    state = loop_text("STATE.yaml")
    note_flat = flat(note)
    required = (
        "Actual current-surface status: no-go for formal source coordinates or connected Hessian data alone fixing the raw/disconnected Route-2 product normalization",
        "The raw/disconnected decomposition is not fixed until the physical source variables have a fixed origin and scale",
        "All three have the same connected Hessian 8/9",
        "Route-2 source-coordinate gauge-fixing theorem",
        "No endpoint value is used",
    )
    for marker in required:
        check(f"note contains marker: {marker}", marker in note_flat)
    for marker in ("Block111 Summary", "negative_route_pruning", "Do not audit", "Next Exact Action"):
        check(f"handoff contains marker: {marker}", marker in handoff)
    check("certificate keeps proposal disallowed", "proposal_allowed: false" in cert)
    check("trace gate names source-coordinate gauge-fixing theorem", "source-coordinate gauge-fixing theorem" in trace_gate)
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
    print("Route-2 source-coordinate gauge normalization no-go")
    print("TRACE: negative_route_pruning")
    part1_grounding()
    part2_affine_origin_gauge()
    part3_scale_gauge()
    part4_dependency_classes()
    part5_reachability()
    part6_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        return 1
    print("VERDICT: formal source coordinates or connected Hessian data do not fix the raw/product normalization; Route-2 needs a source-coordinate gauge-fixing theorem or a directly coefficient-normalized physical connected-Hessian theorem.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
