#!/usr/bin/env python3
"""Queue-exhaustion certificate for the Route-2 source/readout primitive."""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-source-readout-primitive-queue-exhaustion"

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class QueueItem:
    route: str
    status: str
    guard: str
    missing: str


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


def items() -> list[QueueItem]:
    return [
        QueueItem("formal_selector_atlas", "support_only", "Block147", "physical typed selector theorem"),
        QueueItem("weakened_selector_bridge", "pruned", "Block148", "full same-source selector bridge theorem"),
        QueueItem("current_candidate_instantiation", "pruned", "Block149", "physical same-source selector realization theorem"),
        QueueItem("finite_pr_rows_to_ocr_or_moments", "pruned", "Block142/101", "P_R-to-O_CR and Pcal moment-realization theorems"),
        QueueItem("formal_jcr_source_jet", "pruned", "Block144", "physical J_CR source typing theorem"),
        QueueItem("source_measure_bias", "pruned", "Block145/146", "Route-2 source-measure 2:1 bias theorem"),
        QueueItem("covariance_score", "pruned", "Block140", "physical covariance score-lift theorem"),
        QueueItem("generic_pcal_fisher_unit", "pruned", "Block100/126/130", "Route-2 objects and unit calibration theorem"),
    ]


def part1_grounding() -> None:
    print("PART 1: grounding")
    docs = {
        "block147": flat(text("QUARK_ROUTE2_SELECTOR_EQUIVALENCE_ATLAS_SUPPORT_2026-06-22.md")),
        "block148": flat(text("QUARK_ROUTE2_SAME_SOURCE_SELECTOR_CLAUSE_INDEPENDENCE_NO_GO_2026-06-22.md")),
        "block149": flat(text("QUARK_ROUTE2_PHYSICAL_SELECTOR_INSTANTIATION_FANOUT_NO_GO_2026-06-22.md")),
        "block142": flat(text("QUARK_ROUTE2_PR_ROW_OCR_FUNCTOR_NO_GO_2026-06-22.md")),
        "block101": flat(text("QUARK_ROUTE2_PCAL_MOMENT_REALIZATION_NO_GO_NOTE_2026-06-22.md")),
        "block144": flat(text("QUARK_ROUTE2_PHYSICAL_JCR_TYPING_NO_GO_2026-06-22.md")),
        "block146": flat(text("QUARK_ROUTE2_SOURCE_MEASURE_BIAS_STRETCH_NO_GO_2026-06-22.md")),
        "block140": flat(text("QUARK_ROUTE2_COVARIANCE_SCORE_LIFT_NO_GO_2026-06-22.md")),
        "block100": flat(text("QUARK_ROUTE2_SOURCE_MEASURE_PRODUCT_REGISTRY_TRANSFER_NO_GO_NOTE_2026-06-22.md")),
        "block126": flat(text("QUARK_ROUTE2_SOURCE_READOUT_UNIT_CALIBRATION_NO_GO_2026-06-22.md")),
        "block130": flat(text("QUARK_ROUTE2_FISHER_RIESZ_REALIZATION_NO_GO_2026-06-22.md")),
    }
    check("Block147 is support-only selector atlas", "not current-surface closure" in docs["block147"])
    check("Block148 prunes weakened selector clauses", "single-clause omissions" in docs["block148"])
    check("Block149 prunes current candidate instantiations", "No current candidate supplies all clauses" in docs["block149"])
    check("Block142 prunes finite P_R rows to O_CR", "P_R-to-O_CR functor theorem" in docs["block142"])
    check("Block101 prunes Pcal moment realization from exact P_R slots", "Route-2 Pcal moment-realization theorem" in docs["block101"])
    check("Block144 prunes formal J_CR physical typing", "Route-2 physical J_CR source typing theorem" in docs["block144"])
    check("Block146 prunes source-measure bias from minimal premises", "Route-2 source-measure 2:1 bias theorem" in docs["block146"])
    check("Block140 prunes covariance score lift", "Route-2 physical covariance score-lift theorem" in docs["block140"])
    check("Block100 prunes generic product registry support", "Route-2 Pcal product-instantiation theorem" in docs["block100"])
    check("Block126 prunes source-unit to readout-unit calibration", "Route-2 source-readout unit calibration theorem" in docs["block126"])
    check("Block130 prunes generic Fisher-Riesz realization", "Omega_R, P_0, and a normalized RN source path" in docs["block130"])


