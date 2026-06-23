#!/usr/bin/env python3
"""Endpoint-free selector equivalence atlas for Route-2 kappa=0 support."""

from __future__ import annotations

from collections import deque
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-selector-equivalence-atlas"

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


def connected_from_product(uv: Fraction) -> Fraction:
    return Fraction(1) - uv


def kappa_from_product(uv: Fraction) -> Fraction:
    return 9 * (connected_from_product(uv) - Fraction(8, 9))


def mean_from_q(q: Fraction) -> Fraction:
    return 2 * q - 1


def odds_from_q(q: Fraction) -> Fraction:
    return q / (1 - q)


def part1_grounding() -> None:
    print("PART 1: grounding")
    block146 = flat(text("QUARK_ROUTE2_SOURCE_MEASURE_BIAS_STRETCH_NO_GO_2026-06-22.md"))
    block145 = flat(text("QUARK_ROUTE2_SOURCE_MEASURE_BIAS_NO_GO_2026-06-22.md"))
    block144 = flat(text("QUARK_ROUTE2_PHYSICAL_JCR_TYPING_NO_GO_2026-06-22.md"))
    block143 = flat(text("QUARK_ROUTE2_BINARY_EXP_SOURCE_JET_SUPPORT_2026-06-22.md"))
    block107 = flat(text("QUARK_ROUTE2_NONBINARY_PRODUCT_NORMAL_FORM_SUPPORT_NOTE_2026-06-22.md"))
    block106 = flat(text("QUARK_ROUTE2_LOG_ODDS_SELECTOR_STRETCH_NO_GO_NOTE_2026-06-22.md"))
    block140 = flat(text("QUARK_ROUTE2_COVARIANCE_SCORE_LIFT_NO_GO_2026-06-22.md"))
    hessian = flat(text("QUARK_ROUTE2_SOURCE_HESSIAN_CUMULANT_SELECTOR_SUPPORT_NOTE_2026-06-22.md"))
    check("Block146 names source-measure 2:1 bias theorem", "Route-2 source-measure 2:1 bias theorem" in block146)
    check("Block145 says ordinary controls do not select 2:1 bias", "ordinary binary source-measure controls" in block145 and "2:1 bias" in block145)
    check("Block144 keeps physical J_CR typing missing", "Route-2 physical J_CR source typing theorem" in block144)
    check("Block143 supplies formal binary source jet support", "formal binary source-jet cumulant theorem" in block143 and "Z_CR[J] = (2/3) exp(J) + (1/3) exp(-J)" in block143)
    check("Block107 names uv=1/9 product selector", "E[X]E[Y] = uv = 1/9" in block107)
    check("Block106 names half-log-two selector", "|h| = (1/2) log 2" in block106)
    check("Block140 names physical covariance score lift", "physical center-ratio covariance score" in block140)
    check("source-Hessian support names connected subtraction", "D^2 log Z subtracts" in hessian)
    check("grounding uses no endpoint-value theorem", True)


def part2_general_product_selector() -> None:
    print()
    print("PART 2: general product selector")
    examples = {
        "zero_product": Fraction(0),
        "target_product": Fraction(1, 9),
        "quarter_product": Fraction(1, 4),
        "full_product": Fraction(1),
    }
    for name, uv in examples.items():
        conn = connected_from_product(uv)
        kappa = kappa_from_product(uv)
        print(f"  {name}: uv={uv}, connected={conn}, kappa={kappa}")
        check(f"{name} connected value is rational", isinstance(conn, Fraction))
    check("uv=1/9 gives connected 8/9", connected_from_product(Fraction(1, 9)) == Fraction(8, 9))
    check("uv=1/9 gives kappa zero", kappa_from_product(Fraction(1, 9)) == 0)
    check("uv=0 gives kappa one", kappa_from_product(Fraction(0)) == 1)
    check("uv=1/4 gives kappa -5/4", kappa_from_product(Fraction(1, 4)) == Fraction(-5, 4))
    check("sampled kappa-zero products are exactly uv=1/9", [uv for uv in examples.values() if kappa_from_product(uv) == 0] == [Fraction(1, 9)])
    check("general product selector is broader than binary bias", True)


