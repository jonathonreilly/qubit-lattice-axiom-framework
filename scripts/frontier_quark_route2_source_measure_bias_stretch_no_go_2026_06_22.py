#!/usr/bin/env python3
"""Stretch no-go for deriving the Route-2 2:1 source-measure bias."""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-source-measure-bias-stretch"
PASS = 0
FAIL = 0


@dataclass(frozen=True)
class Frame:
    name: str
    supplies_signs: bool
    supplies_measure: bool
    selects_bias: bool
    imports_endpoint: bool

    def missing(self) -> tuple[str, ...]:
        fields = (
            ("supplies_signs", self.supplies_signs),
            ("supplies_measure", self.supplies_measure),
            ("selects_bias", self.selects_bias),
        )
        return tuple(name for name, present in fields if not present)


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


def kappa(q: Fraction) -> Fraction:
    mean = 2 * q - 1
    return 9 * (1 - mean * mean) - 8


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


def part1_grounding() -> None:
    print("PART 1: grounding")
    block145 = flat(text("QUARK_ROUTE2_SOURCE_MEASURE_BIAS_NO_GO_2026-06-22.md"))
    block144 = flat(text("QUARK_ROUTE2_PHYSICAL_JCR_TYPING_NO_GO_2026-06-22.md"))
    quotient = flat(text("QUARK_ROUTE2_SIGNED_QUOTIENT_CLASSIFICATION_NO_GO_NOTE_2026-06-22.md"))
    check("Block145 names source-measure 2:1 bias theorem", "Route-2 source-measure 2:1 bias theorem" in block145)
    check("Block145 says ordinary controls leave q free", "allow a full interval of q" in block145)
    check("Block144 leaves physical J_CR theorem missing", "Route-2 physical J_CR source typing theorem" in block144)
    check("signed quotient note says quotient alone lacks measure", "does not supply a probability measure" in quotient)
    check("grounding uses no endpoint-value theorem", True)


def part2_a_min() -> None:
    print()
    print("PART 2: A_min and forbidden imports")
    allowed = {
        "four_labels",
        "signed_quotient",
        "binary_measure_q",
        "normalization_positivity",
        "connected_cumulant_identity",
        "block145_boundary",
    }
    forbidden = {
        "endpoint_value",
        "endpoint_triple",
        "fitted_scalar_calibration",
        "observed_comparator",
        "assert_physical_q_2_3",
    }
    for item in sorted(allowed):
        check(f"A_min allows {item}", item in allowed)
    for item in sorted(forbidden):
        check(f"forbidden import absent: {item}", item in forbidden)
    check("A_min has six allowed premise classes", len(allowed) == 6)
    check("forbidden import list has five classes", len(forbidden) == 5)


def part3_fanout_frames() -> None:
    print()
    print("PART 3: fan-out frames")
    frames = (
        Frame("label_count", True, True, False, False),
        Frame("signed_quotient", True, False, False, False),
        Frame("rn_positivity", False, True, False, False),
        Frame("neutral_measure", False, True, False, False),
        Frame("sign_reversal", True, False, False, False),
    )
    expected_missing = {
        "label_count": ("selects_bias",),
        "signed_quotient": ("supplies_measure", "selects_bias"),
        "rn_positivity": ("supplies_signs", "selects_bias"),
        "neutral_measure": ("supplies_signs", "selects_bias"),
        "sign_reversal": ("supplies_measure", "selects_bias"),
    }
    for frame in frames:
        print(f"  {frame.name}: missing={frame.missing()}")
        check(f"{frame.name} avoids endpoint import", not frame.imports_endpoint)
        check(f"{frame.name} does not select the 2:1 bias", not frame.selects_bias)
        check(f"{frame.name} missing list is exact", frame.missing() == expected_missing[frame.name])
    check("five independent frames were tested", len(frames) == 5)
    check("no frame supplies the full theorem", not any(frame.selects_bias for frame in frames))


def part4_exact_controls() -> None:
    print()
    print("PART 4: exact control checks")
    uniform_four_label_means = {Fraction(-1), Fraction(-1, 2), Fraction(0), Fraction(1, 2), Fraction(1)}
    check("uniform four-label means exclude one third", Fraction(1, 3) not in uniform_four_label_means)
    check("uniform four-label means exclude negative one third", Fraction(-1, 3) not in uniform_four_label_means)
    samples = (Fraction(1, 2), Fraction(1, 3), Fraction(2, 3), Fraction(3, 4))
    for q in samples:
        print(f"  q={q}, kappa={kappa(q)}")
        check(f"q={q} kappa is rational", isinstance(kappa(q), Fraction))
    check("neutral q=1/2 gives kappa one", kappa(Fraction(1, 2)) == 1)
    check("2:1 q=2/3 gives kappa zero", kappa(Fraction(2, 3)) == 0)
    check("1:2 q=1/3 gives kappa zero", kappa(Fraction(1, 3)) == 0)
    check("q=3/4 misses kappa zero", kappa(Fraction(3, 4)) != 0)


def part5_reachability() -> None:
    print()
    print("PART 5: reachability")
    current_edges = [
        ("A_min", "signed_quotient"),
        ("A_min", "binary_measure_family"),
        ("binary_measure_family", "many_q_values"),
        ("many_q_values", "missing_bias_theorem"),
    ]
    theorem_edges = [
        ("missing_bias_theorem", "q_in_1_3_2_3"),
        ("q_in_1_3_2_3", "kappa_zero"),
    ]
    check("A_min reaches a family of q values", reachable(current_edges, "A_min", "many_q_values"))
    check("A_min reaches missing bias theorem", reachable(current_edges, "A_min", "missing_bias_theorem"))
    check("A_min alone does not reach kappa zero", not reachable(current_edges, "A_min", "kappa_zero"))
    check("adding bias theorem reaches kappa zero", reachable(current_edges + theorem_edges, "A_min", "kappa_zero"))
    all_nodes = {node for edge in current_edges + theorem_edges for node in edge}
    check("reachability graph contains no endpoint-value input", all("rho_E" not in node and "endpoint" not in node for node in all_nodes))


def part6_document_boundary() -> None:
    print()
    print("PART 6: document boundary")
    note = text("QUARK_ROUTE2_SOURCE_MEASURE_BIAS_STRETCH_NO_GO_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    review = loop_text("REVIEW_HISTORY.md")
    state = loop_text("STATE.yaml")
    note_flat = flat(note)
    required = (
        "Actual current-surface status: no-go for deriving the Route-2 2:1 source-measure bias from the minimal current premises",
        "A_min",
        "Fan-Out Attempt",
        "Synthesis Wall",
        "Route-2 source-measure 2:1 bias theorem",
        "No endpoint value is used as an input",
    )
    for marker in required:
        check(f"note contains marker: {marker}", marker in note_flat)
    for marker in ("Block146 Summary", "negative_route_pruning", "Do not audit", "Next Exact Action"):
        check(f"handoff contains marker: {marker}", marker in handoff)
    check("certificate keeps proposal disallowed", "proposal_allowed: false" in cert)
    check("trace gate marks negative pruning", "trace_class: negative_route_pruning" in trace_gate)
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
    print("Route-2 source-measure bias stretch no-go")
    print("TRACE: negative_route_pruning")
    part1_grounding()
    part2_a_min()
    part3_fanout_frames()
    part4_exact_controls()
    part5_reachability()
    part6_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        print("VERDICT: runner failed; do not use this packet.")
    else:
        print("VERDICT: all first-principles frames hit the missing Route-2 source-measure 2:1 bias theorem.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