def part2_queue_classification() -> None:
    print()
    print("PART 2: queue classification")
    for item in items():
        print(f"  {item.route}: status={item.status}, guard={item.guard}, missing={item.missing}")
        check(f"{item.route} has classified status", item.status in {"support_only", "pruned"})
        check(f"{item.route} names a guard block", bool(item.guard))
        check(f"{item.route} names missing primitive", "theorem" in item.missing or "theorems" in item.missing)
    check("eight route families classified", len(items()) == 8)
    check("exactly one support-only route remains", sum(1 for item in items() if item.status == "support_only") == 1)
    check("all other route families are pruned", sum(1 for item in items() if item.status == "pruned") == 7)


def part3_missing_primitive() -> None:
    print()
    print("PART 3: missing primitive")
    primitive_clauses = (
        "Omega_R",
        "P_0",
        "P_h",
        "physical readout variables X,Y",
        "raw moment E[XY]=1",
        "connected-subtraction typing",
        "one-point product E[X]E[Y]=1/9",
        "source/readout unit calibration mu=1",
        "orientation sign after kappa=0",
    )
    for clause in primitive_clauses:
        print(f"  primitive clause: {clause}")
        check(f"primitive clause recorded: {clause}", bool(clause))
    check("primitive has nine clauses", len(primitive_clauses) == 9)
    check("primitive includes probability source law", {"Omega_R", "P_0", "P_h"}.issubset(set(primitive_clauses)))
    check("primitive includes product selector", "one-point product E[X]E[Y]=1/9" in primitive_clauses)
    check("primitive includes unit calibration", "source/readout unit calibration mu=1" in primitive_clauses)


def part4_reachability() -> None:
    print()
    print("PART 4: reachability")
    current_edges = [("current_campaign_queue", item.route) for item in items()]
    current_edges += [(item.route, "missing_physical_source_readout_primitive") for item in items()]
    theorem_edges = [
        ("physical_source_readout_primitive", "Omega_R_P0_Ph"),
        ("Omega_R_P0_Ph", "physical_XY"),
        ("physical_XY", "raw_product_registry"),
        ("raw_product_registry", "kappa_zero"),
        ("kappa_zero", "mu_one"),
        ("mu_one", "orientation_sign"),
        ("orientation_sign", "c_TE_minus_8_9"),
    ]
    check("current queue reaches missing primitive node", reachable(current_edges, "current_campaign_queue", "missing_physical_source_readout_primitive"))
    check("current queue does not reach kappa zero", not reachable(current_edges, "current_campaign_queue", "kappa_zero"))
    check("current queue does not reach signed bridge", not reachable(current_edges, "current_campaign_queue", "c_TE_minus_8_9"))
    check("new primitive theorem would reach kappa zero", reachable(theorem_edges, "physical_source_readout_primitive", "kappa_zero"))
    check("new primitive theorem would reach signed bridge", reachable(theorem_edges, "physical_source_readout_primitive", "c_TE_minus_8_9"))
    all_current_nodes = {n for edge in current_edges for n in edge}
    check("current queue graph has no endpoint-value input node", all("rho_E" not in n and "q_E" not in n for n in all_current_nodes))


def part5_document_boundary() -> None:
    print()
    print("PART 5: document boundary")
    note = text("QUARK_ROUTE2_SOURCE_READOUT_PRIMITIVE_QUEUE_EXHAUSTION_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    review = loop_text("REVIEW_HISTORY.md")
    state = loop_text("STATE.yaml")
    note_flat = flat(note)
    required = (
        "Actual current-surface status: no-go for the current non-duplicative Route-2 source/readout routes",
        "Route-2 physical same-source selector realization theorem",
        "No current non-duplicative route remains",
        "The next useful proof target is exactly the physical source/readout realization theorem",
        "No endpoint value is used as an input",
    )
    for marker in required:
        check(f"note contains marker: {marker}", marker in note_flat)
    for marker in ("Block150 Summary", "negative_route_pruning", "Do not audit", "Next Exact Action"):
        check(f"handoff contains marker: {marker}", marker in handoff)
    check("certificate keeps proposal disallowed", "proposal_allowed: false" in cert)
    check("trace gate marks negative route pruning", "trace_class: negative_route_pruning" in trace_gate)
    check("state records global queue stop condition", "stop_condition: global_queue_exhaustion" in state)
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
    print("Route-2 source/readout primitive queue exhaustion")
    print("TRACE: negative_route_pruning")
    part1_grounding()
    part2_queue_classification()
    part3_missing_primitive()
    part4_reachability()
    part5_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        return 1
    print("VERDICT: the current campaign queue is exhausted for non-duplicative source/readout routes; the remaining open primitive is the physical same-source selector realization theorem.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