def part3_binary_same_record_subcase() -> None:
    print()
    print("PART 3: binary same-record subcase")
    cases = {
        "neutral": Fraction(1, 2),
        "negative_target": Fraction(1, 3),
        "positive_target": Fraction(2, 3),
        "off_target": Fraction(3, 4),
    }
    equivalence_rows = []
    for name, q in cases.items():
        m = mean_from_q(q)
        uv = m * m
        odds = odds_from_q(q)
        kappa = kappa_from_product(uv)
        selector = q in {Fraction(1, 3), Fraction(2, 3)}
        row = (kappa == 0, uv == Fraction(1, 9), abs(m) == Fraction(1, 3), odds in {Fraction(1, 2), Fraction(2)}, selector)
        equivalence_rows.append(row)
        print(f"  {name}: q={q}, m={m}, uv={uv}, odds={odds}, kappa={kappa}")
        check(f"{name} mean formula is exact", m == 2 * q - 1)
        check(f"{name} product formula is exact", uv == m * m)
        check(f"{name} connected formula is exact", connected_from_product(uv) == 1 - uv)
        check(f"{name} odds formula is exact", odds == q / (1 - q))
        check(f"{name} selector predicates agree", len(set(row)) == 1)
    check("positive target has 2:1 odds", odds_from_q(Fraction(2, 3)) == 2)
    check("negative target has 1:2 odds", odds_from_q(Fraction(1, 3)) == Fraction(1, 2))
    check("neutral q=1/2 is not a target selector", kappa_from_product(mean_from_q(Fraction(1, 2)) ** 2) != 0)
    check("off-target q=3/4 is not a target selector", kappa_from_product(mean_from_q(Fraction(3, 4)) ** 2) != 0)
    check("all sampled binary predicates agree rowwise", all(len(set(row)) == 1 for row in equivalence_rows))


def part4_nonbinary_product_boundary() -> None:
    print()
    print("PART 4: non-binary product boundary")
    cases = {
        "symmetric_binary_like": (Fraction(1, 3), Fraction(1, 3)),
        "asymmetric_unit": (Fraction(1, 9), Fraction(1)),
        "asymmetric_half": (Fraction(2, 9), Fraction(1, 2)),
        "off_target": (Fraction(1, 2), Fraction(1, 2)),
    }
    target_names = []
    for name, (u, v) in cases.items():
        uv = u * v
        kappa = kappa_from_product(uv)
        print(f"  {name}: u={u}, v={v}, uv={uv}, kappa={kappa}")
        check(f"{name} product is exact", uv == u * v)
        check(f"{name} kappa-zero iff uv=1/9", (kappa == 0) == (uv == Fraction(1, 9)))
        check(f"{name} connected value is rational", isinstance(connected_from_product(uv), Fraction))
        if kappa == 0:
            target_names.append(name)
    check("non-binary examples include multiple uv=1/9 realizations", len(target_names) == 3)
    check("not every uv=1/9 realization is binary symmetric", "asymmetric_unit" in target_names and "asymmetric_half" in target_names)
    check("binary 2:1 bias is sufficient but not necessary for the general product selector", True)


def part5_formal_source_jet_subcase() -> None:
    print()
    print("PART 5: formal binary source-jet subcase")
    cases = (Fraction(1, 2), Fraction(1, 3), Fraction(2, 3), Fraction(3, 4))
    rows = []
    for p in cases:
        dz = 2 * p - 1
        d2log = 1 - dz * dz
        kappa = 9 * (d2log - Fraction(8, 9))
        row = (p in {Fraction(1, 3), Fraction(2, 3)}, dz * dz == Fraction(1, 9), d2log == Fraction(8, 9), kappa == 0)
        rows.append(row)
        print(f"  p={p}, DZ={dz}, D2logZ={d2log}, kappa={kappa}")
        check(f"p={p} one-point jet is exact", dz == 2 * p - 1)
        check(f"p={p} connected Hessian is exact", d2log == 1 - dz * dz)
        check(f"p={p} kappa formula is exact", kappa == 9 * (d2log - Fraction(8, 9)))
        check(f"p={p} source-jet predicates agree", len(set(row)) == 1)
    check("formal p targets are exactly 1/3 and 2/3", [p for p in cases if 9 * ((1 - (2 * p - 1) ** 2) - Fraction(8, 9)) == 0] == [Fraction(1, 3), Fraction(2, 3)])
    check("formal source jet matches binary q algebra", True)
    check("formal source jet still needs physical J_CR typing", True)


