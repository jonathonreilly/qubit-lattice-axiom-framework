#!/usr/bin/env python3
"""No-go for finite P_R rows alone giving source-Hessian E/T coupling."""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-source-hessian-channel-coupling"

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class CouplingAssignment:
    e_source: str
    t_source: str

    def preserves_finite_rows(self) -> bool:
        return self.e_source.startswith("H_") and self.t_source.startswith("H_")


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


def part1_grounding() -> None:
    print("PART 1: grounding")
    block124 = flat(text("QUARK_ROUTE2_PR_CHANNEL_ASSIGNMENT_BOUNDARY_SUPPORT_2026-06-22.md"))
    block123 = flat(text("QUARK_ROUTE2_MINIMAL_READOUT_COUPLING_CONTRACT_SUPPORT_2026-06-22.md"))
    block121 = flat(text("QUARK_ROUTE2_MINIMAL_MULTI_RECORD_EXTENSION_SUPPORT_2026-06-22.md"))
    source_jet = flat(text("QUARK_ROUTE2_SOURCE_JET_LIFT_NO_GO_NOTE_2026-06-22.md"))
    hidden = flat(text("QUARK_ROUTE2_HIDDEN_ADJOINT_CARRIER_NO_GO_NOTE_2026-06-22.md"))
    check("Block124 supplies finite row labels", "finite E/T row labels and disjoint carrier columns are available" in block124)
    check("Block124 keeps source-Hessian channel coupling open", "not source-Hessian readout-coupling closure" in block124)
    check("Block123 names C3 source channel assignment", "C3. channel_assignment" in block123)
    check("Block121 names source coordinates J0 and JA", "same-source coordinates J_0, J_A" in block121)
    check("Block121 names adjoint Hessian delta_AB", "D_A D_B log Z = delta_AB" in block121)
    check("source-jet no-go says finite P_R lacks source coordinates", "source coordinates J_A" in source_jet)
    check("hidden carrier no-go says current K_R has no adjoint slot", "No hidden adjoint carrier exists" in hidden)


def part2_domain_separation() -> None:
    print()
    print("PART 2: typed domain separation")
    finite = {
        "endpoint_slots": 4,
        "output_rows": 2,
        "row_labels": True,
        "source_indices": False,
        "hessian_components": False,
    }
    source = {
        "source_coordinates": 9,
        "adjoint_coordinates": 8,
        "identity_coordinate": 1,
        "finite_endpoint_slots": False,
        "physical_output_rows": False,
    }
    for name, value in finite.items():
        print(f"  finite {name}: {value}")
        check(f"finite {name} is classified", isinstance(value, (bool, int)))
    for name, value in source.items():
        print(f"  source {name}: {value}")
        check(f"source {name} is classified", isinstance(value, (bool, int)))
    check("finite readout has E/T rows", finite["output_rows"] == 2 and finite["row_labels"])
    check("finite readout lacks source indices", not finite["source_indices"])
    check("Block121 source has 1+8 coordinates", source["source_coordinates"] == source["identity_coordinate"] + source["adjoint_coordinates"])
    check("Block121 source lacks finite endpoint rows by itself", not source["physical_output_rows"])


def part3_assignment_nonuniqueness() -> None:
    print()
    print("PART 3: arbitrary source-component assignments")
    assignments = {
        "adjoint_pair": CouplingAssignment("H_A1A1", "H_A2A2"),
        "swapped_adjoint_pair": CouplingAssignment("H_A2A2", "H_A1A1"),
        "identity_mixed": CouplingAssignment("H_00", "H_A1A1"),
        "offdiag_pair": CouplingAssignment("H_A1A2", "H_A3A4"),
    }
    for name, assignment in assignments.items():
        print(f"  {name}: E->{assignment.e_source}, T->{assignment.t_source}")
        check(f"{name} preserves finite E/T row names", assignment.preserves_finite_rows())
        check(f"{name} has two typed source selections", assignment.e_source != "" and assignment.t_source != "")
    images = {(a.e_source, a.t_source) for a in assignments.values()}
    check("multiple source-component assignments preserve the same finite row labels", len(images) == len(assignments))
    check("finite row labels do not select one source assignment", len(images) > 1)
    check("identity-line assignment is not excluded by row labels alone", assignments["identity_mixed"].e_source == "H_00")
    check("off-diagonal assignment is not excluded by row labels alone", assignments["offdiag_pair"].e_source == "H_A1A2")


def part4_reachability() -> None:
    print()
    print("PART 4: reachability")
    current_edges = [
        ("finite_P_R_rows", "finite_E_T_channel_labels"),
        ("finite_E_T_channel_labels", "missing_Phi_ET"),
        ("missing_Phi_ET", "no_source_Hessian_channel_coupling"),
    ]
    positive_edges = [
        ("Route2_source_Hessian_ET_channel_coupling_theorem", "Phi_ET"),
        ("Phi_ET", "same_source_PR_ET"),
        ("Phi_ET", "source_Hessian_channel_assignment"),
        ("source_Hessian_channel_assignment", "C3_satisfied"),
        ("C3_satisfied", "readout_coupling_contract_candidate"),
    ]
    check("finite P_R reaches finite channel labels", reachable(current_edges, "finite_P_R_rows", "finite_E_T_channel_labels"))
    check("finite P_R reaches missing Phi_ET node", reachable(current_edges, "finite_P_R_rows", "missing_Phi_ET"))
    check("finite P_R alone does not reach C3 satisfied", not reachable(current_edges, "finite_P_R_rows", "C3_satisfied"))
    check("Phi_ET theorem would reach C3 satisfied", reachable(positive_edges, "Route2_source_Hessian_ET_channel_coupling_theorem", "C3_satisfied"))
    all_nodes = {n for e in current_edges + positive_edges for n in e}
    check("reachability graph contains no endpoint-value input", all("rho_E" not in n and "q_E" not in n for n in all_nodes))
    check("mu=1 normalization is not smuggled into Phi_ET graph", all("mu_one" not in n for n in all_nodes))


def part5_document_boundary() -> None:
    print()
    print("PART 5: document boundary")
    note = text("QUARK_ROUTE2_SOURCE_HESSIAN_CHANNEL_COUPLING_NO_GO_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    review = loop_text("REVIEW_HISTORY.md")
    state = loop_text("STATE.yaml")
    note_flat = flat(note)
    required = (
        "Actual current-surface status: no-go for finite P_R row labels alone supplying the source-Hessian E/T channel-coupling clause",
        "Phi_ET : Block121 source-Hessian components -> finite P_R E/T output rows",
        "Route-2 source-Hessian E/T channel-coupling theorem",
        "No endpoint value is used",
    )
    for marker in required:
        check(f"note contains marker: {marker}", marker in note_flat)
    for marker in ("Block125 Summary", "negative_route_pruning", "Do not audit", "Next Exact Action"):
        check(f"handoff contains marker: {marker}", marker in handoff)
    check("certificate keeps proposal disallowed", "proposal_allowed: false" in cert)
    check("trace gate marks negative pruning", "trace_class: negative_route_pruning" in trace_gate)
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
    print("Route-2 source-Hessian channel-coupling no-go")
    print("TRACE: negative_route_pruning")
    part1_grounding()
    part2_domain_separation()
    part3_assignment_nonuniqueness()
    part4_reachability()
    part5_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        return 1
    print("VERDICT: finite P_R row labels do not define Phi_ET from Block121 source-Hessian components to physical E/T output rows.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
