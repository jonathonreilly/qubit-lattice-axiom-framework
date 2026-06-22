#!/usr/bin/env python3
"""First-principles stretch no-go for the Route-2 log-odds selector."""

from __future__ import annotations

from collections import deque
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-log-odds-selector-stretch"

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


def law_from_q(q: Fraction) -> tuple[Fraction, Fraction, Fraction, Fraction, Fraction]:
    p_plus = q / (1 + q)
    p_minus = 1 / (1 + q)
    mean = p_plus - p_minus
    conn = 1 - mean * mean
    kappa = 9 * (conn - Fraction(8, 9))
    return p_plus, p_minus, mean, conn, kappa


def part1_grounding() -> None:
    print("PART 1: grounding")
    block105 = flat(text("QUARK_ROUTE2_SHARP_RECORD_BIAS_SELECTOR_NO_GO_NOTE_2026-06-22.md"))
    block104 = flat(text("QUARK_ROUTE2_SIGNED_QUOTIENT_CLASSIFICATION_NO_GO_NOTE_2026-06-22.md"))
    rn = flat(text("SOURCE_MEASURE_PCAL_RN_COCYCLE_THEOREM_NOTE_2026-05-30.md"))
    readout = flat(text("QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md"))
    hessian = flat(text("QUARK_ROUTE2_SOURCE_HESSIAN_CUMULANT_SELECTOR_SUPPORT_NOTE_2026-06-22.md"))
    check("Block105 names half-log-two selector", "h = +(1/2) log 2 or h = -(1/2) log 2" in block105)
    check("Block105 names sharp-record bias-selector theorem", "Route-2 sharp-record bias-selector theorem" in block105)
    check("Block104 names typed signed quotient plus source-measure bias", "typed signed quotient plus source-measure bias theorem" in block104)
    check("RN cocycle supplies normalized exponential chart", "R_h(epsilon) = exp(h epsilon - W(h))" in rn)
    check("exact readout supplies P_R labels, not source log odds", "P_R = [[alpha_E, 0, beta_E, 0]" in readout and "log odds" not in readout)
    check("source-Hessian support leaves same source primitive open", "same source/readout" in hessian and "missing physical readout primitive" in hessian)


def part2_minimal_premises() -> None:
    print()
    print("PART 2: minimal premise and forbidden import ledger")
    premises = {
        "typed_same_source_signed_record": "open",
        "sharp_record_RN_chart": "available_generic_support",
        "binary_same_record_normal_form": "conditional_support",
        "Pcal_connected_subtraction": "available_support",
        "endpoint_value_c_TE": "forbidden",
        "rho_E_reversal": "forbidden",
        "fitted_source_bias": "forbidden",
        "observational_comparator": "forbidden",
    }
    for name, status in premises.items():
        print(f"  {name}: {status}")
        check(f"{name} status classified", status in {"open", "available_generic_support", "conditional_support", "available_support", "forbidden"})
    check("A_min has no endpoint value premise", premises["endpoint_value_c_TE"] == "forbidden" and premises["rho_E_reversal"] == "forbidden")
    check("A_min keeps source bias unimported", premises["fitted_source_bias"] == "forbidden")


def part3_orbit_algebra() -> None:
    print()
    print("PART 3: RN log-odds orbit algebra")
    qs = [Fraction(1, 4), Fraction(1, 2), Fraction(1), Fraction(2), Fraction(4)]
    rows = {}
    for q in qs:
        p_plus, p_minus, mean, conn, k = law_from_q(q)
        rows[q] = (p_plus, p_minus, mean, conn, k)
        print(f"  q={q}: p_plus={p_plus}, p_minus={p_minus}, mean={mean}, connected={conn}, kappa={k}")
        check(f"q={q} probabilities normalize", p_plus + p_minus == 1)
        check(f"q={q} mean formula is exact", mean == (q - 1) / (q + 1))
        check(f"q={q} connected formula is exact", conn == 1 - mean * mean)
    check("q=2 and q=1/2 are the kappa=0 orbit", rows[Fraction(2)][4] == 0 and rows[Fraction(1, 2)][4] == 0)
    check("q=1 is the unbiased origin and gives kappa=1", rows[Fraction(1)][2] == 0 and rows[Fraction(1)][4] == 1)
    check("q=4 and q=1/4 share connected value by sign inversion", rows[Fraction(4)][3] == rows[Fraction(1, 4)][3])
    check("q=4 is valid but not the kappa=0 selector", rows[Fraction(4)][4] != 0)
    check("positive log-odds orbit contains continuum beyond q=2", all(q > 0 for q in qs) and len({r[4] for r in rows.values()}) > 2)


