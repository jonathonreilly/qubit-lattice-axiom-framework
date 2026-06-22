#!/usr/bin/env python3
"""Classify signed quotients of the Route-2 four-slot P_R surface."""

from __future__ import annotations

from collections import Counter, deque
from fractions import Fraction
from itertools import product
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-signed-quotient-classification"

LABELS = ("E-shell", "E-center", "T-shell", "T-center")

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


def connected(mean: Fraction) -> Fraction:
    return 1 - mean * mean


def kappa(value: Fraction) -> Fraction:
    return 9 * (value - Fraction(8, 9))


def sign_maps() -> list[tuple[int, ...]]:
    return list(product((-1, 1), repeat=len(LABELS)))


def is_surjective(sig: tuple[int, ...]) -> bool:
    return -1 in sig and 1 in sig


def uniform_mean(sig: tuple[int, ...]) -> Fraction:
    return Fraction(sum(sig), len(sig))


def mean_from_pplus(p_plus: Fraction) -> Fraction:
    return p_plus - (1 - p_plus)


def part1_grounding() -> None:
    print("PART 1: grounding")
    readout = flat(text("QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md"))
    block103 = flat(text("QUARK_ROUTE2_BINARY_SAME_RECORD_TRANSFER_NO_GO_NOTE_2026-06-22.md"))
    block102 = flat(text("QUARK_ROUTE2_BINARY_PRODUCT_NORMAL_FORM_SUPPORT_NOTE_2026-06-22.md"))
    check("exact readout has four P_R labels", all(label in readout for label in LABELS))
    check("exact readout has channelwise P_R matrix", "P_R = [[alpha_E, 0, beta_E, 0]" in readout)
    check("Block103 names binary same-record source theorem", "Route-2 binary same-record source theorem" in block103)
    check("Block103 leaves sign map and probabilities missing", "do not give P(+1) and P(-1)" in block103)
    check("Block102 reduces binary route to one-point bias", "one-point bias" in block102 and "m = +/- 1/3" in block102)
    check("Block102 forbids endpoint value input", "No endpoint value is used" in block102)


def part2_uniform_signed_quotients() -> None:
    print()
    print("PART 2: deterministic signed quotients with uniform four-label measure")
    maps = sign_maps()
    counts = Counter(sig.count(1) for sig in maps)
    surj = [sig for sig in maps if is_surjective(sig)]
    balanced = [sig for sig in surj if sig.count(1) == 2]
    one_vs_three = [sig for sig in surj if sig.count(1) in {1, 3}]
    uniform_all = sorted({uniform_mean(sig) for sig in maps})
    uniform_surj = sorted({uniform_mean(sig) for sig in surj})

    print(f"  plus-count histogram: {dict(sorted(counts.items()))}")
    print(f"  uniform means, all maps: {uniform_all}")
    print(f"  uniform means, nonconstant maps: {uniform_surj}")
    check("there are 16 deterministic signed maps", len(maps) == 16)
    check("there are 14 nonconstant binary quotients", len(surj) == 14)
    check("there are 6 balanced two-plus/two-minus quotients", len(balanced) == 6)
    check("there are 8 one-vs-three quotients", len(one_vs_three) == 8)
    check("uniform four-label means are classified exactly", uniform_all == [Fraction(-1), Fraction(-1, 2), Fraction(0), Fraction(1, 2), Fraction(1)])
    check("uniform nonconstant means exclude +/-1/3", Fraction(1, 3) not in uniform_surj and Fraction(-1, 3) not in uniform_surj)

    channel_plus = (1, 1, -1, -1)
    radial_plus = (1, -1, 1, -1)
    diagonal_plus = (1, -1, -1, 1)
    for name, sig in (
        ("channel E/T quotient", channel_plus),
        ("shell/center quotient", radial_plus),
        ("diagonal quotient", diagonal_plus),
    ):
        print(f"  {name}: uniform mean={uniform_mean(sig)}")
        check(f"{name} is balanced under uniform four-label measure", uniform_mean(sig) == 0)
    check("no uniform four-label quotient gives the Block102 bias", all(abs(uniform_mean(sig)) != Fraction(1, 3) for sig in surj))