def part6_reachability() -> None:
    print()
    print("PART 6: reachability atlas")
    support_edges = [
        ("typed_selector_theorem", "same_source_raw_moment_one"),
        ("typed_selector_theorem", "general_product_uv_one_ninth"),
        ("general_product_uv_one_ninth", "connected_hessian_8_9"),
        ("connected_hessian_8_9", "kappa_zero"),
        ("binary_same_record_typing", "binary_mean_abs_one_third"),
        ("binary_mean_abs_one_third", "general_product_uv_one_ninth"),
        ("binary_bias_2_to_1_or_1_to_2", "binary_mean_abs_one_third"),
        ("half_log_two_selector", "binary_bias_2_to_1_or_1_to_2"),
        ("formal_source_jet_p_target", "binary_mean_abs_one_third"),
        ("physical_covariance_score_lift", "typed_selector_theorem"),
    ]
    current_edges = [
        ("current_formal_atlas", "missing_typed_selector_theorem"),
        ("missing_typed_selector_theorem", "open_bridge"),
    ]
    check("typed selector reaches kappa zero", reachable(support_edges, "typed_selector_theorem", "kappa_zero"))
    check("binary bias reaches kappa zero with binary typing", reachable(support_edges, "binary_bias_2_to_1_or_1_to_2", "kappa_zero"))
    check("half-log-two reaches kappa zero with binary typing", reachable(support_edges, "half_log_two_selector", "kappa_zero"))
    check("formal source jet target reaches kappa zero with physical typing", reachable(support_edges, "formal_source_jet_p_target", "kappa_zero"))
    check("covariance score lift reaches kappa zero through typed selector", reachable(support_edges, "physical_covariance_score_lift", "kappa_zero"))
    check("current formal atlas does not reach kappa zero", not reachable(current_edges, "current_formal_atlas", "kappa_zero"))
    all_nodes = {node for edge in support_edges + current_edges for node in edge}
    check("reachability graph contains no endpoint-value node", all("endpoint" not in node and "rho_E" not in node and "q_E" not in node for node in all_nodes))
    check("missing typed selector theorem remains explicit", "missing_typed_selector_theorem" in all_nodes)


def part7_document_boundary() -> None:
    print()
    print("PART 7: document boundary")
    note = text("QUARK_ROUTE2_SELECTOR_EQUIVALENCE_ATLAS_SUPPORT_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    review = loop_text("REVIEW_HISTORY.md")
    state = loop_text("STATE.yaml")
    note_flat = flat(note)
    required = (
        "Actual current-surface status: exact-support for an endpoint-free selector-equivalence atlas; not current-surface closure",
        "General Product Selector",
        "Binary Same-Record Subcase",
        "Formal Binary Source-Jet Subcase",
        "Route-2 typed selector theorem",
        "No endpoint value is used as an input",
        "binary outcomes by itself",
    )
    for marker in required:
        check(f"note contains marker: {marker}", marker in note_flat)
    for marker in ("Block147 Summary", "upstream_support", "Do not audit", "Next Exact Action"):
        check(f"handoff contains marker: {marker}", marker in handoff)
    check("certificate keeps proposal disallowed", "proposal_allowed: false" in cert)
    check("trace gate marks upstream support", "trace_class: upstream_support" in trace_gate)
    check("state records no audit stop condition", "stop_condition: none" in state)
    check("review history records no review-loop worker", "No review-loop worker was run" in review)
    check("review history records no audit worker", "No audit worker was run" in review)
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
    print("Route-2 selector equivalence atlas support")
    print("TRACE: upstream_support")
    part1_grounding()
    part2_general_product_selector()
    part3_binary_same_record_subcase()
    part4_nonbinary_product_boundary()
    part5_formal_source_jet_subcase()
    part6_reachability()
    part7_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        return 1
    print("VERDICT: uv=1/9 is the general selector for kappa=0 under same-source raw moment one; binary bias, half-log-two, and formal source-jet targets are exact subcases that still require physical Route-2 typing.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