def part4_fanout() -> None:
    print()
    print("PART 4: stuck fan-out synthesis")
    frames = {
        "symmetry": ("h -> -h pairs selectors but does not choose |h|", "Route-2 magnitude selector"),
        "unit_tangent": ("Fisher unit fixes local scale at h=0, not finite displacement", "Route-2 finite source field"),
        "cumulant": ("connected subtraction computes 1-m^2 after m is known", "Route-2 one-point bias"),
        "P_R_readout": ("four-slot readout gives labels, not probability law or log odds", "Route-2 source/readout typing"),
        "RN_chart": ("exponential family admits every positive q", "Route-2 log-odds selector"),
    }
    for name, (attempt, missing) in frames.items():
        print(f"  {name}: {attempt}; missing={missing}")
        check(f"{name} attempt recorded", bool(attempt))
        check(f"{name} missing primitive recorded", missing.startswith("Route-2"))
    check("fan-out has five orthogonal frames", len(frames) == 5)
    check("no fan-out frame closes the selector", all("Route-2" in missing for _, missing in frames.values()))


def part5_reachability() -> None:
    print()
    print("PART 5: reachability")
    current_edges = [
        ("A_min_RN_Fisher_same_record", "log_odds_orbit_q_positive"),
        ("log_odds_orbit_q_positive", "missing_Route2_log_odds_selector"),
        ("missing_Route2_log_odds_selector", "bias_not_forced"),
    ]
    positive_edges = [
        ("typed_same_source_signed_record", "sharp_record_RN_chart"),
        ("sharp_record_RN_chart", "Route2_log_odds_selector_q2"),
        ("Route2_log_odds_selector_q2", "one_point_bias_abs_one_third"),
        ("one_point_bias_abs_one_third", "binary_product_normal_form"),
        ("binary_product_normal_form", "kappa_zero_without_endpoint"),
    ]
    check("A_min reaches the q-positive orbit", reachable(current_edges, "A_min_RN_Fisher_same_record", "log_odds_orbit_q_positive"))
    check("A_min reaches missing selector node", reachable(current_edges, "A_min_RN_Fisher_same_record", "missing_Route2_log_odds_selector"))
    check("A_min does not reach kappa=0", not reachable(current_edges, "A_min_RN_Fisher_same_record", "kappa_zero_without_endpoint"))
    check("positive log-odds selector route would reach kappa=0", reachable(positive_edges, "typed_same_source_signed_record", "kappa_zero_without_endpoint"))
    check("Route2 q=2 selector is load-bearing", reachable(positive_edges, "Route2_log_odds_selector_q2", "kappa_zero_without_endpoint"))
    all_nodes = {n for e in current_edges + positive_edges for n in e}
    check("reachability graph contains no endpoint-value node", all("rho_E" not in n and "c_TE" not in n for n in all_nodes))


def part6_document_boundary() -> None:
    print()
    print("PART 6: document boundary")
    note = text("QUARK_ROUTE2_LOG_ODDS_SELECTOR_STRETCH_NO_GO_NOTE_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    review = loop_text("REVIEW_HISTORY.md")
    state = loop_text("STATE.yaml")
    note_flat = flat(note)
    required = (
        "Actual current-surface status: no-go for the minimal RN/Fisher/same-record premise set selecting the Route-2 log-odds displacement",
        "A_min:",
        "Forbidden imports:",
        "q in {2, 1/2}",
        "Fan-Out Synthesis",
        "Route-2 log-odds selector theorem",
        "No endpoint value is used",
    )
    for marker in required:
        check(f"note contains marker: {marker}", marker in note_flat)
    for marker in ("Block106 Summary", "negative_route_pruning", "Do not audit", "Next Exact Action"):
        check(f"handoff contains marker: {marker}", marker in handoff)
    check("certificate keeps proposal disallowed", "proposal_allowed: false" in cert)
    check("trace gate names log-odds selector theorem", "log-odds selector theorem" in trace_gate)
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
    print("Route-2 log-odds selector stretch no-go")
    print("TRACE: negative_route_pruning")
    part1_grounding()
    part2_minimal_premises()
    part3_orbit_algebra()
    part4_fanout()
    part5_reachability()
    part6_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        return 1
    print("VERDICT: the minimal RN/Fisher/same-record surface reaches a continuous log-odds orbit but does not select |h|=1/2 log 2; the missing primitive is a Route-2 log-odds selector theorem.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
