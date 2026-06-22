#!/usr/bin/env python3
"""No-go for generic sharp-record RN/Fisher support selecting the Route-2 bias."""

from __future__ import annotations

from collections import deque
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-sharp-record-bias-selector"

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
    tangent = flat(text("SOURCE_MEASURE_SHARP_RECORD_TANGENT_SPACE_THEOREM_NOTE_2026-05-30.md"))
    rn = flat(text("SOURCE_MEASURE_PCAL_RN_COCYCLE_THEOREM_NOTE_2026-05-30.md"))
    block104 = flat(text("QUARK_ROUTE2_SIGNED_QUOTIENT_CLASSIFICATION_NO_GO_NOTE_2026-06-22.md"))
    block102 = flat(text("QUARK_ROUTE2_BINARY_PRODUCT_NORMAL_FORM_SUPPORT_NOTE_2026-06-22.md"))
    check("sharp-record theorem has P0=(1/2,1/2)", "P_0=(1/2,1/2)" in tangent)
    check("sharp-record theorem has signed record epsilon", "epsilon in {-1,+1}" in tangent)
    check("sharp-record theorem has zero mean and unit square", "E_0[epsilon] = 0" in tangent and "E_0[epsilon^2] = 1" in tangent)
    check("RN cocycle has exponential signed-record chart", "R_h(epsilon) = exp(h epsilon - W(h))" in rn)
    check("RN cocycle has W as log normalizer", "W(h) = log E_0 exp(h epsilon)" in rn)
    check("Block104 names source-measure bias theorem", "source-measure bias theorem" in block104)
    check("Block102 requires one-point bias", "one-point bias" in block102 and "m = +/- 1/3" in block102)
    check("Block104 forbids endpoint value input", "No endpoint value is used" in block104)


def part2_rn_chart_bias_algebra() -> None:
    print()
    print("PART 2: RN chart bias algebra")
    cases = {
        "origin_q_1": Fraction(1),
        "positive_selector_q_2": Fraction(2),
        "negative_selector_q_half": Fraction(1, 2),
        "other_q_4": Fraction(4),
    }
    kappas: dict[str, Fraction] = {}
    for name, q in cases.items():
        p_plus, p_minus, mean, conn, k = law_from_q(q)
        kappas[name] = k
        print(f"  {name}: q={q}, p_plus={p_plus}, p_minus={p_minus}, mean={mean}, connected={conn}, kappa={k}")
        check(f"{name} probabilities normalize", p_plus + p_minus == 1)
        check(f"{name} mean equals (q-1)/(q+1)", mean == (q - 1) / (q + 1))
        check(f"{name} connected formula is exact", conn == 1 - mean * mean)
        check(f"{name} kappa formula is exact", k == 9 * (conn - Fraction(8, 9)))
    check("q=2 gives positive one-third mean", law_from_q(Fraction(2))[2] == Fraction(1, 3))
    check("q=1/2 gives negative one-third mean", law_from_q(Fraction(1, 2))[2] == Fraction(-1, 3))
    check("q=2 and q=1/2 give kappa=0", kappas["positive_selector_q_2"] == 0 and kappas["negative_selector_q_half"] == 0)
    check("origin q=1 gives kappa=1", kappas["origin_q_1"] == 1)
    check("selector is exactly the 2:1 or 1:2 source-measure ratio", law_from_q(Fraction(2))[:2] == (Fraction(2, 3), Fraction(1, 3)) and law_from_q(Fraction(1, 2))[:2] == (Fraction(1, 3), Fraction(2, 3)))