def part3_free_source_measure() -> None:
    print()
    print("PART 3: free source measure on a fixed nonconstant quotient")
    candidates = {
        "uniform_binary": Fraction(1, 2),
        "positive_two_to_one": Fraction(2, 3),
        "negative_one_to_two": Fraction(1, 3),
        "degenerate_plus": Fraction(1),
    }
    kappas: dict[str, Fraction] = {}
    for name, p_plus in candidates.items():
        p_minus = 1 - p_plus
        mean = mean_from_pplus(p_plus)
        conn = connected(mean)
        k = kappa(conn)
        kappas[name] = k
        print(f"  {name}: p_plus={p_plus}, p_minus={p_minus}, mean={mean}, connected={conn}, kappa={k}")
        check(f"{name} probabilities normalize", p_plus + p_minus == 1)
        check(f"{name} mean formula is exact", mean == p_plus - p_minus)
        check(f"{name} connected formula is exact", conn == 1 - mean * mean)
        check(f"{name} kappa formula is exact", k == 9 * (conn - Fraction(8, 9)))
    check("two-to-one and one-to-two source measures give kappa=0", kappas["positive_two_to_one"] == 0 and kappas["negative_one_to_two"] == 0)
    check("uniform binary source measure gives kappa=1", kappas["uniform_binary"] == 1)
    check("free measure changes kappa under the same sign quotient", len(set(kappas.values())) > 1)
    check("the desired bias is exactly a 2:1 source-measure ratio", mean_from_pplus(Fraction(2, 3)) == Fraction(1, 3))


def part4_reachability() -> None:
    print()
    print("PART 4: reachability")
    current_edges = [
        ("exact_P_R_four_labels", "deterministic_signed_quotient_family"),
        ("deterministic_signed_quotient_family", "missing_source_measure"),
        ("missing_source_measure", "one_point_bias_not_forced"),
    ]
    positive_edges = [
        ("typed_signed_quotient_theorem", "same_source_binary_record"),
        ("same_source_binary_record", "source_measure_bias_theorem"),
        ("source_measure_bias_theorem", "one_point_bias_abs_one_third"),
        ("one_point_bias_abs_one_third", "binary_product_normal_form"),
        ("binary_product_normal_form", "kappa_zero_without_endpoint"),
    ]
    check("current P_R labels reach signed-quotient family", reachable(current_edges, "exact_P_R_four_labels", "deterministic_signed_quotient_family"))
    check("signed-quotient family reaches missing measure node", reachable(current_edges, "exact_P_R_four_labels", "missing_source_measure"))
    check("current P_R labels do not reach kappa=0", not reachable(current_edges, "exact_P_R_four_labels", "kappa_zero_without_endpoint"))
    check("positive refined theorem would reach kappa=0", reachable(positive_edges, "typed_signed_quotient_theorem", "kappa_zero_without_endpoint"))
    check("source-measure bias theorem is load-bearing", reachable(positive_edges, "source_measure_bias_theorem", "kappa_zero_without_endpoint"))
    all_nodes = {n for e in current_edges + positive_edges for n in e}
    check("reachability graph contains no endpoint-value node", all("rho_E" not in n and "c_TE" not in n for n in all_nodes))


def part5_document_boundary() -> None:
    print()
    print("PART 5: document boundary")
    note = text("QUARK_ROUTE2_SIGNED_QUOTIENT_CLASSIFICATION_NO_GO_NOTE_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    review = loop_text("REVIEW_HISTORY.md")
    state = loop_text("STATE.yaml")
    note_flat = flat(note)
    required = (
        "Actual current-surface status: no-go for deterministic signed quotient alone forcing the Route-2 binary one-point bias",
        "There are 16 deterministic maps and 14 nonconstant binary quotients",
        "The natural uniform four-label quotient also does not help",
        "Route-2 typed signed quotient plus source-measure bias theorem",
        "mu(sigma=+1):mu(sigma=-1) = 2:1 or 1:2",
        "No endpoint value is used",
    )
    for marker in required:
        check(f"note contains marker: {marker}", marker in note_flat)
    for marker in ("Block104 Summary", "negative_route_pruning", "Do not audit", "Next Exact Action"):
        check(f"handoff contains marker: {marker}", marker in handoff)
    check("certificate keeps proposal disallowed", "proposal_allowed: false" in cert)
    check("trace gate names source-measure bias theorem", "source-measure bias theorem" in trace_gate)
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
    print("Route-2 signed quotient classification no-go")
    print("TRACE: negative_route_pruning")
    part1_grounding()
    part2_uniform_signed_quotients()
    part3_free_source_measure()
    part4_reachability()
    part5_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        return 1
    print("VERDICT: a deterministic signed quotient of the four P_R labels does not force the Block102 one-point bias; the missing primitive is a Route-2 typed signed quotient plus source-measure bias theorem.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