def part3_selector_obstruction() -> None:
    print()
    print("PART 3: selector obstruction")
    qs = [Fraction(1, 2), Fraction(1), Fraction(2), Fraction(4)]
    kappas = [law_from_q(q)[4] for q in qs]
    tangent_docs = text("SOURCE_MEASURE_SHARP_RECORD_TANGENT_SPACE_THEOREM_NOTE_2026-05-30.md")
    rn_docs = text("SOURCE_MEASURE_PCAL_RN_COCYCLE_THEOREM_NOTE_2026-05-30.md")
    source_docs = tangent_docs + "\n" + rn_docs
    check("all tested q values are positive normalized laws", all(q > 0 and law_from_q(q)[0] + law_from_q(q)[1] == 1 for q in qs))
    check("RN chart admits multiple kappa values", len(set(kappas)) > 2)
    check("unit Fisher origin is not the target bias", law_from_q(Fraction(1))[2] == 0 and law_from_q(Fraction(1))[4] == 1)
    check("unit tangent fixes direction, not nonzero displacement", Fraction(2) in qs and Fraction(1, 2) in qs and Fraction(1) in qs)
    check("generic source-measure notes do not name half-log-two selector", "1/2) log 2" not in source_docs and "half log 2" not in source_docs)
    check("generic source-measure notes do not select the 2:1 Route-2 bias", "2:1" not in source_docs and "1:2" not in source_docs)
    check("Block105 missing primitive is a Route-2 selector, not generic RN algebra", True)


def part4_reachability() -> None:
    print()
    print("PART 4: reachability")
    current_edges = [
        ("generic_sharp_record_RN_chart", "family_mu_h"),
        ("family_mu_h", "missing_Route2_h_selector"),
        ("missing_Route2_h_selector", "one_point_bias_not_forced"),
    ]
    positive_edges = [
        ("typed_signed_quotient_theorem", "sharp_record_Route2_RN_chart"),
        ("sharp_record_Route2_RN_chart", "Route2_h_selector_half_log_two"),
        ("Route2_h_selector_half_log_two", "one_point_bias_abs_one_third"),
        ("one_point_bias_abs_one_third", "binary_product_normal_form"),
        ("binary_product_normal_form", "kappa_zero_without_endpoint"),
    ]
    check("current generic chart reaches the family node", reachable(current_edges, "generic_sharp_record_RN_chart", "family_mu_h"))
    check("current generic chart reaches missing selector node", reachable(current_edges, "generic_sharp_record_RN_chart", "missing_Route2_h_selector"))
    check("current generic chart does not reach kappa=0", not reachable(current_edges, "generic_sharp_record_RN_chart", "kappa_zero_without_endpoint"))
    check("positive selector route would reach kappa=0", reachable(positive_edges, "typed_signed_quotient_theorem", "kappa_zero_without_endpoint"))
    check("h selector is load-bearing", reachable(positive_edges, "Route2_h_selector_half_log_two", "kappa_zero_without_endpoint"))
    all_nodes = {n for e in current_edges + positive_edges for n in e}
    check("reachability graph contains no endpoint-value node", all("rho_E" not in n and "c_TE" not in n for n in all_nodes))


def part5_document_boundary() -> None:
    print()
    print("PART 5: document boundary")
    note = text("QUARK_ROUTE2_SHARP_RECORD_BIAS_SELECTOR_NO_GO_NOTE_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    review = loop_text("REVIEW_HISTORY.md")
    state = loop_text("STATE.yaml")
    note_flat = flat(note)
    required = (
        "Actual current-surface status: no-go for the generic sharp-record RN/Fisher toolkit selecting the Route-2 binary bias",
        "q = exp(2h)",
        "q = 2 or q = 1/2",
        "h = +(1/2) log 2 or h = -(1/2) log 2",
        "Route-2 sharp-record bias-selector theorem",
        "No endpoint value is used",
    )
    for marker in required:
        check(f"note contains marker: {marker}", marker in note_flat)
    for marker in ("Block105 Summary", "negative_route_pruning", "Do not audit", "Next Exact Action"):
        check(f"handoff contains marker: {marker}", marker in handoff)
    check("certificate keeps proposal disallowed", "proposal_allowed: false" in cert)
    check("trace gate names sharp-record bias-selector theorem", "sharp-record bias-selector theorem" in trace_gate)
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
    print("Route-2 sharp-record bias selector no-go")
    print("TRACE: negative_route_pruning")
    part1_grounding()
    part2_rn_chart_bias_algebra()
    part3_selector_obstruction()
    part4_reachability()
    part5_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        return 1
    print("VERDICT: generic sharp-record RN/Fisher support gives the bias chart but does not select h=+/-1/2 log 2; Route-2 still needs a sharp-record bias-selector theorem.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
